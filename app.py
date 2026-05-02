import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Shravan Parthe — Space Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  #MainMenu, header, footer, [data-testid="stToolbar"],
  [data-testid="stDecoration"], [data-testid="stStatusWidget"],
  .stDeployButton { visibility: hidden !important; display: none !important; }
  .stApp { background: #02040e !important; }
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
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Sora:wght@300;400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
:root{
  --void:#02040e;
  --surf:rgba(255,255,255,0.032);
  --surf2:rgba(255,255,255,0.062);
  --bd:rgba(122,162,255,0.12);
  --bd2:rgba(122,162,255,0.22);
  --text:#dce8ff;
  --muted:#7b8db5;
  --sub:#404d6a;
  --cyan:#5ef3ff;
  --gold:#ffc94d;
  --violet:#a78bfa;
  --green:#34d399;
  --pink:#f472b6;
  --blue:#60a5fa;
  --H:'Orbitron',monospace;
  --B:'Sora',sans-serif;
  --M:'Space Mono',monospace;
}
body{
  font-family:var(--B);background:var(--void);color:var(--text);
  line-height:1.65;overflow-x:hidden;-webkit-font-smoothing:antialiased;
}
::selection{background:var(--violet);color:#fff}
::-webkit-scrollbar{width:3px}
::-webkit-scrollbar-track{background:var(--void)}
::-webkit-scrollbar-thumb{background:var(--violet);border-radius:99px}
a{color:inherit;text-decoration:none}

/* CANVAS */
#c{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}

/* NEBULAE */
.nb{position:fixed;border-radius:50%;pointer-events:none;z-index:1;animation:ndrift 20s ease-in-out infinite alternate;filter:blur(80px)}
.n1{width:700px;height:700px;background:radial-gradient(circle,rgba(167,139,250,.18),transparent);top:-200px;left:-200px;animation-delay:0s}
.n2{width:600px;height:600px;background:radial-gradient(circle,rgba(94,243,255,.14),transparent);top:20%;right:-180px;animation-delay:-7s}
.n3{width:500px;height:500px;background:radial-gradient(circle,rgba(96,165,250,.1),transparent);bottom:-100px;left:30%;animation-delay:-14s}
.n4{width:350px;height:350px;background:radial-gradient(circle,rgba(244,114,182,.1),transparent);top:55%;left:5%;animation-delay:-4s}
@keyframes ndrift{from{transform:translate(0,0) scale(1)}to{transform:translate(35px,55px) scale(1.1)}}

/* GRAIN */
body::after{
  content:'';position:fixed;inset:0;z-index:2;pointer-events:none;opacity:.5;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.88' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.032'/%3E%3C/svg%3E");
}

/* LAYOUT */
#root{position:relative;z-index:3}
.w{max-width:1160px;margin:0 auto;padding:0 clamp(1.2rem,5vw,3.5rem)}

/* NAV */
#nav{
  position:fixed;top:0;left:0;right:0;z-index:999;
  padding:.9rem 0;background:rgba(2,4,14,.72);
  backdrop-filter:blur(20px);border-bottom:1px solid rgba(94,243,255,.06);
  transition:background .3s,border-color .3s;
}
#nav.scrolled{background:rgba(2,4,14,.92);border-bottom-color:rgba(94,243,255,.12)}
.ni{
  max-width:1160px;margin:0 auto;
  padding:0 clamp(1.2rem,5vw,3.5rem);
  display:flex;align-items:center;justify-content:space-between;
}
.logo{font-family:var(--H);font-weight:900;font-size:.95rem;letter-spacing:3px;color:var(--text)}
.logo em{color:var(--cyan);font-style:normal}
.nl{display:flex;align-items:center;gap:2rem}
.nl a{
  font-family:var(--M);font-size:.6rem;letter-spacing:2.5px;
  text-transform:uppercase;color:var(--muted);transition:color .2s;
  padding:.2rem 0;position:relative;
}
.nl a::after{content:'';position:absolute;bottom:0;left:0;width:0;height:1px;background:var(--cyan);transition:width .3s}
.nl a:hover{color:var(--cyan)}
.nl a:hover::after{width:100%}
.live-badge{
  display:flex;align-items:center;gap:.45rem;
  padding:.3rem .85rem;border:1px solid rgba(52,211,153,.22);
  border-radius:99px;font-family:var(--M);font-size:.6rem;
  color:var(--green);background:rgba(52,211,153,.06);transition:all .3s;
}
.live-badge:hover{background:rgba(52,211,153,.12);border-color:rgba(52,211,153,.4)}
.ld{width:6px;height:6px;border-radius:50%;background:var(--green);box-shadow:0 0 10px var(--green);animation:ldp 2.2s ease-in-out infinite}
@keyframes ldp{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(.7)}}

/* HERO */
#hero{min-height:100vh;display:flex;align-items:center;padding:8rem 0 5rem;position:relative}
.hg{display:grid;grid-template-columns:1.1fr .9fr;gap:4rem;align-items:center;width:100%}
.coord{
  font-family:var(--M);font-size:.6rem;color:var(--cyan);
  letter-spacing:3px;text-transform:uppercase;margin-bottom:1.4rem;
  display:flex;align-items:center;gap:.7rem;
  opacity:0;animation:fsu .8s ease forwards .15s;
}
.coord::before{content:'';width:40px;height:1px;background:linear-gradient(90deg,var(--cyan),transparent)}
h1.ht{
  font-family:var(--H);font-weight:900;text-transform:uppercase;
  font-size:clamp(2.6rem,6.5vw,5.2rem);line-height:1.04;
  letter-spacing:-1px;margin-bottom:1.2rem;
  opacity:0;animation:fsu .9s ease forwards .3s;
}
.ht .glow{color:var(--cyan);text-shadow:0 0 30px rgba(94,243,255,.35),0 0 70px rgba(94,243,255,.12)}
.hrole{
  font-family:var(--M);font-size:.7rem;color:var(--gold);
  letter-spacing:2.5px;text-transform:uppercase;margin-bottom:1.8rem;
  opacity:0;animation:fsu .9s ease forwards .45s;
}
.hrole::before{content:'// ';color:var(--sub)}
.hdesc{
  color:var(--muted);font-size:.95rem;line-height:1.95;
  max-width:520px;margin-bottom:2.2rem;
  opacity:0;animation:fsu .9s ease forwards .6s;
}
.hdesc strong{color:var(--text);font-weight:600}
.hacts{display:flex;gap:.75rem;flex-wrap:wrap;opacity:0;animation:fsu .9s ease forwards .75s}
@keyframes fsu{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}

