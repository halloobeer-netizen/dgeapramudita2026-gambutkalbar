from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== LOGIN COMPANY TITLE 2026 ===== */"
if MARKER in s:
    print("Login company title already applied")
    raise SystemExit(0)

css = r'''
    /* ===== LOGIN COMPANY TITLE 2026 ===== */
    .login-title {
      font-size: clamp(1.55rem, 5.2vw, 2.15rem);
      line-height: 1.16;
      letter-spacing: -.025em;
      margin-bottom: 12px;
      font-weight: 800;
    }
    .login-subtitle {
      max-width: 430px;
      margin: 0 auto 30px;
      font-size: clamp(.88rem, 2.8vw, 1rem);
      line-height: 1.62;
      letter-spacing: .005em;
      font-weight: 500;
    }
    @media (max-width: 620px) {
      .login-title { font-size: clamp(1.45rem, 7vw, 1.9rem); }
      .login-subtitle { font-size: .92rem; line-height: 1.6; max-width: 330px; }
    }
'''

s = s.replace("  </style>", css + "  </style>", 1)

s = s.replace('>Survei Ekosistem Gambut</h2>', '>PT.DGEA PRAMUDITA</h2>', 1)

old_sub = 'Inventarisasi karakteristik KHG<br>Kalimantan Barat.<br><br>Masuk menggunakan akun Google untuk melanjutkan ke dashboard.'
new_sub = 'Inventarisasi Karakteristik Ekosistem Gambut<br>Kalimantan Barat<br><br>Masuk menggunakan akun Google untuk melanjutkan ke dashboard.'
s = s.replace(old_sub, new_sub, 1)

if 'PT.DGEA PRAMUDITA' not in s:
    raise RuntimeError('Title replacement failed')
if 'Inventarisasi Karakteristik Ekosistem Gambut' not in s:
    raise RuntimeError('Subtitle replacement failed')

p.write_text(s, encoding="utf-8")
print("Login company title applied successfully")
