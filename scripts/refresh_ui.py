from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== DASHBOARD REFERENCE ALIGNMENT 2026 ===== */"
if MARKER in s:
    print("Dashboard reference alignment already applied")
    raise SystemExit(0)

css = r'''
    /* ===== DASHBOARD REFERENCE ALIGNMENT 2026 ===== */
    #appRoot .app-header {
      background: linear-gradient(110deg, #074a2d 0%, #075d34 52%, #064329 100%);
      min-height: 76px;
      padding: 12px 22px;
    }
    #appRoot .brand { gap: 12px; }
    #appRoot .brand-logo {
      width: 50px; height: 50px; min-width: 50px;
      border-radius: 12px; padding: 3px; background: #fff;
      box-shadow: 0 5px 14px rgba(0,0,0,.12);
    }
    #appRoot .brand h1 {
      font-size: clamp(.98rem, 1.7vw, 1.22rem);
      line-height: 1.08;
      font-weight: 850;
      letter-spacing: -.02em;
      color: #fff;
    }
    #appRoot .brand p {
      margin-top: 3px;
      font-size: clamp(.62rem, 1vw, .72rem);
      color: rgba(255,255,255,.74);
      line-height: 1.2;
    }

    #view-dashboard .stats-row {
      grid-template-columns: repeat(2,minmax(0,1fr));
      gap: 16px;
      margin-top: 16px;
      margin-bottom: 18px;
    }
    #view-dashboard .stat-card,
    #view-dashboard .stat-card.green {
      min-height: 146px;
      padding: 22px;
      display: grid;
      grid-template-columns: 78px minmax(0,1fr);
      gap: 20px;
      align-items: center;
      background: #fff;
      color: var(--text);
      border: 1px solid #dfe8e2;
      border-radius: 16px;
      box-shadow: 0 8px 24px rgba(18,55,35,.055);
    }
    #view-dashboard .stat-card::before,
    #view-dashboard .stat-card::after { display:none !important; content:none !important; }
    #view-dashboard .stat-icon {
      width: 78px; height: 78px;
      border-radius: 15px;
      display:flex; align-items:center; justify-content:center;
      background: linear-gradient(145deg, #edf8f1, #e4f2e9);
      color: #087a3d;
    }
    #view-dashboard .stat-icon svg { width: 42px; height: 42px; display:block; }
    #view-dashboard .stat-content { min-width:0; }
    #view-dashboard .stat-card .label {
      color:#25352b;
      font-size:.88rem;
      font-weight:800;
      margin:0 0 4px;
    }
    #view-dashboard .stat-card .value {
      color:#08733c;
      font-size:2.35rem;
      line-height:1;
      margin:7px 0 7px;
      letter-spacing:-.045em;
    }
    #view-dashboard .stat-card .stat-note {
      color:#6d7871;
      font-size:.74rem;
      line-height:1.4;
    }

    #view-dashboard .summary-box {
      border-radius: 16px;
      border-color:#dfe8e2;
      box-shadow:0 8px 24px rgba(18,55,35,.05);
    }
    #view-dashboard .summary-item {
      background:#fbfdfb;
      border-color:#e2ebe5;
    }

    @media (max-width:620px) {
      #appRoot .app-header { min-height:68px; padding:10px 12px; }
      #appRoot .brand-logo { width:44px; height:44px; min-width:44px; border-radius:11px; }
      #appRoot .brand { gap:9px; }
      #appRoot .brand h1 { font-size:.86rem; max-width:210px; }
      #appRoot .brand p { font-size:.58rem; }
      #view-dashboard .stats-row { gap:10px; margin-top:13px; }
      #view-dashboard .stat-card,
      #view-dashboard .stat-card.green {
        min-height:124px;
        padding:14px;
        grid-template-columns:48px minmax(0,1fr);
        gap:10px;
        border-radius:14px;
      }
      #view-dashboard .stat-icon { width:48px; height:48px; border-radius:12px; }
      #view-dashboard .stat-icon svg { width:28px; height:28px; }
      #view-dashboard .stat-card .label { font-size:.72rem; }
      #view-dashboard .stat-card .value { font-size:1.75rem; margin:5px 0 4px; }
      #view-dashboard .stat-card .stat-note { font-size:.62rem; }
    }
'''

s = s.replace("  </style>", css + "  </style>", 1)

# Header brand: match the professional reference while preserving the existing logo.
s = s.replace('<h1>Survei Ekosistem Gambut</h1>', '<h1>PT.DGEA PRAMUDITA</h1>', 1)

old_stats = '''        <div class="stats-row">
          <div class="stat-card green">
            <div class="label">Total KHG</div>
            <div class="value" id="statKHG">0</div>
          </div>
          <div class="stat-card">
            <div class="label">Titik Tersurvei</div>
            <div class="value" id="statPoints">0</div>
            <div class="stat-note">dari target 1.073 titik</div>
          </div>
        </div>'''

new_stats = '''        <div class="stats-row">
          <div class="stat-card green">
            <div class="stat-icon" aria-hidden="true">
              <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 35h30M15 35V22l9-7 9 7v13M20 35V25h8v10" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M24 15V9M20 12h8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
              </svg>
            </div>
            <div class="stat-content">
              <div class="label">Total KHG</div>
              <div class="value" id="statKHG">0</div>
              <div class="stat-note">Kesatuan Hidrologis Gambut aktif</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" aria-hidden="true">
              <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M24 42s13-12.5 13-24a13 13 0 1 0-26 0c0 11.5 13 24 13 24Z" fill="currentColor" opacity=".16"/>
                <path d="M24 42s13-12.5 13-24a13 13 0 1 0-26 0c0 11.5 13 24 13 24Z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
                <circle cx="24" cy="18" r="4.5" fill="currentColor"/>
              </svg>
            </div>
            <div class="stat-content">
              <div class="label">Titik Tersurvei</div>
              <div class="value" id="statPoints">0</div>
              <div class="stat-note">dari target 1.073 titik</div>
            </div>
          </div>
        </div>'''

if old_stats not in s:
    raise RuntimeError("Current stat cards not found")
s = s.replace(old_stats, new_stats, 1)

if 'PT.DGEA PRAMUDITA' not in s:
    raise RuntimeError('Header branding replacement failed')
if 'class="stat-icon"' not in s:
    raise RuntimeError('KPI icons were not inserted')

p.write_text(s, encoding="utf-8")
print("Dashboard reference alignment applied successfully")
