import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Shravan Parthe — Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, header, footer { visibility: hidden; }
.stApp { background: #050816; margin: 0; padding: 0; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Shravan Parthe</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#050816;
  --panel:rgba(12,18,40,0.72);
  --border:rgba(126,162,255,0.14);
  --text:#eef4ff;
  --muted:#98a7d0;
  --soft:#6f7da8;
  --cyan:#6ee7ff;
  --blue:#7aa2ff;
  --violet:#a78bfa;
  --green:#66f2b0;
  --gold:#ffd37a;
  --sans:'Inter',sans-serif;
  --display:'Orbitron',sans-serif;
  --mono:'JetBrains Mono',monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:var(--sans);
  color:var(--text);
  background:
    radial-gradient(circle at 20% 20%,rgba(122,162,255,0.18),transparent 28%),
    radial-gradient(circle at 80% 30%,rgba(167,139,250,0.16),transparent 30%),
    radial-gradient(circle at 50% 75%,rgba(110,231,255,0.12),transparent 35%),
    linear-gradient(180deg,#02040a 0%,#060b1a 40%,#050816 100%);
  overflow-x:hidden;
  min-height:100vh;
}
body::before{
  content:"";position:fixed;inset:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.035'/%3E%3C/svg%3E");
  opacity:0.6;pointer-events:none;z-index:9999;
}
.stars{position:fixed;inset:0;pointer-events:none;z-index:0;}
.stars-layer-1{
  position:absolute;inset:0;
  background-image:
    radial-gradient(1.8px 1.8px at 40px 60px,rgba(255,255,255,0.95),transparent),
    radial-gradient(1.2px 1.2px at 140px 120px,rgba(255,255,255,0.8),transparent),
    radial-gradient(1.5px 1.5px at 260px 40px,rgba(110,231,255,0.85),transparent),
    radial-gradient(1px 1px at 380px 180px,rgba(255,255,255,0.7),transparent),
    radial-gradient(1.6px 1.6px at 520px 100px,rgba(167,139,250,0.8),transparent),
    radial-gradient(1.3px 1.3px at 680px 220px,rgba(255,255,255,0.75),transparent),
    radial-gradient(1.7px 1.7px at 820px 80px,rgba(110,231,255,0.7),transparent),
    radial-gradient(1.4px 1.4px at 1100px 50px,rgba(122,162,255,0.85),transparent),
    radial-gradient(1.6px 1.6px at 1250px 200px,rgba(255,255,255,0.7),transparent);
  background-size:1300px 800px;
  animation:drift1 100s linear infinite;opacity:0.7;
}
.stars-layer-2{
  position:absolute;inset:0;
  background-image:
    radial-gradient(1px 1px at 80px 100px,rgba(255,255,255,0.6),transparent),
    radial-gradient(1.3px 1.3px at 220px 40px,rgba(110,231,255,0.5),transparent),
    radial-gradient(0.8px 0.8px at 360px 160px,rgba(167,139,250,0.55),transparent),
    radial-gradient(1.4px 1.4px at 620px 240px,rgba(122,162,255,0.6),transparent),
    radial-gradient(1.2px 1.2px at 900px 60px,rgba(110,231,255,0.5),transparent);
  background-size:1200px 700px;
  animation:drift2 140s linear infinite reverse;opacity:0.5;
}
.stars-layer-3{
  position:absolute;inset:0;
  background-image:
    radial-gradient(2.2px 2.2px at 150px 80px,rgba(255,255,255,0.9),transparent),
    radial-gradient(1.8px 1.8px at 350px 200px,rgba(110,231,255,0.8),transparent),
    radial-gradient(2px 2px at 550px 60px,rgba(167,139,250,0.75),transparent),
    radial-gradient(1.9px 1.9px at 950px 90px,rgba(255,255,255,0.8),transparent);
  background-size:1300px 800px;
  animation:drift3 180s linear infinite;opacity:0.4;
}
@keyframes drift1{from{transform:translateY(0)}to{transform:translateY(-80px)}}
@keyframes drift2{from{transform:translateY(0)}to{transform:translateY(-60px)}}
@keyframes drift3{from{transform:translateY(0)}to{transform:translateY(-40px)}}
.horizon{
  position:fixed;bottom:0;left:0;right:0;height:40vh;
  background:radial-gradient(ellipse at 50% 100%,rgba(122,162,255,0.08) 0%,transparent 70%);
  pointer-events:none;z-index:0;
}
a{color:inherit;text-decoration:none}
.wrap{width:min(1180px,calc(100% - 32px));margin:0 auto;position:relative;z-index:2;}

/* Nav */
nav{
  position:sticky;top:0;left:0;right:0;z-index:20;
  backdrop-filter:blur(20px) saturate(1.2);
  background:rgba(3,8,20,0.6);
  border-bottom:1px solid rgba(126,162,255,0.08);
  transition:all 0.3s ease;
}
.nav-inner{
  width:min(1180px,calc(100% - 32px));margin:0 auto;
  min-height:74px;display:flex;align-items:center;justify-content:space-between;
}
.nav-logo{font-family:var(--display);letter-spacing:1.5px;font-weight:800;color:var(--text);font-size:1.1rem;position:relative;}
.nav-logo::after{content:"";position:absolute;bottom:-4px;left:0;width:0;height:2px;background:linear-gradient(90deg,var(--cyan),var(--blue));transition:width 0.4s ease;}
.nav-logo:hover::after{width:100%}
.nav-logo span{color:var(--cyan)}
.nav-links{display:flex;align-items:center;gap:1.4rem;flex-wrap:wrap;}
.nav-links a{font-size:0.78rem;text-transform:uppercase;letter-spacing:1.8px;color:var(--muted);position:relative;padding:0.2rem 0;transition:color 0.3s ease;}
.nav-links a::after{content:"";position:absolute;bottom:-2px;left:0;width:0;height:1.5px;background:var(--cyan);transition:width 0.3s ease;}
.nav-links a:hover{color:var(--cyan)}
.nav-links a:hover::after{width:100%}
.badge-live{
  display:inline-flex;align-items:center;gap:.55rem;
  border:1px solid rgba(102,242,176,0.2);color:var(--green);
  background:rgba(102,242,176,0.06);padding:.45rem 1rem;border-radius:999px;
  font-family:var(--mono);font-size:.72rem;backdrop-filter:blur(10px);transition:all 0.3s ease;
}
.badge-live:hover{background:rgba(102,242,176,0.12);border-color:rgba(102,242,176,0.35);box-shadow:0 0 20px rgba(102,242,176,0.15);}
.dot{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 12px var(--green);animation:pulse 2.5s ease-in-out infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.35;transform:scale(.75)}}

