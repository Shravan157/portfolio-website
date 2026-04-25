import streamlit as st

st.set_page_config(
    page_title="Shravan Parthe — Space Explorer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Sora:wght@300;400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
"""

PORTFOLIO = """
<style>
/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, header, footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.stDeployButton,
[data-testid="stAppViewBlockContainer"] > div > div > div[style] {
  display: none !important;
}
.block-container {
  padding: 0 !important;
  max-width: 100% !important;
}
[data-testid="stAppViewContainer"] > section > div:first-child {
  padding: 0 !important;
}
[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* ── VARIABLES ── */
:root {
  --void:   #000208;
  --deep:   #020b1a;
  --surf:   rgba(255,255,255,0.03);
  --surf2:  rgba(255,255,255,0.06);
  --bd:     rgba(255,255,255,0.07);
  --bd2:    rgba(255,255,255,0.14);
  --text:   #ccd6f6;
  --muted:  #8892b0;
  --sub:    #495670;
  --cyan:   #64ffda;
  --gold:   #ffd54f;
  --gold2:  #ffab40;
  --violet: #7c4dff;
  --blue:   #2979ff;
  --green:  #00e676;
  --pink:   #f06292;
  --h:      'Orbitron', 'Courier New', monospace;
  --b:      'Sora', system-ui, sans-serif;
  --m:      'Space Mono', 'Courier New', monospace;
}

*,*::before,*::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body, #sp { background: var(--void); color: var(--text); font-family: var(--b); line-height: 1.6; overflow-x: hidden; -webkit-font-smoothing: antialiased; }
::selection { background: var(--violet); color: #fff; }
::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: var(--void); }
::-webkit-scrollbar-thumb { background: var(--violet); border-radius: 99px; }

/* ── CANVAS + NEBULA ── */
#spaceCanvas {
  position: fixed; inset: 0; width: 100%; height: 100%;
  z-index: 0; pointer-events: none;
}
.neb {
  position: fixed; border-radius: 50%; pointer-events: none; z-index: 1;
  animation: neb-drift 22s ease-in-out infinite alternate;
}
.n1 { width: 700px; height: 700px; background: radial-gradient(circle, #7c4dff55, transparent); top: -250px; left: -250px; opacity:.22; animation-delay:0s; }
.n2 { width: 550px; height: 550px; background: radial-gradient(circle, #2979ff44, transparent); top: 25%; right: -180px; opacity:.20; animation-delay:-8s; }
.n3 { width: 450px; height: 450px; background: radial-gradient(circle, #00e5ff22, transparent); bottom: -120px; left: 25%; opacity:.15; animation-delay:-16s; }
.n4 { width: 300px; height: 300px; background: radial-gradient(circle, #f0629233, transparent); top: 60%; left: 10%; opacity:.12; animation-delay:-5s; }
@keyframes neb-drift {
  from { transform: translate(0,0) scale(1); filter: blur(80px); }
  to   { transform: translate(40px,60px) scale(1.12); filter: blur(90px); }
}

/* ── LAYOUT ── */
#sp { position: relative; z-index: 2; }
.w { max-width: 1140px; margin: 0 auto; padding: 0 clamp(1.25rem,5vw,3.5rem); }

/* ── SCANLINE OVERLAY ── */
#sp::before {
  content: '';
  position: fixed; inset: 0; z-index: 3; pointer-events: none;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.03) 2px, rgba(0,0,0,0.03) 4px);
  animation: scan 8s linear infinite;
}
@keyframes scan {
  from { background-position: 0 0; }
  to   { background-position: 0 100vh; }
}

/* ── NAV ── */
#nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 999;
  padding: .9rem 0;
  background: rgba(0,2,8,0.75);
  backdrop-filter: blur(24px);
  border-bottom: 1px solid rgba(100,255,218,0.07);
}
.nav-in {
  max-width: 1140px; margin: 0 auto;
  padding: 0 clamp(1.25rem,5vw,3.5rem);
  display: flex; align-items: center; justify-content: space-between;
}
.logo {
  font-family: var(--h); font-size: 1rem; font-weight: 800;
  color: var(--cyan); text-decoration: none; letter-spacing: 3px;
}
.logo sup { color: var(--gold); font-size: .6rem; }
.nav-links { display: flex; gap: 2.5rem; align-items: center; }
.nav-links a {
  color: var(--muted); text-decoration: none;
  font-family: var(--m); font-size: .6rem; letter-spacing: 2.5px;
  text-transform: uppercase; transition: color .2s;
}
.nav-links a:hover { color: var(--cyan); }
.signal-pill {
  display: flex; align-items: center; gap: .4rem;
  padding: .28rem .75rem;
  border: 1px solid rgba(0,230,118,.25);
  border-radius: 99px; font-family: var(--m); font-size: .58rem;
  color: var(--green); background: rgba(0,230,118,.06);
  letter-spacing: 1.5px;
}
.sdot {
  width: 5px; height: 5px; border-radius: 50%;
  background: var(--green); box-shadow: 0 0 8px var(--green);
  animation: pulse 2.2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1;box-shadow:0 0 8px var(--green)} 50%{opacity:.3;box-shadow:0 0 2px var(--green)} }

/* ── HERO ── */
#hero {
  min-height: 100vh; display: flex; align-items: center;
  padding: 8rem 0 5rem; position: relative;
}
.hero-grid {
  display: grid; grid-template-columns: 1fr 460px;
  gap: 3rem; align-items: center; width: 100%;
}
.coords {
  font-family: var(--m); font-size: .6rem; color: var(--cyan);
  letter-spacing: 3px; text-transform: uppercase; margin-bottom: 1.5rem;
  display: flex; align-items: center; gap: .6rem;
}
.coords span { opacity: .4; }
.htitle {
  font-family: var(--h);
  font-size: clamp(2.6rem,6vw,5rem);
  font-weight: 900; line-height: 1.04;
  text-transform: uppercase; margin-bottom: .5rem;
  letter-spacing: -1px;
}
.htitle .glow {
  color: var(--cyan);
  text-shadow: 0 0 40px rgba(100,255,218,.45), 0 0 90px rgba(100,255,218,.15);
}
.htitle .dim { color: var(--text); }
.sub-role {
  font-family: var(--m); font-size: .78rem; color: var(--gold);
  letter-spacing: 2.5px; text-transform: uppercase; margin-bottom: 2rem;
}
.sub-role::before { content: '// '; color: var(--sub); }
.hdesc {
  color: var(--muted); font-size: .93rem; line-height: 1.9;
  max-width: 500px; margin-bottom: 2.5rem;
}
.hdesc strong { color: var(--text); font-weight: 600; }
.ctas { display: flex; gap: .75rem; flex-wrap: wrap; }
.btn-a {
  display: inline-flex; align-items: center; gap: .5rem;
  padding: .8rem 1.8rem;
  background: linear-gradient(135deg, var(--cyan), #26c6da);
  color: #000; border-radius: 3px; text-decoration: none;
  font-family: var(--m); font-size: .65rem; font-weight: 700;
  letter-spacing: 2.5px; text-transform: uppercase;
  transition: all .25s; box-shadow: 0 0 24px rgba(100,255,218,.2);
}
.btn-a:hover { transform: translateY(-3px); box-shadow: 0 8px 32px rgba(100,255,218,.35); }
.btn-b {
  display: inline-flex; align-items: center; gap: .5rem;
  padding: .78rem 1.5rem;
  border: 1px solid rgba(100,255,218,.3); color: var(--cyan);
  border-radius: 3px; text-decoration: none;
  font-family: var(--m); font-size: .65rem; letter-spacing: 2.5px;
  text-transform: uppercase; transition: all .25s;
  background: rgba(100,255,218,.04);
}
.btn-b:hover { border-color: var(--cyan); background: rgba(100,255,218,.1); transform: translateY(-3px); }

/* ── ASTRONAUT ── */
.hero-r { display: flex; justify-content: center; align-items: center; position: relative; }
.astro-wrap {
  position: relative; width: 300px; height: 360px;
  animation: afloat 7s ease-in-out infinite;
}
@keyframes afloat {
  0%,100% { transform: translateY(0) rotate(-1.5deg); }
  50%      { transform: translateY(-22px) rotate(1.5deg); }
}
.orbit {
  position: absolute; top: 50%; left: 50%;
  width: 360px; height: 110px;
  transform: translate(-50%,-50%) rotateX(72deg);
  border: 1px solid rgba(100,255,218,.22);
  border-radius: 50%;
  animation: orbit-spin 9s linear infinite;
}
.orbit-satellite {
  position: absolute; width: 8px; height: 8px;
  background: var(--cyan); border-radius: 50%;
  top: -4px; left: 50%; margin-left: -4px;
  box-shadow: 0 0 14px var(--cyan), 0 0 28px rgba(100,255,218,.4);
}
@keyframes orbit-spin { to { transform: translate(-50%,-50%) rotateX(72deg) rotate(360deg); } }
.pmini { position: absolute; border-radius: 50%; }
.pm1 {
  width: 65px; height: 65px;
  background: radial-gradient(circle at 35% 30%, #9c4dcc, #1a0040);
  bottom: 10px; right: -30px;
  box-shadow: 0 0 30px rgba(156,77,204,.4);
  animation: afloat 8s ease-in-out infinite reverse;
}
.pm2 {
  width: 38px; height: 38px;
  background: radial-gradient(circle at 35% 30%, #ffd54f, #e65100);
  top: 20px; left: -15px;
  box-shadow: 0 0 20px rgba(255,213,79,.35);
  animation: afloat 5s ease-in-out infinite;
}
/* Saturn ring on pm1 */
.pm1::after {
  content: '';
  position: absolute; top: 50%; left: 50%;
  width: 90px; height: 20px;
  border: 2px solid rgba(156,77,204,.5);
  border-radius: 50%; transform: translate(-50%,-50%) rotateX(70deg);
}

/* ── HUD CORNER ── */
.hud-corner {
  position: absolute; top: 0; right: 0;
  width: 90px; height: 90px; opacity: .25;
}
.hud-scan {
  position: absolute; top: 0; right: 0;
  width: 80px; height: 80px;
  border: 1px solid var(--cyan); border-radius: 50%;
  opacity: .15;
  animation: hud-rot 6s linear infinite;
}
.hud-scan::before {
  content: '';
  position: absolute; top: 50%; left: 50%;
  width: 80px; height: 2px; margin-left: 0; margin-top: -1px;
  background: linear-gradient(90deg, var(--cyan), transparent);
  transform-origin: left center;
}
@keyframes hud-rot { to { transform: rotate(360deg); } }

/* ── STATS ── */
#stats { padding: 4rem 0 5rem; }
.mission-badge {
  text-align: center; margin-bottom: 2.5rem;
}
.mbadge {
  display: inline-flex; align-items: center; gap: .6rem;
  font-family: var(--m); font-size: .6rem; letter-spacing: 3px;
  text-transform: uppercase; color: var(--cyan); padding: .3rem 1rem;
  border: 1px solid rgba(100,255,218,.2); border-radius: 99px;
}
.mbadge::before,.mbadge::after { content: '◈'; opacity: .5; }
.stats-grid {
  display: grid; grid-template-columns: repeat(4,1fr);
  gap: 1px; background: var(--bd);
  border: 1px solid var(--bd); border-radius: 6px; overflow: hidden;
}
.stat-box {
  background: var(--surf); padding: 2rem 1.5rem; text-align: center;
  position: relative; transition: background .3s; overflow: hidden;
}
.stat-box::after {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, var(--cyan), transparent);
  opacity: 0; transition: opacity .3s;
}
.stat-box:hover { background: var(--surf2); }
.stat-box:hover::after { opacity: 1; }
.snum {
  font-family: var(--h); font-size: 2.4rem; font-weight: 800;
  line-height: 1; margin-bottom: .3rem;
  background: linear-gradient(135deg, var(--cyan), var(--blue));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.slbl { font-family: var(--m); font-size: .55rem; letter-spacing: 2.5px; text-transform: uppercase; color: var(--muted); }

/* ── SECTION HEAD ── */
.sh {
  display: flex; align-items: center; gap: .75rem;
  margin-bottom: 3rem; padding-top: .25rem;
}
.sh-num { font-family: var(--m); font-size: .6rem; color: var(--cyan); letter-spacing: 2px; }
.sh-ico { font-size: .95rem; }
.sh-title {
  font-family: var(--h); font-size: .68rem; font-weight: 700;
  letter-spacing: 4px; text-transform: uppercase; color: var(--text);
}
.sh-line { flex: 1; height: 1px; background: linear-gradient(90deg, var(--bd2), transparent); }

/* ── SKILLS ── */
#skills { padding: 5rem 0; }
.skills-g { display: grid; grid-template-columns: repeat(2,1fr); gap: .75rem; }
.sk-card {
  border: 1px solid var(--bd); border-radius: 6px;
  padding: 1.5rem; background: var(--surf);
  position: relative; overflow: hidden; transition: border-color .3s, background .3s;
}
.sk-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, var(--cyan), transparent);
  opacity: 0; transition: opacity .3s;
}
.sk-card:hover { border-color: rgba(100,255,218,.2); background: var(--surf2); }
.sk-card:hover::before { opacity: 1; }
.sk-lbl {
  font-family: var(--m); font-size: .57rem; letter-spacing: 2.5px;
  text-transform: uppercase; color: var(--cyan);
  margin-bottom: .9rem; display: flex; align-items: center; gap: .45rem;
}
.sk-lbl::before { content: '▶'; font-size: .45rem; opacity: .7; }
.chips { display: flex; flex-wrap: wrap; gap: .38rem; }
.chip {
  padding: .24rem .65rem; border-radius: 3px;
  font-family: var(--m); font-size: .67rem;
  transition: transform .15s, box-shadow .15s; cursor: default;
}
.chip:hover { transform: translateY(-2px); }
.cl { background: rgba(100,255,218,.07); color: var(--cyan); border: 1px solid rgba(100,255,218,.2); }
.cl:hover { box-shadow: 0 4px 14px rgba(100,255,218,.2); }
.cf { background: rgba(124,77,255,.08); color: #b39ddb; border: 1px solid rgba(124,77,255,.22); }
.cf:hover { box-shadow: 0 4px 14px rgba(124,77,255,.2); }
.ct { background: rgba(41,121,255,.07); color: #90caf9; border: 1px solid rgba(41,121,255,.2); }
.ct:hover { box-shadow: 0 4px 14px rgba(41,121,255,.2); }
.cd { background: rgba(255,213,79,.07); color: var(--gold); border: 1px solid rgba(255,213,79,.22); }
.cd:hover { box-shadow: 0 4px 14px rgba(255,213,79,.2); }

/* ── MISSIONS / PROJECTS ── */
#missions { padding: 5rem 0; }
.ml { display: flex; flex-direction: column; }
.mi {
  display: grid; grid-template-columns: 72px 1fr;
  border-top: 1px solid var(--bd);
  padding: 2.25rem 0; position: relative;
  overflow: hidden;
}
.mi:last-child { border-bottom: 1px solid var(--bd); }
.mi::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px;
  background: linear-gradient(to bottom, transparent, var(--cyan), transparent);
  opacity: 0; transition: opacity .35s;
}
.mi:hover::before { opacity: 1; }
.mi-num { font-family: var(--m); font-size: .58rem; color: var(--sub); padding-top: .3rem; letter-spacing: 1.5px; }
.mi-top {
  display: flex; align-items: flex-start; justify-content: space-between;
  gap: 1rem; margin-bottom: .55rem;
}
.mi-name {
  font-family: var(--h); font-size: .9rem; font-weight: 600;
  color: var(--text); letter-spacing: .5px;
}
.mi-tag {
  padding: .18rem .6rem; border-radius: 2px;
  font-family: var(--m); font-size: .55rem; letter-spacing: 1px;
  text-transform: uppercase; white-space: nowrap; flex-shrink: 0;
}
.t-ai  { background: rgba(183,148,244,.1); color: #b794f4; border: 1px solid rgba(183,148,244,.22); }
.t-ft  { background: rgba(100,255,218,.08); color: var(--cyan); border: 1px solid rgba(100,255,218,.2); }
.t-fs  { background: rgba(128,203,196,.08); color: #80cbc4; border: 1px solid rgba(128,203,196,.2); }
.t-ml  { background: rgba(255,213,79,.08);  color: var(--gold); border: 1px solid rgba(255,213,79,.2); }
.mi-desc { color: var(--muted); font-size: .84rem; line-height: 1.82; margin-bottom: .9rem; max-width: 700px; }
.mi-foot { display: flex; align-items: center; justify-content: space-between; }
.mi-tech { display: flex; flex-wrap: wrap; gap: .3rem; }
.tt {
  padding: .14rem .48rem; border-radius: 2px;
  font-family: var(--m); font-size: .6rem; color: var(--sub); border: 1px solid var(--bd);
}
.mi-link {
  display: inline-flex; align-items: center; gap: .3rem;
  font-family: var(--m); font-size: .62rem; color: var(--muted);
  text-decoration: none; transition: color .2s;
  flex-shrink: 0; margin-left: 1rem;
}
.mi-link:hover { color: var(--cyan); }
.mi-link svg { transition: transform .2s; }
.mi-link:hover svg { transform: translate(2px,-2px); }

/* ── EXPERIENCE ── */
#log { padding: 5rem 0; }
.exp-g { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.exp-card {
  border: 1px solid var(--bd); border-radius: 6px;
  padding: 2rem; background: var(--surf);
  position: relative; overflow: hidden; transition: border-color .3s, background .3s;
}
.exp-card:hover { border-color: rgba(100,255,218,.18); background: var(--surf2); }
.exp-card::after {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--cyan), var(--violet), transparent);
  opacity: 0; transition: opacity .35s;
}
.exp-card:hover::after { opacity: 1; }
.ep { font-family: var(--m); font-size: .58rem; color: var(--cyan); letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: .7rem; }
.er { font-family: var(--h); font-size: .88rem; color: var(--text); font-weight: 600; margin-bottom: .2rem; letter-spacing: .5px; }
.eo { font-family: var(--m); font-size: .72rem; color: var(--gold); margin-bottom: 1.2rem; }
.el { list-style: none; }
.el li { color: var(--muted); font-size: .82rem; line-height: 1.75; padding: .15rem 0 .15rem 1.25rem; position: relative; }
.el li::before { content: '›'; position: absolute; left: 0; color: var(--cyan); font-size: 1.1rem; line-height: 1.4; }
.active-badge {
  display: inline-flex; align-items: center; gap: .4rem; margin-top: 1.25rem;
  padding: .28rem .75rem; border-radius: 99px;
  font-family: var(--m); font-size: .58rem; color: var(--green);
  border: 1px solid rgba(0,230,118,.25); background: rgba(0,230,118,.06);
}
.cgpa {
  display: inline-block; margin-top: 1.25rem;
  padding: .28rem .75rem; border-radius: 3px;
  font-family: var(--m); font-size: .65rem; color: var(--gold);
  border: 1px solid rgba(255,213,79,.25); background: rgba(255,213,79,.06);
}

/* ── CONTACT ── */
#contact { padding: 5rem 0 8rem; }
.contact-g { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; }
.ch {
  font-family: var(--h);
  font-size: clamp(2rem,4vw,2.8rem);
  font-weight: 800; text-transform: uppercase;
  line-height: 1.08; margin-bottom: 1.25rem; letter-spacing: -.5px;
}
.ch span { color: var(--cyan); text-shadow: 0 0 30px rgba(100,255,218,.3); }
.csub { color: var(--muted); font-size: .88rem; line-height: 1.8; margin-bottom: 2rem; }
.ccs { display: grid; grid-template-columns: 1fr 1fr; gap: .6rem; }
.cc {
  border: 1px solid var(--bd); border-radius: 5px;
  padding: 1rem 1.2rem; background: var(--surf);
  transition: all .25s;
}
.cc:hover { border-color: rgba(100,255,218,.2); background: var(--surf2); transform: translateY(-2px); }
.ccl { font-family: var(--m); font-size: .55rem; letter-spacing: 2.5px; text-transform: uppercase; color: var(--cyan); margin-bottom: .3rem; }
.ccv { font-size: .82rem; color: var(--text); }
.ccv a { color: var(--muted); text-decoration: none; transition: color .2s; }
.ccv a:hover { color: var(--cyan); }
.cc.wide { grid-column: span 2; }

/* ── QUOTE ── */
.qwrap {
  border-top: 1px solid var(--bd);
  padding: 5rem 0; text-align: center; position: relative;
}
.qwrap::before {
  content: '';
  position: absolute; top: 0; left: 50%; transform: translateX(-50%);
  width: 120px; height: 1px;
  background: linear-gradient(90deg, transparent, var(--cyan), transparent);
}
.qmark {
  font-family: var(--h); font-size: 3.5rem; line-height: 1;
  color: var(--sub); display: block; margin-bottom: 1.5rem;
}
.qtext {
  font-family: var(--b); font-size: 1rem; line-height: 2.1;
  color: var(--muted); max-width: 560px; margin: 0 auto 1.25rem;
  font-style: italic;
}
.qtext em { color: var(--cyan); font-style: normal; }
.qsrc { font-family: var(--m); font-size: .58rem; letter-spacing: 3px; text-transform: uppercase; color: var(--sub); }

/* ── ROCKET BTN ── */
.rkt-btn {
  position: fixed; bottom: 2rem; right: 2rem; z-index: 50;
  width: 44px; cursor: pointer; text-decoration: none;
  filter: drop-shadow(0 0 10px rgba(100,255,218,.4));
  animation: rkt-idle 3.5s ease-in-out infinite;
  transition: filter .3s;
}
.rkt-btn:hover { filter: drop-shadow(0 0 20px rgba(100,255,218,.7)); }
@keyframes rkt-idle {
  0%,100% { transform: translateY(0) rotate(0deg); }
  50%      { transform: translateY(-10px) rotate(2deg); }
}

/* ── FOOTER ── */
#foot {
  border-top: 1px solid var(--bd);
  padding: 1.5rem 0;
}
.fi {
  max-width: 1140px; margin: 0 auto;
  padding: 0 clamp(1.25rem,5vw,3.5rem);
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 1rem;
}
.fl { font-family: var(--m); font-size: .62rem; color: var(--sub); }
.fl a { color: var(--muted); text-decoration: none; }
.flinks { display: flex; gap: 1.5rem; }
.flinks a {
  font-family: var(--m); font-size: .6rem; letter-spacing: 1.5px;
  color: var(--sub); text-decoration: none; text-transform: uppercase; transition: color .2s;
}
.flinks a:hover { color: var(--cyan); }

/* ── REVEAL ── */
.rev { opacity: 0; transform: translateY(26px); transition: opacity .7s ease, transform .7s ease; }
.rev.in { opacity: 1; transform: none; }

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
  .hero-grid { grid-template-columns: 1fr; }
  .hero-r { display: none; }
  .stats-grid { grid-template-columns: repeat(2,1fr); }
  .skills-g { grid-template-columns: 1fr; }
  .exp-g { grid-template-columns: 1fr; }
  .contact-g { grid-template-columns: 1fr; gap: 3rem; }
  .nav-links a:not(.signal-pill) { display: none; }
}
@media (max-width: 560px) {
  .ccs { grid-template-columns: 1fr; }
  .cc.wide { grid-column: span 1; }
}
</style>

<!-- ════ BACKGROUND LAYERS ════ -->
<canvas id="spaceCanvas"></canvas>
<div class="neb n1"></div>
<div class="neb n2"></div>
<div class="neb n3"></div>
<div class="neb n4"></div>

<div id="sp">

<!-- ════ NAV ════ -->
<nav id="nav">
  <div class="nav-in">
    <a href="#hero" class="logo">SP<sup>®</sup></a>
    <div class="nav-links">
      <a href="#skills">Equipment</a>
      <a href="#missions">Missions</a>
      <a href="#log">Log</a>
      <a href="#contact">Contact</a>
      <div class="signal-pill"><div class="sdot"></div>Signal Active</div>
    </div>
  </div>
</nav>

<!-- ════ HERO ════ -->
<section id="hero">
  <div class="w">
    <div class="hero-grid">

      <!-- LEFT -->
      <div>
        <div class="coords rev">
          ◈ LAT 19.0760°N <span>·</span> LON 72.8777°E <span>·</span> ALT ∞
        </div>
        <h1 class="htitle rev">
          <span class="glow">Shravan</span><br>
          <span class="dim">Parthe.</span>
        </h1>
        <div class="sub-role rev">Backend Engineer & AI Developer</div>
        <p class="hdesc rev">
          <strong>3rd year B.Tech CSE (AI&ML)</strong> student crafting production-grade systems that explore the edge of what's possible. Building with Java, Spring Boot, and Python. Currently on active mission at <strong>Innovexis</strong> — deploying real-world Gen AI integrations.
        </p>
        <div class="ctas rev">
          <a href="mailto:shravanparthe@gmail.com" class="btn-a">🚀 Launch Contact</a>
          <a href="https://github.com/Shravan157" target="_blank" class="btn-b">⚡ Explore Work</a>
        </div>
      </div>

      <!-- RIGHT: ASTRONAUT -->
      <div class="hero-r rev">
        <div class="astro-wrap">
          <div class="orbit"><div class="orbit-satellite"></div></div>
          <svg viewBox="0 0 200 280" xmlns="http://www.w3.org/2000/svg" width="290" style="position:relative;z-index:2;display:block;margin:auto;">
            <defs>
              <radialGradient id="vg" cx="38%" cy="32%">
                <stop offset="0%" stop-color="#82b1ff" stop-opacity=".95"/>
                <stop offset="100%" stop-color="#0d47a1" stop-opacity=".75"/>
              </radialGradient>
              <radialGradient id="sg" cx="33%" cy="28%">
                <stop offset="0%" stop-color="#263238"/>
                <stop offset="100%" stop-color="#080818"/>
              </radialGradient>
              <radialGradient id="fg1" cx="50%" cy="0%">
                <stop offset="0%" stop-color="#64ffda"/>
                <stop offset="55%" stop-color="#2979ff"/>
                <stop offset="100%" stop-color="transparent"/>
              </radialGradient>
              <radialGradient id="fg2" cx="50%" cy="0%">
                <stop offset="0%" stop-color="#64ffda"/>
                <stop offset="55%" stop-color="#7c4dff"/>
                <stop offset="100%" stop-color="transparent"/>
              </radialGradient>
              <filter id="gf">
                <feGaussianBlur stdDeviation="1.5" result="b"/>
                <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
            </defs>
            <!-- Jetpack -->
            <rect x="78" y="136" width="44" height="54" rx="9" fill="#0d1b2a" stroke="#455a64" stroke-width="1.5"/>
            <rect x="83" y="144" width="11" height="18" rx="4" fill="#006064" opacity=".7"/>
            <rect x="107" y="144" width="11" height="18" rx="4" fill="#006064" opacity=".7"/>
            <!-- Thruster flames -->
            <ellipse cx="88" cy="196" rx="6" ry="14" fill="url(#fg1)" opacity=".85">
              <animate attributeName="ry" values="14;17;11;15;14" dur="0.38s" repeatCount="indefinite"/>
            </ellipse>
            <ellipse cx="112" cy="196" rx="6" ry="14" fill="url(#fg2)" opacity=".85">
              <animate attributeName="ry" values="11;15;13;12;11" dur="0.32s" repeatCount="indefinite"/>
            </ellipse>
            <ellipse cx="88" cy="193" rx="3" ry="7" fill="#64ffda" opacity=".7">
              <animate attributeName="ry" values="7;9;5;8;7" dur="0.25s" repeatCount="indefinite"/>
            </ellipse>
            <ellipse cx="112" cy="193" rx="3" ry="7" fill="#64ffda" opacity=".7">
              <animate attributeName="ry" values="6;8;7;5;6" dur="0.3s" repeatCount="indefinite"/>
            </ellipse>
            <!-- Body -->
            <rect x="54" y="126" width="92" height="84" rx="24" fill="url(#sg)" stroke="#546e7a" stroke-width="1.5"/>
            <!-- Arms -->
            <rect x="16" y="131" width="39" height="28" rx="14" fill="url(#sg)" stroke="#546e7a" stroke-width="1.5"/>
            <rect x="145" y="131" width="39" height="28" rx="14" fill="url(#sg)" stroke="#546e7a" stroke-width="1.5"/>
            <!-- Gloves -->
            <ellipse cx="23" cy="160" rx="10" ry="8" fill="#37474f" stroke="#64ffda" stroke-width="1"/>
            <ellipse cx="177" cy="160" rx="10" ry="8" fill="#37474f" stroke="#64ffda" stroke-width="1"/>
            <!-- Legs -->
            <rect x="61" y="204" width="33" height="55" rx="16" fill="url(#sg)" stroke="#546e7a" stroke-width="1.5"/>
            <rect x="106" y="204" width="33" height="55" rx="16" fill="url(#sg)" stroke="#546e7a" stroke-width="1.5"/>
            <!-- Boots -->
            <ellipse cx="78" cy="260" rx="22" ry="9" fill="#1c2833" stroke="#546e7a" stroke-width="1"/>
            <ellipse cx="122" cy="260" rx="22" ry="9" fill="#1c2833" stroke="#546e7a" stroke-width="1"/>
            <!-- Helmet -->
            <ellipse cx="100" cy="88" rx="54" ry="60" fill="url(#sg)" stroke="#546e7a" stroke-width="2"/>
            <!-- Visor -->
            <ellipse cx="100" cy="92" rx="37" ry="38" fill="url(#vg)" stroke="#2979ff" stroke-width="1.5" filter="url(#gf)"/>
            <!-- Visor shimmer -->
            <ellipse cx="87" cy="79" rx="9" ry="14" fill="white" opacity=".1" transform="rotate(-18,87,79)"/>
            <ellipse cx="108" cy="76" rx="4" ry="7" fill="white" opacity=".07"/>
            <!-- Stars reflection in visor -->
            <circle cx="95" cy="95" r="1.2" fill="#64ffda" opacity=".6"/>
            <circle cx="110" cy="88" r="0.8" fill="#64ffda" opacity=".5"/>
            <circle cx="88" cy="100" r="0.7" fill="white" opacity=".5"/>
            <!-- Helmet stripe -->
            <path d="M50 82 Q100 60 150 82" stroke="#64ffda" stroke-width="1.5" fill="none" opacity=".4"/>
            <!-- Chest display -->
            <rect x="66" y="142" width="20" height="16" rx="3" fill="#0a192f" stroke="#64ffda" stroke-width="1" opacity=".85"/>
            <circle cx="71" cy="147" r="2.2" fill="#00e676"/>
            <circle cx="79" cy="147" r="2.2" fill="#ffd54f"/>
            <circle cx="71" cy="154" r="2.2" fill="#2979ff"/>
            <circle cx="79" cy="154" r="2.2" fill="#ff5252"/>
            <!-- Chest emblem -->
            <circle cx="100" cy="163" r="14" fill="none" stroke="#64ffda" stroke-width="1.5" opacity=".65"/>
            <text x="100" y="168" text-anchor="middle" fill="#64ffda" font-size="9" font-family="Orbitron" font-weight="700">SP</text>
            <!-- Shoulder patches -->
            <rect x="51" y="126" width="20" height="9" rx="4" fill="#0d1b2a" stroke="#64ffda" stroke-width="1"/>
            <rect x="129" y="126" width="20" height="9" rx="4" fill="#0d1b2a" stroke="#64ffda" stroke-width="1"/>
            <!-- Antenna -->
            <line x1="100" y1="28" x2="100" y2="14" stroke="#64ffda" stroke-width="1.5" opacity=".7"/>
            <circle cx="100" cy="11" r="3.5" fill="#64ffda" opacity=".8">
              <animate attributeName="opacity" values="0.8;0.3;0.8" dur="1.2s" repeatCount="indefinite"/>
            </circle>
          </svg>
          <div class="pmini pm1"></div>
          <div class="pmini pm2"></div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ════ STATS ════ -->
<section id="stats">
  <div class="w">
    <div class="mission-badge rev">
      <div class="mbadge">Mission Data</div>
    </div>
    <div class="stats-grid rev">
      <div class="stat-box">
        <div class="snum">5+</div>
        <div class="slbl">Missions Launched</div>
      </div>
      <div class="stat-box">
        <div class="snum">7.5</div>
        <div class="slbl">Academic Score</div>
      </div>
      <div class="stat-box">
        <div class="snum">3rd</div>
        <div class="slbl">Year of Training</div>
      </div>
      <div class="stat-box">
        <div class="snum">1</div>
        <div class="slbl">Active Deployment</div>
      </div>
    </div>
  </div>
</section>

<!-- ════ SKILLS ════ -->
<section id="skills">
  <div class="w">
    <div class="sh rev">
      <span class="sh-num">01</span>
      <span class="sh-ico">⚙️</span>
      <span class="sh-title">Equipment Manifest</span>
      <div class="sh-line"></div>
    </div>
    <div class="skills-g rev">
      <div class="sk-card">
        <div class="sk-lbl">Languages</div>
        <div class="chips">
          <span class="chip cl">Java</span>
          <span class="chip cl">Python</span>
          <span class="chip cl">JavaScript</span>
          <span class="chip cl">Dart</span>
          <span class="chip cl">SQL</span>
        </div>
      </div>
      <div class="sk-card">
        <div class="sk-lbl">Frameworks</div>
        <div class="chips">
          <span class="chip cf">Spring Boot</span>
          <span class="chip cf">React</span>
          <span class="chip cf">Flutter</span>
          <span class="chip cf">FastAPI</span>
          <span class="chip cf">Spring AI</span>
        </div>
      </div>
      <div class="sk-card">
        <div class="sk-lbl">Tools & Libraries</div>
        <div class="chips">
          <span class="chip ct">Docker</span>
          <span class="chip ct">GitHub</span>
          <span class="chip ct">NumPy</span>
          <span class="chip ct">Pandas</span>
          <span class="chip ct">Scikit-learn</span>
          <span class="chip ct">NLTK</span>
        </div>
      </div>
      <div class="sk-card">
        <div class="sk-lbl">Databases</div>
        <div class="chips">
          <span class="chip cd">MySQL</span>
          <span class="chip cd">PostgreSQL</span>
          <span class="chip cd">Firebase</span>
          <span class="chip cd">Redis</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ════ MISSIONS ════ -->
<section id="missions">
  <div class="w">
    <div class="sh rev">
      <span class="sh-num">02</span>
      <span class="sh-ico">🛸</span>
      <span class="sh-title">Mission Log</span>
      <div class="sh-line"></div>
    </div>
    <div class="ml rev">

      <div class="mi">
        <span class="mi-num">M-01</span>
        <div>
          <div class="mi-top">
            <div class="mi-name">MedoraX AI — Clinical AI Assistant</div>
            <span class="mi-tag t-ai">Healthcare AI</span>
          </div>
          <p class="mi-desc">Multimodal clinical assistant supporting voice, image, and text. Transcribes symptoms via Whisper-large-v3, analyzes medical images via Llama-4-scout, and generates structured diagnostic responses using Llama-3.3-70b. Multilingual (English, Hindi, Marathi) with GPS hospital finder and real-time AQI monitoring.</p>
          <div class="mi-foot">
            <div class="mi-tech">
              <span class="tt">Python</span><span class="tt">Gradio</span><span class="tt">Groq API</span><span class="tt">Google Maps API</span>
            </div>
            <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="mi-link">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="mi">
        <span class="mi-num">M-02</span>
        <div>
          <div class="mi-top">
            <div class="mi-name">SahayLoan — Micro-Loan Platform</div>
            <span class="mi-tag t-ft">FinTech</span>
          </div>
          <p class="mi-desc">Full-stack micro-lending platform for loans up to ₹1,00,000. Flutter frontend, FastAPI backend, AI credit scoring with Random Forest classifier, digital KYC with Aadhaar & PAN OCR via Tesseract, Stripe EMI integration, Firebase Auth and Firestore multi-role system.</p>
          <div class="mi-foot">
            <div class="mi-tech">
              <span class="tt">Flutter</span><span class="tt">FastAPI</span><span class="tt">Scikit-learn</span><span class="tt">Firebase</span><span class="tt">Stripe</span>
            </div>
            <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="mi-link">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="mi">
        <span class="mi-num">M-03</span>
        <div>
          <div class="mi-top">
            <div class="mi-name">SikshaSetu — Rural Education Platform</div>
            <span class="mi-tag t-fs">Full-Stack</span>
          </div>
          <p class="mi-desc">Education platform bridging the digital divide for rural communities. Role-based access control with Spring Security and JWT/OAuth 2.0, optimized relational schema, responsive React frontend, ZEGOCLOUD real-time video SDK for virtual classrooms.</p>
          <div class="mi-foot">
            <div class="mi-tech">
              <span class="tt">React</span><span class="tt">Spring Boot</span><span class="tt">Spring Security</span><span class="tt">JWT</span><span class="tt">MySQL</span>
            </div>
            <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="mi-link">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="mi">
        <span class="mi-num">M-04</span>
        <div>
          <div class="mi-top">
            <div class="mi-name">AI-Powered E-Commerce Backend</div>
            <span class="mi-tag t-ai">AI / Full-Stack</span>
          </div>
          <p class="mi-desc">Intelligent e-commerce backend with AI-driven product recommendations using Spring AI and vector similarity search via Redis Vector DB. Generative AI chatbot for real-time customer support, AI-powered product image generation pipeline, secured with Spring Security and JWT.</p>
          <div class="mi-foot">
            <div class="mi-tech">
              <span class="tt">React</span><span class="tt">Spring Boot</span><span class="tt">Spring AI</span><span class="tt">Redis Vector DB</span><span class="tt">Tailwind</span>
            </div>
            <a href="https://github.com/Shravan157" target="_blank" class="mi-link">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="mi">
        <span class="mi-num">M-05</span>
        <div>
          <div class="mi-top">
            <div class="mi-name">Zomato Review Sentiment Analysis</div>
            <span class="mi-tag t-ml">ML / NLP</span>
          </div>
          <p class="mi-desc">End-to-end NLP pipeline classifying 10,000+ Zomato restaurant reviews. Extensive EDA with 15 visualizations, hypothesis testing, TF-IDF vectorization, model comparison across Logistic Regression, Random Forest, and Naive Bayes. Logistic Regression achieved the highest F1 score.</p>
          <div class="mi-foot">
            <div class="mi-tech">
              <span class="tt">Python</span><span class="tt">Scikit-learn</span><span class="tt">NLTK</span><span class="tt">TF-IDF</span><span class="tt">Pandas</span>
            </div>
            <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="mi-link">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ════ EXPERIENCE ════ -->
<section id="log">
  <div class="w">
    <div class="sh rev">
      <span class="sh-num">03</span>
      <span class="sh-ico">📡</span>
      <span class="sh-title">Flight Record</span>
      <div class="sh-line"></div>
    </div>
    <div class="exp-g rev">
      <div class="exp-card">
        <div class="ep">APR 2026 — PRESENT · REMOTE</div>
        <div class="er">Data Science with Gen AI Intern</div>
        <div class="eo">Innovexis</div>
        <ul class="el">
          <li>Selected for Innovexis's competitive Data Science with Gen AI program</li>
          <li>Real-world projects integrating LLMs and generative AI techniques</li>
          <li>Python, NumPy, Pandas, Scikit-learn for data analysis and model building</li>
          <li>Hands-on exposure to production-level Gen AI workflows</li>
        </ul>
        <div class="active-badge"><div class="sdot"></div> Currently Active</div>
      </div>
      <div class="exp-card">
        <div class="ep">JUN 2023 — MAY 2027 (EXPECTED)</div>
        <div class="er">B.Tech, Computer Science (AI & ML)</div>
        <div class="eo">ViMEET · University of Mumbai</div>
        <ul class="el">
          <li>Specializing in Artificial Intelligence & Machine Learning</li>
          <li>Coursework: DSA, Machine Learning, Cloud Computing, Microservices, System Design</li>
          <li>Building production projects alongside coursework</li>
        </ul>
        <div class="cgpa">CGPA 7.5 / 10.0</div>
      </div>
    </div>
  </div>
</section>

<!-- ════ CONTACT ════ -->
<section id="contact">
  <div class="w">
    <div class="sh rev">
      <span class="sh-num">04</span>
      <span class="sh-ico">📻</span>
      <span class="sh-title">Establish Contact</span>
      <div class="sh-line"></div>
    </div>
    <div class="contact-g rev">
      <div>
        <h2 class="ch">Ready to<br><span>Launch?</span></h2>
        <p class="csub">Open to internships, collaborations, and deep-space conversations about backend systems, AI, and engineering. Transmission line is open.</p>
        <a href="mailto:shravanparthe@gmail.com" class="btn-a">📡 Send Transmission</a>
      </div>
      <div class="ccs">
        <div class="cc">
          <div class="ccl">Email</div>
          <div class="ccv"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div>
        </div>
        <div class="cc">
          <div class="ccl">Phone</div>
          <div class="ccv">7385813010</div>
        </div>
        <div class="cc">
          <div class="ccl">LinkedIn</div>
          <div class="ccv"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div>
        </div>
        <div class="cc">
          <div class="ccl">GitHub</div>
          <div class="ccv"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div>
        </div>
        <div class="cc wide">
          <div class="ccl">Base of Operations</div>
          <div class="ccv">Mumbai, India · Earth · Solar System · Milky Way Galaxy</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ════ QUOTE ════ -->
<div class="w">
  <div class="qwrap rev">
    <span class="qmark">"</span>
    <p class="qtext">
      The woods are lovely, dark and deep,<br>
      But I have promises to keep,<br>
      And <em>miles to go before I sleep,</em><br>
      And miles to go before I sleep.
    </p>
    <div class="qsrc">— Robert Frost · Stopping by Woods on a Snowy Evening</div>
  </div>
</div>

<!-- ════ ROCKET BTN ════ -->
<a href="#hero" class="rkt-btn" title="Back to top">
  <svg viewBox="0 0 60 110" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="rb" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#263238"/>
        <stop offset="100%" stop-color="#0a0f1e"/>
      </linearGradient>
      <radialGradient id="rf" cx="50%" cy="0%">
        <stop offset="0%" stop-color="#64ffda"/>
        <stop offset="50%" stop-color="#2979ff"/>
        <stop offset="100%" stop-color="transparent"/>
      </radialGradient>
    </defs>
    <ellipse cx="30" cy="92" rx="12" ry="20" fill="url(#rf)" opacity=".9">
      <animate attributeName="ry" values="20;24;17;22;20" dur="0.3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".9;.7;1;.8;.9" dur="0.4s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="30" cy="90" rx="6" ry="11" fill="#64ffda" opacity=".8">
      <animate attributeName="ry" values="11;14;9;12;11" dur="0.25s" repeatCount="indefinite"/>
    </ellipse>
    <path d="M16 68 L5 88 L18 76 Z" fill="#0d47a1" opacity=".9"/>
    <path d="M44 68 L55 88 L42 76 Z" fill="#0d47a1" opacity=".9"/>
    <rect x="16" y="25" width="28" height="52" rx="6" fill="url(#rb)" stroke="#546e7a" stroke-width="1"/>
    <path d="M16 30 Q30 4 44 30 Z" fill="#0d47a1" stroke="#455a64" stroke-width="1"/>
    <circle cx="30" cy="55" r="8" fill="#0d47a1" stroke="#64ffda" stroke-width="1.5"/>
    <circle cx="30" cy="55" r="5" fill="#1565c0" opacity=".8"/>
    <circle cx="28" cy="53" r="2" fill="white" opacity=".18"/>
    <rect x="16" y="68" width="28" height="5" fill="#64ffda" opacity=".35"/>
  </svg>
</a>

<!-- ════ FOOTER ════ -->
<footer id="foot">
  <div class="fi">
    <div class="fl">Built by <a href="https://github.com/Shravan157">Shravan Parthe</a> · 2026 · Earth</div>
    <div class="flinks">
      <a href="https://github.com/Shravan157" target="_blank">GitHub</a>
      <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn</a>
      <a href="mailto:shravanparthe@gmail.com">Email</a>
    </div>
  </div>
</footer>

</div><!-- /#sp -->

<script>
(function(){
  function go(){

    // ── CANVAS STARFIELD ──
    var C = document.getElementById('spaceCanvas');
    if(!C) return;
    var ctx = C.getContext('2d');
    function rsz(){
      C.width  = window.innerWidth;
      C.height = window.innerHeight;
    }
    rsz();
    window.addEventListener('resize', rsz);

    var N = 280;
    var stars = [];
    for(var i=0;i<N;i++){
      stars.push({
        x: Math.random()*C.width,
        y: Math.random()*C.height,
        r: Math.random()*1.7+0.2,
        a: Math.random(),
        spd: Math.random()*0.006+0.002,
        ph: Math.random()*Math.PI*2,
        col: ['#ffffff','#ccd6f6','#64ffda','#ffd54f','#b39ddb','#90caf9'][Math.floor(Math.random()*6)]
      });
    }

    var shooters=[];
    function addShooter(){
      if(shooters.length<4){
        var angle = Math.PI/4+(Math.random()-0.5)*0.35;
        shooters.push({
          x: Math.random()*C.width*0.75,
          y: Math.random()*C.height*0.45,
          len: Math.random()*130+70,
          spd: Math.random()*9+6,
          a: 1, angle: angle,
          col: Math.random()>.6?'#64ffda':'#ccd6f6'
        });
      }
    }
    setInterval(addShooter, 3200);

    // Nebula dust particles
    var dust=[];
    for(var d=0;d<60;d++){
      dust.push({
        x: Math.random()*C.width,
        y: Math.random()*C.height,
        r: Math.random()*3+1,
        a: Math.random()*0.15,
        vx:(Math.random()-.5)*0.2,
        vy:(Math.random()-.5)*0.2,
        col:['#7c4dff','#2979ff','#64ffda'][Math.floor(Math.random()*3)]
      });
    }

    function frame(){
      ctx.clearRect(0,0,C.width,C.height);

      // Stars
      for(var i=0;i<stars.length;i++){
        var s=stars[i];
        s.ph+=s.spd;
        s.a=0.3+0.7*(Math.sin(s.ph)*0.5+0.5);
        ctx.save();
        ctx.globalAlpha=s.a;
        ctx.fillStyle=s.col;
        ctx.beginPath();
        ctx.arc(s.x,s.y,s.r,0,Math.PI*2);
        ctx.fill();
        // Twinkle cross for bright stars
        if(s.r>1.4&&s.a>0.8){
          ctx.globalAlpha=s.a*0.35;
          ctx.strokeStyle=s.col;
          ctx.lineWidth=0.5;
          ctx.beginPath();
          ctx.moveTo(s.x-s.r*3,s.y);ctx.lineTo(s.x+s.r*3,s.y);
          ctx.moveTo(s.x,s.y-s.r*3);ctx.lineTo(s.x,s.y+s.r*3);
          ctx.stroke();
        }
        ctx.restore();
      }

      // Dust
      for(var d=0;d<dust.length;d++){
        var p=dust[d];
        p.x+=p.vx; p.y+=p.vy;
        if(p.x<0)p.x=C.width; if(p.x>C.width)p.x=0;
        if(p.y<0)p.y=C.height; if(p.y>C.height)p.y=0;
        ctx.save();
        ctx.globalAlpha=p.a;
        ctx.fillStyle=p.col;
        ctx.beginPath();
        ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
        ctx.fill();
        ctx.restore();
      }

      // Shooting stars
      for(var j=shooters.length-1;j>=0;j--){
        var sh=shooters[j];
        var dx=Math.cos(sh.angle)*sh.len;
        var dy=Math.sin(sh.angle)*sh.len;
        var g=ctx.createLinearGradient(sh.x,sh.y,sh.x-dx,sh.y-dy);
        g.addColorStop(0,'rgba(100,255,218,'+sh.a+')');
        g.addColorStop(0.3,'rgba(100,200,255,'+(sh.a*0.6)+')');
        g.addColorStop(1,'transparent');
        ctx.save();
        ctx.strokeStyle=g;
        ctx.lineWidth=1.8;
        ctx.shadowBlur=6;
        ctx.shadowColor='#64ffda';
        ctx.beginPath();
        ctx.moveTo(sh.x,sh.y);
        ctx.lineTo(sh.x-dx,sh.y-dy);
        ctx.stroke();
        ctx.restore();
        sh.x+=sh.spd*Math.cos(sh.angle);
        sh.y+=sh.spd*Math.sin(sh.angle);
        sh.a-=0.012;
        if(sh.a<=0||sh.x>C.width||sh.y>C.height) shooters.splice(j,1);
      }

      requestAnimationFrame(frame);
    }
    frame();

    // ── SCROLL REVEAL ──
    var revs = document.querySelectorAll('.rev');
    var obs = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){
          e.target.classList.add('in');
          obs.unobserve(e.target);
        }
      });
    },{threshold:0.07});
    revs.forEach(function(el){ obs.observe(el); });

    // Immediate hero reveals
    var hrevs = document.querySelectorAll('#hero .rev');
    hrevs.forEach(function(el,i){
      setTimeout(function(){ el.classList.add('in'); }, i*130+80);
    });

    // ── SMOOTH SCROLL ──
    document.querySelectorAll('a[href^="#"]').forEach(function(a){
      a.addEventListener('click',function(e){
        var t=document.querySelector(a.getAttribute('href'));
        if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth'});}
      });
    });

    // ── NAV ACTIVE STATE ──
    var sections = ['hero','skills','missions','log','contact'];
    var navAs = document.querySelectorAll('#nav .nav-links a');
    window.addEventListener('scroll',function(){
      var y = window.scrollY+120;
      sections.forEach(function(id,i){
        var sec = document.getElementById(id);
        if(sec&&y>=sec.offsetTop){
          navAs.forEach(function(a){a.style.color='';});
          if(navAs[i]) navAs[i].style.color='#64ffda';
        }
      });
    });

  }

  if(document.readyState!=='loading') go();
  else document.addEventListener('DOMContentLoaded',go);
})();
</script>
"""

st.markdown(FONTS, unsafe_allow_html=True)
st.markdown(PORTFOLIO, unsafe_allow_html=True)


# import streamlit as st
# import streamlit.components.v1 as components

# st.set_page_config(
#     page_title="Shravan Parthe — Space Portfolio",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# st.markdown("""
# <style>
# #MainMenu, header, footer {visibility: hidden;}
# .stApp {
#     background: #050816;
#     margin: 0;
#     padding: 0;
# }
# .block-container {
#     padding: 0 !important;
#     max-width: 100% !important;
# }
# iframe {
#     border: none !important;
# }
# </style>
# """, unsafe_allow_html=True)

