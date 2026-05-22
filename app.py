import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Shravan Parthe — Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  #MainMenu, header, footer, [data-testid="stToolbar"],
  [data-testid="stDecoration"], [data-testid="stStatusWidget"],
  .stDeployButton { visibility: hidden !important; display: none !important; }
  .stApp { background: #080b12 !important; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { border: none !important; display: block !important; }
  section[data-testid="stAppViewContainer"] > div { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

RESUME_URL = "https://raw.githubusercontent.com/Shravan157/portfolio-website/master/resume_shravan2.pdf"

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Shravan Parthe</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Clash+Display:wght@400;500;600;700&family=Bricolage+Grotesque:opsz,wght@12..96,300;12..96,400;12..96,500;12..96,600;12..96,700&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;font-size:16px}
:root{
  --bg:#080b12;
  --bg1:#0d1120;
  --bg2:#111827;
  --bg3:rgba(255,255,255,0.03);
  --bg4:rgba(255,255,255,0.055);
  --bd:rgba(255,255,255,0.07);
  --bd2:rgba(255,255,255,0.12);
  --bd3:rgba(255,255,255,0.18);
  --text:#eef2ff;
  --text2:#8b9cc8;
  --text3:#4a5578;
  --accent:#6366f1;
  --accent2:#818cf8;
  --accent3:rgba(99,102,241,0.12);
  --accent4:rgba(99,102,241,0.22);
  --gold:#f59e0b;
  --gold2:rgba(245,158,11,0.1);
  --green:#10b981;
  --green2:rgba(16,185,129,0.1);
  --H:'Clash Display',sans-serif;
  --B:'Bricolage Grotesque',sans-serif;
  --M:'JetBrains Mono',monospace;
  --r:6px;
  --r2:10px;
  --r3:14px;
}
body{
  font-family:var(--B);background:var(--bg);color:var(--text);
  line-height:1.6;overflow-x:hidden;-webkit-font-smoothing:antialiased;
}
::selection{background:var(--accent);color:#fff}
::-webkit-scrollbar{width:2px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--accent);border-radius:99px}
a{color:inherit;text-decoration:none}

/* NOISE OVERLAY */
body::before{
  content:'';position:fixed;inset:0;z-index:1;pointer-events:none;
  opacity:.4;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E");
}

/* AMBIENT GLOW */
.glow-orb{position:fixed;border-radius:50%;pointer-events:none;z-index:0;filter:blur(120px);opacity:.55}
.g1{width:600px;height:600px;background:radial-gradient(circle,rgba(99,102,241,.22),transparent);top:-180px;left:-180px;animation:gd 18s ease-in-out infinite alternate}
.g2{width:500px;height:500px;background:radial-gradient(circle,rgba(16,185,129,.1),transparent);bottom:-120px;right:-120px;animation:gd 22s ease-in-out infinite alternate-reverse}
.g3{width:400px;height:400px;background:radial-gradient(circle,rgba(245,158,11,.08),transparent);top:40%;right:15%;animation:gd 26s ease-in-out infinite alternate}
@keyframes gd{from{transform:translate(0,0)}to{transform:translate(40px,60px)}}

#root{position:relative;z-index:2}
.w{max-width:1120px;margin:0 auto;padding:0 clamp(1.25rem,5vw,3.5rem)}

/* ─── NAV ─── */
#nav{
  position:fixed;top:0;left:0;right:0;z-index:999;
  padding:0;height:60px;display:flex;align-items:center;
  background:rgba(8,11,18,0);
  transition:background .4s,border-color .4s;
  border-bottom:1px solid transparent;
}
#nav.s{background:rgba(8,11,18,.88);border-color:var(--bd);backdrop-filter:blur(20px)}
.ni{
  max-width:1120px;margin:0 auto;width:100%;
  padding:0 clamp(1.25rem,5vw,3.5rem);
  display:flex;align-items:center;justify-content:space-between;
}
.logo{
  font-family:var(--H);font-weight:700;font-size:1.05rem;
  letter-spacing:-.3px;color:var(--text);
  display:flex;align-items:center;gap:.5rem;
}
.logo-dot{width:7px;height:7px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.nl{display:flex;align-items:center;gap:.25rem}
.nl a{
  font-family:var(--M);font-size:.68rem;letter-spacing:.5px;
  color:var(--text2);padding:.45rem .85rem;border-radius:var(--r);
  transition:color .2s,background .2s;
}
.nl a:hover{color:var(--text);background:var(--bg3)}
.nav-cta{
  background:var(--accent3);border:1px solid var(--accent4);
  color:var(--accent2) !important;border-radius:var(--r) !important;
  padding:.42rem 1rem !important;
  transition:background .2s,border-color .2s !important;
}
.nav-cta:hover{background:var(--accent4) !important;border-color:var(--accent) !important;color:#fff !important}

/* ─── HERO ─── */
#hero{min-height:100vh;display:flex;align-items:center;padding:7rem 0 4rem;position:relative}
.hg{display:grid;grid-template-columns:1fr 420px;gap:5rem;align-items:center;width:100%}

.h-eyebrow{
  display:inline-flex;align-items:center;gap:.6rem;
  font-family:var(--M);font-size:.68rem;color:var(--accent2);
  background:var(--accent3);border:1px solid var(--accent4);
  padding:.32rem .85rem;border-radius:99px;
  margin-bottom:1.6rem;
  opacity:0;animation:fu .7s ease forwards .1s;
}
.h-eyebrow-dot{width:5px;height:5px;border-radius:50%;background:var(--green);box-shadow:0 0 8px var(--green);animation:pulse 2s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}

h1.ht{
  font-family:var(--H);font-weight:700;
  font-size:clamp(3rem,6.5vw,5.4rem);
  line-height:1.02;letter-spacing:-2px;
  margin-bottom:1.4rem;
  opacity:0;animation:fu .8s ease forwards .25s;
}
.ht-name{color:var(--text)}
.ht-line{display:block;color:var(--text3);font-weight:400}
.ht-accent{
  background:linear-gradient(135deg,var(--accent2),#a5b4fc);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}

.h-role{
  font-family:var(--M);font-size:.75rem;
  color:var(--text3);letter-spacing:1.5px;
  text-transform:uppercase;margin-bottom:1.6rem;
  opacity:0;animation:fu .8s ease forwards .38s;
}
.h-role-bar{display:inline-block;width:28px;height:1px;background:var(--accent);margin-right:.7rem;vertical-align:middle}

.hdesc{
  font-size:1rem;color:var(--text2);line-height:1.85;
  max-width:500px;margin-bottom:2.2rem;
  opacity:0;animation:fu .8s ease forwards .5s;
}
.hdesc strong{color:var(--text);font-weight:500}

.hacts{display:flex;gap:.75rem;flex-wrap:wrap;opacity:0;animation:fu .8s ease forwards .62s}

@keyframes fu{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}

/* BUTTONS */
.btn{
  display:inline-flex;align-items:center;gap:.5rem;
  padding:.78rem 1.55rem;border-radius:var(--r);
  font-family:var(--M);font-size:.68rem;font-weight:500;
  letter-spacing:.5px;transition:all .25s cubic-bezier(.4,0,.2,1);cursor:pointer;
}
.btn-primary{
  background:var(--accent);color:#fff;
  box-shadow:0 2px 20px rgba(99,102,241,.28);
}
.btn-primary:hover{background:#4f46e5;transform:translateY(-2px);box-shadow:0 6px 28px rgba(99,102,241,.38)}
.btn-ghost{
  border:1px solid var(--bd2);color:var(--text2);background:transparent;
}
.btn-ghost:hover{border-color:var(--bd3);color:var(--text);background:var(--bg3);transform:translateY(-2px)}
.btn-outline{
  border:1px solid rgba(245,158,11,.22);color:var(--gold);background:var(--gold2);
}
.btn-outline:hover{border-color:var(--gold);transform:translateY(-2px)}

/* HERO CARD */
.hcard{
  background:var(--bg1);border:1px solid var(--bd);border-radius:20px;
  padding:2rem;position:relative;overflow:hidden;
  opacity:0;animation:fu 1s ease forwards .4s;
  box-shadow:0 24px 80px rgba(0,0,0,.4);
}
.hcard::before{
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--accent),rgba(129,140,248,.4),transparent);
}
.hcard-header{
  display:flex;align-items:center;gap:.6rem;
  padding-bottom:1.2rem;margin-bottom:1.4rem;
  border-bottom:1px solid var(--bd);
}
.hch-dots{display:flex;gap:.35rem}
.hch-dot{width:10px;height:10px;border-radius:50%}
.d1{background:#ef4444}.d2{background:#f59e0b}.d3{background:#10b981}
.hch-title{font-family:var(--M);font-size:.65rem;color:var(--text3);margin-left:.4rem}

.code-block{font-family:var(--M);font-size:.75rem;line-height:1.9}
.cl{display:flex;gap:.75rem;align-items:baseline}
.ln{color:var(--text3);font-size:.62rem;min-width:1.2rem;text-align:right;user-select:none}
.kw{color:#818cf8}.str{color:#a5b4fc}.cm{color:var(--text3);font-style:italic}
.fn{color:#6ee7b7}.pr{color:#fcd34d}.op{color:var(--text2)}.val{color:#f9a8d4}
.blink{display:inline-block;width:2px;height:.85em;background:var(--accent2);margin-left:1px;vertical-align:text-bottom;animation:blink .9s step-end infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}

.hcard-tags{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:1.4rem;padding-top:1.4rem;border-top:1px solid var(--bd)}
.htag{
  font-family:var(--M);font-size:.62rem;padding:.22rem .65rem;border-radius:var(--r);
  border:1px solid var(--bd);color:var(--text3);background:var(--bg3);transition:all .2s;
}
.htag:hover{border-color:var(--accent);color:var(--accent2);background:var(--accent3)}

/* ─── STATS BAR ─── */
#stats{padding:3rem 0 4rem}
.stats-row{
  display:grid;grid-template-columns:repeat(4,1fr);
  border:1px solid var(--bd);border-radius:var(--r2);overflow:hidden;background:var(--bg1);
}
.stat{
  padding:2rem 1.75rem;border-right:1px solid var(--bd);
  position:relative;transition:background .25s;
}
.stat:last-child{border-right:none}
.stat:hover{background:var(--bg3)}
.stat-n{
  font-family:var(--H);font-size:2.6rem;font-weight:700;line-height:1;
  margin-bottom:.3rem;
  background:linear-gradient(135deg,var(--text),var(--accent2));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.stat-l{font-family:var(--M);font-size:.6rem;letter-spacing:2px;text-transform:uppercase;color:var(--text3)}

/* ─── SECTION HEADER ─── */
.sh{margin-bottom:3rem}
.sh-top{display:flex;align-items:center;gap:1rem;margin-bottom:.5rem}
.sh-idx{font-family:var(--M);font-size:.65rem;color:var(--accent2);letter-spacing:1px}
.sh-line{flex:1;height:1px;background:var(--bd)}
.sh-t{font-family:var(--H);font-size:clamp(1.6rem,3vw,2.1rem);font-weight:700;letter-spacing:-.5px}
.sh-sub{color:var(--text2);font-size:.9rem;margin-top:.4rem}

/* ─── SKILLS ─── */
#skills{padding:5rem 0}
.sk-g{display:grid;grid-template-columns:repeat(2,1fr);gap:.75rem}
.sk-c{
  border:1px solid var(--bd);border-radius:var(--r2);padding:1.6rem;
  background:var(--bg1);transition:border-color .25s,background .25s;
  position:relative;overflow:hidden;
}
.sk-c::after{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:var(--accent);opacity:0;transition:opacity .3s;
}
.sk-c:hover{border-color:var(--bd2);background:var(--bg2)}
.sk-c:hover::after{opacity:1}
.sk-label{
  font-family:var(--M);font-size:.62rem;letter-spacing:2px;
  text-transform:uppercase;color:var(--accent2);margin-bottom:1rem;
}
.chips{display:flex;flex-wrap:wrap;gap:.38rem}
.chip{
  font-family:var(--M);font-size:.68rem;padding:.28rem .7rem;
  border-radius:var(--r);border:1px solid var(--bd);
  color:var(--text2);background:var(--bg3);
  transition:all .15s;cursor:default;
}
.chip:hover{transform:translateY(-1px)}
.ca{border-color:rgba(99,102,241,.25);color:#a5b4fc;background:rgba(99,102,241,.07)}
.ca:hover{box-shadow:0 3px 12px rgba(99,102,241,.15)}
.cb{border-color:rgba(16,185,129,.22);color:#6ee7b7;background:rgba(16,185,129,.06)}
.cb:hover{box-shadow:0 3px 12px rgba(16,185,129,.12)}
.cc{border-color:rgba(245,158,11,.22);color:#fcd34d;background:rgba(245,158,11,.06)}
.cc:hover{box-shadow:0 3px 12px rgba(245,158,11,.12)}
.cd{border-color:rgba(244,114,182,.22);color:#f9a8d4;background:rgba(244,114,182,.06)}
.cd:hover{box-shadow:0 3px 12px rgba(244,114,182,.12)}

/* ─── PROJECTS ─── */
#projects{padding:5rem 0}
.proj-list{display:flex;flex-direction:column;gap:0}
.proj{
  display:grid;grid-template-columns:64px 1fr auto;gap:1.5rem;align-items:start;
  padding:2rem 0;border-bottom:1px solid var(--bd);
  transition:background .2s;position:relative;
}
.proj:first-child{border-top:1px solid var(--bd)}
.proj::before{
  content:'';position:absolute;left:-1.5rem;top:0;bottom:0;width:2px;
  background:var(--accent);transform:scaleY(0);transition:transform .35s ease;
  transform-origin:top;
}
.proj:hover::before{transform:scaleY(1)}
.proj-idx{font-family:var(--M);font-size:.62rem;color:var(--text3);padding-top:.2rem;letter-spacing:1px}
.proj-main{}
.proj-title{
  font-family:var(--H);font-size:1.05rem;font-weight:600;
  color:var(--text);margin-bottom:.4rem;letter-spacing:-.2px;
  transition:color .2s;
}
.proj:hover .proj-title{color:var(--accent2)}
.proj-desc{color:var(--text2);font-size:.88rem;line-height:1.8;margin-bottom:.9rem;max-width:680px}
.proj-stack{display:flex;flex-wrap:wrap;gap:.3rem}
.stk{
  font-family:var(--M);font-size:.6rem;padding:.15rem .5rem;
  border-radius:4px;border:1px solid var(--bd);
  color:var(--text3);background:transparent;
}
.proj-right{display:flex;flex-direction:column;align-items:flex-end;gap:.6rem;padding-top:.15rem}
.proj-badge{
  font-family:var(--M);font-size:.58rem;letter-spacing:.5px;
  padding:.2rem .65rem;border-radius:99px;white-space:nowrap;
}
.ba{background:rgba(99,102,241,.1);color:#a5b4fc;border:1px solid rgba(99,102,241,.2)}
.bb{background:rgba(16,185,129,.08);color:#6ee7b7;border:1px solid rgba(16,185,129,.18)}
.bc{background:rgba(245,158,11,.08);color:#fcd34d;border:1px solid rgba(245,158,11,.18)}
.bd-badge{background:rgba(244,114,182,.08);color:#f9a8d4;border:1px solid rgba(244,114,182,.18)}
.proj-link{
  display:inline-flex;align-items:center;gap:.3rem;
  font-family:var(--M);font-size:.62rem;color:var(--text3);
  transition:color .2s;
}
.proj-link:hover{color:var(--accent2)}
.proj-link svg{transition:transform .2s}
.proj-link:hover svg{transform:translate(2px,-2px)}

/* ─── EXPERIENCE ─── */
#experience{padding:5rem 0}
.exp-grid{display:grid;grid-template-columns:1fr 1fr;gap:.75rem}
.exp-card{
  border:1px solid var(--bd);border-radius:var(--r2);padding:2rem;
  background:var(--bg1);transition:border-color .25s,background .25s;
  position:relative;overflow:hidden;
}
.exp-card::before{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  opacity:0;transition:opacity .3s;
}
.exp-card.active::before{background:linear-gradient(90deg,var(--green),var(--accent));opacity:1}
.exp-card.edu::before{background:linear-gradient(90deg,var(--accent),#a78bfa);opacity:1}
.exp-card:hover{border-color:var(--bd2);background:var(--bg2)}
.exp-period{font-family:var(--M);font-size:.6rem;color:var(--text3);letter-spacing:1px;margin-bottom:.8rem}
.exp-role{font-family:var(--H);font-size:1.05rem;font-weight:600;margin-bottom:.2rem;letter-spacing:-.2px}
.exp-company{font-family:var(--M);font-size:.72rem;color:var(--gold);margin-bottom:1.3rem}
.exp-list{list-style:none}
.exp-list li{
  font-size:.86rem;color:var(--text2);line-height:1.8;
  padding:.12rem 0 .12rem 1.1rem;position:relative;
}
.exp-list li::before{
  content:'';position:absolute;left:0;top:.68rem;
  width:4px;height:4px;border-radius:50%;background:var(--accent);
}
.exp-pill{
  display:inline-flex;align-items:center;gap:.4rem;
  margin-top:1.2rem;padding:.28rem .8rem;border-radius:99px;font-family:var(--M);font-size:.6rem;
}
.pill-green{color:var(--green);border:1px solid rgba(16,185,129,.22);background:var(--green2)}
.pill-amber{color:var(--gold);border:1px solid rgba(245,158,11,.22);background:var(--gold2)}
.pulse{width:6px;height:6px;border-radius:50%;background:var(--green);box-shadow:0 0 8px var(--green);animation:pulse 2s ease-in-out infinite}

/* ─── CONTACT ─── */
#contact{padding:5rem 0 8rem}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start}
.contact-h{
  font-family:var(--H);font-size:clamp(2rem,4vw,3rem);
  font-weight:700;line-height:1.05;letter-spacing:-1px;margin-bottom:1.2rem;
}
.contact-h span{
  background:linear-gradient(135deg,var(--accent2),#a5b4fc);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.contact-sub{color:var(--text2);font-size:.93rem;line-height:1.8;margin-bottom:2rem}
.clinks{display:flex;flex-direction:column;gap:.5rem}
.clink{
  display:flex;align-items:center;justify-content:space-between;
  padding:1.1rem 1.3rem;border:1px solid var(--bd);border-radius:var(--r2);
  background:var(--bg1);transition:all .25s;
}
.clink:hover{border-color:var(--accent);background:var(--accent3);transform:translateX(4px)}
.clink-left{display:flex;align-items:center;gap:.9rem}
.clink-icon{
  width:32px;height:32px;border-radius:var(--r);
  background:var(--bg3);border:1px solid var(--bd2);
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
}
.clink-icon svg{width:15px;height:15px;stroke:var(--text2)}
.clink:hover .clink-icon svg{stroke:var(--accent2)}
.clink-label{font-family:var(--M);font-size:.6rem;color:var(--text3);letter-spacing:1px;text-transform:uppercase;margin-bottom:.18rem}
.clink-val{font-size:.88rem;color:var(--text);font-weight:500}
.clink-arrow{color:var(--text3);font-size:.8rem;transition:transform .2s,color .2s}
.clink:hover .clink-arrow{transform:translate(3px,-3px);color:var(--accent2)}

/* ─── FOOTER ─── */
#foot{border-top:1px solid var(--bd);padding:1.6rem 0}
.foot-inner{
  max-width:1120px;margin:0 auto;
  padding:0 clamp(1.25rem,5vw,3.5rem);
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;
}
.foot-copy{font-family:var(--M);font-size:.62rem;color:var(--text3)}
.foot-links{display:flex;gap:1.5rem}
.foot-links a{font-family:var(--M);font-size:.6rem;color:var(--text3);transition:color .2s;letter-spacing:.5px}
.foot-links a:hover{color:var(--accent2)}

/* ─── SCROLL REVEAL ─── */
.rev{opacity:0;transform:translateY(24px);transition:opacity .65s ease,transform .65s ease}
.rev.in{opacity:1;transform:none}
.rev-d1{transition-delay:.08s}.rev-d2{transition-delay:.16s}.rev-d3{transition-delay:.24s}

/* ─── RESPONSIVE ─── */
@media(max-width:900px){
  .hg{grid-template-columns:1fr}.hcard{display:none}
  .stats-row{grid-template-columns:repeat(2,1fr)}
  .stat:nth-child(2){border-right:none}
  .stat:nth-child(3){border-top:1px solid var(--bd)}
  .sk-g{grid-template-columns:1fr}
  .exp-grid{grid-template-columns:1fr}
  .contact-grid{grid-template-columns:1fr;gap:3rem}
  .proj{grid-template-columns:48px 1fr}
  .proj-right{display:none}
  .nl a:not(.nav-cta):not(:last-child){display:none}
}
@media(max-width:560px){
  .stats-row{grid-template-columns:1fr 1fr}
  .stat:nth-child(2){border-right:none}
}
</style>
</head>
<body>

<div class="glow-orb g1"></div>
<div class="glow-orb g2"></div>
<div class="glow-orb g3"></div>

<div id="root">

<!-- NAV -->
<nav id="nav">
  <div class="ni">
    <a href="#hero" class="logo">
      <div class="logo-dot"></div>
      Shravan Parthe
    </a>
    <div class="nl">
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#experience">Experience</a>
      <a href="#contact" class="nav-cta">Hire Me</a>
    </div>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="w">
    <div class="hg">
      <div>
        <div class="h-eyebrow">
          <div class="h-eyebrow-dot"></div>
          Available for internships &amp; collaborations
        </div>
        <h1 class="ht">
          <span class="ht-name">Shravan</span>
          <span class="ht-line">Parthe<span class="ht-accent">.</span></span>
        </h1>
        <div class="h-role">
          <span class="h-role-bar"></span>
          Backend &amp; AI Developer &nbsp;·&nbsp; B.Tech CSE AI/ML
        </div>
        <p class="hdesc">
          I build <strong>production-grade backends</strong> in Java and Spring Boot,
          cross-platform apps in Flutter, and integrate <strong>Gen AI</strong> into real systems.
          Currently interning at <strong>Innovexis</strong> — deploying ML pipelines to production.
        </p>
        <div class="hacts">
          <a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
            Get in Touch
          </a>
          <a href="https://github.com/Shravan157" target="_blank" class="btn btn-ghost">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            GitHub
          </a>
          <a href=""" + f'"{RESUME_URL}"' + """ target="_blank" download class="btn btn-outline">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><polyline points="9 15 12 18 15 15"/></svg>
            Resume
          </a>
        </div>
      </div>

      <!-- CODE CARD -->
      <div class="hcard">
        <div class="hcard-header">
          <div class="hch-dots">
            <div class="hch-dot d1"></div>
            <div class="hch-dot d2"></div>
            <div class="hch-dot d3"></div>
          </div>
          <span class="hch-title">shravan.java</span>
        </div>
        <div class="code-block">
          <div class="cl"><span class="ln">1</span><span class="cm">// Developer profile</span></div>
          <div class="cl"><span class="ln">2</span><span class="kw">public class </span><span class="fn">Shravan</span><span class="op"> {</span></div>
          <div class="cl"><span class="ln">3</span>&nbsp;</div>
          <div class="cl"><span class="ln">4</span>&nbsp;&nbsp;<span class="kw">String</span><span class="op"> </span><span class="pr">name</span><span class="op"> = </span><span class="str">"Shravan Parthe"</span><span class="op">;</span></div>
          <div class="cl"><span class="ln">5</span>&nbsp;&nbsp;<span class="kw">String</span><span class="op"> </span><span class="pr">role</span><span class="op"> = </span><span class="str">"Backend + AI Dev"</span><span class="op">;</span></div>
          <div class="cl"><span class="ln">6</span>&nbsp;&nbsp;<span class="kw">int</span><span class="op"> </span><span class="pr">year</span><span class="op"> = </span><span class="val">3</span><span class="op">;</span></div>
          <div class="cl"><span class="ln">7</span>&nbsp;</div>
          <div class="cl"><span class="ln">8</span>&nbsp;&nbsp;<span class="kw">String</span><span class="op">[] </span><span class="pr">stack</span><span class="op"> = {</span></div>
          <div class="cl"><span class="ln">9</span>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Java"</span><span class="op">, </span><span class="str">"Spring Boot"</span><span class="op">,</span></div>
          <div class="cl"><span class="ln">10</span>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Python"</span><span class="op">, </span><span class="str">"Flutter"</span><span class="op">,</span></div>
          <div class="cl"><span class="ln">11</span>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"FastAPI"</span><span class="op">, </span><span class="str">"Spring AI"</span></div>
          <div class="cl"><span class="ln">12</span>&nbsp;&nbsp;<span class="op">};</span></div>
          <div class="cl"><span class="ln">13</span>&nbsp;</div>
          <div class="cl"><span class="ln">14</span>&nbsp;&nbsp;<span class="fn">boolean</span><span class="op"> </span><span class="pr">openToWork</span><span class="op"> = </span><span class="val">true</span><span class="op">;</span><span class="blink"></span></div>
          <div class="cl"><span class="ln">15</span><span class="op">}</span></div>
        </div>
        <div class="hcard-tags">
          <span class="htag">Java</span>
          <span class="htag">Spring Boot</span>
          <span class="htag">Python</span>
          <span class="htag">Flutter</span>
          <span class="htag">FastAPI</span>
          <span class="htag">Spring AI</span>
          <span class="htag">MySQL</span>
          <span class="htag">Redis</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- STATS -->
<section id="stats">
  <div class="w">
    <div class="stats-row rev">
      <div class="stat"><div class="stat-n">6+</div><div class="stat-l">Projects Shipped</div></div>
      <div class="stat"><div class="stat-n">7.5</div><div class="stat-l">CGPA</div></div>
      <div class="stat"><div class="stat-n">3rd</div><div class="stat-l">Year B.Tech</div></div>
      <div class="stat"><div class="stat-n">2027</div><div class="stat-l">Graduating</div></div>
    </div>
  </div>
</section>

<!-- SKILLS -->
<section id="skills">
  <div class="w">
    <div class="sh rev">
      <div class="sh-top">
        <span class="sh-idx">01</span>
        <div class="sh-line"></div>
      </div>
      <div class="sh-t">Tech Stack</div>
      <div class="sh-sub">Languages, frameworks, and tools I work with daily</div>
    </div>
    <div class="sk-g rev">
      <div class="sk-c">
        <div class="sk-label">Languages</div>
        <div class="chips">
          <span class="chip ca">Java</span>
          <span class="chip ca">Python</span>
          <span class="chip ca">JavaScript</span>
          <span class="chip ca">Dart</span>
          <span class="chip ca">SQL</span>
        </div>
      </div>
      <div class="sk-c">
        <div class="sk-label">Frameworks</div>
        <div class="chips">
          <span class="chip cb">Spring Boot</span>
          <span class="chip cb">FastAPI</span>
          <span class="chip cb">Flutter</span>
          <span class="chip cb">React</span>
          <span class="chip cb">Spring AI</span>
        </div>
      </div>
      <div class="sk-c">
        <div class="sk-label">ML / Data</div>
        <div class="chips">
          <span class="chip cc">Scikit-learn</span>
          <span class="chip cc">Pandas</span>
          <span class="chip cc">NumPy</span>
          <span class="chip cc">NLTK</span>
          <span class="chip cc">TF-IDF</span>
        </div>
      </div>
      <div class="sk-c">
        <div class="sk-label">Infrastructure</div>
        <div class="chips">
          <span class="chip cd">Docker</span>
          <span class="chip cd">MySQL</span>
          <span class="chip cd">PostgreSQL</span>
          <span class="chip cd">Redis</span>
          <span class="chip cd">Firebase</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PROJECTS -->
<section id="projects">
  <div class="w">
    <div class="sh rev">
      <div class="sh-top">
        <span class="sh-idx">02</span>
        <div class="sh-line"></div>
      </div>
      <div class="sh-t">Selected Work</div>
      <div class="sh-sub">Production-grade projects built from scratch</div>
    </div>
    <div class="proj-list rev">

      <div class="proj">
        <span class="proj-idx">01</span>
        <div class="proj-main">
          <div class="proj-title">MedoraX AI — Clinical AI Assistant</div>
          <div class="proj-desc">Multimodal clinical assistant with voice, image, and text. Transcribes symptoms via Whisper-large-v3, analyzes medical images via Llama-4-scout, generates structured diagnostic responses. Multilingual support (English, Hindi, Marathi) with GPS hospital finder and real-time AQI monitoring.</div>
          <div class="proj-stack">
            <span class="stk">Python</span><span class="stk">Gradio</span><span class="stk">Groq API</span><span class="stk">Whisper</span><span class="stk">Google Maps API</span>
          </div>
        </div>
        <div class="proj-right">
          <span class="proj-badge ba">Healthcare AI</span>
          <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="proj-link">
            GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
          </a>
        </div>
      </div>

      <div class="proj">
        <span class="proj-idx">02</span>
        <div class="proj-main">
          <div class="proj-title">SahayLoan — Micro-Lending Platform</div>
          <div class="proj-desc">Full-stack micro-lending platform for loans up to ₹1,00,000. Flutter frontend, FastAPI backend, Random Forest credit scoring model, Aadhaar &amp; PAN OCR via Tesseract for digital KYC, Stripe EMI integration, Firebase Auth with multi-role access control.</div>
          <div class="proj-stack">
            <span class="stk">Flutter</span><span class="stk">FastAPI</span><span class="stk">Scikit-learn</span><span class="stk">Firebase</span><span class="stk">Stripe</span><span class="stk">Tesseract</span>
          </div>
        </div>
        <div class="proj-right">
          <span class="proj-badge bb">FinTech</span>
          <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="proj-link">
            GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
          </a>
        </div>
      </div>

      <div class="proj">
        <span class="proj-idx">03</span>
        <div class="proj-main">
          <div class="proj-title">SikshaSetu — Rural Education Platform</div>
          <div class="proj-desc">Education platform bridging the digital divide for rural communities. Spring Security + JWT/OAuth 2.0 auth, optimized relational schema, React frontend, ZEGOCLOUD real-time video SDK for virtual classrooms. Role-based access for students, teachers, and admins.</div>
          <div class="proj-stack">
            <span class="stk">React</span><span class="stk">Spring Boot</span><span class="stk">Spring Security</span><span class="stk">JWT</span><span class="stk">MySQL</span><span class="stk">ZEGOCLOUD</span>
          </div>
        </div>
        <div class="proj-right">
          <span class="proj-badge bc">Full-Stack</span>
          <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="proj-link">
            GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
          </a>
        </div>
      </div>

      <div class="proj">
        <span class="proj-idx">04</span>
        <div class="proj-main">
          <div class="proj-title">AI-Powered E-Commerce Backend</div>
          <div class="proj-desc">Intelligent e-commerce backend with AI product recommendations via Spring AI + Redis Vector DB similarity search. Generative AI chatbot for real-time support, AI image generation pipeline, Spring Security + JWT auth, React storefront with Tailwind.</div>
          <div class="proj-stack">
            <span class="stk">Spring Boot</span><span class="stk">Spring AI</span><span class="stk">Redis Vector DB</span><span class="stk">React</span><span class="stk">Tailwind</span>
          </div>
        </div>
        <div class="proj-right">
          <span class="proj-badge ba">AI / Full-Stack</span>
          <a href="https://github.com/Shravan157" target="_blank" class="proj-link">
            GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
          </a>
        </div>
      </div>

      <div class="proj">
        <span class="proj-idx">05</span>
        <div class="proj-main">
          <div class="proj-title">Zomato Review Sentiment Analysis</div>
          <div class="proj-desc">End-to-end NLP pipeline classifying 10,000+ Zomato reviews. Extensive EDA with 15 visualizations, hypothesis testing, TF-IDF vectorization with bigrams, model comparison across Logistic Regression, Random Forest, and LinearSVC — Logistic Regression achieved highest F1 score.</div>
          <div class="proj-stack">
            <span class="stk">Python</span><span class="stk">Scikit-learn</span><span class="stk">NLTK</span><span class="stk">TF-IDF</span><span class="stk">Pandas</span><span class="stk">Seaborn</span>
          </div>
        </div>
        <div class="proj-right">
          <span class="proj-badge bd-badge">ML / NLP</span>
          <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="proj-link">
            GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
          </a>
        </div>
      </div>

      <div class="proj">
        <span class="proj-idx">06</span>
        <div class="proj-main">
          <div class="proj-title">PhonePe Insights — Data Engineering Dashboard</div>
          <div class="proj-desc">End-to-end ETL and visualization platform for PhonePe transaction data. Automated database setup and data loading, MySQL backend via SQLAlchemy + PyMySQL, interactive Streamlit dashboard with Plotly and Seaborn for transaction analytics.</div>
          <div class="proj-stack">
            <span class="stk">Python</span><span class="stk">Streamlit</span><span class="stk">MySQL</span><span class="stk">SQLAlchemy</span><span class="stk">Plotly</span><span class="stk">Pandas</span>
          </div>
        </div>
        <div class="proj-right">
          <span class="proj-badge bb">Data Engineering</span>
          <a href="https://github.com/Shravan157/phonepe-insights" target="_blank" class="proj-link">
            GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
          </a>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- EXPERIENCE -->
<section id="experience">
  <div class="w">
    <div class="sh rev">
      <div class="sh-top">
        <span class="sh-idx">03</span>
        <div class="sh-line"></div>
      </div>
      <div class="sh-t">Experience &amp; Education</div>
      <div class="sh-sub">Where I've worked and what I'm studying</div>
    </div>
    <div class="exp-grid rev">
      <div class="exp-card active">
        <div class="exp-period">APR 2026 — PRESENT &nbsp;·&nbsp; REMOTE</div>
        <div class="exp-role">Data Science with Gen AI Intern</div>
        <div class="exp-company">Innovexis</div>
        <ul class="exp-list">
          <li>Selected for competitive Gen AI internship program</li>
          <li>Building real-world projects integrating LLMs and generative AI</li>
          <li>Python, Pandas, Scikit-learn for data analysis and model development</li>
          <li>Production-level Gen AI workflow exposure</li>
        </ul>
        <div class="exp-pill pill-green"><div class="pulse"></div>Currently Active</div>
      </div>
      <div class="exp-card edu">
        <div class="exp-period">JUN 2023 — MAY 2027 (EXPECTED)</div>
        <div class="exp-role">B.Tech, Computer Science (AI &amp; ML)</div>
        <div class="exp-company">ViMEET · University of Mumbai</div>
        <ul class="exp-list">
          <li>Specializing in Artificial Intelligence &amp; Machine Learning</li>
          <li>Coursework: DSA, ML, Cloud Computing, Microservices, System Design</li>
          <li>Building production projects alongside academics</li>
        </ul>
        <div class="exp-pill pill-amber">CGPA 7.5 / 10.0</div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section id="contact">
  <div class="w">
    <div class="sh rev">
      <div class="sh-top">
        <span class="sh-idx">04</span>
        <div class="sh-line"></div>
      </div>
      <div class="sh-t">Let's Connect</div>
    </div>
    <div class="contact-grid rev">
      <div>
        <div class="contact-h">Open to <span>opportunities</span><br>and collaboration</div>
        <p class="contact-sub">Looking for backend, mobile, or AI engineering internships. Also open to project collaborations and open-source contributions. If you're building something interesting, let's talk.</p>
        <div style="display:flex;gap:.75rem;flex-wrap:wrap">
          <a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">Send a Message</a>
          <a href=""" + f'"{RESUME_URL}"' + """ target="_blank" download class="btn btn-outline">Download Resume</a>
        </div>
      </div>
      <div class="clinks">
        <a href="mailto:shravanparthe@gmail.com" class="clink">
          <div class="clink-left">
            <div class="clink-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
            </div>
            <div>
              <div class="clink-label">Email</div>
              <div class="clink-val">shravanparthe@gmail.com</div>
            </div>
          </div>
          <span class="clink-arrow">↗</span>
        </a>
        <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank" class="clink">
          <div class="clink-left">
            <div class="clink-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
            </div>
            <div>
              <div class="clink-label">LinkedIn</div>
              <div class="clink-val">Shravan Parthe</div>
            </div>
          </div>
          <span class="clink-arrow">↗</span>
        </a>
        <a href="https://github.com/Shravan157" target="_blank" class="clink">
          <div class="clink-left">
            <div class="clink-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </div>
            <div>
              <div class="clink-label">GitHub</div>
              <div class="clink-val">Shravan157</div>
            </div>
          </div>
          <span class="clink-arrow">↗</span>
        </a>
        <div class="clink" style="cursor:default">
          <div class="clink-left">
            <div class="clink-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </div>
            <div>
              <div class="clink-label">Location</div>
              <div class="clink-val">Nagpur, Maharashtra, India</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer id="foot">
  <div class="foot-inner">
    <div class="foot-copy">Built by Shravan Parthe &nbsp;·&nbsp; 2026</div>
    <div class="foot-links">
      <a href="https://github.com/Shravan157" target="_blank">GitHub</a>
      <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn</a>
      <a href="mailto:shravanparthe@gmail.com">Email</a>
    </div>
  </div>
</footer>

</div>

<script>
(function(){
  /* NAV SCROLL */
  var nav = document.getElementById('nav');
  window.addEventListener('scroll', function(){
    if(window.scrollY > 50) nav.classList.add('s');
    else nav.classList.remove('s');
  }, {passive:true});

  /* SMOOTH SCROLL */
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var t = document.querySelector(a.getAttribute('href'));
      if(t){ e.preventDefault(); t.scrollIntoView({behavior:'smooth'}); }
    });
  });

  /* SCROLL REVEAL */
  var obs = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){ e.target.classList.add('in'); obs.unobserve(e.target); }
    });
  }, {threshold:0.06});
  document.querySelectorAll('.rev').forEach(function(el){ obs.observe(el); });
})();
</script>
</body>
</html>"""

components.html(HTML, height=5600, scrolling=True)
