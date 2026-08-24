from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== PROFESSIONAL DASHBOARD 2026 ===== */"
if MARKER in s:
    print("Professional dashboard already applied")
    raise SystemExit(0)

css = r'''
    /* ===== PROFESSIONAL DASHBOARD 2026 ===== */
    #appRoot {
      --bg: #f5f8f6;
      --card: #ffffff;
      --text: #17241c;
      --muted: #6b7770;
      --border: #e3ebe6;
      --primary: #087a3d;
      --primary-dark: #075f32;
      --accent: #edf7f1;
      background: #f5f8f6;
      min-height: 100vh;
    }
    #appRoot .app-header {
      background: linear-gradient(115deg, #075f32, #0a713a);
      border: 0;
      padding: 13px 18px;
      box-shadow: 0 3px 16px rgba(7,95,50,.16);
    }
    #appRoot .brand-logo { width: 46px; height: 46px; min-width: 46px; border-radius: 12px; background:#fff; }
    #appRoot .brand h1 { color:#fff; font-size:.98rem; letter-spacing:-.01em; }
    #appRoot .brand p { color:rgba(255,255,255,.78); font-size:.7rem; }
    #appRoot .user-chip { color:rgba(255,255,255,.86); }
    #appRoot .btn-home, #appRoot .app-header .btn-outline {
      background:rgba(255,255,255,.12); color:#fff; border:1px solid rgba(255,255,255,.22);
    }
    #view-dashboard .container { max-width:1040px; padding:24px 18px 110px; }
    .dash-intro { display:flex; justify-content:space-between; gap:18px; align-items:center; margin:0 0 22px; }
    .dash-eyebrow { color:var(--primary); font-size:.72rem; font-weight:800; text-transform:uppercase; letter-spacing:.1em; margin-bottom:5px; }
    .dash-intro h2 { font-size:clamp(1.45rem,3vw,2rem); line-height:1.15; letter-spacing:-.035em; }
    .dash-intro p { color:var(--muted); font-size:.86rem; margin-top:5px; }
    .dash-date { background:#fff; border:1px solid var(--border); border-radius:12px; padding:10px 14px; color:#415047; font-size:.78rem; box-shadow:0 5px 18px rgba(20,55,35,.05); white-space:nowrap; }
    #view-dashboard .stats-row { grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px; margin-bottom:14px; }
    #view-dashboard .stat-card, #view-dashboard .stat-card.green {
      position:relative; min-height:132px; padding:20px; background:#fff; color:var(--text); border:1px solid var(--border); border-radius:16px; box-shadow:0 7px 22px rgba(20,55,35,.055); overflow:hidden;
    }
    #view-dashboard .stat-card::before { content:''; position:absolute; width:62px; height:62px; right:18px; top:18px; border-radius:50%; background:#e8f4ed; }
    #view-dashboard .stat-card::after { position:absolute; right:38px; top:33px; font-size:1.55rem; z-index:1; }
    #view-dashboard .stat-card.green::after { content:'▰'; color:var(--primary); transform:rotate(90deg); }
    #view-dashboard .stat-card:not(.green)::after { content:'●'; color:var(--primary); }
    #view-dashboard .stat-card .label { color:#526158; font-size:.8rem; font-weight:700; }
    #view-dashboard .stat-card .value { color:var(--primary-dark); font-size:2.15rem; font-weight:800; margin-top:9px; letter-spacing:-.04em; }
    #view-dashboard .stat-card .stat-note { color:var(--muted); font-size:.72rem; margin-top:2px; }
    #view-dashboard .summary-box { background:#fff; border:1px solid var(--border); border-radius:16px; padding:20px; box-shadow:0 7px 22px rgba(20,55,35,.055); margin-bottom:18px; }
    #view-dashboard .summary-box h3 { color:var(--primary-dark); font-size:1rem; margin-bottom:14px; }
    #view-dashboard .progress-header { font-size:.86rem; }
    #view-dashboard .progress-header .pct { color:var(--primary); font-size:1.65rem; font-weight:800; }
    #view-dashboard .progress-bar-bg { height:11px; background:#eaf1ed; }
    #view-dashboard .progress-bar-fill { background:linear-gradient(90deg,#0a8b48,#08733c); }
    #view-dashboard .summary-grid { grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; }
    #view-dashboard .summary-item { background:#f7faf8; border:1px solid var(--border); border-radius:12px; padding:12px; }
    #view-dashboard .summary-item .s-label { font-size:.7rem; }
    #view-dashboard .summary-item .s-value { color:var(--primary-dark); font-size:1.1rem; margin-top:3px; }
    #view-dashboard .recent-list { margin-top:18px; }
    #view-dashboard .recent-list::before { content:'Data Terbaru'; display:block; color:#26372d; font-size:.86rem; font-weight:800; margin-bottom:6px; }
    #view-dashboard .recent-item { padding:10px 4px; font-size:.77rem; }
    #view-dashboard .section-title { margin-top:22px; margin-bottom:8px; }
    #view-dashboard .section-title h2 { font-size:1.08rem; color:#1b2d22; }
    #view-dashboard .khg-card { border-radius:15px; padding:16px; box-shadow:0 5px 18px rgba(20,55,35,.045); }
    #view-dashboard .khg-card h3 { color:var(--primary-dark); font-size:.92rem; }
    #view-dashboard .btn { border-radius:10px; }
    #view-dashboard .btn-primary { background:var(--primary); }
    #view-dashboard .btn-outline { background:#fff; border-color:#dbe7df; }
    @media (min-width: 760px) {
      #view-dashboard .summary-box { padding:24px; }
    }
    @media (max-width: 620px) {
      #appRoot .app-header { padding:10px 12px; }
      #appRoot .brand-logo { width:40px; height:40px; min-width:40px; }
      #appRoot .brand h1 { font-size:.82rem; }
      #appRoot .brand p { font-size:.6rem; }
      #appRoot .user-chip { display:none; }
      #view-dashboard .container { padding:18px 14px 100px; }
      .dash-intro { align-items:flex-start; margin-bottom:16px; }
      .dash-intro h2 { font-size:1.45rem; }
      .dash-intro p { font-size:.78rem; max-width:260px; }
      .dash-date { display:none; }
      #view-dashboard .stats-row { gap:10px; }
      #view-dashboard .stat-card, #view-dashboard .stat-card.green { min-height:116px; padding:15px; border-radius:14px; }
      #view-dashboard .stat-card::before { width:44px; height:44px; right:12px; top:12px; }
      #view-dashboard .stat-card::after { right:26px; top:21px; font-size:1.1rem; }
      #view-dashboard .stat-card .label { font-size:.72rem; max-width:75%; }
      #view-dashboard .stat-card .value { font-size:1.75rem; margin-top:10px; }
      #view-dashboard .summary-box { padding:16px; border-radius:14px; }
      #view-dashboard .summary-grid { grid-template-columns:1fr 1fr; }
      #view-dashboard .recent-item { align-items:flex-start; }
      #view-dashboard .section-title { align-items:center; }
    }
'''

