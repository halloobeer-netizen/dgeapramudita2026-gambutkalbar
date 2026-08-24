from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== ROLE ACCESS CONTROL 2026 ===== */"
if MARKER in s:
    print("Role access control already applied")
    raise SystemExit(0)

css = r'''
    /* ===== ROLE ACCESS CONTROL 2026 ===== */
    .role-badge {
      display:inline-flex; align-items:center; justify-content:center;
      min-height:32px; padding:6px 10px; border-radius:999px;
      background:rgba(255,255,255,.13); border:1px solid rgba(255,255,255,.20);
      color:#fff; font-size:.68rem; font-weight:800; text-transform:uppercase;
      letter-spacing:.05em; white-space:nowrap;
    }
    .role-badge[data-role="admin"] { background:rgba(72,199,116,.22); }
    .role-badge[data-role="editor"] { background:rgba(255,193,7,.18); }
    .role-badge[data-role="viewer"] { background:rgba(255,255,255,.10); }
    .permission-hidden { display:none !important; }
    @media (max-width:620px) {
      .role-badge { min-height:28px; padding:5px 8px; font-size:.59rem; }
    }
'''
s = s.replace("  </style>", css + "  </style>", 1)

# Show current access level in the header.
s = s.replace('<span class="user-chip" id="userName">User</span>', '<span class="user-chip" id="userName">User</span>\n        <span class="role-badge" id="roleBadge" data-role="viewer">Viewer</span>', 1)

# Role is stored in Firebase at /survei/roles/{uid}. Unknown users are Viewer by default.
s = s.replace(
"    let state = { user: null, khgs: [], currentKHG: null, editingPointId: null, previewPointId: null, importRows: [], photos: {}, docs: [], map: null, currentPhotoField: null };",
"    let state = { user: null, role: 'viewer', khgs: [], currentKHG: null, editingPointId: null, previewPointId: null, importRows: [], photos: {}, docs: [], map: null, currentPhotoField: null };",
1)

role_js = r'''

    // ========== ROLE ACCESS CONTROL ==========
    // Roles: admin, editor, viewer. Default is viewer when no role exists.
    const ROLE_PERMISSIONS = {
      admin:  { manageKHG:true, importData:true, addPoint:true, editPoint:true, deletePoint:true },
      editor: { manageKHG:false, importData:false, addPoint:true, editPoint:true, deletePoint:false },
      viewer: { manageKHG:false, importData:false, addPoint:false, editPoint:false, deletePoint:false }
    };

    function can(permission) {
      return !!(ROLE_PERMISSIONS[state.role] && ROLE_PERMISSIONS[state.role][permission]);
    }

    function requirePermission(permission, message='Anda tidak memiliki izin untuk tindakan ini.') {
      if (can(permission)) return true;
      toast('🔒 ' + message);
      return false;
    }

    async function loadUserRole() {
      state.role = 'viewer';
      if (!state.user?.uid) { applyRoleUI(); return; }
      try {
        const snap = await db.ref('survei/roles/' + state.user.uid).once('value');
        const role = String(snap.val() || 'viewer').toLowerCase();
        state.role = ['admin','editor','viewer'].includes(role) ? role : 'viewer';
      } catch (err) {
        console.error('Gagal membaca role:', err);
        state.role = 'viewer';
      }
      applyRoleUI();
    }

    function applyRoleUI() {
      const badge = document.getElementById('roleBadge');
      if (badge) {
        const labels = { admin:'Admin', editor:'Editor', viewer:'Viewer' };
        badge.textContent = labels[state.role] || 'Viewer';
        badge.dataset.role = state.role;
        badge.title = state.user?.email ? `${state.user.email} • ${badge.textContent}` : badge.textContent;
      }

      document.querySelectorAll('[data-permission]').forEach(el => {
        el.classList.toggle('permission-hidden', !can(el.dataset.permission));
      });
    }

    function saveEditorPoint(data, existingIndex) {
      if (!state.currentKHG?.id) return Promise.reject(new Error('KHG tidak ditemukan'));
      const isEdit = existingIndex >= 0;
      const index = isEdit ? existingIndex : (state.currentKHG.points?.length || 0);
      return KHG_REF.child(state.currentKHG.id).child('points').child(String(index)).set(data);
    }
'''