/* Hero */
.hero{min-height:100vh;display:flex;align-items:center;padding:7rem 0 4rem;position:relative;}
.hero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:3.5rem;align-items:center;}
.hero-entrance .kicker{opacity:0;animation:fadeSlideUp 0.8s ease forwards 0.2s;}
.hero-entrance h1{opacity:0;animation:fadeSlideUp 0.9s ease forwards 0.4s;}
.hero-entrance .hero-sub{opacity:0;animation:fadeSlideUp 0.9s ease forwards 0.6s;}
.hero-entrance .hero-actions{opacity:0;animation:fadeSlideUp 0.9s ease forwards 0.8s;}
.hero-panel-entrance{opacity:0;animation:fadeSlideUp 1s ease forwards 0.5s;}
@keyframes fadeSlideUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
.kicker{display:inline-flex;align-items:center;gap:.7rem;margin-bottom:1.4rem;color:var(--cyan);font-family:var(--mono);font-size:.75rem;letter-spacing:2.5px;text-transform:uppercase;}
.kicker::before{content:"";width:48px;height:1.5px;background:linear-gradient(90deg,var(--cyan),transparent);}
.hero h1{font-family:var(--display);font-size:clamp(2.8rem,7.5vw,6rem);line-height:1.05;letter-spacing:-1.5px;text-transform:uppercase;margin-bottom:1.4rem;font-weight:800;}
.hero h1 .glow{color:var(--cyan);text-shadow:0 0 24px rgba(110,231,255,0.35),0 0 60px rgba(110,231,255,0.12);}
.hero-sub{max-width:680px;color:var(--muted);font-size:1.05rem;line-height:1.9;margin-bottom:2.2rem;font-weight:400;}
.hero-sub strong{color:var(--text);font-weight:600;}
.hero-actions{display:flex;gap:1rem;flex-wrap:wrap;}
.btn{display:inline-flex;align-items:center;gap:.65rem;padding:1rem 1.5rem;border-radius:14px;font-weight:600;font-size:.82rem;text-transform:uppercase;letter-spacing:1.2px;transition:all 0.35s cubic-bezier(0.4,0,0.2,1);cursor:pointer;border:none;font-family:var(--sans);}
.btn-primary{background:linear-gradient(135deg,var(--cyan),var(--blue));color:#04111b;box-shadow:0 4px 24px rgba(110,231,255,0.2);position:relative;overflow:hidden;}
.btn-primary::before{content:"";position:absolute;inset:0;background:linear-gradient(135deg,transparent,rgba(255,255,255,0.25),transparent);transform:translateX(-100%);transition:transform 0.6s ease;}
.btn-primary:hover{transform:translateY(-3px) scale(1.02);box-shadow:0 8px 40px rgba(110,231,255,0.3);}
.btn-primary:hover::before{transform:translateX(100%);}
.btn-secondary{border:1px solid var(--border);background:rgba(255,255,255,0.03);color:var(--text);backdrop-filter:blur(10px);}
.btn-secondary:hover{border-color:rgba(110,231,255,0.4);color:var(--cyan);transform:translateY(-3px);background:rgba(110,231,255,0.05);box-shadow:0 4px 24px rgba(110,231,255,0.1);}
.btn-resume{border:1px solid rgba(255,211,122,0.3);background:rgba(255,211,122,0.06);color:var(--gold);backdrop-filter:blur(10px);}
.btn-resume:hover{border-color:rgba(255,211,122,0.6);transform:translateY(-3px);background:rgba(255,211,122,0.12);box-shadow:0 4px 24px rgba(255,211,122,0.15);}

/* Hero Panel */
.hero-panel{position:relative;min-height:540px;border:1px solid var(--border);border-radius:32px;background:linear-gradient(180deg,rgba(14,20,48,0.9),rgba(8,14,32,0.75));overflow:hidden;box-shadow:0 20px 80px rgba(0,0,0,0.4),inset 0 1px 0 rgba(255,255,255,0.05);}
.hero-panel::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 70% 22%,rgba(110,231,255,0.18),transparent 20%),radial-gradient(circle at 28% 70%,rgba(167,139,250,0.18),transparent 20%);}
.orbit{position:absolute;border:1px dashed rgba(255,255,255,0.1);border-radius:50%;animation:orbitRotate 60s linear infinite;}
.o1{width:440px;height:440px;top:50px;left:50%;transform:translateX(-50%);}
.o2{width:300px;height:300px;top:120px;left:50%;transform:translateX(-50%);animation-direction:reverse;animation-duration:45s;}
@keyframes orbitRotate{from{transform:translateX(-50%) rotate(0deg)}to{transform:translateX(-50%) rotate(360deg)}}
.planet{position:absolute;width:92px;height:92px;border-radius:50%;top:185px;left:50%;transform:translateX(-50%);background:radial-gradient(circle at 30% 30%,#e0ecff,#7aa2ff 40%,#2d3f8a 80%,#1a2450 100%);box-shadow:0 0 50px rgba(122,162,255,0.35),0 0 100px rgba(122,162,255,0.15),inset -8px -8px 20px rgba(0,0,0,0.3);animation:planetPulse 4s ease-in-out infinite;}
@keyframes planetPulse{0%,100%{box-shadow:0 0 50px rgba(122,162,255,0.35),0 0 100px rgba(122,162,255,0.15),inset -8px -8px 20px rgba(0,0,0,0.3)}50%{box-shadow:0 0 60px rgba(122,162,255,0.45),0 0 120px rgba(122,162,255,0.2),inset -8px -8px 20px rgba(0,0,0,0.3)}}
.rocket{position:absolute;right:80px;top:100px;font-size:2.8rem;transform:rotate(18deg);animation:floatRocket 5s ease-in-out infinite;filter:drop-shadow(0 0 20px rgba(255,211,122,.2));z-index:5;}
.astronaut{position:absolute;left:55px;bottom:110px;font-size:3.2rem;animation:floatAstro 6s ease-in-out infinite;filter:drop-shadow(0 0 20px rgba(255,255,255,.18));z-index:5;}
.starship-note{position:absolute;left:28px;right:28px;bottom:24px;display:grid;grid-template-columns:1fr 1fr;gap:14px;z-index:5;}
.mini-card{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:18px;padding:1.1rem;backdrop-filter:blur(12px);transition:all 0.3s ease;}
.mini-card:hover{background:rgba(255,255,255,0.07);border-color:rgba(255,255,255,0.15);transform:translateY(-2px);}
.mini-label{font-family:var(--mono);color:var(--soft);font-size:.68rem;text-transform:uppercase;letter-spacing:1.4px;margin-bottom:.5rem;}
.mini-value{color:var(--text);font-size:.92rem;line-height:1.6;font-weight:500;}
@keyframes floatRocket{0%,100%{transform:translateY(0) rotate(18deg)}50%{transform:translateY(-16px) rotate(14deg)}}
@keyframes floatAstro{0%,100%{transform:translateY(0) rotate(-8deg)}50%{transform:translateY(-14px) rotate(5deg)}}

/* Sections */
.section{padding:2rem 0 5rem;}
.section-label{display:flex;align-items:center;gap:1rem;margin-bottom:2.2rem;font-family:var(--mono);color:var(--soft);font-size:.74rem;text-transform:uppercase;letter-spacing:2.5px;}
.section-label::after{content:"";height:1px;flex:1;background:linear-gradient(90deg,rgba(110,231,255,.25),rgba(255,255,255,0.04));}
.section-label span{color:var(--cyan);font-weight:500;}

/* Stats */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem;}
.stat{border:1px solid var(--border);background:var(--panel);border-radius:24px;padding:1.8rem 1.5rem;backdrop-filter:blur(16px);position:relative;overflow:hidden;transition:all 0.4s cubic-bezier(0.4,0,0.2,1);}
.stat::before{content:"";position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--cyan),var(--blue),var(--violet));opacity:0;transition:opacity 0.4s ease;}
.stat:hover{transform:translateY(-6px);border-color:rgba(126,162,255,0.3);box-shadow:0 20px 60px rgba(0,0,0,0.3);}
.stat:hover::before{opacity:1;}
.stat h3{font-family:var(--display);font-size:2.4rem;margin-bottom:.5rem;font-weight:700;background:linear-gradient(135deg,var(--text),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.stat p{color:var(--muted);font-family:var(--mono);font-size:.74rem;text-transform:uppercase;letter-spacing:1.2px;}

/* Grid & Cards */
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:1.2rem;}
.card{border:1px solid var(--border);background:var(--panel);border-radius:24px;padding:1.6rem;backdrop-filter:blur(16px);position:relative;overflow:hidden;transition:all 0.4s cubic-bezier(0.4,0,0.2,1);}
.card::before{content:"";position:absolute;top:0;left:0;width:100%;height:2px;background:linear-gradient(90deg,var(--cyan),transparent);opacity:0;transition:opacity 0.4s ease;}
.card:hover{transform:translateY(-4px);border-color:rgba(126,162,255,0.25);box-shadow:0 16px 50px rgba(0,0,0,0.25);}
.card:hover::before{opacity:0.6;}
.card h3{font-family:var(--display);color:var(--text);font-size:1.1rem;margin-bottom:1.2rem;letter-spacing:.5px;font-weight:700;}
.chips{display:flex;flex-wrap:wrap;gap:.6rem;}
.chip{padding:.5rem .85rem;border-radius:999px;border:1px solid rgba(255,255,255,0.08);background:rgba(255,255,255,0.04);color:var(--muted);font-family:var(--mono);font-size:.76rem;transition:all 0.3s ease;cursor:default;}
.chip:hover{transform:translateY(-2px);background:rgba(255,255,255,0.08);}
.chip.c1{color:var(--cyan);border-color:rgba(110,231,255,.2)}
.chip.c1:hover{background:rgba(110,231,255,.1);}
.chip.c2{color:var(--violet);border-color:rgba(167,139,250,.2)}
.chip.c2:hover{background:rgba(167,139,250,.1);}
.chip.c3{color:var(--gold);border-color:rgba(255,211,122,.2)}
.chip.c3:hover{background:rgba(255,211,122,.1);}
.chip.c4{color:var(--green);border-color:rgba(102,242,176,.2)}
.chip.c4:hover{background:rgba(102,242,176,.1);}

/* Projects */
.projects{display:flex;flex-direction:column;gap:1.2rem;}
.project{border:1px solid var(--border);background:linear-gradient(180deg,rgba(14,20,42,0.9),rgba(10,14,32,0.78));border-radius:28px;padding:1.8rem;transition:all 0.4s cubic-bezier(0.4,0,0.2,1);position:relative;overflow:hidden;}
.project::before{content:"";position:absolute;top:0;left:0;width:3px;height:100%;background:linear-gradient(180deg,var(--cyan),var(--blue),transparent);opacity:0;transition:opacity 0.4s ease;}
.project:hover{transform:translateY(-6px);border-color:rgba(110,231,255,.3);box-shadow:0 20px 60px rgba(0,0,0,.25);}
.project:hover::before{opacity:1;}
.proj-top{display:flex;justify-content:space-between;align-items:flex-start;gap:1rem;margin-bottom:1rem;}
.project h3{font-size:1.25rem;color:var(--text);margin-bottom:.3rem;font-weight:600;}
.proj-tag{white-space:nowrap;padding:.4rem .85rem;border-radius:999px;font-family:var(--mono);font-size:.7rem;text-transform:uppercase;letter-spacing:1px;border:1px solid rgba(255,255,255,.1);backdrop-filter:blur(10px);}
.t1{color:var(--violet);background:rgba(167,139,250,.1)}
.t2{color:var(--cyan);background:rgba(110,231,255,.1)}
.t3{color:var(--green);background:rgba(102,242,176,.1)}
.t4{color:var(--gold);background:rgba(255,211,122,.1)}
.project p{color:var(--muted);line-height:1.85;font-size:.96rem;margin-bottom:1.2rem;}
.proj-bottom{display:flex;justify-content:space-between;gap:1rem;align-items:center;flex-wrap:wrap;}
.techs{display:flex;flex-wrap:wrap;gap:.5rem;}
.tech{border:1px solid rgba(255,255,255,.1);background:rgba(255,255,255,.04);color:var(--soft);border-radius:999px;padding:.4rem .75rem;font-family:var(--mono);font-size:.73rem;transition:all 0.3s ease;}
.tech:hover{background:rgba(255,255,255,.08);color:var(--text);transform:translateY(-1px);}
.proj-link{color:var(--cyan);font-weight:600;font-size:.9rem;position:relative;padding-right:1.2rem;transition:all 0.3s ease;}
.proj-link::after{content:"&#8594;";position:absolute;right:0;transition:transform 0.3s ease;}
.proj-link:hover{color:var(--text);}
.proj-link:hover::after{transform:translateX(4px);}

/* Experience */
.exp-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;}
.exp-card{border:1px solid var(--border);background:var(--panel);border-radius:28px;padding:1.8rem;position:relative;overflow:hidden;transition:all 0.4s cubic-bezier(0.4,0,0.2,1);}
.exp-card::before{content:"";position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--violet),var(--cyan));opacity:0;transition:opacity 0.4s ease;}
.exp-card:hover{transform:translateY(-4px);border-color:rgba(126,162,255,0.25);box-shadow:0 16px 50px rgba(0,0,0,0.2);}
.exp-card:hover::before{opacity:0.7;}
.exp-period{color:var(--soft);font-family:var(--mono);font-size:.74rem;margin-bottom:.8rem;text-transform:uppercase;letter-spacing:1px;}
.exp-role{font-family:var(--display);font-size:1.15rem;color:var(--text);margin-bottom:.4rem;font-weight:700;}
.exp-org{color:var(--cyan);font-family:var(--mono);margin-bottom:1.2rem;font-size:.82rem;font-weight:500;}
.exp-card ul{list-style:none;}
.exp-card li{color:var(--muted);line-height:1.85;padding-left:1.2rem;position:relative;margin:.35rem 0;font-size:.94rem;}
.exp-card li::before{content:"&#10022;";position:absolute;left:0;color:var(--cyan);font-size:.8rem;}
.pill{display:inline-block;margin-top:1.2rem;padding:.5rem 1rem;border-radius:999px;font-family:var(--mono);font-size:.74rem;border:1px solid rgba(102,242,176,.2);background:rgba(102,242,176,.08);color:var(--green);}

