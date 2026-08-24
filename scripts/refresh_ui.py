from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== UI REFRESH 2026 ===== */"
if MARKER in s:
    print("UI refresh already applied")
    raise SystemExit(0)

css = r'''
    /* ===== UI REFRESH 2026 ===== */
    :root {
      --primary: #176b42; --primary-dark: #0b4f30; --primary-light: #2b8b5b;
      --accent: #eaf7f0; --bg: #f2f6f3; --card: #ffffff; --text: #16271f;
      --muted: #66776e; --border: #dce8e0; --danger: #c62828; --radius: 18px;
      --shadow: 0 10px 30px rgba(18, 65, 43, .08);
    }
    body { background: radial-gradient(circle at top left, #edf8f1 0, #f6f8f6 38%, #f2f6f3 100%); }
    .app-header { background: rgba(255,255,255,.92); backdrop-filter: blur(14px); border-bottom: 1px solid rgba(23,107,66,.10); padding: 12px 18px; box-shadow: 0 5px 22px rgba(15,76,47,.05); }
    .brand-logo { width: 46px; height: 46px; min-width: 46px; border-radius: 14px; background: #fff; box-shadow: 0 5px 16px rgba(23,107,66,.10); }
    .brand h1 { font-size: .96rem; color: var(--primary-dark); }
    .brand p { font-size: .68rem; letter-spacing: .01em; }
    .header-right { gap: 8px; }
    .user-chip { background: var(--accent); color: var(--primary-dark); max-width: 150px; padding: 7px 10px; border-radius: 999px; font-weight: 700; border: 1px solid #d7ebdf; }
    .btn-home { border: 0; background: #edf8f1; padding: 8px 12px; border-radius: 11px; }
    .container { max-width: 980px; padding: 22px 18px; }
    .stats-row { gap: 14px; margin-bottom: 18px; }
    .stat-card, .summary-box, .khg-card, .point-item, .form-card { box-shadow: var(--shadow); border: 1px solid rgba(23,107,66,.09); }
    .stat-card { padding: 20px; position: relative; overflow: hidden; }
    .stat-card.green { background: linear-gradient(135deg, #176b42 0%, #0b4f30 100%); box-shadow: 0 14px 32px rgba(11,79,48,.20); }
    .stat-card.green::after { content: ''; position: absolute; width: 120px; height: 120px; border-radius: 50%; background: rgba(255,255,255,.08); right: -38px; top: -42px; }
    .stat-card .label { font-size: .78rem; font-weight: 650; }
    .stat-card .value { font-size: 2rem; letter-spacing: -.03em; }
    .summary-box { padding: 18px; }
    .summary-item { background: linear-gradient(180deg, #f2fbf5, #e9f5ed); border: 1px solid #dcecdf; }
    .progress-bar-bg { height: 12px; background: #e5ece7; }
    .khg-card { transition: transform .18s ease, box-shadow .18s ease; }
    .khg-card:hover { transform: translateY(-2px); box-shadow: 0 14px 34px rgba(18,65,43,.12); }
    .btn { border-radius: 11px; transition: transform .15s ease, box-shadow .15s ease; }
    .btn:hover { transform: translateY(-1px); }
    .btn-primary { background: linear-gradient(135deg, #1d7a4c, #0f5c38); box-shadow: 0 8px 18px rgba(15,92,56,.18); }
    .btn-outline { background: #fff; border-color: #d5e5da; }
    .login-screen { min-height: 100vh; padding: 28px 18px; position: relative; overflow: hidden; background: linear-gradient(140deg, #0b4f30 0%, #176b42 44%, #eef7f1 44%, #f8faf8 100%); }
    .login-screen::before, .login-screen::after { content:''; position:absolute; border-radius:50%; pointer-events:none; }
    .login-screen::before { width: 280px; height: 280px; background: rgba(255,255,255,.07); top:-90px; left:-70px; }
    .login-screen::after { width: 210px; height: 210px; background: rgba(23,107,66,.08); right:-80px; bottom:-60px; }
    .login-card { max-width: 430px; padding: 36px 34px 30px; border-radius: 26px; box-shadow: 0 28px 70px rgba(5,49,28,.22); border: 1px solid rgba(255,255,255,.85); position:relative; z-index:2; }
    .login-card .logo { width: 104px; height: 104px; margin-bottom: 18px; filter: drop-shadow(0 8px 16px rgba(15,92,56,.14)); }
    .login-title { font-size: 1.45rem; color: var(--primary-dark); letter-spacing: -.02em; margin-bottom: 7px; }
    .login-subtitle { font-size: .84rem; color: var(--muted); line-height: 1.6; margin-bottom: 24px; }
    .login-badge { display:inline-flex; align-items:center; gap:6px; background:#edf8f1; color:#176b42; border:1px solid #d6ebde; border-radius:999px; padding:6px 10px; font-size:.7rem; font-weight:700; margin-bottom:15px; }
    .btn-google { max-width: none; padding: 13px 18px; border-radius: 12px; font-weight: 700; box-shadow: 0 6px 18px rgba(0,0,0,.06); }
    .login-note { margin-top: 18px; padding-top: 16px; border-top: 1px solid #edf1ee; font-size: .72rem; color: #7b8981; line-height: 1.55; }
    .bottom-bar { background: rgba(255,255,255,.94); backdrop-filter: blur(12px); border-top: 1px solid rgba(23,107,66,.10); box-shadow: 0 -8px 26px rgba(18,65,43,.06); }
    @media (max-width: 620px) {
      .login-screen { background: linear-gradient(160deg, #0b4f30 0%, #176b42 27%, #f2f7f3 27%); align-items: stretch; }
      .login-card { max-width: 100%; margin-top: 10vh; padding: 30px 22px 26px; border-radius: 22px; }
      .stats-row { grid-template-columns: 1fr 1fr; gap: 10px; }
      .stat-card { padding: 16px; }
      .stat-card .value { font-size: 1.65rem; }
      .container { padding: 16px 12px; }
      .user-chip { display:none; }
      .app-header { padding: 9px 10px; }
    }
'''
s = s.replace("  </style>", css + "  </style>", 1)

