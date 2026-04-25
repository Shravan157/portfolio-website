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
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Shravan Parthe — Space Portfolio",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, header, footer {visibility: hidden;}
html, body, .stApp { background: #050816; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Shravan Parthe — Space Portfolio</title>
//fonts.googleapis.com">
//fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#050816;
  --bg2:#0a1022;
  --panel:rgba(12,17,34,.72);
  --border:rgba(150,170,255,.14);
  --text:#eef3ff;
  --muted:#9aa7c7;
  --soft:#6f7ca2;
  --cyan:#7cecff;
  --violet:#a78bfa;
  --green:#66f2b0;
  --gold:#ffd37a;
  --sans:'Inter',sans-serif;
  --mono:'JetBrains Mono',monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:var(--sans);
  color:var(--text);
  background:
    radial-gradient(circle at 20% 20%, rgba(124,236,255,.11), transparent 22%),
    radial-gradient(circle at 75% 18%, rgba(167,139,250,.10), transparent 24%),
    radial-gradient(circle at 55% 75%, rgba(102,242,176,.06), transparent 26%),
    linear-gradient(180deg, #03050f 0%, #060b18 55%, #050816 100%);
  overflow-x:hidden;
}
body::before{
  content:"";
  position:fixed;
  inset:0;
  background-image:
    radial-gradient(1px 1px at 20px 30px, rgba(255,255,255,.85), transparent),
    radial-gradient(1px 1px at 160px 120px, rgba(255,255,255,.65), transparent),
    radial-gradient(1px 1px at 290px 80px, rgba(124,236,255,.7), transparent),
    radial-gradient(1.2px 1.2px at 460px 160px, rgba(255,255,255,.7), transparent),
    radial-gradient(1px 1px at 680px 60px, rgba(167,139,250,.7), transparent);
  background-size: 900px 500px;
  opacity:.35;
  pointer-events:none;
  z-index:0;
  animation: drift 90s linear infinite;
}
@keyframes drift{from{transform:translateY(0)}to{transform:translateY(55px)}}
.wrap{
  width:min(1160px, calc(100% - 32px));
  margin:0 auto;
  position:relative;
  z-index:2;
}
nav{
  position:fixed; top:0; left:0; right:0; z-index:20;
  background:rgba(5,8,22,.55);
  backdrop-filter:blur(16px);
  border-bottom:1px solid rgba(255,255,255,.05);
}
.nav-inner{
  width:min(1160px, calc(100% - 32px));
  margin:0 auto;
  min-height:72px;
  display:flex; align-items:center; justify-content:space-between;
}
.logo{
  font-weight:800;
  letter-spacing:1px;
  text-transform:uppercase;
}
.logo span{color:var(--cyan)}
.links{
  display:flex; align-items:center; gap:1.1rem; flex-wrap:wrap;
}
.links a{
  color:var(--muted);
  font-size:.76rem;
  text-transform:uppercase;
  letter-spacing:1.4px;
  text-decoration:none;
}
.links a:hover{color:var(--cyan)}
.live{
  display:flex; align-items:center; gap:.5rem;
  padding:.4rem .8rem;
  border-radius:999px;
  border:1px solid rgba(102,242,176,.18);
  background:rgba(102,242,176,.06);
  color:var(--green);
  font-family:var(--mono);
  font-size:.7rem;
}
.dot{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 10px var(--green)}
.hero{
  min-height:100vh;
  display:flex;
  align-items:center;
  padding:7rem 0 4rem;
}
.hero-grid{
  display:grid;
  grid-template-columns:1.1fr .9fr;
  gap:2.5rem;
  align-items:center;
}
.kicker{
  display:flex; align-items:center; gap:.7rem;
  font-family:var(--mono);
  color:var(--cyan);
  font-size:.72rem;
  text-transform:uppercase;
  letter-spacing:2px;
  margin-bottom:1rem;
}
.kicker::before{
  content:"";
  width:44px;height:1px;
  background:linear-gradient(90deg,var(--cyan),transparent);
}
h1{
  font-size:clamp(3rem, 7vw, 6rem);
  line-height:1.02;
  letter-spacing:-1px;
  margin-bottom:1rem;
}
h1 .accent{color:var(--cyan)}
.sub{
  max-width:680px;
  color:var(--muted);
  font-size:1rem;
  line-height:1.9;
  margin-bottom:1.6rem;
}
.actions{
  display:flex; gap:.9rem; flex-wrap:wrap;
}
.btn{
  display:inline-flex; align-items:center; gap:.55rem;
  padding:.9rem 1.2rem;
  border-radius:12px;
  text-decoration:none;
  font-size:.82rem;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:1px;
  transition:.25s ease;
}
.primary{
  background:linear-gradient(135deg,var(--cyan),#8db0ff);
  color:#041019;
}
.secondary{
  border:1px solid var(--border);
  color:var(--text);
  background:rgba(255,255,255,.03);
}
.btn:hover{transform:translateY(-2px)}
.cue{
  margin-top:1rem;
  color:var(--soft);
  font-family:var(--mono);
  font-size:.72rem;
  letter-spacing:1px;
}
.panel{
  position:relative;
  min-height:500px;
  border:1px solid var(--border);
  border-radius:26px;
  background:linear-gradient(180deg, rgba(12,18,40,.78), rgba(8,12,24,.72));
  overflow:hidden;
}
.panel::before{
  content:"";
  position:absolute; inset:0;
  background:
    radial-gradient(circle at 72% 22%, rgba(124,236,255,.14), transparent 18%),
    radial-gradient(circle at 28% 75%, rgba(167,139,250,.12), transparent 18%);
}
.orbit{
  position:absolute;
  border:1px dashed rgba(255,255,255,.12);
  border-radius:50%;
}
.o1{width:390px;height:390px;top:58px;left:50%;transform:translateX(-50%)}
.o2{width:250px;height:250px;top:128px;left:50%;transform:translateX(-50%)}
.planet{
  position:absolute;
  width:78px;height:78px;border-radius:50%;
  top:178px;left:50%;transform:translateX(-50%);
  background:radial-gradient(circle at 30% 30%, #d9e7ff, #7aa2ff 48%, #334c93 82%);
  box-shadow:0 0 34px rgba(122,162,255,.22);
}
.rocket{
  position:absolute; right:72px; top:105px;
  font-size:2.1rem;
  opacity:.82;
  transform:rotate(14deg);
  filter:drop-shadow(0 0 10px rgba(255,255,255,.08));
}
.astronaut{
  position:absolute; left:58px; bottom:110px;
  font-size:2.4rem;
  opacity:.78;
}
.mini{
  position:absolute;
  left:24px; right:24px; bottom:22px;
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:12px;
}
.box{
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.07);
  border-radius:16px;
  padding:1rem;
}
.label{
  font-family:var(--mono);
  color:var(--soft);
  text-transform:uppercase;
  font-size:.66rem;
  letter-spacing:1.2px;
  margin-bottom:.45rem;
}
.value{color:var(--text); line-height:1.7; font-size:.92rem}
.section{padding:1.8rem 0 4.6rem}
.sec{
  display:flex; align-items:center; gap:.8rem;
  margin-bottom:1.5rem;
  font-family:var(--mono);
  color:var(--soft);
  text-transform:uppercase;
  letter-spacing:2px;
  font-size:.7rem;
}
.sec::after{content:"";height:1px;flex:1;background:linear-gradient(90deg, rgba(124,236,255,.18), rgba(255,255,255,.05))}
.sec span{color:var(--cyan)}
.stats{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:1rem;
}
.stat,.card,.project,.exp,.contact-card,.quote{
  border:1px solid var(--border);
  background:var(--panel);
  border-radius:22px;
  backdrop-filter:blur(10px);
}
.stat{padding:1.35rem}
.stat h3{font-size:2rem;margin-bottom:.35rem}
.stat p{color:var(--muted);font-family:var(--mono);font-size:.72rem;text-transform:uppercase;letter-spacing:1px}
.grid-2{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}
.card{padding:1.25rem}
.card h3,.project h3,.exp h3{margin-bottom:.9rem}
.chips{display:flex;flex-wrap:wrap;gap:.5rem}
.chip{
  padding:.42rem .68rem;border-radius:999px;
  border:1px solid rgba(255,255,255,.08);
  background:rgba(255,255,255,.03);
  color:var(--muted);
  font-family:var(--mono);
  font-size:.72rem;
}
.projects{display:flex;flex-direction:column;gap:1rem}
.project{padding:1.35rem;transition:.25s ease}
.project:hover{transform:translateY(-3px);border-color:rgba(124,236,255,.28)}
.proj-top{display:flex;justify-content:space-between;gap:1rem;align-items:flex-start}
.tag{
  padding:.3rem .65rem;border-radius:999px;font-family:var(--mono);font-size:.67rem;text-transform:uppercase;letter-spacing:.8px
}
.t1{color:var(--violet);background:rgba(167,139,250,.08)}
.t2{color:var(--cyan);background:rgba(124,236,255,.08)}
.t3{color:var(--green);background:rgba(102,242,176,.08)}
.t4{color:var(--gold);background:rgba(255,211,122,.08)}
.project p{color:var(--muted);line-height:1.8;font-size:.94rem;margin-bottom:1rem}
.bottom{display:flex;justify-content:space-between;gap:1rem;align-items:center;flex-wrap:wrap}
.techs{display:flex;flex-wrap:wrap;gap:.45rem}
.tech{
  padding:.34rem .6rem;border-radius:999px;
  border:1px solid rgba(255,255,255,.07);
  color:var(--soft);
  font-family:var(--mono);
  font-size:.7rem;
}
.link{color:var(--cyan);font-weight:700;text-decoration:none}
.exp-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.exp{padding:1.35rem}
.period{color:var(--soft);font-family:var(--mono);font-size:.72rem;margin-bottom:.65rem;text-transform:uppercase}
.org{color:var(--cyan);font-family:var(--mono);font-size:.78rem;margin-bottom:.9rem}
.exp ul{list-style:none}
.exp li{
  padding-left:1rem; margin:.35rem 0;
  color:var(--muted); line-height:1.8; position:relative;
}
.exp li::before{content:"✦";position:absolute;left:0;color:var(--cyan);font-size:.7rem}
.contact{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:1rem;
}
.main-contact{
  padding:1.7rem;
  border:1px solid var(--border);
  background:var(--panel);
  border-radius:24px;
}
.main-contact h2{
  font-size:clamp(2rem,4vw,3.4rem);
  line-height:1.1;
  margin-bottom:1rem;
}
.main-contact h2 span{color:var(--cyan)}
.main-contact p{color:var(--muted);line-height:1.9;margin-bottom:1.4rem;max-width:560px}
.contact-grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:1rem;
}
.contact-card{
  padding:1.1rem;
}
.small{color:var(--soft);font-family:var(--mono);font-size:.66rem;text-transform:uppercase;letter-spacing:1.2px;margin-bottom:.4rem}
.big{color:var(--text);line-height:1.7}
.big a{color:var(--cyan)}
.quote{
  margin-top:2rem;
  padding:2.4rem 1.5rem;
  text-align:center;
}
.quote p{
  color:#d8e1f8;
  line-height:2;
  font-size:clamp(1rem,2vw,1.2rem);
}
.quote .src{
  margin-top:1rem;
  color:var(--soft);
  font-family:var(--mono);
  font-size:.7rem;
  text-transform:uppercase;
  letter-spacing:2px;
}
footer{
  padding:1.2rem 0 2.4rem;
  border-top:1px solid rgba(255,255,255,.06);
}
.foot{
  display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;
  color:var(--soft);font-family:var(--mono);font-size:.72rem
}
.reveal{opacity:0;transform:translateY(18px);transition:all .75s ease}
.reveal.in{opacity:1;transform:translateY(0)}
@media (max-width: 980px){
  .hero-grid,.contact,.exp-grid,.stats,.grid-2,.contact-grid{grid-template-columns:1fr}
  .panel{min-height:420px}
}
@media (max-width: 680px){
  .links a{display:none}
  h1{font-size:2.7rem}
  .mini{grid-template-columns:1fr}
}
</style>
</head>
<body>
<nav>
  <div class="nav-inner">
    <a class="logo" href="#home">SHRAVAN<span>.SPACE</span></a>
    <div class="links">
      <a href="#skills">Arsenal</a>
      <a href="#projects">Missions</a>
      <a href="#experience">Flight Log</a>
      <a href="#contact">Contact</a>
      <div class="live"><span class="dot"></span> Available</div>
    </div>
  </div>
</nav>

<section class="hero" id="home">
  <div class="wrap">
    <div class="hero-grid">
      <div class="reveal">
        <div class="kicker">Mission Control · 2026</div>
        <h1>Exploring the <span class="accent">unknown</span><br>through code.</h1>
        <p class="sub">
          I’m Shravan Parthe, a backend and AI developer building reliable systems with Java, Spring Boot, Python, and modern AI tools. This portfolio is a quiet map of the things I’ve learned, built, and am still discovering.
        </p>
        <div class="actions">
          <a class="btn primary" href="mailto:shravanparthe@gmail.com">Start a mission</a>
          <a class="btn secondary" href="https://github.com/Shravan157" target="_blank">GitHub</a>
          <a class="btn secondary" href="#projects">Explore projects</a>
        </div>
        <div class="cue">Scroll to explore the mission log ↓</div>
      </div>

      <div class="panel reveal">
        <div class="orbit o1"></div>
        <div class="orbit o2"></div>
        <div class="planet"></div>
        <div class="rocket">🚀</div>
        <div class="astronaut">👨‍🚀</div>
        <div class="mini">
          <div class="box">
            <div class="label">Current orbit</div>
            <div class="value">Backend Engineer & AI Developer focused on scalable web apps and GenAI integration.</div>
          </div>
          <div class="box">
            <div class="label">Learning mode</div>
            <div class="value">Always exploring new systems, tools, and ideas — one mission at a time.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec reveal"><span>01</span> Mission Stats</div>
    <div class="stats">
      <div class="stat reveal"><h3>5+</h3><p>Projects</p></div>
      <div class="stat reveal"><h3>7.5</h3><p>CGPA</p></div>
      <div class="stat reveal"><h3>3rd</h3><p>Year B.Tech</p></div>
      <div class="stat reveal"><h3>2027</h3><p>Expected Grad</p></div>
    </div>
  </div>
</section>

<section class="section" id="skills">
  <div class="wrap">
    <div class="sec reveal"><span>02</span> Tech Arsenal</div>
    <div class="grid-2">
      <div class="card reveal">
        <h3>Languages</h3>
        <div class="chips">
          <span class="chip">Java</span><span class="chip">Python</span><span class="chip">JavaScript</span><span class="chip">Dart</span><span class="chip">SQL</span>
        </div>
      </div>
      <div class="card reveal">
        <h3>Frameworks</h3>
        <div class="chips">
          <span class="chip">Spring Boot</span><span class="chip">React</span><span class="chip">Flutter</span><span class="chip">FastAPI</span><span class="chip">Spring AI</span>
        </div>
      </div>
      <div class="card reveal">
        <h3>Tools</h3>
        <div class="chips">
          <span class="chip">Docker</span><span class="chip">GitHub</span><span class="chip">NumPy</span><span class="chip">Pandas</span><span class="chip">Scikit-learn</span><span class="chip">NLTK</span>
        </div>
      </div>
      <div class="card reveal">
        <h3>Databases</h3>
        <div class="chips">
          <span class="chip">MySQL</span><span class="chip">PostgreSQL</span><span class="chip">Firebase</span><span class="chip">Redis</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="projects">
  <div class="wrap">
    <div class="sec reveal"><span>03</span> Missions</div>
    <div class="projects">
      <div class="project reveal">
        <div class="proj-top"><h3>MedoraX AI — Clinical AI Assistant</h3><span class="tag t1">Healthcare AI</span></div>
        <p>Multimodal clinical assistant with voice, image, and text support, multilingual interaction, and location-aware assistance.</p>
        <div class="bottom"><div class="techs"><span class="tech">Python</span><span class="tech">Gradio</span><span class="tech">Groq API</span><span class="tech">Maps API</span></div><a class="link" href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank">View ↗</a></div>
      </div>
      <div class="project reveal">
        <div class="proj-top"><h3>SahayLoan — Micro-Loan Platform</h3><span class="tag t2">FinTech</span></div>
        <p>Full-stack lending system with AI credit scoring, OCR-based KYC, multi-role workflows, and EMI integration.</p>
        <div class="bottom"><div class="techs"><span class="tech">Flutter</span><span class="tech">FastAPI</span><span class="tech">Scikit-learn</span><span class="tech">Firebase</span></div><a class="link" href="https://github.com/Shravan157/Sahay-Loan" target="_blank">View ↗</a></div>
      </div>
      <div class="project reveal">
        <div class="proj-top"><h3>SikshaSetu — Rural Education Platform</h3><span class="tag t3">Full-Stack</span></div>
        <p>Education platform with secure auth, role-based access, optimized relational design, and real-time classrooms.</p>
        <div class="bottom"><div class="techs"><span class="tech">React</span><span class="tech">Spring Boot</span><span class="tech">JWT</span><span class="tech">MySQL</span></div><a class="link" href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank">View ↗</a></div>
      </div>
      <div class="project reveal">
        <div class="proj-top"><h3>Zomato Review Sentiment Analysis</h3><span class="tag t4">ML / NLP</span></div>
        <p>End-to-end sentiment analysis pipeline with EDA, TF-IDF, and model comparison across multiple classifiers.</p>
        <div class="bottom"><div class="techs"><span class="tech">Python</span><span class="tech">Scikit-learn</span><span class="tech">NLTK</span><span class="tech">Pandas</span></div><a class="link" href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank">View ↗</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="experience">
  <div class="wrap">
    <div class="sec reveal"><span>04</span> Flight Log</div>
    <div class="exp-grid">
      <div class="exp reveal">
        <div class="period">Apr 2026 — Present</div>
        <h3>Data Science with Gen AI Intern</h3>
        <div class="org">Innovexis</div>
        <u
        <ul>
          >Real-world GenAI projects and workflow exposure.</l/li>
          >Python, NumPy, Pandas, and Scikit-learn usage.</l/li>
          >Production-level problem solving and iteration.</li>
        </ul>
      </div>
      <div class="exp reveal">
        <div class="period">Jun 2023 — May 2027</div>
        <h3>B.Tech CSE (AI & ML)</h3>
        <div class="org">ViMEET · University of Mumbai</div>
        <u
        <ul>
          >Focused on AI, backend systems, cloud, and system design.</l/li>
          >Building production projects alongside coursework.</l/li>
          >CGPA 7.5 / 10.0</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="contact">
  <div class="wrap">
    <div class="sec reveal"><span>05</span> Transmission</div>
    <div class="contact">
      <div class="main-contact reveal">
        <h2>Let’s build the <span>next frontier</span>.</h2>
        <p>Open to internships, collaborations, backend engineering roles, and AI projects that push beyond the obvious.</p>
        <a class="btn primary" href="mailto:shravanparthe@gmail.com">Send transmission</a>
      </div>
      <div class="contact-grid">
        <div class="contact-card reveal"><div class="small">Email</div><div class="big"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div></div>
        <div class="contact-card reveal"><div class="small">Phone</div><div class="big">7385813010</div></div>
        <div class="contact-card reveal"><div class="small">LinkedIn</div><div class="big"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div></div>
        <div class="contact-card reveal"><div class="small">GitHub</div><div class="big"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div></div>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="quote reveal">
    <p>The woods are lovely, dark and deep,<br>But I have promises to keep,<br>And <strong>miles to go before I sleep</strong>.</p>
    <div class="src">— Robert Frost</div>
  </div>
</div>

<footer>
  <div class="wrap foot">
    <div>Built by Shravan Parthe · 2026</div>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;">
      <a style="color:inherit;text-decoration:none" href="https://github.com/Shravan157" target="_blank">GitHub</a>
      <a style="color:inherit;text-decoration:none" href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn</a>
      <a style="color:inherit;text-decoration:none" href="mailto:shravanparthe@gmail.com">Email</a>
    </div>
  </div>
</footer>

<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting) entry.target.classList.add("in");
  });
}, { threshold: 0.12 });

document.querySelectorAll(".reveal").forEach(el => observer.observe(el));
</script>
</body>
</html>
"""

components.html(html_code, height=4300, scrolling=True)
