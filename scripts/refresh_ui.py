from pathlib import Path

p = Path("index.html")
s = p.read_text(encoding="utf-8")

MARKER = "/* ===== LOGIN FULLSCREEN 2026 ===== */"
if MARKER in s:
    print("Fullscreen login refresh already applied")
    raise SystemExit(0)

css = r'''
    /* ===== LOGIN FULLSCREEN 2026 ===== */
    .login-screen {
      min-height: 100vh;
      width: 100%;
      padding: 34px 22px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      background:
        radial-gradient(circle at 50% 42%, rgba(39, 139, 82, .20), transparent 36%),
        linear-gradient(165deg, #07351f 0%, #0a4729 50%, #082f1e 100%);
    }
    .login-screen::before {
      content: '';
      position: absolute;
      width: 125%;
      height: 52%;
      top: -26%;
      left: -12%;
      border-radius: 0 0 55% 55%;
      background: linear-gradient(135deg, rgba(41, 145, 76, .30), rgba(14, 88, 49, .10));
      transform: rotate(-9deg);
      pointer-events: none;
    }
    .login-screen::after {
      content: '';
      position: absolute;
      inset: auto 0 0 0;
      height: 34%;
      background: linear-gradient(to top, rgba(2, 24, 14, .58), rgba(2, 24, 14, 0));
      pointer-events: none;
    }
    .login-card {
      width: 100%;
      max-width: 520px;
      padding: 22px 18px;
      margin: 0 auto;
      background: transparent;
      border: 0;
      border-radius: 0;
      box-shadow: none;
      color: #fff;
      text-align: center;
      position: relative;
      z-index: 2;
    }
    .login-card .logo {
      width: 118px;
      height: 118px;
      margin: 0 auto 18px;
      background: transparent;
      border: 0;
      box-shadow: none;
      filter: drop-shadow(0 10px 24px rgba(0,0,0,.22));
    }
    .login-card .logo img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      border-radius: 24px;
    }
    .login-badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      margin: 2px auto 24px;
      padding: 8px 14px;
      border-radius: 999px;
      color: #c8f5d9;
      background: rgba(9, 47, 28, .32);
      border: 1px solid rgba(116, 225, 155, .30);
      font-size: .74rem;
      font-weight: 700;
      backdrop-filter: blur(8px);
    }
    .login-title {
      margin-bottom: 10px;
      color: #f4fff8;
      font-size: clamp(1.75rem, 6vw, 2.45rem);
      line-height: 1.14;
      letter-spacing: -.035em;
      text-shadow: 0 3px 18px rgba(0,0,0,.18);
    }
    .login-subtitle {
      max-width: 440px;
      margin: 0 auto 30px;
      color: rgba(231, 247, 237, .78);
      font-size: .94rem;
      line-height: 1.7;
    }
    .btn-google {
      width: 100%;
      max-width: 420px;
      margin: 0 auto;
      padding: 15px 20px;
      border: 0;
      border-radius: 16px;
      background: #fff;
      color: #202422;
      font-size: .98rem;
      font-weight: 800;
      box-shadow: 0 14px 34px rgba(0,0,0,.24), 0 0 26px rgba(73, 219, 126, .12);
    }
    .btn-google:hover {
      transform: translateY(-1px);
      box-shadow: 0 18px 38px rgba(0,0,0,.28), 0 0 30px rgba(73, 219, 126, .18);
    }
    .login-note {
      max-width: 430px;
      margin: 26px auto 0;
      padding: 0;
      border: 0;
      color: rgba(226, 243, 232, .70);
      font-size: .75rem;
      line-height: 1.65;
    }
    .login-note::before {
      content: '✓';
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 22px;
      height: 22px;
      margin: 0 8px 0 0;
      border: 1px solid rgba(112, 231, 154, .50);
      border-radius: 50%;
      color: #8cf0ae;
      font-weight: 800;
      vertical-align: middle;
    }
    @media (max-width: 620px) {
      .login-screen { padding: 26px 20px; align-items: center; }
      .login-card { margin: 0; padding: 16px 8px; }
      .login-card .logo { width: 104px; height: 104px; margin-bottom: 16px; }
      .login-badge { margin-bottom: 22px; }
      .login-subtitle { margin-bottom: 28px; font-size: .9rem; }
      .btn-google { max-width: 100%; padding: 15px 16px; }
      .login-note { margin-top: 24px; font-size: .71rem; }
    }
'''

s = s.replace("  </style>", css + "  </style>", 1)

s = s.replace(
    'Inventarisasi karakteristik KHG Kalimantan Barat.<br>Masuk menggunakan akun Google yang berwenang untuk melanjutkan.',
    'Inventarisasi karakteristik KHG<br>Kalimantan Barat.<br><br>Masuk menggunakan akun Google untuk melanjutkan ke dashboard.',
    1
)
s = s.replace('Masuk aman dengan Google', 'Masuk dengan Google', 1)
s = s.replace(
    'Akses dashboard dilindungi oleh Firebase Authentication. Data survei tetap tersinkron secara realtime setelah Anda masuk.',
    'Akses dashboard dilindungi oleh Firebase Authentication. Data survei tetap tersinkron secara realtime setelah Anda masuk.',
    1
)

if MARKER not in s:
    raise RuntimeError("Fullscreen login refresh failed")

p.write_text(s, encoding="utf-8")
print("Fullscreen login refresh applied successfully")