/* Contact */
.contact{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;}
.contact-main{border:1px solid var(--border);background:var(--panel);border-radius:32px;padding:2.5rem;position:relative;overflow:hidden;}
.contact-main::before{content:"";position:absolute;top:-50%;right:-50%;width:100%;height:100%;background:radial-gradient(circle,rgba(110,231,255,0.08),transparent 70%);pointer-events:none;}
.contact-main h2{font-family:var(--display);font-size:clamp(2rem,4vw,3.4rem);line-height:1.15;margin-bottom:1.2rem;font-weight:800;}
.contact-main h2 span{color:var(--cyan);}
.contact-main p{color:var(--muted);line-height:1.9;max-width:560px;margin-bottom:2rem;font-size:1.05rem;}
.contact-btns{display:flex;gap:1rem;flex-wrap:wrap;}
.contact-cards{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;}
.contact-card{border:1px solid var(--border);background:var(--panel);border-radius:24px;padding:1.4rem;transition:all 0.4s cubic-bezier(0.4,0,0.2,1);}
.contact-card:hover{transform:translateY(-4px);border-color:rgba(126,162,255,0.25);box-shadow:0 12px 40px rgba(0,0,0,0.2);}
.clabel{color:var(--soft);font-family:var(--mono);text-transform:uppercase;letter-spacing:1.6px;font-size:.7rem;margin-bottom:.5rem;}
.cvalue{color:var(--text);font-size:.98rem;line-height:1.7;font-weight:500;}
.cvalue a{color:var(--cyan);transition:all 0.3s ease;}
.cvalue a:hover{color:var(--text);}

