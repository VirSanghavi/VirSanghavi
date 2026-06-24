#!/usr/bin/env python3
"""
Regenerate the hero banner (hero-light.png / hero-dark.png).

  python3 gen_banner.py            # writes banner.html
  # then render both themes with headless Chrome (transparent background):
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  for t in light dark; do "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --default-background-color=00000000 \
    --virtual-time-budget=3500 --window-size=1000,460 \
    --screenshot=hero-$t.png "file://$PWD/banner.html#$t"; done
  # then trim transparent margins (getbbox) before committing.

Palette mirrors virsanghavi.com:  light #006cac on #fdfdfd  ·  dark #4ade80 on #050505
Font: Atkinson Hyperlegible (loaded from Google Fonts at render time).
No avatar — GitHub already shows the profile picture next to the README.
"""
import pathlib

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet"/>
<style>
  :root { --bg:#fdfdfd; --fg:#282728; --accent:#006cac; --muted:#5f5f5f; --rule:#ece9e9; }
  html[data-theme="dark"] { --bg:#050505; --fg:#eaedf3; --accent:#4ade80; --muted:#9aa0aa; --rule:#1c1c1c; }
  * { margin:0; padding:0; box-sizing:border-box; }
  html,body { background:transparent; }
  .banner {
    width:760px; background:transparent; color:var(--fg);
    font-family:'Atkinson Hyperlegible',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    text-align:center; padding:8px;
  }
  h1 { font-size:54px; font-weight:700; line-height:1.05; letter-spacing:-0.01em; }
  h1 .at { color:var(--accent); white-space:nowrap; }
  .wave { display:block; width:330px; height:13px; margin:8px auto 0; color:var(--accent); }
  .tag { font-size:27px; font-weight:400; margin-top:22px; color:var(--fg); opacity:.9; line-height:1.35; }
  .tag .accent { color:var(--accent); font-weight:700; }
  .rule { width:104px; height:3px; background:var(--accent); border-radius:2px; margin:28px auto 16px; opacity:.9; }
  .meta { font-size:21px; color:var(--muted); display:flex; align-items:center; justify-content:center; gap:14px; }
  .meta .site { color:var(--accent); font-weight:700; }
  .meta .dot { opacity:.5; }
  .meta .italic { font-style:italic; }
</style>
</head>
<body>
  <div class="banner">
    <h1>Hi, I&#39;m <span class="at">@virsanghavi</span>.</h1>
    <svg class="wave" viewBox="0 0 340 13" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">
      <path d="M2 8 Q 18 1, 34 8 T 66 8 T 98 8 T 130 8 T 162 8 T 194 8 T 226 8 T 258 8 T 290 8 T 322 8 T 338 8"/>
    </svg>
    <div class="tag">CTO @ <span class="accent">Ravioli</span>, building a prediction market for subjective questions.</div>
    <div class="rule"></div>
    <div class="meta"><span class="site">virsanghavi.com</span><span class="dot">&bull;</span><span class="italic">building &amp; writing in public</span></div>
  </div>
<script>
  document.documentElement.setAttribute('data-theme', location.hash.replace('#','') || 'light');
</script>
</body>
</html>"""
pathlib.Path("banner.html").write_text(HTML)
print("wrote banner.html")