/* BUTTONS */
.ba{
  display:inline-flex;align-items:center;gap:.55rem;
  padding:.78rem 1.6rem;border-radius:4px;
  font-family:var(--M);font-size:.62rem;font-weight:700;
  letter-spacing:2.5px;text-transform:uppercase;
  transition:all .3s cubic-bezier(.4,0,.2,1);cursor:pointer;
}
.ba-primary{
  background:linear-gradient(135deg,var(--cyan),#26c6da);color:#000;
  box-shadow:0 4px 24px rgba(94,243,255,.18);position:relative;overflow:hidden;
}
.ba-primary::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,transparent,rgba(255,255,255,.28),transparent);
  transform:translateX(-100%);transition:transform .55s ease;
}
.ba-primary:hover{transform:translateY(-3px);box-shadow:0 8px 36px rgba(94,243,255,.32)}
.ba-primary:hover::before{transform:translateX(100%)}
.ba-ghost{border:1px solid var(--bd2);color:var(--muted);background:rgba(94,243,255,.03)}
.ba-ghost:hover{border-color:var(--cyan);color:var(--cyan);background:rgba(94,243,255,.08);transform:translateY(-3px)}
.ba-resume{border:1px solid rgba(255,201,77,.25);color:var(--gold);background:rgba(255,201,77,.04)}
.ba-resume:hover{border-color:var(--gold);background:rgba(255,201,77,.1);transform:translateY(-3px)}

/* SCENE */
.hscene{position:relative;display:flex;justify-content:center;align-items:center;opacity:0;animation:fsu 1s ease forwards .5s}
.scene-box{
  width:100%;max-width:420px;min-height:500px;
  border:1px solid var(--bd);border-radius:24px;
  background:linear-gradient(160deg,rgba(10,16,42,.92),rgba(4,8,22,.8));
  position:relative;overflow:hidden;
  box-shadow:0 20px 80px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.04);
}
.scene-box::before{
  content:'';position:absolute;inset:0;
  background:radial-gradient(circle at 68% 20%,rgba(94,243,255,.14),transparent 22%),
             radial-gradient(circle at 25% 72%,rgba(167,139,250,.16),transparent 22%);
}
.or{position:absolute;border:1px dashed rgba(94,243,255,.12);border-radius:50%;top:50%;left:50%}
.or1{width:380px;height:380px;margin:-190px 0 0 -190px;animation:orspin 60s linear infinite}
.or2{width:260px;height:260px;margin:-130px 0 0 -130px;animation:orspin 40s linear infinite reverse}
.or3{width:160px;height:160px;margin:-80px 0 0 -80px;animation:orspin 25s linear infinite}
@keyframes orspin{to{transform:rotate(360deg)}}
.od{position:absolute;border-radius:50%;top:0;left:50%;transform:translate(-50%,-50%)}
.od1{width:7px;height:7px;background:var(--cyan);box-shadow:0 0 14px var(--cyan)}
.od2{width:5px;height:5px;background:var(--gold);box-shadow:0 0 10px var(--gold)}
.od3{width:9px;height:9px;background:var(--pink);box-shadow:0 0 16px var(--pink)}
.planet{
  position:absolute;top:50%;left:50%;
  width:88px;height:88px;border-radius:50%;
  transform:translate(-50%,-65%);
  background:radial-gradient(circle at 32% 28%,#9ecfff,#4a80d0 45%,#1a3a7a 80%,#0d1f44);
  box-shadow:0 0 50px rgba(94,163,255,.3),0 0 100px rgba(94,163,255,.12),inset -8px -8px 20px rgba(0,0,0,.35);
  animation:pp 4s ease-in-out infinite;
}
.planet::after{
  content:'';position:absolute;top:50%;left:50%;
  width:130px;height:32px;border:2px solid rgba(94,163,255,.3);border-radius:50%;
  transform:translate(-50%,-50%) rotateX(72deg);
}
@keyframes pp{
  0%,100%{box-shadow:0 0 50px rgba(94,163,255,.3),0 0 100px rgba(94,163,255,.12),inset -8px -8px 20px rgba(0,0,0,.35)}
  50%{box-shadow:0 0 65px rgba(94,163,255,.42),0 0 130px rgba(94,163,255,.18),inset -8px -8px 20px rgba(0,0,0,.35)}
}
.astro-svg{
  position:absolute;top:50%;left:50%;
  transform:translate(-50%,10%);
  animation:afloat 6s ease-in-out infinite;z-index:5;
}
@keyframes afloat{0%,100%{transform:translate(-50%,10%) rotate(-2deg)}50%{transform:translate(-50%,-2%) rotate(2deg)}}
.rkt-svg{
  position:absolute;right:32px;top:40px;
  animation:rfloat 5s ease-in-out infinite;z-index:5;
  filter:drop-shadow(0 0 18px rgba(94,243,255,.22));
}
@keyframes rfloat{0%,100%{transform:translateY(0) rotate(20deg)}50%{transform:translateY(-14px) rotate(15deg)}}
.sbc{
  position:absolute;bottom:20px;left:18px;right:18px;
  display:grid;grid-template-columns:1fr 1fr;gap:10px;z-index:6;
}
.sbc-card{
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);
  border-radius:14px;padding:1rem 1.1rem;backdrop-filter:blur(12px);transition:all .3s;
}
.sbc-card:hover{background:rgba(255,255,255,.07);border-color:rgba(94,243,255,.15);transform:translateY(-2px)}
.sbc-l{font-family:var(--M);color:var(--sub);font-size:.58rem;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:.35rem}
.sbc-v{color:var(--text);font-size:.82rem;line-height:1.55;font-weight:500}