/* Quote */
.quote{margin:2rem 0 4rem;border:1px solid var(--border);border-radius:32px;background:linear-gradient(180deg,rgba(12,18,40,0.9),rgba(8,14,32,0.82));padding:3.5rem 2rem;text-align:center;position:relative;overflow:hidden;}
.quote::before{content:"&#10022;";position:absolute;top:18px;left:28px;color:rgba(110,231,255,.25);font-size:2.2rem;animation:twinkle 4s ease-in-out infinite;}
.quote::after{content:"&#9732;";position:absolute;bottom:22px;right:28px;color:rgba(167,139,250,.2);font-size:2.2rem;animation:twinkle 4s ease-in-out infinite 2s;}
@keyframes twinkle{0%,100%{opacity:0.3;transform:scale(1)}50%{opacity:0.8;transform:scale(1.1)}}
.quote p{font-size:clamp(1.1rem,2.2vw,1.45rem);line-height:2.1;color:#d0d8f5;max-width:780px;margin:0 auto 1.2rem;font-weight:300;letter-spacing:0.3px;}
.quote strong{color:var(--cyan);font-weight:600;}
.quote .src{font-family:var(--mono);color:var(--soft);font-size:.74rem;text-transform:uppercase;letter-spacing:2.5px;}

/* Footer */
footer{padding:1.6rem 0 3rem;border-top:1px solid rgba(255,255,255,.06);}
.foot{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;align-items:center;}
.foot div,.foot a{color:var(--soft);font-family:var(--mono);font-size:.76rem;letter-spacing:0.5px;}
.foot a{position:relative;padding:0.2rem 0;transition:color 0.3s ease;}
.foot a::after{content:"";position:absolute;bottom:0;left:0;width:0;height:1px;background:var(--cyan);transition:width 0.3s ease;}
.foot a:hover{color:var(--cyan)}
.foot a:hover::after{width:100%}

/* Scroll Reveal */
.reveal{opacity:0;transform:translateY(30px);transition:all 1s cubic-bezier(0.4,0,0.2,1);}
.reveal.in{opacity:1;transform:translateY(0);}

@media(max-width:980px){
  .hero-grid,.contact,.exp-grid{grid-template-columns:1fr}
  .stats{grid-template-columns:repeat(2,1fr)}
  .grid-2{grid-template-columns:1fr}
  .hero-panel{min-height:480px}
  .hero{min-height:auto;padding:6rem 0 3rem}
}
@media(max-width:680px){
  .nav-links a{display:none}
  .stats{grid-template-columns:1fr}
  .contact-cards{grid-template-columns:1fr}
  .hero h1{font-size:2.4rem}
  .starship-note{grid-template-columns:1fr}
  .rocket{right:30px;font-size:2.2rem}
  .astronaut{left:20px;font-size:2.6rem}
  .hero-actions{justify-content:center}
  .hero-grid{gap:2rem}
}
</style>
</head>
<body>

<div class="stars">
  <div class="stars-layer-1"></div>
  <div class="stars-layer-2"></div>
  <div class="stars-layer-3"></div>
</div>
<div class="horizon"></div>

<nav id="navbar">
  <div class="nav-inner">
    <a href="#home" class="nav-logo">SHRAVAN<span>.EXE</span></a>
    <div class="nav-links">
      <a href="#skills">Arsenal</a>
      <a href="#projects">Missions</a>
      <a href="#experience">Flight Log</a>
      <a href="#contact">Transmission</a>
      <a href="https://github.com/Shravan157/portfolio-website/blob/master/resume_shravan2.pdf" target="_blank" class="badge-live">
        <span class="dot"></span> Resume
      </a>
    </div>
  </div>
</nav>

<section class="hero" id="home">
  <div class="wrap">
    <div class="hero-grid">
      <div class="hero-entrance">
        <div class="kicker">Mission Log &middot; 2026</div>
        <h1>Exploring the <span class="glow">unknown</span><br>through backend &amp; AI.</h1>
        <p class="hero-sub">
          I'm <strong>Shravan Parthe</strong>, a 3rd year B.Tech CSE (AI &amp; ML) student building production-grade systems with Java, Spring Boot, Python, and modern AI tools. I treat every project like a mission &mdash; launch fast, learn deeply, and keep pushing into new frontiers.
        </p>
        <div class="hero-actions">
          <a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">Start a mission</a>
          <a href="https://github.com/Shravan157/portfolio-website/blob/master/resume_shravan2.pdf" target="_blank" class="btn btn-resume">View Resume &#8599;</a>
          <a href="https://github.com/Shravan157" target="_blank" class="btn btn-secondary">GitHub</a>
          <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank" class="btn btn-secondary">LinkedIn</a>
        </div>
      </div>

      <div class="hero-panel hero-panel-entrance">
        <div class="orbit o1"></div>
        <div class="orbit o2"></div>
        <div class="planet"></div>
        <div class="rocket">&#128640;</div>
        <div class="astronaut">&#128104;&#8205;&#128640;</div>
        <div class="starship-note">
          <div class="mini-card">
            <div class="mini-label">Current trajectory</div>
            <div class="mini-value">Backend Engineer / AI Developer building real-world systems and exploring GenAI integration.</div>
          </div>
          <div class="mini-card">
            <div class="mini-label">Mission status</div>
            <div class="mini-value">Learning, building, shipping &mdash; with miles to go before I sleep.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-label reveal"><span>01</span> Mission Stats</div>
    <div class="stats">
      <div class="stat reveal"><h3>5+</h3><p>Projects launched</p></div>
      <div class="stat reveal"><h3>7.5</h3><p>CGPA</p></div>
      <div class="stat reveal"><h3>3rd</h3><p>Year B.Tech</p></div>
      <div class="stat reveal"><h3>2027</h3><p>Expected graduation</p></div>
    </div>
  </div>
</section>

<section class="section" id="skills">
  <div class="wrap">
    <div class="section-label reveal"><span>02</span> Tech Arsenal</div>
    <div class="grid-2">
      <div class="card reveal">
        <h3>Languages</h3>
        <div class="chips">
          <span class="chip c1">Java</span><span class="chip c1">Python</span>
          <span class="chip c1">JavaScript</span><span class="chip c1">Dart</span><span class="chip c1">SQL</span>
        </div>
      </div>
      <div class="card reveal">
        <h3>Frameworks</h3>
        <div class="chips">
          <span class="chip c2">Spring Boot</span><span class="chip c2">React</span>
          <span class="chip c2">Flutter</span><span class="chip c2">FastAPI</span><span class="chip c2">Spring AI</span>
        </div>
      </div>
      <div class="card reveal">
        <h3>Tools &amp; Libraries</h3>
        <div class="chips">
          <span class="chip c3">Docker</span><span class="chip c3">GitHub</span>
          <span class="chip c3">NumPy</span><span class="chip c3">Pandas</span>
          <span class="chip c3">Scikit-learn</span><span class="chip c3">NLTK</span>
        </div>
      </div>
      <div class="card reveal">
        <h3>Databases</h3>
        <div class="chips">
          <span class="chip c4">MySQL</span><span class="chip c4">PostgreSQL</span>
          <span class="chip c4">Firebase</span><span class="chip c4">Redis</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="projects">
  <div class="wrap">
    <div class="section-label reveal"><span>03</span> Missions</div>
    <div class="projects">

      <div class="project reveal">
        <div class="proj-top">
          <div><h3>MedoraX AI &mdash; Clinical AI Assistant</h3></div>
          <div class="proj-tag t1">Healthcare AI</div>
        </div>
        <p>A multimodal clinical assistant supporting voice, image, and text. It transcribes symptoms, analyzes medical images, generates structured responses, and supports multilingual interaction with location-aware utilities.</p>
        <div class="proj-bottom">
          <div class="techs">
            <span class="tech">Python</span><span class="tech">Gradio</span>
            <span class="tech">Groq API</span><span class="tech">Google Maps API</span>
          </div>
          <a class="proj-link" target="_blank" href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant">View mission</a>
        </div>
      </div>

      <div class="project reveal">
        <div class="proj-top">
          <div><h3>SahayLoan &mdash; Micro-Loan Platform</h3></div>
          <div class="proj-tag t2">FinTech</div>
        </div>
        <p>A full-stack micro-lending platform with AI credit scoring, OCR-based KYC workflows, and a multi-role architecture for modern loan processing.</p>
        <div class="proj-bottom">
          <div class="techs">
            <span class="tech">Flutter</span><span class="tech">FastAPI</span>
            <span class="tech">Scikit-learn</span><span class="tech">Firebase</span><span class="tech">Stripe</span>
          </div>
          <a class="proj-link" target="_blank" href="https://github.com/Shravan157/Sahay-Loan">View mission</a>
        </div>
      </div>

      <div class="project reveal">
        <div class="proj-top">
          <div><h3>SikshaSetu &mdash; Rural Education Platform</h3></div>
          <div class="proj-tag t3">Full-Stack</div>
        </div>
        <p>A scalable education platform focused on access, role-based systems, secure authentication, and real-time digital classroom experiences.</p>
        <div class="proj-bottom">
          <div class="techs">
            <span class="tech">React</span><span class="tech">Spring Boot</span>
            <span class="tech">Spring Security</span><span class="tech">JWT</span><span class="tech">MySQL</span>
          </div>
          <a class="proj-link" target="_blank" href="https://github.com/Shravan157/SikshaSetu_Edu_App">View mission</a>
        </div>
      </div>

      <div class="project reveal">
        <div class="proj-top">
          <div><h3>AI-Powered E-Commerce Backend</h3></div>
          <div class="proj-tag t1">AI / Backend</div>
        </div>
        <p>An intelligent commerce backend with recommendation pipelines, vector search, conversational support, and secure service design.</p>
        <div class="proj-bottom">
          <div class="techs">
            <span class="tech">React</span><span class="tech">Spring Boot</span>
            <span class="tech">Spring AI</span><span class="tech">Redis Vector DB</span><span class="tech">Tailwind</span>
          </div>
          <a class="proj-link" target="_blank" href="https://github.com/Shravan157">View mission</a>
        </div>
      </div>

      <div class="project reveal">
        <div class="proj-top">
          <div><h3>Zomato Review Sentiment Analysis</h3></div>
          <div class="proj-tag t4">ML / NLP</div>
        </div>
        <p>An end-to-end NLP pipeline for review classification with EDA, feature engineering, TF-IDF vectorization, and comparative model evaluation.</p>
        <div class="proj-bottom">
          <div class="techs">
            <span class="tech">Python</span><span class="tech">Scikit-learn</span>
            <span class="tech">NLTK</span><span class="tech">TF-IDF</span><span class="tech">Pandas</span>
          </div>
          <a class="proj-link" target="_blank" href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis">View mission</a>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="section" id="experience">
  <div class="wrap">
    <div class="section-label reveal"><span>04</span> Flight Log</div>
    <div class="exp-grid">
      <div class="exp-card reveal">
        <div class="exp-period">Apr 2026 &mdash; Present &middot; Remote</div>
        <div class="exp-role">Data Science with Gen AI Intern</div>
        <div class="exp-org">Innovexis</div>
        <ul>
          <li>Working on practical projects involving LLMs and generative AI workflows</li>
          <li>Using Python, NumPy, Pandas, and Scikit-learn for applied data work</li>
          <li>Gaining exposure to production-oriented GenAI implementation</li>
        </ul>
        <div class="pill">Currently Active</div>
      </div>
      <div class="exp-card reveal">
        <div class="exp-period">Jun 2023 &mdash; May 2027 (Expected)</div>
        <div class="exp-role">B.Tech, Computer Science Engineering (AI &amp; ML)</div>
        <div class="exp-org">ViMEET &middot; University of Mumbai</div>
        <ul>
          <li>Focused on AI, ML, backend systems, cloud computing, and system design</li>
          <li>Building real-world projects alongside formal coursework</li>
          <li>Growing toward scalable software and AI engineering roles</li>
        </ul>
        <div class="pill" style="color:#ffd37a;border-color:rgba(255,211,122,.2);background:rgba(255,211,122,.1)">CGPA 7.5 / 10</div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="contact">
  <div class="wrap">
    <div class="section-label reveal"><span>05</span> Transmission</div>
    <div class="contact">
      <div class="contact-main reveal">
        <h2>Let's build the <span>next frontier</span>.</h2>
        <p>I'm open to internships, collaborations, backend engineering roles, and AI-focused opportunities. If you're building something ambitious, I'd love to be part of the mission.</p>
        <div class="contact-btns">
          <a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">Send transmission</a>
          <a href="https://github.com/Shravan157/portfolio-website/blob/master/resume_shravan2.pdf" target="_blank" class="btn btn-resume">Download Resume &#8599;</a>
        </div>
      </div>
      <div class="contact-cards">
        <div class="contact-card reveal">
          <div class="clabel">Email</div>
          <div class="cvalue"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div>
        </div>
        <div class="contact-card reveal">
          <div class="clabel">Phone</div>
          <div class="cvalue">7385813010</div>
        </div>
        <div class="contact-card reveal">
          <div class="clabel">LinkedIn</div>
          <div class="cvalue"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div>
        </div>
        <div class="contact-card reveal">
          <div class="clabel">GitHub</div>
          <div class="cvalue"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="quote reveal">
    <p>
      The woods are lovely, dark and deep,<br>
      But I have promises to keep,<br>
      And <strong>miles to go before I sleep,</strong><br>
      And miles to go before I sleep.
    </p>
    <div class="src">&mdash; Robert Frost</div>
  </div>
</div>

<footer>
  <div class="wrap foot">
    <div>Built by Shravan Parthe &middot; 2026</div>
    <div style="display:flex;gap:1.2rem;flex-wrap:wrap;">
      <a target="_blank" href="https://github.com/Shravan157">GitHub</a>
      <a target="_blank" href="https://www.linkedin.com/in/shravan-parthe-00946b2ab">LinkedIn</a>
      <a href="mailto:shravanparthe@gmail.com">Email</a>
      <a target="_blank" href="https://github.com/Shravan157/portfolio-website/blob/master/resume_shravan2.pdf">Resume</a>
    </div>
  </div>
</footer>

<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('in');
  });
}, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

const nav = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.pageYOffset > 100) {
    nav.style.background = 'rgba(3,8,20,0.85)';
    nav.style.borderBottomColor = 'rgba(126,162,255,0.15)';
  } else {
    nav.style.background = 'rgba(3,8,20,0.6)';
    nav.style.borderBottomColor = 'rgba(126,162,255,0.08)';
  }
}, { passive: true });
</script>

</body>
</html>
"""

components.html(html_code, height=5200, scrolling=True)