# html_code = r"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8"/>
# <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
# <title>Shravan Parthe — Space Portfolio</title>
# //fonts.googleapis.com">
# //fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
# <style>
# :root{
#   --bg:#050816;
#   --bg2:#0b1026;
#   --panel:rgba(12,18,40,0.62);
#   --panel-2:rgba(18,26,58,0.82);
#   --border:rgba(126,162,255,0.16);
#   --text:#eef4ff;
#   --muted:#98a7d0;
#   --soft:#6f7da8;
#   --cyan:#6ee7ff;
#   --blue:#7aa2ff;
#   --violet:#a78bfa;
#   --pink:#ff78c6;
#   --green:#66f2b0;
#   --gold:#ffd37a;
#   --danger:#ff7b7b;
#   --sans:'Inter',sans-serif;
#   --display:'Orbitron',sans-serif;
#   --mono:'JetBrains Mono',monospace;
# }

# *{box-sizing:border-box;margin:0;padding:0}
# html{scroll-behavior:smooth}
# body{
#   font-family:var(--sans);
#   color:var(--text);
#   background:
#     radial-gradient(circle at 20% 20%, rgba(122,162,255,0.16), transparent 24%),
#     radial-gradient(circle at 80% 30%, rgba(167,139,250,0.14), transparent 26%),
#     radial-gradient(circle at 50% 75%, rgba(110,231,255,0.10), transparent 30%),
#     linear-gradient(180deg, #03050f 0%, #08101f 45%, #050816 100%);
#   overflow-x:hidden;
# }