/* SECTION HEADER */
.sh{display:flex;align-items:center;gap:.8rem;margin-bottom:2.8rem}
.sh-n{font-family:var(--M);font-size:.6rem;color:var(--cyan);letter-spacing:2px}
.sh-ic{font-size:.9rem}
.sh-t{font-family:var(--H);font-size:.65rem;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:var(--text)}
.sh-ln{flex:1;height:1px;background:linear-gradient(90deg,var(--bd2),transparent)}

/* STATS */
#stats{padding:4rem 0 5rem}
.sg{
  display:grid;grid-template-columns:repeat(4,1fr);
  gap:1px;background:var(--bd);border:1px solid var(--bd);border-radius:8px;overflow:hidden;
}
.sb{background:var(--surf);padding:2rem 1.5rem;text-align:center;transition:background .3s;position:relative;overflow:hidden}
.sb::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--cyan),transparent);
  opacity:0;transition:opacity .3s;
}
.sb:hover{background:var(--surf2)}
.sb:hover::after{opacity:1}
.sn{
  font-family:var(--H);font-size:2.4rem;font-weight:800;line-height:1;margin-bottom:.3rem;
  background:linear-gradient(135deg,var(--cyan),var(--blue));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.sl{font-family:var(--M);font-size:.55rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--muted)}

