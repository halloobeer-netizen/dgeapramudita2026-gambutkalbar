from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== DASHBOARD REFINEMENT 2026 ===== */"
if MARKER in s:
    print("Dashboard refinement already applied")
    raise SystemExit(0)

css = r'''
    /* ===== DASHBOARD REFINEMENT 2026 ===== */
    #appRoot .app-header { min-height:72px; }
    #appRoot .brand { gap:11px; }
    #appRoot .brand h1 { font-weight:800; }
    #appRoot .header-right { gap:8px; }
    #appRoot .user-chip {
      max-width:170px; padding:8px 11px; border-radius:999px;
      background:rgba(255,255,255,.10); border:1px solid rgba(255,255,255,.16);
      font-weight:700; color:#fff;
    }
    #appRoot .btn-home, #appRoot .app-header .btn-outline { padding:8px 12px; border-radius:10px; font-weight:700; }

    .dash-intro { padding-top:2px; }
    .dash-date::before { content:'▣'; margin-right:7px; color:var(--primary); }
    .dash-actions {
      display:flex; gap:8px; flex-wrap:wrap; margin-top:13px;
    }
    .dash-actions .btn { box-shadow:none; }

    #view-dashboard .stat-card { transition:transform .18s ease, box-shadow .18s ease; }
    #view-dashboard .stat-card:hover { transform:translateY(-2px); box-shadow:0 12px 28px rgba(20,55,35,.09); }
    #view-dashboard .stat-card .stat-note { line-height:1.4; }

    #view-dashboard .summary-box { position:relative; overflow:hidden; }
    #view-dashboard .summary-box::after {
      content:''; position:absolute; width:180px; height:180px; border-radius:50%;
      background:radial-gradient(circle, rgba(10,139,72,.07), rgba(10,139,72,0) 70%);
      right:-55px; top:-65px; pointer-events:none;
    }
    #view-dashboard .progress-wrap, #view-dashboard .summary-grid, #view-dashboard .recent-list { position:relative; z-index:1; }
    #view-dashboard .progress-sub { margin-top:8px; }

    #view-dashboard .recent-list::before { margin-top:2px; margin-bottom:9px; }
    #view-dashboard .recent-item {
      display:grid; grid-template-columns:minmax(100px,1fr) minmax(120px,1.35fr) auto;
      gap:12px; align-items:center; min-height:46px; padding:9px 10px;
      border-bottom:1px solid #edf1ee; border-radius:8px;
    }
    #view-dashboard .recent-item:hover { background:#f8fbf9; }
    #view-dashboard .recent-point { color:var(--primary-dark); font-weight:800; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
    #view-dashboard .recent-khg { color:var(--muted); overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
    #view-dashboard .recent-date { color:#7a867f; font-size:.72rem; white-space:nowrap; }

    #view-dashboard .section-title { padding-top:2px; }
    #view-dashboard .section-title > div:last-child { gap:8px !important; }
    #view-dashboard .section-title + p { line-height:1.55; }
    #view-dashboard #khgList { display:grid; gap:10px; }
    #view-dashboard .khg-card {
      display:grid !important; grid-template-columns:48px minmax(0,1fr) auto; align-items:center !important;
      gap:13px !important; padding:15px 16px !important; margin-bottom:0;
      border:1px solid var(--border); background:#fff;
    }
    #view-dashboard .khg-card::before {
      content:'⌖'; width:46px; height:46px; border-radius:13px;
      display:flex; align-items:center; justify-content:center;
      color:var(--primary); background:#eaf6ef; font-size:1.35rem; font-weight:800;
    }
    #view-dashboard .khg-card > div { min-width:0; }
    #view-dashboard .khg-card h3 { margin:0 0 4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
    #view-dashboard .khg-card .meta { line-height:1.45; }
    #view-dashboard .khg-card .btn-danger { opacity:.72; border-radius:9px; }
    #view-dashboard .khg-card .btn-danger:hover { opacity:1; }

    @media (max-width:620px) {
      #appRoot .app-header { min-height:62px; }
      #appRoot .header-right { gap:5px; }
      #appRoot .btn-home { display:none; }
      #appRoot .app-header .btn-outline { padding:7px 10px; font-size:.7rem; }
      .dash-actions { margin-top:11px; }
      .dash-actions .btn { flex:1; min-width:120px; }
      #view-dashboard .recent-item {
        grid-template-columns:minmax(90px,.85fr) minmax(0,1.15fr);
        gap:5px 10px; padding:9px 4px;
      }
      #view-dashboard .recent-date { grid-column:2; }
      #view-dashboard .khg-card { grid-template-columns:40px minmax(0,1fr) auto; gap:10px !important; padding:13px !important; }
      #view-dashboard .khg-card::before { width:40px; height:40px; border-radius:11px; font-size:1.1rem; }
      #view-dashboard .khg-card .btn-danger { padding:6px 8px; font-size:.68rem; }
      #view-dashboard .section-title { gap:10px; }
      #view-dashboard .section-title > div:last-child { width:100%; }
      #view-dashboard .section-title .btn { flex:1; }
    }
'''