# /* Stars */
# body::before{
#   content:"";
#   position:fixed;
#   inset:0;
#   background-image:
#     radial-gradient(2px 2px at 20px 30px, rgba(255,255,255,0.9), transparent),
#     radial-gradient(1.5px 1.5px at 120px 80px, rgba(255,255,255,0.75), transparent),
#     radial-gradient(1.8px 1.8px at 220px 180px, rgba(110,231,255,0.8), transparent),
#     radial-gradient(1.2px 1.2px at 340px 60px, rgba(255,255,255,0.7), transparent),
#     radial-gradient(1.4px 1.4px at 500px 140px, rgba(167,139,250,0.75), transparent),
#     radial-gradient(1.8px 1.8px at 700px 90px, rgba(255,255,255,0.8), transparent),
#     radial-gradient(1.3px 1.3px at 900px 200px, rgba(110,231,255,0.65), transparent),
#     radial-gradient(1.7px 1.7px at 1100px 120px, rgba(255,255,255,0.8), transparent);
#   background-size: 1200px 700px;
#   opacity:0.55;
#   pointer-events:none;
#   z-index:0;
#   animation: drift 80s linear infinite;
# }

# body::after{
#   content:"";
#   position:fixed;
#   inset:0;
#   background:
#     radial-gradient(circle at center, transparent 0 58%, rgba(122,162,255,0.05) 58.5%, transparent 59%),
#     radial-gradient(circle at center, transparent 0 70%, rgba(110,231,255,0.04) 70.5%, transparent 71%);
#   pointer-events:none;
#   z-index:0;
# }

