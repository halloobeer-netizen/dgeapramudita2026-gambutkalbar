from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== LOGIN KAPUAS HULU 2026 ===== */"
if MARKER in s:
    print("Kapuas Hulu login subtitle already applied")
    raise SystemExit(0)

css = r'''
    /* ===== LOGIN KAPUAS HULU 2026 ===== */
    .login-title {
      font-size: clamp(1.48rem, 5vw, 2rem);
      line-height: 1.15;
      letter-spacing: -.02em;
      margin-bottom: 12px;
      font-weight: 800;
    }
    .login-subtitle {
      max-width: 440px;
      margin: 0 auto 28px;
      font-size: clamp(.84rem, 2.6vw, .96rem);
      line-height: 1.58;
      letter-spacing: .002em;
      font-weight: 500;
    }
    @media (max-width: 620px) {
      .login-title {
        font-size: clamp(1.38rem, 6.5vw, 1.72rem);
        line-height: 1.14;
      }
      .login-subtitle {
        max-width: 340px;
        font-size: .86rem;
        line-height: 1.55;
        padding: 0 6px;
      }
    }
'''

s = s.replace("  </style>", css + "  </style>", 1)

old_sub = 'Inventarisasi Karakteristik Ekosistem Gambut<br>Kalimantan Barat<br><br>Masuk menggunakan akun Google untuk melanjutkan ke dashboard.'
new_sub = 'Inventarisasi Karakteristik Ekosistem Gambut<br>Kab. Kapuas Hulu, Kalimantan Barat<br><br>Masuk menggunakan akun Google untuk melanjutkan ke dashboard.'

if old_sub not in s:
    raise RuntimeError('Current login subtitle not found')

s = s.replace(old_sub, new_sub, 1)

if 'Kab. Kapuas Hulu, Kalimantan Barat' not in s:
    raise RuntimeError('Kapuas Hulu subtitle replacement failed')

p.write_text(s, encoding="utf-8")
print("Kapuas Hulu login subtitle applied successfully")