anchor = "    // Simpan seluruh data KHG ke Firebase (realtime)\n"
if anchor not in s:
    raise RuntimeError("Role JS insertion anchor not found")
s = s.replace(anchor, role_js + "\n" + anchor, 1)

# Load role before opening the application.
old_enter = '''    function enterApp() {
      document.getElementById('view-login').classList.remove('active');
      document.getElementById('appRoot').classList.remove('hidden');
      document.getElementById('userName').textContent = state.user?.name || 'User';
      goDashboard();
    }'''
new_enter = '''    async function enterApp() {
      await loadUserRole();
      document.getElementById('view-login').classList.remove('active');
      document.getElementById('appRoot').classList.remove('hidden');
      document.getElementById('userName').textContent = state.user?.name || 'User';
      applyRoleUI();
      goDashboard();
      if (state.role === 'viewer') toast('Mode Viewer: hanya dapat melihat data');
    }'''
if old_enter not in s:
    raise RuntimeError("enterApp block not found")
s = s.replace(old_enter, new_enter, 1)

# Static action buttons.
s = s.replace('onclick="openImportModal()">📥 Import Excel</button>', 'data-permission="importData" onclick="openImportModal()">📥 Import Excel</button>', 1)
s = s.replace('onclick="openAddKHG()">＋ Tambah KHG</button>', 'data-permission="manageKHG" onclick="openAddKHG()">＋ Tambah KHG</button>', 1)
s = s.replace('onclick="openAddPoint()">+ Tambah Titik</button>', 'data-permission="addPoint" onclick="openAddPoint()">+ Tambah Titik</button>', 1)
s = s.replace('onclick="editFromPreview()">✏️ Edit</button>', 'data-permission="editPoint" onclick="editFromPreview()">✏️ Edit</button>', 1)
s = s.replace('onclick="savePoint()">💾 Simpan</button>', 'data-permission="editPoint" onclick="savePoint()">💾 Simpan</button>', 1)

# Dashboard: hide destructive KHG action unless Admin.
old_khg_button = '''          <button class="btn btn-danger btn-sm" onclick="event.stopPropagation(); deleteKHG('${k.id}')" title="Hapus KHG">Hapus</button>'''
new_khg_button = '''          ${can('manageKHG') ? `<button class="btn btn-danger btn-sm" onclick="event.stopPropagation(); deleteKHG('${k.id}')" title="Hapus KHG">Hapus</button>` : ''}'''
if old_khg_button not in s:
    raise RuntimeError("KHG delete render button not found")
s = s.replace(old_khg_button, new_khg_button, 1)

# Point list: Viewer gets view-only; Editor gets Edit; Admin gets Edit + Hapus.
old_actions = '''          <div class="actions-row">
            <button class="btn btn-outline btn-sm" onclick="event.stopPropagation(); previewPoint('${p.id}')">👁️</button>
            <button class="btn btn-outline btn-sm" onclick="event.stopPropagation(); editPoint('${p.id}')">Edit</button>
            <button class="btn btn-danger btn-sm" onclick="event.stopPropagation(); deletePoint('${p.id}')">Hapus</button>
          </div>'''
new_actions = '''          <div class="actions-row">
            <button class="btn btn-outline btn-sm" onclick="event.stopPropagation(); previewPoint('${p.id}')">👁️</button>
            ${can('editPoint') ? `<button class="btn btn-outline btn-sm" onclick="event.stopPropagation(); editPoint('${p.id}')">Edit</button>` : ''}
            ${can('deletePoint') ? `<button class="btn btn-danger btn-sm" onclick="event.stopPropagation(); deletePoint('${p.id}')">Hapus</button>` : ''}
          </div>'''
if old_actions not in s:
    raise RuntimeError("Point action render block not found")
s = s.replace(old_actions, new_actions, 1)