# @keyframes drift{
#   from{transform:translateY(0)}
#   to{transform:translateY(60px)}
# }

# a{color:inherit;text-decoration:none}
# .wrap{
#   width:min(1180px, calc(100% - 32px));
#   margin:0 auto;
#   position:relative;
#   z-index:2;
# }

# nav{
#   position:fixed;
#   top:0; left:0; right:0;
#   z-index:20;
#   backdrop-filter: blur(18px);
#   background:rgba(3,8,20,0.55);
#   border-bottom:1px solid rgba(126,162,255,0.08);
# }
# .nav-inner{
#   width:min(1180px, calc(100% - 32px));
#   margin:0 auto;
#   min-height:74px;
#   display:flex;
#   align-items:center;
#   justify-content:space-between;
# }
# .nav-logo{
#   font-family:var(--display);
#   letter-spacing:1px;
#   font-weight:800;
#   color:var(--text);
# }
# .nav-logo span{color:var(--cyan)}
# .nav-links{
#   display:flex;
#   align-items:center;
#   gap:1.2rem;
#   flex-wrap:wrap;
# }
# .nav-links a{
#   font-size:0.78rem;
#   text-transform:uppercase;
#   letter-spacing:1.6px;
#   color:var(--muted);
# }
# .nav-links a:hover{color:var(--cyan)}
# .badge-live{
#   display:inline-flex;
#   align-items:center;
#   gap:.55rem;
#   border:1px solid rgba(102,242,176,0.25);
#   color:var(--green);
#   background:rgba(102,242,176,0.07);
#   padding:.45rem .9rem;
#   border-radius:999px;
#   font-family:var(--mono);
#   font-size:.72rem;
# }
# .dot{
#   width:8px;height:8px;border-radius:50%;
#   background:var(--green);
#   box-shadow:0 0 10px var(--green);
#   animation:pulse 2s infinite;
# }
# @keyframes pulse{
#   0%,100%{opacity:1; transform:scale(1)}
#   50%{opacity:.4; transform:scale(.8)}
# }