s = s.replace("  </style>", css + "  </style>", 1)

# Add quick actions below the dashboard intro, using existing functions only.
intro_end = '''          <div class="dash-date" id="dashDate">Survei Lapangan 2026</div>
        </div>'''
intro_new = '''          <div class="dash-date" id="dashDate">Survei Lapangan 2026</div>
        </div>
        <div class="dash-actions">
          <button class="btn btn-outline btn-sm" onclick="openImportModal()">📥 Import Excel</button>
          <button class="btn btn-primary btn-sm" onclick="openAddKHG()">＋ Tambah KHG</button>
        </div>'''
if intro_end in s:
    s = s.replace(intro_end, intro_new, 1)

# Avoid duplicate top-level action buttons in the KHG section while retaining section title.
old_actions = '''          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <button class="btn btn-outline btn-sm" onclick="openImportModal()">📥 Import Excel</button>
            <button class="btn btn-primary btn-sm" onclick="openAddKHG()">+ Tambah KHG</button>
          </div>'''
s = s.replace(old_actions, '', 1)

# Set the date chip from real local date each dashboard render.
needle = "      const remaining = Math.max(0, TARGET_TOTAL - surveyed);\n"
addition = """      const remaining = Math.max(0, TARGET_TOTAL - surveyed);\n\n      const dashDate = document.getElementById('dashDate');\n      if (dashDate) {\n        dashDate.textContent = new Intl.DateTimeFormat('id-ID', { weekday:'short', day:'2-digit', month:'short', year:'numeric' }).format(new Date());\n      }\n"""
if needle in s:
    s = s.replace(needle, addition, 1)

# Render recent data as a cleaner three-column list while preserving the same source data.
old_recent = '''      if (recent.length) {
        recentEl.innerHTML = '<div style="font-size:0.78rem;font-weight:600;margin-bottom:4px;color:var(--muted);">Titik Terbaru</div>' +
          recent.map(p => `<div class="recent-item"><span>${p.namaTitik || '-'} <small style="color:var(--muted);">(${p.khgNama})</small></span><span style="color:var(--muted);font-size:0.72rem;">${p.tanggal || '-'}</span></div>`).join('');
      } else recentEl.innerHTML = '';'''
new_recent = '''      if (recent.length) {
        recentEl.innerHTML = recent.map(p => `
          <div class="recent-item">
            <span class="recent-point">${p.namaTitik || '-'}</span>
            <span class="recent-khg">${p.khgNama || '-'}</span>
            <span class="recent-date">${p.tanggal || '-'}</span>
          </div>`).join('');
      } else recentEl.innerHTML = '';'''
if old_recent in s:
    s = s.replace(old_recent, new_recent, 1)

p.write_text(s, encoding="utf-8")
print("Dashboard refinement applied successfully")
