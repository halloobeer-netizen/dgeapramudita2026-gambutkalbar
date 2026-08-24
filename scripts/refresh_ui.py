from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== PEATLAND HEADER REFINEMENT 2026 ===== */"
if MARKER in s:
    print("Peatland header refinement already applied")
    raise SystemExit(0)

css = r'''
    /* ===== PEATLAND HEADER REFINEMENT 2026 ===== */
    #appRoot .brand p { display:none !important; }
    #appRoot .brand h1 {
      margin:0;
      display:flex;
      align-items:center;
      min-height:50px;
      font-size:clamp(1rem,1.8vw,1.28rem);
      line-height:1;
    }
    @media (max-width:620px) {
      #appRoot .brand h1 {
        min-height:44px;
        font-size:.9rem;
        max-width:220px;
      }
    }
'''

s = s.replace("  </style>", css + "  </style>", 1)

# Remove the subtitle under PT.DGEA PRAMUDITA in the app header.
s = s.replace('          <p>Inventarisasi Karakteristik</p>\n', '', 1)

old_khg_icon = '''              <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 35h30M15 35V22l9-7 9 7v13M20 35V25h8v10" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M24 15V9M20 12h8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
              </svg>'''

new_khg_icon = '''              <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M8 35c5-4 10-4 16 0s11 4 16 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                <path d="M10 29c4-3 8-3 12 0s8 3 12 0 6-3 8-2" stroke="currentColor" stroke-width="3" stroke-linecap="round" opacity=".75"/>
                <path d="M24 27V13" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
                <path d="M24 18c-5-6-11-6-14-2 3 6 8 9 14 8" fill="currentColor" opacity=".18"/>
                <path d="M24 18c-5-6-11-6-14-2 3 6 8 9 14 8M24 17c5-6 11-6 14-2-3 6-8 9-14 8" stroke="currentColor" stroke-width="2.7" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="24" cy="36" r="2.3" fill="currentColor"/>
              </svg>'''

if old_khg_icon not in s:
    raise RuntimeError("Current KHG icon not found")
s = s.replace(old_khg_icon, new_khg_icon, 1)

p.write_text(s, encoding="utf-8")
print("Peatland header refinement applied successfully")