# .hero{
#   min-height:100vh;
#   display:flex;
#   align-items:center;
#   padding:7rem 0 4rem;
#   position:relative;
# }
# .hero-grid{
#   display:grid;
#   grid-template-columns: 1.15fr .85fr;
#   gap:3rem;
#   align-items:center;
# }
# .kicker{
#   display:inline-flex;
#   align-items:center;
#   gap:.6rem;
#   margin-bottom:1.3rem;
#   color:var(--cyan);
#   font-family:var(--mono);
#   font-size:.74rem;
#   letter-spacing:2px;
#   text-transform:uppercase;
# }
# .kicker::before{
#   content:"";
#   width:42px;
#   height:1px;
#   background:linear-gradient(90deg, var(--cyan), transparent);
# }
# .hero h1{
#   font-family:var(--display);
#   font-size:clamp(3rem, 8vw, 6.4rem);
#   line-height:1.02;
#   letter-spacing:-1px;
#   text-transform:uppercase;
#   margin-bottom:1.2rem;
# }
# .hero h1 .glow{
#   color:var(--cyan);
#   text-shadow:0 0 18px rgba(110,231,255,0.32);
# }
# .hero-sub{
#   max-width:700px;
#   color:var(--muted);
#   font-size:1rem;
#   line-height:1.9;
#   margin-bottom:2rem;
# }
# .hero-sub strong{color:var(--text)}
# .hero-actions{
#   display:flex;
#   gap:1rem;
#   flex-wrap:wrap;
# }
# .btn{
#   display:inline-flex;
#   align-items:center;
#   gap:.6rem;
#   padding:.95rem 1.35rem;
#   border-radius:12px;
#   font-weight:700;
#   font-size:.84rem;
#   text-transform:uppercase;
#   letter-spacing:1px;
#   transition:.25s ease;
# }
# .btn-primary{
#   background:linear-gradient(135deg, var(--cyan), var(--blue));
#   color:#04111b;
#   box-shadow:0 8px 30px rgba(110,231,255,0.18);
# }
# .btn-primary:hover{transform:translateY(-2px) scale(1.01)}
# .btn-secondary{
#   border:1px solid var(--border);
#   background:rgba(255,255,255,0.03);
#   color:var(--text);
# }
# .btn-secondary:hover{
#   border-color:rgba(110,231,255,0.35);
#   color:var(--cyan);
#   transform:translateY(-2px);
# }