# Permission guards for privileged actions.
guards = {
"    function openAddKHG() {": "    function openAddKHG() {\n      if (!requirePermission('manageKHG', 'Hanya Admin yang dapat menambah KHG.')) return;",
"    function saveKHG() {": "    function saveKHG() {\n      if (!requirePermission('manageKHG', 'Hanya Admin yang dapat menyimpan KHG.')) return;",
"    function deleteKHG(id) {": "    function deleteKHG(id) {\n      if (!requirePermission('manageKHG', 'Hanya Admin yang dapat menghapus KHG.')) return;",
"    function openAddPoint() {": "    function openAddPoint() {\n      if (!requirePermission('addPoint', 'Akun Anda tidak memiliki izin menambah titik.')) return;",
"    function editPoint(id) {": "    function editPoint(id) {\n      if (!requirePermission('editPoint', 'Akun Anda tidak memiliki izin mengedit titik.')) return;",
"    function editFromPreview() {": "    function editFromPreview() {\n      if (!requirePermission('editPoint', 'Akun Anda tidak memiliki izin mengedit titik.')) return;",
"    function deletePoint(id) {": "    function deletePoint(id) {\n      if (!requirePermission('deletePoint', 'Hanya Admin yang dapat menghapus titik.')) return;",
"    function openImportModal() {": "    function openImportModal() {\n      if (!requirePermission('importData', 'Hanya Admin yang dapat import Excel.')) return;",
"    function doImport() {": "    function doImport() {\n      if (!requirePermission('importData', 'Hanya Admin yang dapat import data.')) return;",
"    function triggerPhoto(box) {": "    function triggerPhoto(box) { if (!requirePermission('editPoint', 'Akun Anda tidak memiliki izin mengubah foto.')) return;",
"    function triggerDoc() {": "    function triggerDoc() { if (!requirePermission('editPoint', 'Akun Anda tidak memiliki izin mengubah dokumen.')) return;"
}
for old, new in guards.items():
    if old not in s:
        raise RuntimeError(f"Guard target not found: {old}")
    s = s.replace(old, new, 1)

# Save point securely: Admin may use existing full persist; Editor writes only one point path.
old_save = '''    function savePoint() {
      const data = collectForm();
      if (!data.surveyor || !data.namaTitik || !data.tanggal) {
        toast('Nama Surveyor, Nama Titik, dan Tanggal wajib diisi'); switchTab('umum'); return;
      }
      if (!state.currentKHG.points) state.currentKHG.points = [];
      const idx = state.currentKHG.points.findIndex(p => p.id === data.id);
      if (idx >= 0) state.currentKHG.points[idx] = data;
      else state.currentKHG.points.unshift(data);
      persist(); toast('✅ Titik berhasil disimpan'); showView('khg'); renderPoints();
    }'''
new_save = '''    async function savePoint() {
      if (!requirePermission('editPoint', 'Akun Anda tidak memiliki izin menyimpan titik.')) return;
      const data = collectForm();
      if (!data.surveyor || !data.namaTitik || !data.tanggal) {
        toast('Nama Surveyor, Nama Titik, dan Tanggal wajib diisi'); switchTab('umum'); return;
      }
      if (!state.currentKHG.points) state.currentKHG.points = [];
      const idx = state.currentKHG.points.findIndex(p => p.id === data.id);

      try {
        if (state.role === 'admin') {
          if (idx >= 0) state.currentKHG.points[idx] = data;
          else state.currentKHG.points.unshift(data);
          persist();
        } else if (state.role === 'editor') {
          await saveEditorPoint(data, idx);
        } else {
          return toast('🔒 Mode Viewer tidak dapat menyimpan perubahan.');
        }
        toast('✅ Titik berhasil disimpan'); showView('khg');
      } catch (err) {
        console.error(err);
        toast('❌ Gagal simpan: ' + err.message);
      }
    }'''
if old_save not in s:
    raise RuntimeError("savePoint block not found")
s = s.replace(old_save, new_save, 1)

# Re-apply visibility every time the dashboard/point views render dynamic controls.
s = s.replace("      list.innerHTML = state.khgs.map(k => `", "      list.innerHTML = state.khgs.map(k => `", 1)
s = s.replace("        </div>`).join('');\n    }\n\n    function openAddKHG()", "        </div>`).join('');\n      applyRoleUI();\n    }\n\n    function openAddKHG()", 1)
s = s.replace("        </div>`).join('');\n    }\n\n    function deletePoint(id)", "        </div>`).join('');\n      applyRoleUI();\n    }\n\n    function deletePoint(id)", 1)

p.write_text(s, encoding="utf-8")
print("Role access control applied successfully")