/* SKILLS */
#skills{padding:5rem 0}
.sk-g{display:grid;grid-template-columns:repeat(2,1fr);gap:.75rem}
.sk-c{
  border:1px solid var(--bd);border-radius:8px;padding:1.5rem;
  background:var(--surf);position:relative;overflow:hidden;transition:border-color .3s,background .3s;
}
.sk-c::before{
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--cyan),transparent);opacity:0;transition:opacity .3s;
}
.sk-c:hover{border-color:rgba(94,243,255,.2);background:var(--surf2)}
.sk-c:hover::before{opacity:1}
.sk-l{
  font-family:var(--M);font-size:.57rem;letter-spacing:2.5px;
  text-transform:uppercase;color:var(--cyan);
  margin-bottom:.9rem;display:flex;align-items:center;gap:.45rem;
}
.sk-l::before{content:'&#9658;';font-size:.42rem;opacity:.7}
.chips{display:flex;flex-wrap:wrap;gap:.38rem}
.chip{padding:.24rem .65rem;border-radius:3px;font-family:var(--M);font-size:.66rem;transition:transform .15s,box-shadow .15s;cursor:default}
.chip:hover{transform:translateY(-2px)}
.c1{background:rgba(94,243,255,.07);color:var(--cyan);border:1px solid rgba(94,243,255,.2)}
.c1:hover{box-shadow:0 4px 14px rgba(94,243,255,.15)}
.c2{background:rgba(167,139,250,.08);color:#c4b5fd;border:1px solid rgba(167,139,250,.22)}
.c2:hover{box-shadow:0 4px 14px rgba(167,139,250,.15)}
.c3{background:rgba(96,165,250,.07);color:#93c5fd;border:1px solid rgba(96,165,250,.2)}
.c3:hover{box-shadow:0 4px 14px rgba(96,165,250,.15)}
.c4{background:rgba(52,211,153,.07);color:#6ee7b7;border:1px solid rgba(52,211,153,.2)}
.c4:hover{box-shadow:0 4px 14px rgba(52,211,153,.15)}

/* PROJECTS */
#missions{padding:5rem 0}
.plist{display:flex;flex-direction:column}
.pi{
  display:grid;grid-template-columns:72px 1fr;
  border-top:1px solid var(--bd);padding:2.2rem 0;
  position:relative;overflow:hidden;
}
.pi:last-child{border-bottom:1px solid var(--bd)}
.pi::before{
  content:'';position:absolute;left:0;top:0;bottom:0;width:2px;
  background:linear-gradient(to bottom,transparent,var(--cyan),transparent);
  opacity:0;transition:opacity .35s;
}
.pi:hover::before{opacity:1}
.pi-n{font-family:var(--M);font-size:.58rem;color:var(--sub);padding-top:.25rem;letter-spacing:1.5px}
.pi-top{display:flex;align-items:flex-start;justify-content:space-between;gap:1rem;margin-bottom:.5rem}
.pi-nm{font-family:var(--H);font-size:.88rem;font-weight:600;color:var(--text);letter-spacing:.5px}
.pi-tg{padding:.18rem .65rem;border-radius:3px;font-family:var(--M);font-size:.55rem;letter-spacing:1px;text-transform:uppercase;white-space:nowrap;flex-shrink:0}
.ta{background:rgba(167,139,250,.1);color:#c4b5fd;border:1px solid rgba(167,139,250,.22)}
.tb{background:rgba(94,243,255,.08);color:var(--cyan);border:1px solid rgba(94,243,255,.2)}
.tc{background:rgba(52,211,153,.08);color:#6ee7b7;border:1px solid rgba(52,211,153,.2)}
.td{background:rgba(255,201,77,.08);color:var(--gold);border:1px solid rgba(255,201,77,.2)}
.pi-d{color:var(--muted);font-size:.85rem;line-height:1.85;margin-bottom:.9rem;max-width:700px}
.pi-ft{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:.5rem}
.pi-tech{display:flex;flex-wrap:wrap;gap:.3rem}
.tt{padding:.14rem .48rem;border-radius:3px;font-family:var(--M);font-size:.6rem;color:var(--sub);border:1px solid var(--bd)}
.pi-lk{display:inline-flex;align-items:center;gap:.3rem;font-family:var(--M);font-size:.62rem;color:var(--muted);transition:color .2s;flex-shrink:0}
.pi-lk:hover{color:var(--cyan)}
.pi-lk:hover svg{transform:translate(2px,-2px)}
.pi-lk svg{transition:transform .2s}

/* EXPERIENCE */
#log{padding:5rem 0}
.eg{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.ec{
  border:1px solid var(--bd);border-radius:8px;padding:2rem;
  background:var(--surf);position:relative;overflow:hidden;transition:border-color .3s,background .3s;
}
.ec::after{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,var(--cyan),var(--violet),transparent);opacity:0;transition:opacity .35s;
}
.ec:hover{border-color:rgba(94,243,255,.18);background:var(--surf2)}
.ec:hover::after{opacity:1}
.ep{font-family:var(--M);font-size:.58rem;color:var(--cyan);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:.7rem}
.er{font-family:var(--H);font-size:.88rem;color:var(--text);font-weight:600;margin-bottom:.2rem;letter-spacing:.5px}
.eo{font-family:var(--M);font-size:.72rem;color:var(--gold);margin-bottom:1.2rem}
.el{list-style:none}
.el li{color:var(--muted);font-size:.83rem;line-height:1.8;padding:.15rem 0 .15rem 1.2rem;position:relative}
.el li::before{content:'\\203A';position:absolute;left:0;color:var(--cyan);font-size:1.1rem;line-height:1.4}
.epill{display:inline-flex;align-items:center;gap:.4rem;margin-top:1.2rem;padding:.28rem .75rem;border-radius:99px;font-family:var(--M);font-size:.58rem}
.pill-g{color:var(--green);border:1px solid rgba(52,211,153,.22);background:rgba(52,211,153,.06)}
.pill-y{color:var(--gold);border:1px solid rgba(255,201,77,.22);background:rgba(255,201,77,.06)}

/* CONTACT */
#contact{padding:5rem 0 8rem}
.cg{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start}
.ch{
  font-family:var(--H);font-size:clamp(1.9rem,3.8vw,2.8rem);
  font-weight:900;text-transform:uppercase;line-height:1.08;
  margin-bottom:1.2rem;letter-spacing:-.5px;
}
.ch em{color:var(--cyan);font-style:normal;text-shadow:0 0 28px rgba(94,243,255,.3)}
.csub{color:var(--muted);font-size:.9rem;line-height:1.85;margin-bottom:2rem}
.cc-grid{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}
.cc{border:1px solid var(--bd);border-radius:6px;padding:1rem 1.2rem;background:var(--surf);transition:all .25s}
.cc:hover{border-color:rgba(94,243,255,.2);background:var(--surf2);transform:translateY(-2px)}
.cc-l{font-family:var(--M);font-size:.55rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--cyan);margin-bottom:.3rem}
.cc-v{font-size:.82rem;color:var(--text)}
.cc-v a{color:var(--muted);transition:color .2s}
.cc-v a:hover{color:var(--cyan)}
.cc.wide{grid-column:span 2}

/* QUOTE */
.qw{border-top:1px solid var(--bd);padding:5rem 0;text-align:center;position:relative}
.qw::before{
  content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);
  width:100px;height:1px;background:linear-gradient(90deg,transparent,var(--cyan),transparent);
}
.qm{font-family:var(--H);font-size:3rem;line-height:1;color:var(--sub);display:block;margin-bottom:1.5rem}
.qt{font-family:var(--B);font-style:italic;font-size:1rem;line-height:2.1;color:var(--muted);max-width:540px;margin:0 auto 1.2rem}
.qt em{color:var(--cyan);font-style:normal}
.qs{font-family:var(--M);font-size:.58rem;letter-spacing:3px;text-transform:uppercase;color:var(--sub)}

/* FOOTER */
#foot{border-top:1px solid var(--bd);padding:1.5rem 0}
.fi{
  max-width:1160px;margin:0 auto;
  padding:0 clamp(1.2rem,5vw,3.5rem);
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;
}
.fl{font-family:var(--M);font-size:.62rem;color:var(--sub)}
.fl a{color:var(--muted);transition:color .2s}
.fl a:hover{color:var(--cyan)}
.fls{display:flex;gap:1.5rem}
.fls a{font-family:var(--M);font-size:.6rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--sub);transition:color .2s}
.fls a:hover{color:var(--cyan)}

/* SCROLL REVEAL */
.rev{opacity:0;transform:translateY(28px);transition:opacity .7s ease,transform .7s ease}
.rev.in{opacity:1;transform:none}

/* RESPONSIVE */
@media(max-width:900px){
  .hg{grid-template-columns:1fr}
  .hscene{display:none}
  .sg{grid-template-columns:repeat(2,1fr)}
  .sk-g{grid-template-columns:1fr}
  .eg{grid-template-columns:1fr}
  .cg{grid-template-columns:1fr;gap:3rem}
  .nl a:not(.live-badge){display:none}
}
@media(max-width:560px){
  .cc-grid{grid-template-columns:1fr}
  .cc.wide{grid-column:span 1}
}
</style>
</head>
<body>
<canvas id="c"></canvas>
<div class="nb n1"></div>
<div class="nb n2"></div>
<div class="nb n3"></div>
<div class="nb n4"></div>

<div id="root">

<!-- NAV -->
<nav id="nav">
  <div class="ni">
    <a href="#hero" class="logo">SHRAVAN<em>.</em></a>
    <div class="nl">
      <a href="#skills">Arsenal</a>
      <a href="#missions">Missions</a>
      <a href="#log">Flight Log</a>
      <a href="#contact">Transmit</a>
      <div class="live-badge"><div class="ld"></div>Signal Live</div>
    </div>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="w">
    <div class="hg">

      <div>
        <div class="coord">&#9672; 19.0760&deg;N &middot; 72.8777&deg;E &middot; ALT &infin;</div>
        <h1 class="ht">
          <span class="glow">Shravan</span><br>Parthe.
        </h1>
        <div class="hrole">Backend Engineer &amp; AI Developer</div>
        <p class="hdesc">
          <strong>3rd year B.Tech CSE (AI&amp;ML)</strong> student building production&#8209;grade systems in Java, Spring Boot, and Python. On active mission at <strong>Innovexis</strong> &mdash; deploying real&#8209;world Gen&nbsp;AI integrations. Every project is a launch. Every bug, a re&#8209;entry.
        </p>
        <div class="hacts">
          <a href="mailto:shravanparthe@gmail.com" class="ba ba-primary">&#128640; Launch Contact</a>
          <a href="https://github.com/Shravan157" target="_blank" class="ba ba-ghost">&#9889; GitHub</a>
          <a href=\"""" + RESUME_URL + """\" target="_blank" download="Shravan_Parthe_Resume.pdf" class="ba ba-resume">&#128196; Resume</a>
        </div>
      </div>

      <div class="hscene">
        <div class="scene-box">
          <div class="or or1"><div class="od od1"></div></div>
          <div class="or or2"><div class="od od2"></div></div>
          <div class="or or3"><div class="od od3"></div></div>
          <div class="planet"></div>

          <!-- Rocket SVG -->
          <div class="rkt-svg">
            <svg viewBox="0 0 55 100" width="55" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <linearGradient id="rb" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1e3a5f"/><stop offset="100%" stop-color="#0a1628"/></linearGradient>
                <radialGradient id="rf" cx="50%" cy="0%"><stop offset="0%" stop-color="#5ef3ff"/><stop offset="50%" stop-color="#2979ff"/><stop offset="100%" stop-color="transparent"/></radialGradient>
              </defs>
              <ellipse cx="27.5" cy="86" rx="10" ry="18" fill="url(#rf)" opacity=".9">
                <animate attributeName="ry" values="18;22;15;20;18" dur=".32s" repeatCount="indefinite"/>
              </ellipse>
              <ellipse cx="27.5" cy="83" rx="5" ry="10" fill="#5ef3ff" opacity=".8">
                <animate attributeName="ry" values="10;13;8;11;10" dur=".25s" repeatCount="indefinite"/>
              </ellipse>
              <path d="M12 62 L2 80 L16 70 Z" fill="#1a3a6a"/>
              <path d="M43 62 L53 80 L39 70 Z" fill="#1a3a6a"/>
              <rect x="14" y="22" width="27" height="48" rx="6" fill="url(#rb)" stroke="#3d6080" stroke-width="1"/>
              <path d="M14 27 Q27.5 4 41 27 Z" fill="#1a3a6a" stroke="#3d5070" stroke-width="1"/>
              <circle cx="27.5" cy="50" r="7.5" fill="#0d2240" stroke="#5ef3ff" stroke-width="1.5"/>
              <circle cx="27.5" cy="50" r="4.5" fill="#163560" opacity=".8"/>
              <circle cx="26" cy="48.5" r="1.8" fill="white" opacity=".18"/>
              <rect x="14" y="64" width="27" height="4" fill="#5ef3ff" opacity=".3"/>
              <line x1="27.5" y1="18" x2="27.5" y2="7" stroke="#5ef3ff" stroke-width="1.4" opacity=".7"/>
              <circle cx="27.5" cy="5" r="3" fill="#5ef3ff" opacity=".85">
                <animate attributeName="opacity" values=".85;.3;.85" dur="1.1s" repeatCount="indefinite"/>
              </circle>
            </svg>
          </div>

          <!-- Astronaut SVG -->
          <div class="astro-svg">
            <svg viewBox="0 0 160 220" width="165" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <radialGradient id="vg" cx="36%" cy="30%"><stop offset="0%" stop-color="#82b4ff" stop-opacity=".92"/><stop offset="100%" stop-color="#0d3a8a" stop-opacity=".7"/></radialGradient>
                <radialGradient id="sg2" cx="33%" cy="28%"><stop offset="0%" stop-color="#1e2a3e"/><stop offset="100%" stop-color="#07101e"/></radialGradient>
                <radialGradient id="fg2" cx="50%" cy="0%"><stop offset="0%" stop-color="#5ef3ff"/><stop offset="55%" stop-color="#2979ff"/><stop offset="100%" stop-color="transparent"/></radialGradient>
              </defs>
              <rect x="62" y="107" width="36" height="44" rx="8" fill="#0d1a2a" stroke="#3d5a70" stroke-width="1.2"/>
              <rect x="67" y="114" width="9" height="15" rx="3" fill="#004d55" opacity=".7"/>
              <rect x="85" y="114" width="9" height="15" rx="3" fill="#004d55" opacity=".7"/>
              <ellipse cx="71" cy="157" rx="5" ry="12" fill="url(#fg2)" opacity=".85">
                <animate attributeName="ry" values="12;15;9;13;12" dur=".35s" repeatCount="indefinite"/>
              </ellipse>
              <ellipse cx="89" cy="157" rx="5" ry="12" fill="url(#fg2)" opacity=".85">
                <animate attributeName="ry" values="9;13;11;10;9" dur=".28s" repeatCount="indefinite"/>
              </ellipse>
              <ellipse cx="71" cy="154" rx="2.5" ry="6" fill="#5ef3ff" opacity=".7">
                <animate attributeName="ry" values="6;8;4;7;6" dur=".22s" repeatCount="indefinite"/>
              </ellipse>
              <ellipse cx="89" cy="154" rx="2.5" ry="6" fill="#5ef3ff" opacity=".7">
                <animate attributeName="ry" values="5;7;6;4;5" dur=".26s" repeatCount="indefinite"/>
              </ellipse>
              <rect x="42" y="98" width="76" height="68" rx="20" fill="url(#sg2)" stroke="#44607a" stroke-width="1.2"/>
              <rect x="12" y="103" width="32" height="22" rx="11" fill="url(#sg2)" stroke="#44607a" stroke-width="1.2"/>
              <rect x="116" y="103" width="32" height="22" rx="11" fill="url(#sg2)" stroke="#44607a" stroke-width="1.2"/>
              <ellipse cx="17" cy="125" rx="8.5" ry="7" fill="#2c3d4e" stroke="#5ef3ff" stroke-width=".9"/>
              <ellipse cx="143" cy="125" rx="8.5" ry="7" fill="#2c3d4e" stroke="#5ef3ff" stroke-width=".9"/>
              <rect x="49" y="160" width="27" height="44" rx="13" fill="url(#sg2)" stroke="#44607a" stroke-width="1.2"/>
              <rect x="84" y="160" width="27" height="44" rx="13" fill="url(#sg2)" stroke="#44607a" stroke-width="1.2"/>
              <ellipse cx="63" cy="204" rx="18" ry="8" fill="#18222e" stroke="#44607a" stroke-width="1"/>
              <ellipse cx="97" cy="204" rx="18" ry="8" fill="#18222e" stroke="#44607a" stroke-width="1"/>
              <ellipse cx="80" cy="67" rx="44" ry="48" fill="url(#sg2)" stroke="#44607a" stroke-width="1.6"/>
              <ellipse cx="80" cy="70" rx="30" ry="32" fill="url(#vg)" stroke="#2979ff" stroke-width="1.2"/>
              <ellipse cx="70" cy="60" rx="7" ry="11" fill="white" opacity=".1" transform="rotate(-18,70,60)"/>
              <circle cx="76" cy="72" r="1.1" fill="#5ef3ff" opacity=".6"/>
              <circle cx="86" cy="66" r=".8" fill="#5ef3ff" opacity=".5"/>
              <circle cx="70" cy="76" r=".7" fill="white" opacity=".5"/>
              <path d="M39 60 Q80 44 121 60" stroke="#5ef3ff" stroke-width="1.2" fill="none" opacity=".35"/>
              <rect x="52" y="111" width="17" height="14" rx="3" fill="#081626" stroke="#5ef3ff" stroke-width=".9"/>
              <circle cx="57" cy="116" r="2" fill="#34d399"/>
              <circle cx="63" cy="116" r="2" fill="#ffd37a"/>
              <circle cx="57" cy="122" r="2" fill="#60a5fa"/>
              <circle cx="63" cy="122" r="2" fill="#f472b6"/>
              <circle cx="80" cy="130" r="12" fill="none" stroke="#5ef3ff" stroke-width="1.2" opacity=".55"/>
              <text x="80" y="134.5" text-anchor="middle" fill="#5ef3ff" font-size="7.5" font-family="Orbitron" font-weight="700">SP</text>
              <line x1="80" y1="19" x2="80" y2="8" stroke="#5ef3ff" stroke-width="1.2" opacity=".7"/>
              <circle cx="80" cy="6" r="3" fill="#5ef3ff" opacity=".85">
                <animate attributeName="opacity" values=".85;.25;.85" dur="1.3s" repeatCount="indefinite"/>
              </circle>
            </svg>
          </div>

          <div class="sbc">
            <div class="sbc-card">
              <div class="sbc-l">Trajectory</div>
              <div class="sbc-v">Backend + AI Dev. Real&#8209;world Gen AI missions at Innovexis.</div>
            </div>
            <div class="sbc-card">
              <div class="sbc-l">Status</div>
              <div class="sbc-v">Learning, building, shipping &mdash; miles to go before I sleep.</div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- STATS -->
<section id="stats">
  <div class="w">
    <div class="sg rev">
      <div class="sb"><div class="sn">6+</div><div class="sl">Missions</div></div>
      <div class="sb"><div class="sn">7.5</div><div class="sl">CGPA</div></div>
      <div class="sb"><div class="sn">3rd</div><div class="sl">Year</div></div>
      <div class="sb"><div class="sn">2027</div><div class="sl">Graduation</div></div>
    </div>
  </div>
</section>

<!-- SKILLS -->
<section id="skills">
  <div class="w">
    <div class="sh rev">
      <span class="sh-n">01</span><span class="sh-ic">&#9881;&#65039;</span>
      <span class="sh-t">Tech Arsenal</span><div class="sh-ln"></div>
    </div>
    <div class="sk-g rev">
      <div class="sk-c">
        <div class="sk-l">Languages</div>
        <div class="chips">
          <span class="chip c1">Java</span><span class="chip c1">Python</span>
          <span class="chip c1">JavaScript</span><span class="chip c1">Dart</span><span class="chip c1">SQL</span>
        </div>
      </div>
      <div class="sk-c">
        <div class="sk-l">Frameworks</div>
        <div class="chips">
          <span class="chip c2">Spring Boot</span><span class="chip c2">React</span>
          <span class="chip c2">Flutter</span><span class="chip c2">FastAPI</span><span class="chip c2">Spring AI</span>
        </div>
      </div>
      <div class="sk-c">
        <div class="sk-l">Tools &amp; Libraries</div>
        <div class="chips">
          <span class="chip c3">Docker</span><span class="chip c3">GitHub</span>
          <span class="chip c3">NumPy</span><span class="chip c3">Pandas</span>
          <span class="chip c3">Scikit-learn</span><span class="chip c3">NLTK</span>
        </div>
      </div>
      <div class="sk-c">
        <div class="sk-l">Databases</div>
        <div class="chips">
          <span class="chip c4">MySQL</span><span class="chip c4">PostgreSQL</span>
          <span class="chip c4">Firebase</span><span class="chip c4">Redis</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- MISSIONS -->
<section id="missions">
  <div class="w">
    <div class="sh rev">
      <span class="sh-n">02</span><span class="sh-ic">&#128760;</span>
      <span class="sh-t">Mission Log</span><div class="sh-ln"></div>
    </div>
    <div class="plist rev">

      <div class="pi">
        <span class="pi-n">M-01</span>
        <div>
          <div class="pi-top">
            <div class="pi-nm">MedoraX AI &mdash; Clinical AI Assistant</div>
            <span class="pi-tg ta">Healthcare AI</span>
          </div>
          <p class="pi-d">Multimodal clinical assistant with voice, image, and text. Transcribes symptoms via Whisper-large-v3, analyzes medical images via Llama-4-scout, generates structured diagnostic responses. Multilingual (English, Hindi, Marathi) with GPS hospital finder and real-time AQI monitoring.</p>
          <div class="pi-ft">
            <div class="pi-tech"><span class="tt">Python</span><span class="tt">Gradio</span><span class="tt">Groq API</span><span class="tt">Google Maps API</span></div>
            <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="pi-lk">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="pi">
        <span class="pi-n">M-02</span>
        <div>
          <div class="pi-top">
            <div class="pi-nm">SahayLoan &mdash; Micro-Loan Platform</div>
            <span class="pi-tg tb">FinTech</span>
          </div>
          <p class="pi-d">Full-stack micro-lending platform for loans up to &#8377;1,00,000. Flutter frontend, FastAPI backend, AI credit scoring via Random Forest, digital KYC with Aadhaar &amp; PAN OCR via Tesseract, Stripe EMI integration, Firebase Auth + Firestore multi-role system.</p>
          <div class="pi-ft">
            <div class="pi-tech"><span class="tt">Flutter</span><span class="tt">FastAPI</span><span class="tt">Scikit-learn</span><span class="tt">Firebase</span><span class="tt">Stripe</span></div>
            <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="pi-lk">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="pi">
        <span class="pi-n">M-03</span>
        <div>
          <div class="pi-top">
            <div class="pi-nm">SikshaSetu &mdash; Rural Education Platform</div>
            <span class="pi-tg tc">Full-Stack</span>
          </div>
          <p class="pi-d">Education platform bridging the digital divide for rural communities. Role-based access with Spring Security + JWT/OAuth 2.0, optimized relational schema, responsive React frontend, ZEGOCLOUD real-time video SDK for virtual classrooms.</p>
          <div class="pi-ft">
            <div class="pi-tech"><span class="tt">React</span><span class="tt">Spring Boot</span><span class="tt">Spring Security</span><span class="tt">JWT</span><span class="tt">MySQL</span></div>
            <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="pi-lk">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="pi">
        <span class="pi-n">M-04</span>
        <div>
          <div class="pi-top">
            <div class="pi-nm">AI-Powered E-Commerce Backend</div>
            <span class="pi-tg ta">AI / Full-Stack</span>
          </div>
          <p class="pi-d">Intelligent e-commerce backend with AI-driven product recommendations via Spring AI + vector similarity search with Redis Vector DB. Generative AI chatbot for real-time support, AI-powered image generation pipeline, secured with Spring Security + JWT.</p>
          <div class="pi-ft">
            <div class="pi-tech"><span class="tt">React</span><span class="tt">Spring Boot</span><span class="tt">Spring AI</span><span class="tt">Redis Vector DB</span><span class="tt">Tailwind</span></div>
            <a href="https://github.com/Shravan157" target="_blank" class="pi-lk">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="pi">
        <span class="pi-n">M-05</span>
        <div>
          <div class="pi-top">
            <div class="pi-nm">Zomato Review Sentiment Analysis</div>
            <span class="pi-tg td">ML / NLP</span>
          </div>
          <p class="pi-d">End-to-end NLP pipeline classifying 10,000+ Zomato reviews. Extensive EDA with 15 visualizations, hypothesis testing, TF-IDF vectorization, model comparison across Logistic Regression, Random Forest, and Naive Bayes &mdash; Logistic Regression achieved highest F1 score.</p>
          <div class="pi-ft">
            <div class="pi-tech"><span class="tt">Python</span><span class="tt">Scikit-learn</span><span class="tt">NLTK</span><span class="tt">TF-IDF</span><span class="tt">Pandas</span></div>
            <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="pi-lk">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="pi">
        <span class="pi-n">M-06</span>
        <div>
          <div class="pi-top">
            <div class="pi-nm">PhonePe Insights &mdash; Data Engineering &amp; Dashboard</div>
            <span class="pi-tg tb">Data Engineering</span>
          </div>
          <p class="pi-d">End-to-end ETL and visualization platform for PhonePe transaction data. Automated database setup and data loading scripts, MySQL backend via SQLAlchemy + PyMySQL, interactive Streamlit dashboard with Plotly/Seaborn for transaction analytics, plus Jupyter notebooks for EDA and deeper insights.</p>
          <div class="pi-ft">
            <div class="pi-tech"><span class="tt">Python</span><span class="tt">Streamlit</span><span class="tt">MySQL</span><span class="tt">SQLAlchemy</span><span class="tt">Plotly</span><span class="tt">Pandas</span></div>
            <a href="https://github.com/Shravan157/phonepe-insights" target="_blank" class="pi-lk">
              GitHub <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- EXPERIENCE -->
<section id="log">
  <div class="w">
    <div class="sh rev">
      <span class="sh-n">03</span><span class="sh-ic">&#128225;</span>
      <span class="sh-t">Flight Record</span><div class="sh-ln"></div>
    </div>
    <div class="eg rev">
      <div class="ec">
        <div class="ep">APR 2026 &mdash; PRESENT &middot; REMOTE</div>
        <div class="er">Data Science with Gen AI Intern</div>
        <div class="eo">Innovexis</div>
        <ul class="el">
          <li>Selected for Innovexis's competitive Data Science with Gen AI program</li>
          <li>Real-world projects integrating LLMs and generative AI techniques</li>
          <li>Python, NumPy, Pandas, Scikit-learn for data analysis and model building</li>
          <li>Hands-on exposure to production-level Gen AI workflows</li>
        </ul>
        <div class="epill pill-g"><div class="ld"></div>Currently Active</div>
      </div>
      <div class="ec">
        <div class="ep">JUN 2023 &mdash; MAY 2027 (EXPECTED)</div>
        <div class="er">B.Tech, Computer Science (AI &amp; ML)</div>
        <div class="eo">ViMEET &middot; University of Mumbai</div>
        <ul class="el">
          <li>Specializing in Artificial Intelligence &amp; Machine Learning</li>
          <li>Coursework: DSA, Machine Learning, Cloud Computing, Microservices, System Design</li>
          <li>Building production projects alongside coursework</li>
        </ul>
        <div class="epill pill-y">CGPA 7.5 / 10.0</div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section id="contact">
  <div class="w">
    <div class="sh rev">
      <span class="sh-n">04</span><span class="sh-ic">&#128251;</span>
      <span class="sh-t">Establish Contact</span><div class="sh-ln"></div>
    </div>
    <div class="cg rev">
      <div>
        <h2 class="ch">Ready to<br><em>Launch?</em></h2>
        <p class="csub">Open to internships, collaborations, and deep-space conversations about backend systems, AI, and engineering. Transmission line is open.</p>
        <div style="display:flex;gap:.75rem;flex-wrap:wrap;">
          <a href="mailto:shravanparthe@gmail.com" class="ba ba-primary">&#128225; Send Transmission</a>
          <a href=\"""" + RESUME_URL + """\" target="_blank" download="Shravan_Parthe_Resume.pdf" class="ba ba-resume">&#128196; Download Resume</a>
        </div>
      </div>
      <div class="cc-grid">
        <div class="cc">
          <div class="cc-l">Email</div>
          <div class="cc-v"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div>
        </div>
        <div class="cc">
          <div class="cc-l">Phone</div>
          <div class="cc-v">7385813010</div>
        </div>
        <div class="cc">
          <div class="cc-l">LinkedIn</div>
          <div class="cc-v"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div>
        </div>
        <div class="cc">
          <div class="cc-l">GitHub</div>
          <div class="cc-v"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div>
        </div>
        <div class="cc wide">
          <div class="cc-l">Base of Operations</div>
          <div class="cc-v">Mumbai, India &middot; Earth &middot; Solar System &middot; Milky Way Galaxy</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- QUOTE -->
<div class="w">
  <div class="qw rev">
    <span class="qm">&ldquo;</span>
    <p class="qt">
      AIML aur Fullstack ke bich me
      chutiya banake choda hai bhai..
    </p>
    
  </div>
</div>

<!-- FOOTER -->
<footer id="foot">
  <div class="fi">
    <div class="fl">Built by <a href="https://github.com/Shravan157">Shravan Parthe</a> &middot; 2026 &middot; Earth</div>
    <div class="fls">
      <a href="https://github.com/Shravan157" target="_blank">GitHub</a>
      <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn</a>
      <a href="mailto:shravanparthe@gmail.com">Email</a>
    </div>
  </div>
</footer>

</div>

<script>
(function() {
  /* STARFIELD */
  var canvas = document.getElementById('c');
  var ctx = canvas.getContext('2d');
  function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
  resize();
  window.addEventListener('resize', resize);

  var COLS = ['#ffffff','#ccd6f6','#5ef3ff','#ffd37a','#c4b5fd','#93c5fd','#6ee7b7'];
  var stars = [];
  for (var i = 0; i < 300; i++) {
    stars.push({
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      r: Math.random() * 1.6 + 0.2,
      a: Math.random(),
      spd: Math.random() * 0.007 + 0.002,
      ph: Math.random() * Math.PI * 2,
      col: COLS[Math.floor(Math.random() * COLS.length)]
    });
  }

  var shooters = [];
  function addShooter() {
    if (shooters.length < 5) {
      var ang = Math.PI / 4 + (Math.random() - 0.5) * 0.4;
      shooters.push({ x: Math.random() * canvas.width * 0.7, y: Math.random() * canvas.height * 0.5, len: Math.random() * 140 + 60, spd: Math.random() * 10 + 6, a: 1, ang: ang });
    }
  }
  setInterval(addShooter, 3000);

  var DCOLS = ['#7c4dff','#2979ff','#5ef3ff','#f472b6'];
  var dust = [];
  for (var d = 0; d < 55; d++) {
    dust.push({ x: Math.random() * window.innerWidth, y: Math.random() * window.innerHeight, r: Math.random() * 2.5 + 0.8, a: Math.random() * 0.12, vx: (Math.random() - 0.5) * 0.18, vy: (Math.random() - 0.5) * 0.18, col: DCOLS[Math.floor(Math.random() * DCOLS.length)] });
  }

  function frame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (var d = 0; d < dust.length; d++) {
      var p = dust[d];
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x = canvas.width; if (p.x > canvas.width) p.x = 0;
      if (p.y < 0) p.y = canvas.height; if (p.y > canvas.height) p.y = 0;
      ctx.save(); ctx.globalAlpha = p.a; ctx.fillStyle = p.col;
      ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill(); ctx.restore();
    }
    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      s.ph += s.spd; s.a = 0.28 + 0.72 * (Math.sin(s.ph) * 0.5 + 0.5);
      ctx.save(); ctx.globalAlpha = s.a; ctx.fillStyle = s.col;
      ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2); ctx.fill();
      if (s.r > 1.3 && s.a > 0.78) {
        ctx.globalAlpha = s.a * 0.3; ctx.strokeStyle = s.col; ctx.lineWidth = 0.5;
        ctx.beginPath(); ctx.moveTo(s.x - s.r * 3.5, s.y); ctx.lineTo(s.x + s.r * 3.5, s.y);
        ctx.moveTo(s.x, s.y - s.r * 3.5); ctx.lineTo(s.x, s.y + s.r * 3.5); ctx.stroke();
      }
      ctx.restore();
    }
    for (var j = shooters.length - 1; j >= 0; j--) {
      var sh = shooters[j];
      var dx = Math.cos(sh.ang) * sh.len; var dy = Math.sin(sh.ang) * sh.len;
      var g = ctx.createLinearGradient(sh.x, sh.y, sh.x - dx, sh.y - dy);
      g.addColorStop(0, 'rgba(94,243,255,' + sh.a + ')');
      g.addColorStop(0.3, 'rgba(96,165,250,' + (sh.a * 0.55) + ')');
      g.addColorStop(1, 'transparent');
      ctx.save(); ctx.strokeStyle = g; ctx.lineWidth = 1.8; ctx.shadowBlur = 8; ctx.shadowColor = '#5ef3ff';
      ctx.beginPath(); ctx.moveTo(sh.x, sh.y); ctx.lineTo(sh.x - dx, sh.y - dy); ctx.stroke(); ctx.restore();
      sh.x += sh.spd * Math.cos(sh.ang); sh.y += sh.spd * Math.sin(sh.ang); sh.a -= 0.011;
      if (sh.a <= 0 || sh.x > canvas.width || sh.y > canvas.height) shooters.splice(j, 1);
    }
    requestAnimationFrame(frame);
  }
  frame();

  /* SCROLL REVEAL */
  var obs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) { if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); } });
  }, { threshold: 0.07 });
  document.querySelectorAll('.rev').forEach(function(el) { obs.observe(el); });

  /* NAV SCROLL */
  var nav = document.getElementById('nav');
  window.addEventListener('scroll', function() {
    if (window.scrollY > 60) nav.classList.add('scrolled'); else nav.classList.remove('scrolled');
  });

  /* SMOOTH SCROLL */
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var t = document.querySelector(a.getAttribute('href'));
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
    });
  });
})();
</script>
</body>
</html>"""

components.html(HTML, height=5400, scrolling=True)