s = s.replace("  </style>", css + "  </style>", 1)

old_intro = '''        <div style="margin:2px 0 16px;">
          <div style="font-size:.72rem;font-weight:700;color:var(--primary);text-transform:uppercase;letter-spacing:.08em;margin-bottom:4px;">Dashboard Survei</div>
          <h2 style="font-size:1.28rem;letter-spacing:-.02em;color:var(--text);">Ringkasan Ekosistem Gambut</h2>
          <p style="font-size:.8rem;color:var(--muted);margin-top:3px;">Pantau progres KHG dan titik survei dalam satu tampilan.</p>
        </div>'''
new_intro = '''        <div class="dash-intro">
          <div>
            <div class="dash-eyebrow">Dashboard Survei</div>
            <h2>Ringkasan Ekosistem Gambut</h2>
            <p>Inventarisasi Karakteristik Ekosistem Gambut Kab. Kapuas Hulu, Kalimantan Barat</p>
          </div>
          <div class="dash-date" id="dashDate">Survei Lapangan 2026</div>
        </div>'''
s = s.replace(old_intro, new_intro, 1)
s = s.replace('<div style="font-size:0.72rem;color:var(--muted);margin-top:2px;">dari 1.073 titik</div>', '<div class="stat-note">dari target 1.073 titik</div>', 1)
s = s.replace('<h2>Dasbor KHG</h2>', '<h2>KHG Aktif</h2>', 1)
s = s.replace('Kelola Kesatuan Hidrologis Gambut dan hasil surveinya', 'Kelola Kesatuan Hidrologis Gambut dan data hasil survei lapangan', 1)

p.write_text(s, encoding="utf-8")
print("Professional dashboard applied successfully")