# .hero-panel{
#   position:relative;
#   min-height:520px;
#   border:1px solid var(--border);
#   border-radius:28px;
#   background:linear-gradient(180deg, rgba(12,18,40,0.82), rgba(7,12,28,0.7));
#   overflow:hidden;
#   box-shadow:0 20px 80px rgba(0,0,0,0.35);
# }
# .hero-panel::before{
#   content:"";
#   position:absolute;
#   inset:0;
#   background:
#     radial-gradient(circle at 70% 22%, rgba(110,231,255,0.16), transparent 18%),
#     radial-gradient(circle at 28% 70%, rgba(167,139,250,0.16), transparent 18%);
# }
# .orbit{
#   position:absolute;
#   border:1px dashed rgba(255,255,255,0.12);
#   border-radius:50%;
# }
# .o1{width:420px;height:420px;top:55px;left:50%;transform:translateX(-50%)}
# .o2{width:280px;height:280px;top:125px;left:50%;transform:translateX(-50%)}
# .planet{
#   position:absolute;
#   width:88px;height:88px;border-radius:50%;
#   top:190px;left:50%;transform:translateX(-50%);
#   background:radial-gradient(circle at 30% 30%, #d8e8ff, #7aa2ff 45%, #344e9a 80%);
#   box-shadow:0 0 40px rgba(122,162,255,0.3);
# }
# .rocket{
#   position:absolute;
#   right:85px;
#   top:110px;
#   font-size:2.6rem;
#   transform:rotate(18deg);
#   animation:floatRocket 4s ease-in-out infinite;
#   filter:drop-shadow(0 0 18px rgba(255,211,122,.18));
# }
# .astronaut{
#   position:absolute;
#   left:58px;
#   bottom:115px;
#   font-size:3rem;
#   animation:floatAstro 5s ease-in-out infinite;
#   filter:drop-shadow(0 0 18px rgba(255,255,255,.16));
# }
# .starship-note{
#   position:absolute;
#   left:28px;
#   right:28px;
#   bottom:24px;
#   display:grid;
#   grid-template-columns:1fr 1fr;
#   gap:12px;
# }
# .mini-card{
#   background:rgba(255,255,255,0.04);
#   border:1px solid rgba(255,255,255,0.08);
#   border-radius:16px;
#   padding:1rem;
# }
# .mini-label{
#   font-family:var(--mono);
#   color:var(--soft);
#   font-size:.67rem;
#   text-transform:uppercase;
#   letter-spacing:1.2px;
#   margin-bottom:.45rem;
# }
# .mini-value{
#   color:var(--text);
#   font-size:.95rem;
#   line-height:1.6;
# }
# @keyframes floatRocket{
#   0%,100%{transform:translateY(0) rotate(18deg)}
#   50%{transform:translateY(-12px) rotate(15deg)}
# }
# @keyframes floatAstro{
#   0%,100%{transform:translateY(0) rotate(-8deg)}
#   50%{transform:translateY(-12px) rotate(6deg)}
# }

# .section{
#   padding:2rem 0 5rem;
# }
# .section-label{
#   display:flex;
#   align-items:center;
#   gap:.9rem;
#   margin-bottom:1.8rem;
#   font-family:var(--mono);
#   color:var(--soft);
#   font-size:.72rem;
#   text-transform:uppercase;
#   letter-spacing:2px;
# }
# .section-label::after{
#   content:"";
#   height:1px;
#   flex:1;
#   background:linear-gradient(90deg, rgba(110,231,255,.22), rgba(255,255,255,0.04));
# }
# .section-label span{color:var(--cyan)}

# .stats{
#   display:grid;
#   grid-template-columns:repeat(4,1fr);
#   gap:1rem;
# }
# .stat{
#   border:1px solid var(--border);
#   background:var(--panel);
#   border-radius:20px;
#   padding:1.5rem;
#   backdrop-filter: blur(10px);
# }
# .stat h3{
#   font-family:var(--display);
#   font-size:2.1rem;
#   color:var(--text);
#   margin-bottom:.4rem;
# }
# .stat p{
#   color:var(--muted);
#   font-family:var(--mono);
#   font-size:.74rem;
#   text-transform:uppercase;
#   letter-spacing:1px;
# }