old_heading = '<h2 style="font-size:1.15rem;margin-bottom:6px;">Survei Ekosistem Gambut</h2>\n        <p style="font-size:0.82rem;color:var(--muted);margin-bottom:22px;">Inventarisasi Karakteristik<br>Login untuk melanjutkan</p>'
new_heading = '<div class="login-badge">● Sistem Survei Lapangan 2026</div>\n        <h2 class="login-title">Survei Ekosistem Gambut</h2>\n        <p class="login-subtitle">Inventarisasi karakteristik KHG Kalimantan Barat.<br>Masuk menggunakan akun Google yang berwenang untuk melanjutkan.</p>'
s = s.replace(old_heading, new_heading, 1)

old_guest = '''        </button>
        <p style="font-size:0.72rem;color:var(--muted);margin-bottom:10px;">— atau —</p>
        <button class="btn btn-outline btn-block" onclick="loginAsGuest()" style="max-width:280px;margin:0 auto;">Lanjut sebagai Tamu</button>'''
new_guest = '''        </button>
        <div class="login-note">Akses dashboard dilindungi oleh Firebase Authentication. Data survei tetap tersinkron secara realtime setelah Anda masuk.</div>'''
s = s.replace(old_guest, new_guest, 1)
s = s.replace("          Masuk dengan Google", "          Masuk aman dengan Google", 1)

old_auth = '''      } else {
        // Cek mode tamu
        try {
          if (localStorage.getItem('gambut_guest') === '1' && !state.user) {
            state.user = { name: 'Tamu', email: '', provider: 'guest' };
            enterApp();
            return;
          }
        } catch(e) {}
        if (!state.user || state.user.provider === 'google') {'''
new_auth = '''      } else {
        // Login diwajibkan. Hapus sisa sesi tamu dari versi sebelumnya.
        try { localStorage.removeItem('gambut_guest'); } catch(e) {}
        if (!state.user || state.user.provider === 'google') {'''
s = s.replace(old_auth, new_auth, 1)

needle = '''    <div id="view-dashboard" class="view">
      <div class="container">
        <div class="stats-row">'''
replacement = '''    <div id="view-dashboard" class="view">
      <div class="container">
        <div style="margin:2px 0 16px;">
          <div style="font-size:.72rem;font-weight:700;color:var(--primary);text-transform:uppercase;letter-spacing:.08em;margin-bottom:4px;">Dashboard Survei</div>
          <h2 style="font-size:1.28rem;letter-spacing:-.02em;color:var(--text);">Ringkasan Ekosistem Gambut</h2>
          <p style="font-size:.8rem;color:var(--muted);margin-top:3px;">Pantau progres KHG dan titik survei dalam satu tampilan.</p>
        </div>
        <div class="stats-row">'''
s = s.replace(needle, replacement, 1)

if MARKER not in s:
    raise RuntimeError("UI refresh failed: marker not inserted")
if "Lanjut sebagai Tamu" in s:
    raise RuntimeError("UI refresh failed: guest button still present")

p.write_text(s, encoding="utf-8")
print("UI refresh applied successfully")