# .grid-2{
#   display:grid;
#   grid-template-columns:repeat(2,1fr);
#   gap:1rem;
# }
# .card{
#   border:1px solid var(--border);
#   background:var(--panel);
#   border-radius:22px;
#   padding:1.35rem;
#   backdrop-filter: blur(10px);
# }
# .card h3{
#   font-family:var(--display);
#   color:var(--text);
#   font-size:1.05rem;
#   margin-bottom:1rem;
#   letter-spacing:.5px;
# }
# .chips{
#   display:flex;
#   flex-wrap:wrap;
#   gap:.55rem;
# }
# .chip{
#   padding:.45rem .75rem;
#   border-radius:999px;
#   border:1px solid rgba(255,255,255,0.08);
#   background:rgba(255,255,255,0.04);
#   color:var(--muted);
#   font-family:var(--mono);
#   font-size:.75rem;
# }
# .chip.c1{color:var(--cyan); border-color:rgba(110,231,255,.18)}
# .chip.c2{color:var(--violet); border-color:rgba(167,139,250,.18)}
# .chip.c3{color:var(--gold); border-color:rgba(255,211,122,.18)}
# .chip.c4{color:var(--green); border-color:rgba(102,242,176,.18)}

# .projects{
#   display:flex;
#   flex-direction:column;
#   gap:1rem;
# }
# .project{
#   border:1px solid var(--border);
#   background:linear-gradient(180deg, rgba(13,18,38,0.85), rgba(10,14,30,0.72));
#   border-radius:24px;
#   padding:1.4rem;
#   transition:.25s ease;
# }
# .project:hover{
#   transform:translateY(-4px);
#   border-color:rgba(110,231,255,.28);
#   box-shadow:0 14px 40px rgba(0,0,0,.18);
# }
# .proj-top{
#   display:flex;
#   justify-content:space-between;
#   align-items:flex-start;
#   gap:1rem;
#   margin-bottom:.8rem;
# }
# .project h3{
#   font-size:1.2rem;
#   color:var(--text);
#   margin-bottom:.25rem;
# }
# .proj-tag{
#   white-space:nowrap;
#   padding:.35rem .7rem;
#   border-radius:999px;
#   font-family:var(--mono);
#   font-size:.68rem;
#   text-transform:uppercase;
#   letter-spacing:.8px;
#   border:1px solid rgba(255,255,255,.08);
# }
# .t1{color:var(--violet); background:rgba(167,139,250,.08)}
# .t2{color:var(--cyan); background:rgba(110,231,255,.08)}
# .t3{color:var(--green); background:rgba(102,242,176,.08)}
# .t4{color:var(--gold); background:rgba(255,211,122,.08)}
# .project p{
#   color:var(--muted);
#   line-height:1.8;
#   font-size:.95rem;
#   margin-bottom:1rem;
# }
# .proj-bottom{
#   display:flex;
#   justify-content:space-between;
#   gap:1rem;
#   align-items:center;
#   flex-wrap:wrap;
# }
# .techs{
#   display:flex;
#   flex-wrap:wrap;
#   gap:.45rem;
# }
# .tech{
#   border:1px solid rgba(255,255,255,.08);
#   background:rgba(255,255,255,.03);
#   color:var(--soft);
#   border-radius:999px;
#   padding:.35rem .65rem;
#   font-family:var(--mono);
#   font-size:.72rem;
# }
# .proj-link{
#   color:var(--cyan);
#   font-weight:600;
# }

# .exp-grid{
#   display:grid;
#   grid-template-columns:1fr 1fr;
#   gap:1rem;
# }
# .exp-card{
#   border:1px solid var(--border);
#   background:var(--panel);
#   border-radius:24px;
#   padding:1.5rem;
# }
# .exp-period{
#   color:var(--soft);
#   font-family:var(--mono);
#   font-size:.72rem;
#   margin-bottom:.7rem;
#   text-transform:uppercase;
# }
# .exp-role{
#   font-family:var(--display);
#   font-size:1.1rem;
#   color:var(--text);
#   margin-bottom:.35rem;
# }
# .exp-org{
#   color:var(--cyan);
#   font-family:var(--mono);
#   margin-bottom:1rem;
#   font-size:.8rem;
# }
# .exp-card ul{
#   list-style:none;
# }
# .exp-card li{
#   color:var(--muted);
#   line-height:1.8;
#   padding-left:1rem;
#   position:relative;
#   margin:.3rem 0;
# }
# .exp-card li::before{
#   content:"✦";
#   position:absolute;
#   left:0;
#   color:var(--cyan);
#   font-size:.75rem;
# }
# .pill{
#   display:inline-block;
#   margin-top:1rem;
#   padding:.42rem .8rem;
#   border-radius:999px;
#   font-family:var(--mono);
#   font-size:.72rem;
#   border:1px solid rgba(102,242,176,.18);
#   background:rgba(102,242,176,.08);
#   color:var(--green);
# }

# .contact{
#   display:grid;
#   grid-template-columns:1fr 1fr;
#   gap:1rem;
# }
# .contact-main{
#   border:1px solid var(--border);
#   background:var(--panel);
#   border-radius:28px;
#   padding:2rem;
# }
# .contact-main h2{
#   font-family:var(--display);
#   font-size:clamp(2rem,4vw,3.6rem);
#   line-height:1.1;
#   margin-bottom:1rem;
# }
# .contact-main h2 span{color:var(--cyan)}
# .contact-main p{
#   color:var(--muted);
#   line-height:1.9;
#   max-width:560px;
#   margin-bottom:1.5rem;
# }
# .contact-cards{
#   display:grid;
#   grid-template-columns:1fr 1fr;
#   gap:1rem;
# }
# .contact-card{
#   border:1px solid var(--border);
#   background:var(--panel);
#   border-radius:22px;
#   padding:1.2rem;
# }
# .label{
#   color:var(--soft);
#   font-family:var(--mono);
#   text-transform:uppercase;
#   letter-spacing:1.4px;
#   font-size:.68rem;
#   margin-bottom:.45rem;
# }
# .value{
#   color:var(--text);
#   font-size:.96rem;
#   line-height:1.7;
# }
# .value a{color:var(--cyan)}

# .quote{
#   margin:2rem 0 4rem;
#   border:1px solid var(--border);
#   border-radius:28px;
#   background:linear-gradient(180deg, rgba(10,16,36,0.82), rgba(8,12,24,0.74));
#   padding:3rem 1.5rem;
#   text-align:center;
#   position:relative;
#   overflow:hidden;
# }
# .quote::before{
#   content:"✦";
#   position:absolute;
#   top:14px;
#   left:24px;
#   color:rgba(110,231,255,.22);
#   font-size:2rem;
# }
# .quote::after{
#   content:"☄";
#   position:absolute;
#   bottom:18px;
#   right:24px;
#   color:rgba(167,139,250,.18);
#   font-size:2rem;
# }
# .quote p{
#   font-size:clamp(1.05rem,2vw,1.35rem);
#   line-height:2;
#   color:#cfd8f7;
#   max-width:760px;
#   margin:0 auto 1rem;
# }
# .quote strong{color:var(--cyan)}
# .quote .src{
#   font-family:var(--mono);
#   color:var(--soft);
#   font-size:.72rem;
#   text-transform:uppercase;
#   letter-spacing:2px;
# }

# footer{
#   padding:1.4rem 0 2.5rem;
#   border-top:1px solid rgba(255,255,255,.06);
# }
# .foot{
#   display:flex;
#   justify-content:space-between;
#   gap:1rem;
#   flex-wrap:wrap;
# }
# .foot div, .foot a{
#   color:var(--soft);
#   font-family:var(--mono);
#   font-size:.74rem;
# }
# .foot a:hover{color:var(--cyan)}

# .reveal{
#   opacity:0;
#   transform:translateY(24px);
#   transition:all .8s ease;
# }
# .reveal.in{
#   opacity:1;
#   transform:translateY(0);
# }

# @media (max-width: 980px){
#   .hero-grid,.contact,.exp-grid{grid-template-columns:1fr}
#   .stats{grid-template-columns:repeat(2,1fr)}
#   .grid-2{grid-template-columns:1fr}
#   .hero-panel{min-height:460px}
# }
# @media (max-width: 680px){
#   .nav-links a{display:none}
#   .stats{grid-template-columns:1fr}
#   .contact-cards{grid-template-columns:1fr}
#   .hero h1{font-size:2.6rem}
#   .starship-note{grid-template-columns:1fr}
#   .rocket{right:40px}
#   .astronaut{left:24px}
# }
# </style>
# </head>
# <body>

# <nav>
#   <div class="nav-inner">
#     <a href="#home" class="nav-logo">SHRAVAN<span>.EXE</span></a>
#     <div class="nav-links">
#       <a href="#skills">Arsenal</a>
#       <a href="#projects">Missions</a>
#       <a href="#experience">Flight Log</a>
#       <a href="#contact">Transmission</a>
#       <div class="badge-live"><span class="dot"></span> Open to work</div>
#     </div>
#   </div>
# </nav>

# <section class="hero" id="home">
#   <div class="wrap">
#     <div class="hero-grid">
#       <div class="reveal">
#         <div class="kicker">Mission Log · 2026</div>
#         <h1>
#           Exploring the <span class="glow">unknown</span><br>
#           through backend & AI.
#         </h1>
#         <p class="hero-sub">
#           I’m <strong>Shravan Parthe</strong>, a 3rd year B.Tech CSE (AI & ML) student building production-grade systems with Java, Spring Boot, Python, and modern AI tools. I treat every project like a mission — launch fast, learn deeply, and keep pushing into new frontiers.
#         </p>
#         <div class="hero-actions">
#           <a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">Start a mission</a>
#           <a href="https://github.com/Shravan157" target="_blank" class="btn btn-secondary">View GitHub</a>
#           <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank" class="btn btn-secondary">LinkedIn</a>
#         </div>
#       </div>

#       <div class="hero-panel reveal">
#         <div class="orbit o1"></div>
#         <div class="orbit o2"></div>
#         <div class="planet"></div>
#         <div class="rocket">🚀</div>
#         <div class="astronaut">👨‍🚀</div>

#         <div class="starship-note">
#           <div class="mini-card">
#             <div class="mini-label">Current trajectory</div>
#             <div class="mini-value">Backend Engineer / AI Developer building real-world systems and exploring GenAI integration.</div>
#           </div>
#           <div class="mini-card">
#             <div class="mini-label">Mission status</div>
#             <div class="mini-value">Learning, building, shipping — with miles to go before I sleep.</div>
#           </div>
#         </div>
#       </div>
#     </div>
#   </div>
# </section>

# <section class="section">
#   <div class="wrap">
#     <div class="section-label reveal"><span>01</span> Mission Stats</div>
#     <div class="stats">
#       <div class="stat reveal"><h3>5+</h3><p>Projects launched</p></div>
#       <div class="stat reveal"><h3>7.5</h3><p>CGPA</p></div>
#       <div class="stat reveal"><h3>3rd</h3><p>Year B.Tech</p></div>
#       <div class="stat reveal"><h3>2027</h3><p>Expected graduation</p></div>
#     </div>
#   </div>
# </section>

# <section class="section" id="skills">
#   <div class="wrap">
#     <div class="section-label reveal"><span>02</span> Tech Arsenal</div>
#     <div class="grid-2">
#       <div class="card reveal">
#         <h3>Languages</h3>
#         <div class="chips">
#           <span class="chip c1">Java</span>
#           <span class="chip c1">Python</span>
#           <span class="chip c1">JavaScript</span>
#           <span class="chip c1">Dart</span>
#           <span class="chip c1">SQL</span>
#         </div>
#       </div>

#       <div class="card reveal">
#         <h3>Frameworks</h3>
#         <div class="chips">
#           <span class="chip c2">Spring Boot</span>
#           <span class="chip c2">React</span>
#           <span class="chip c2">Flutter</span>
#           <span class="chip c2">FastAPI</span>
#           <span class="chip c2">Spring AI</span>
#         </div>
#       </div>

#       <div class="card reveal">
#         <h3>Tools & Libraries</h3>
#         <div class="chips">
#           <span class="chip c3">Docker</span>
#           <span class="chip c3">GitHub</span>
#           <span class="chip c3">NumPy</span>
#           <span class="chip c3">Pandas</span>
#           <span class="chip c3">Scikit-learn</span>
#           <span class="chip c3">NLTK</span>
#         </div>
#       </div>

#       <div class="card reveal">
#         <h3>Databases</h3>
#         <div class="chips">
#           <span class="chip c4">MySQL</span>
#           <span class="chip c4">PostgreSQL</span>
#           <span class="chip c4">Firebase</span>
#           <span class="chip c4">Redis</span>
#         </div>
#       </div>
#     </div>
#   </div>
# </section>

# <section class="section" id="projects">
#   <div class="wrap">
#     <div class="section-label reveal"><span>03</span> Missions</div>
#     <div class="projects">

#       <div class="project reveal">
#         <div class="proj-top">
#           <div>
#             <h3>MedoraX AI — Clinical AI Assistant</h3>
#           </div>
#           <div class="proj-tag t1">Healthcare AI</div>
#         </div>
#         <p>
#           A multimodal clinical assistant supporting voice, image, and text. It transcribes symptoms, analyzes medical images, generates structured responses, and supports multilingual interaction with location-aware utilities.
#         </p>
#         <div class="proj-bottom">
#           <div class="techs">
#             <span class="tech">Python</span>
#             <span class="tech">Gradio</span>
#             <span class="tech">Groq API</span>
#             <span class="tech">Google Maps API</span>
#           </div>
#           <a class="proj-link" target="_blank" href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant">View mission ↗</a>
#         </div>
#       </div>

#       <div class="project reveal">
#         <div class="proj-top">
#           <div>
#             <h3>SahayLoan — Micro-Loan Platform</h3>
#           </div>
#           <div class="proj-tag t2">FinTech</div>
#         </div>
#         <p>
#           A full-stack micro-lending platform with AI credit scoring, OCR-based KYC workflows, and a multi-role architecture for modern loan processing.
#         </p>
#         <div class="proj-bottom">
#           <div class="techs">
#             <span class="tech">Flutter</span>
#             <span class="tech">FastAPI</span>
#             <span class="tech">Scikit-learn</span>
#             <span class="tech">Firebase</span>
#             <span class="tech">Stripe</span>
#           </div>
#           <a class="proj-link" target="_blank" href="https://github.com/Shravan157/Sahay-Loan">View mission ↗</a>
#         </div>
#       </div>

#       <div class="project reveal">
#         <div class="proj-top">
#           <div>
#             <h3>SikshaSetu — Rural Education Platform</h3>
#           </div>
#           <div class="proj-tag t3">Full-Stack</div>
#         </div>
#         <p>
#           A scalable education platform focused on access, role-based systems, secure authentication, and real-time digital classroom experiences.
#         </p>
#         <div class="proj-bottom">
#           <div class="techs">
#             <span class="tech">React</span>
#             <span class="tech">Spring Boot</span>
#             <span class="tech">Spring Security</span>
#             <span class="tech">JWT</span>
#             <span class="tech">MySQL</span>
#           </div>
#           <a class="proj-link" target="_blank" href="https://github.com/Shravan157/SikshaSetu_Edu_App">View mission ↗</a>
#         </div>
#       </div>

#       <div class="project reveal">
#         <div class="proj-top">
#           <div>
#             <h3>AI-Powered E-Commerce Backend</h3>
#           </div>
#           <div class="proj-tag t1">AI / Backend</div>
#         </div>
#         <p>
#           An intelligent commerce backend with recommendation pipelines, vector search, conversational support, and secure service design.
#         </p>
#         <div class="proj-bottom">
#           <div class="techs">
#             <span class="tech">React</span>
#             <span class="tech">Spring Boot</span>
#             <span class="tech">Spring AI</span>
#             <span class="tech">Redis Vector DB</span>
#             <span class="tech">Tailwind</span>
#           </div>
#           <a class="proj-link" target="_blank" href="https://github.com/Shravan157">View mission ↗</a>
#         </div>
#       </div>

#       <div class="project reveal">
#         <div class="proj-top">
#           <div>
#             <h3>Zomato Review Sentiment Analysis</h3>
#           </div>
#           <div class="proj-tag t4">ML / NLP</div>
#         </div>
#         <p>
#           An end-to-end NLP pipeline for review classification with EDA, feature engineering, TF-IDF vectorization, and comparative model evaluation.
#         </p>
#         <div class="proj-bottom">
#           <div class="techs">
#             <span class="tech">Python</span>
#             <span class="tech">Scikit-learn</span>
#             <span class="tech">NLTK</span>
#             <span class="tech">TF-IDF</span>
#             <span class="tech">Pandas</span>
#           </div>
#           <a class="proj-link" target="_blank" href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis">View mission ↗</a>
#         </div>
#       </div>

#     </div>
#   </div>
# </section>

# <section class="section" id="experience">
#   <div class="wrap">
#     <div class="section-label reveal"><span>04</span> Flight Log</div>
#     <div class="exp-grid">
#       <div class="exp-card reveal">
#         <div class="exp-period">Apr 2026 — Present · Remote</div>
#         <div class="exp-role">Data Science with Gen AI Intern</div>
#         <div class="exp-org">Innovexis</div>
#         <u
#         <ul>
#           >Working on practical projects involving LLMs and generative AI workflows</l/li>
#           >Using Python, NumPy, Pandas, and Scikit-learn for applied data work</l/li>
#           >Gaining exposure to production-oriented GenAI implementation</li>
#         </ul>
#         <div class="pill">Currently Active</div>
#       </div>

#       <div class="exp-card reveal">
#         <div class="exp-period">Jun 2023 — May 2027 (Expected)</div>
#         <div class="exp-role">B.Tech, Computer Science Engineering (AI & ML)</div>
#         <div class="exp-org">ViMEET · University of Mumbai</div>
#         <u
#         <ul>
#           >Focused on AI, ML, backend systems, cloud computing, and system design</l/li>
#           >Building real-world projects alongside formal coursework</l/li>
#           >Growing toward scalable software and AI engineering roles</li>
#         </ul>
#         <div class="pill" style="color:#ffd37a;border-color:rgba(255,211,122,.18);background:rgba(255,211,122,.08)">CGPA 7.5 / 10</div>
#       </div>
#     </div>
#   </div>
# </section>

# <section class="section" id="contact">
#   <div class="wrap">
#     <div class="section-label reveal"><span>05</span> Transmission</div>
#     <div class="contact">
#       <div class="contact-main reveal">
#         <h2>Let’s build the <span>next frontier</span>.</h2>
#         <p>
#           I’m open to internships, collaborations, backend engineering roles, and AI-focused opportunities. If you’re building something ambitious, I’d love to be part of the mission.
#         </p>
#         <a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">Send transmission</a>
#       </div>

#       <div class="contact-cards">
#         <div class="contact-card reveal">
#           <div class="label">Email</div>
#           <div class="value"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div>
#         </div>

#         <div class="contact-card reveal">
#           <div class="label">Phone</div>
#           <div class="value">7385813010</div>
#         </div>

#         <div class="contact-card reveal">
#           <div class="label">LinkedIn</div>
#           <div class="value"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div>
#         </div>

#         <div class="contact-card reveal">
#           <div class="label">GitHub</div>
#           <div class="value"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div>
#         </div>
#       </div>
#     </div>
#   </div>
# </section>

# <div class="wrap">
#   <div class="quote reveal">
#     <p>
#       The woods are lovely, dark and deep,<br>
#       But I have promises to keep,<br>
#       And <strong>miles to go before I sleep,</strong><br>
#       And miles to go before I sleep.
#     </p>
#     <div class="src">— Robert Frost</div>
#   </div>
# </div>

# <footer>
#   <div class="wrap foot">
#     <div>Built by Shravan Parthe · 2026</div>
#     <div style="display:flex; gap:1rem; flex-wrap:wrap;">
#       <a target="_blank" href="https://github.com/Shravan157">GitHub</a>
#       <a target="_blank" href="https://www.linkedin.com/in/shravan-parthe-00946b2ab">LinkedIn</a>
#       <a href="mailto:shravanparthe@gmail.com">Email</a>
#     </div>
#   </div>
# </footer>

# <script>
# const observer = new IntersectionObserver((entries) => {
#   entries.forEach(entry => {
#     if(entry.isIntersecting){
#       entry.target.classList.add('in');
#     }
#   });
# }, { threshold: 0.12 });

# document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
# </script>

# </body>
# </html>
# """

# components.html(html_code, height=4600, scrolling=True)
