import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Shravan Parthe - Portfolio",
    page_icon="SP",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Shravan Parthe - Backend &amp; AI Engineer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #0a0a0a;
  --surface: #111111;
  --surface2: #161616;
  --border: #1e1e1e;
  --border2: #262626;
  --text: #f0ede8;
  --muted: #6b6b6b;
  --subtle: #3a3a3a;
  --accent: #e8d5b0;
  --accent2: #c8a96e;
  --green: #4ade80;
  --serif: 'Instrument Serif', Georgia, serif;
  --sans: 'Syne', sans-serif;
  --mono: 'JetBrains Mono', monospace;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  font-size: 15px;
  line-height: 1.6;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}
body::before {
  content: '';
  position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none; z-index: 1000; opacity: 0.5;
}
::selection { background: var(--accent2); color: #000; }
::-webkit-scrollbar { width: 2px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--subtle); border-radius: 99px; }
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 clamp(1.25rem, 5vw, 3.5rem); }
nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  padding: 1.25rem 0;
  background: rgba(10,10,10,0.85);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255,255,255,0.04);
}
.nav-inner {
  max-width: 1080px; margin: 0 auto;
  padding: 0 clamp(1.25rem, 5vw, 3.5rem);
  display: flex; align-items: center; justify-content: space-between;
}
.nav-logo { font-family: var(--sans); font-weight: 700; font-size: 1rem; color: var(--text); text-decoration: none; letter-spacing: -0.3px; }
.nav-logo span { font-family: var(--serif); font-style: italic; color: var(--accent2); font-size: 1.1rem; }
.nav-links { display: flex; gap: 2rem; align-items: center; }
.nav-links a { color: var(--muted); text-decoration: none; font-size: 0.8rem; font-weight: 500; letter-spacing: 0.5px; text-transform: uppercase; transition: color 0.2s; }
.nav-links a:hover { color: var(--text); }
.nav-available { display: flex; align-items: center; gap: 0.4rem; padding: 0.35rem 0.85rem; border: 1px solid rgba(74,222,128,0.25); border-radius: 99px; font-size: 0.7rem; font-family: var(--mono); color: var(--green); background: rgba(74,222,128,0.06); }
.nav-dot { width: 5px; height: 5px; border-radius: 50%; background: var(--green); box-shadow: 0 0 6px var(--green); animation: blink 2.5s infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }
.hero { min-height: 100vh; display: grid; place-items: center; padding: 8rem 0 5rem; position: relative; }
.hero-grid { display: grid; grid-template-columns: 1fr auto; gap: 6rem; align-items: end; width: 100%; }
.hero-num { font-family: var(--mono); font-size: 0.7rem; color: var(--subtle); letter-spacing: 2px; margin-bottom: 2rem; }
.hero-title { font-family: var(--serif); font-size: clamp(3.5rem, 7vw, 6rem); font-weight: 400; line-height: 1.02; letter-spacing: -1px; color: var(--text); }
.hero-title em { color: var(--accent2); font-style: italic; }
.hero-title .line2 { display: block; }
.hero-body { margin-top: 2.5rem; display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: start; }
.hero-desc { color: var(--muted); font-size: 0.9rem; line-height: 1.8; }
.hero-desc strong { color: var(--text); font-weight: 600; }
.hero-actions { display: flex; flex-direction: column; gap: 0.6rem; align-items: flex-start; padding-top: 0.25rem; }
.btn-primary { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.7rem 1.4rem; background: var(--accent); color: #0a0a0a; border-radius: 4px; text-decoration: none; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; transition: all 0.2s; }
.btn-primary:hover { background: var(--accent2); transform: translateY(-2px); }
.btn-secondary { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.68rem 1.2rem; border: 1px solid var(--border2); color: var(--muted); border-radius: 4px; text-decoration: none; font-size: 0.8rem; font-weight: 500; letter-spacing: 0.5px; text-transform: uppercase; transition: all 0.2s; }
.btn-secondary:hover { border-color: var(--subtle); color: var(--text); }
.hero-side { padding-bottom: 1rem; }
.hero-meta-list { list-style: none; }
.hero-meta-list li { display: flex; justify-content: space-between; gap: 2rem; padding: 0.75rem 0; border-bottom: 1px solid var(--border); font-size: 0.78rem; }
.meta-key { color: var(--muted); font-family: var(--mono); font-size: 0.68rem; letter-spacing: 0.5px; text-transform: uppercase; }
.meta-val { color: var(--text); text-align: right; }
.meta-val.green { color: var(--green); }
.sec-label { display: flex; align-items: center; gap: 0.75rem; font-family: var(--mono); font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: var(--subtle); margin-bottom: 3rem; }
.sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }
.sec-num { color: var(--accent2); }
.stats-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; margin-bottom: 6rem; }
.stat { background: var(--surface); padding: 2rem 1.5rem; text-align: center; transition: background 0.2s; }
.stat:hover { background: var(--surface2); }
.stat-n { font-family: var(--serif); font-size: 2.75rem; font-weight: 400; color: var(--text); line-height: 1; margin-bottom: 0.35rem; }
.stat-n em { font-style: italic; color: var(--accent2); }
.stat-l { font-family: var(--mono); font-size: 0.65rem; letter-spacing: 1.5px; text-transform: uppercase; color: var(--muted); }
.skills-section { padding-bottom: 6rem; }
.skills-col { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem; }
.skill-block { border: 1px solid var(--border); border-radius: 6px; padding: 1.25rem 1.4rem; background: var(--surface); transition: border-color 0.2s, background 0.2s; }
.skill-block:hover { border-color: var(--border2); background: var(--surface2); }
.skill-label { font-family: var(--mono); font-size: 0.62rem; letter-spacing: 1.5px; text-transform: uppercase; color: var(--subtle); margin-bottom: 0.85rem; }
.chip-row { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.chip { padding: 0.22rem 0.6rem; border-radius: 3px; font-family: var(--mono); font-size: 0.72rem; transition: transform 0.15s; }
.chip:hover { transform: translateY(-1px); }
.c1 { background: rgba(232,213,176,0.08); color: var(--accent); border: 1px solid rgba(232,213,176,0.15); }
.c2 { background: rgba(200,169,110,0.08); color: var(--accent2); border: 1px solid rgba(200,169,110,0.15); }
.c3 { background: rgba(255,255,255,0.04); color: #aaa; border: 1px solid var(--border2); }
.c4 { background: rgba(74,222,128,0.06); color: #6ee7a0; border: 1px solid rgba(74,222,128,0.15); }
.projects-section { padding-bottom: 6rem; }
.proj-list { display: flex; flex-direction: column; }
.proj-item { display: grid; grid-template-columns: 48px 1fr; border-top: 1px solid var(--border); padding: 2rem 0; position: relative; transition: background 0.2s; cursor: default; }
.proj-item:last-child { border-bottom: 1px solid var(--border); }
.proj-item::before { content: ''; position: absolute; left: -24px; right: -24px; top: 0; bottom: 0; background: var(--surface); border-radius: 6px; opacity: 0; transition: opacity 0.25s; pointer-events: none; }
.proj-item:hover::before { opacity: 1; }
.proj-idx { font-family: var(--mono); font-size: 0.65rem; color: var(--subtle); padding-top: 0.25rem; letter-spacing: 1px; position: relative; z-index: 1; }
.proj-content { position: relative; z-index: 1; }
.proj-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 1.5rem; margin-bottom: 0.5rem; }
.proj-name { font-family: var(--serif); font-size: 1.2rem; font-weight: 400; color: var(--text); letter-spacing: -0.3px; }
.proj-tag { padding: 0.18rem 0.6rem; border-radius: 3px; font-family: var(--mono); font-size: 0.62rem; letter-spacing: 0.5px; text-transform: uppercase; white-space: nowrap; flex-shrink: 0; }
.tag-ai  { background: rgba(183,148,244,0.1); color: #b794f4; border: 1px solid rgba(183,148,244,0.2); }
.tag-ft  { background: rgba(99,179,237,0.1); color: #63b3ed; border: 1px solid rgba(99,179,237,0.2); }
.tag-fs  { background: rgba(74,222,128,0.08); color: #6ee7a0; border: 1px solid rgba(74,222,128,0.15); }
.tag-ml  { background: rgba(251,211,141,0.1); color: #fbd38d; border: 1px solid rgba(251,211,141,0.2); }
.proj-desc { color: var(--muted); font-size: 0.85rem; line-height: 1.75; margin-bottom: 0.85rem; max-width: 680px; }
.proj-row { display: flex; align-items: center; justify-content: space-between; }
.proj-tech { display: flex; flex-wrap: wrap; gap: 0.3rem; }
.tech { padding: 0.15rem 0.45rem; border-radius: 3px; font-family: var(--mono); font-size: 0.65rem; color: var(--subtle); border: 1px solid var(--border); background: transparent; }
.proj-link { display: inline-flex; align-items: center; gap: 0.3rem; font-family: var(--mono); font-size: 0.7rem; color: var(--muted); text-decoration: none; letter-spacing: 0.3px; transition: color 0.2s; flex-shrink: 0; margin-left: 1rem; }
.proj-link:hover { color: var(--accent2); }
.proj-link svg { transition: transform 0.2s; }
.proj-link:hover svg { transform: translate(2px,-2px); }
.exp-section { padding-bottom: 6rem; }
.exp-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; }
.exp-card { border: 1px solid var(--border); border-radius: 8px; padding: 1.75rem; background: var(--surface); position: relative; overflow: hidden; transition: border-color 0.25s, background 0.25s; }
.exp-card:hover { border-color: var(--border2); background: var(--surface2); }
.exp-card::after { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, var(--accent2), transparent); opacity: 0; transition: opacity 0.3s; }
.exp-card:hover::after { opacity: 1; }
.exp-period { font-family: var(--mono); font-size: 0.65rem; color: var(--subtle); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 0.75rem; }
.exp-role { font-family: var(--serif); font-size: 1.1rem; color: var(--text); line-height: 1.3; margin-bottom: 0.2rem; }
.exp-org { font-family: var(--mono); font-size: 0.78rem; color: var(--accent2); margin-bottom: 1rem; }
.exp-points { list-style: none; }
.exp-points li { color: var(--muted); font-size: 0.83rem; line-height: 1.7; padding: 0.2rem 0 0.2rem 1rem; position: relative; }
.exp-points li::before { content: '\2014'; position: absolute; left: 0; color: var(--subtle); }
.exp-badge { display: inline-flex; align-items: center; gap: 0.4rem; margin-top: 1rem; padding: 0.25rem 0.7rem; border-radius: 99px; font-family: var(--mono); font-size: 0.65rem; color: var(--green); border: 1px solid rgba(74,222,128,0.2); background: rgba(74,222,128,0.06); }
.exp-cgpa { display: inline-block; margin-top: 1rem; padding: 0.25rem 0.7rem; border-radius: 4px; font-family: var(--mono); font-size: 0.7rem; color: var(--accent2); border: 1px solid rgba(200,169,110,0.25); background: rgba(200,169,110,0.06); }
.contact-section { padding-bottom: 8rem; }
.contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: start; }
.contact-headline { font-family: var(--serif); font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 400; line-height: 1.1; letter-spacing: -0.5px; color: var(--text); margin-bottom: 1.5rem; }
.contact-headline em { color: var(--accent2); font-style: italic; }
.contact-sub { color: var(--muted); font-size: 0.88rem; line-height: 1.75; margin-bottom: 2rem; }
.contact-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; }
.contact-card { border: 1px solid var(--border); border-radius: 6px; padding: 1.1rem 1.25rem; background: var(--surface); transition: all 0.2s; }
.contact-card:hover { border-color: var(--border2); background: var(--surface2); transform: translateY(-2px); }
.cc-label { font-family: var(--mono); font-size: 0.6rem; letter-spacing: 1.5px; text-transform: uppercase; color: var(--subtle); margin-bottom: 0.3rem; }
.cc-val { font-size: 0.82rem; color: var(--text); }
.cc-val a { color: var(--accent2); text-decoration: none; transition: color 0.2s; }
.cc-val a:hover { color: var(--accent); }
.contact-card.wide { grid-column: span 2; }
.quote-wrap { border-top: 1px solid var(--border); padding: 4rem 0; text-align: center; }
.quote-mark { font-family: var(--serif); font-size: 5rem; line-height: 0.5; color: var(--border2); display: block; margin-bottom: 1.5rem; }
.quote-body { font-family: var(--serif); font-style: italic; font-size: clamp(1rem, 2vw, 1.2rem); line-height: 2; color: var(--muted); max-width: 480px; margin: 0 auto 1rem; }
.quote-body strong { color: var(--accent2); font-weight: 400; }
.quote-src { font-family: var(--mono); font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: var(--subtle); }
footer { border-top: 1px solid var(--border); padding: 1.5rem 0; }
.foot-inner { max-width: 1080px; margin: 0 auto; padding: 0 clamp(1.25rem, 5vw, 3.5rem); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; }
.foot-copy { font-family: var(--mono); font-size: 0.68rem; color: var(--subtle); }
.foot-copy a { color: var(--muted); text-decoration: none; }
.foot-links { display: flex; gap: 1.5rem; }
.foot-links a { font-family: var(--mono); font-size: 0.68rem; letter-spacing: 0.5px; color: var(--subtle); text-decoration: none; text-transform: uppercase; transition: color 0.2s; }
.foot-links a:hover { color: var(--text); }
.reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
.reveal.in { opacity: 1; transform: translateY(0); }
.reveal:nth-child(2) { transition-delay: 0.1s; }
.reveal:nth-child(3) { transition-delay: 0.2s; }
.reveal:nth-child(4) { transition-delay: 0.3s; }
@media (max-width: 860px) {
  .hero-grid { grid-template-columns: 1fr; }
  .hero-body { grid-template-columns: 1fr; gap: 2rem; }
  .hero-side { display: none; }
  .stats-row { grid-template-columns: repeat(2, 1fr); }
  .skills-col { grid-template-columns: 1fr; }
  .exp-grid { grid-template-columns: 1fr; }
  .contact-grid { grid-template-columns: 1fr; gap: 3rem; }
  .nav-links a:not(.nav-available) { display: none; }
}
@media (max-width: 560px) {
  .contact-cards { grid-template-columns: 1fr; }
  .contact-card.wide { grid-column: span 1; }
}
</style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <a href="#" class="nav-logo">Shravan<span>.</span></a>
    <div class="nav-links">
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#experience">Experience</a>
      <a href="#contact">Contact</a>
      <div class="nav-available"><div class="nav-dot"></div>Available</div>
    </div>
  </div>
</nav>

<section class="hero" id="home">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <div class="hero-num reveal">SP &#183; 2026</div>
        <h1 class="hero-title reveal">
          <em>Shravan</em>
          <span class="line2">Parthe.</span>
        </h1>
        <div class="hero-body reveal">
          <p class="hero-desc">
            <strong>Backend Engineer &amp; AI Developer.</strong><br>
            3rd year B.Tech CSE (AI&amp;ML) student building
            production-grade systems in Java, Spring Boot, and Python.
            Currently working on real-world Gen AI integrations at Innovexis.
          </p>
          <div class="hero-actions">
            <a href="mailto:shravanparthe@gmail.com" class="btn-primary">Get in Touch</a>
            <a href="https://github.com/Shravan157" target="_blank" class="btn-secondary">GitHub Profile</a>
          </div>
        </div>
      </div>
      <div class="hero-side reveal">
        <ul class="hero-meta-list">
          <li><span class="meta-key">Role</span><span class="meta-val">Backend / AI Dev</span></li>
          <li><span class="meta-key">Status</span><span class="meta-val green">Open to work</span></li>
          <li><span class="meta-key">Location</span><span class="meta-val">Mumbai, India</span></li>
          <li><span class="meta-key">CGPA</span><span class="meta-val">7.5 / 10</span></li>
          <li><span class="meta-key">Batch</span><span class="meta-val">2027</span></li>
          <li><span class="meta-key">Internship</span><span class="meta-val">Innovexis &#183; Apr 2026</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="stats-row reveal">
    <div class="stat"><div class="stat-n">5<em>+</em></div><div class="stat-l">Projects</div></div>
    <div class="stat"><div class="stat-n">7<em>.</em>5</div><div class="stat-l">CGPA</div></div>
    <div class="stat"><div class="stat-n">3<em>rd</em></div><div class="stat-l">Year B.Tech</div></div>
    <div class="stat"><div class="stat-n">1</div><div class="stat-l">Internship</div></div>
  </div>
</div>

<section class="skills-section" id="skills">
  <div class="wrap">
    <div class="sec-label reveal"><span class="sec-num">01</span> Skills</div>
    <div class="skills-col reveal">
      <div class="skill-block">
        <div class="skill-label">Languages</div>
        <div class="chip-row">
          <span class="chip c1">Java</span><span class="chip c1">Python</span><span class="chip c1">JavaScript</span><span class="chip c1">Dart</span><span class="chip c1">SQL</span>
        </div>
      </div>
      <div class="skill-block">
        <div class="skill-label">Frameworks</div>
        <div class="chip-row">
          <span class="chip c2">Spring Boot</span><span class="chip c2">React</span><span class="chip c2">Flutter</span><span class="chip c2">FastAPI</span><span class="chip c2">Spring AI</span>
        </div>
      </div>
      <div class="skill-block">
        <div class="skill-label">Tools &amp; Libraries</div>
        <div class="chip-row">
          <span class="chip c3">Docker</span><span class="chip c3">GitHub</span><span class="chip c3">NumPy</span><span class="chip c3">Pandas</span><span class="chip c3">Scikit-learn</span><span class="chip c3">NLTK</span>
        </div>
      </div>
      <div class="skill-block">
        <div class="skill-label">Databases</div>
        <div class="chip-row">
          <span class="chip c4">MySQL</span><span class="chip c4">PostgreSQL</span><span class="chip c4">Firebase</span><span class="chip c4">Redis</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="projects-section" id="projects">
  <div class="wrap">
    <div class="sec-label reveal"><span class="sec-num">02</span> Projects</div>
    <div class="proj-list reveal">

      <div class="proj-item">
        <span class="proj-idx">01</span>
        <div class="proj-content">
          <div class="proj-top">
            <div class="proj-name">MedoraX AI &#8212; Clinical AI Assistant</div>
            <span class="proj-tag tag-ai">Healthcare AI</span>
          </div>
          <p class="proj-desc">Multimodal clinical assistant supporting voice, image, and text. Transcribes symptoms via Whisper-large-v3, analyzes medical images via Llama-4-scout, and generates structured diagnostic responses using Llama-3.3-70b. Multilingual (English, Hindi, Marathi) with GPS hospital finder and real-time AQI monitoring.</p>
          <div class="proj-row">
            <div class="proj-tech">
              <span class="tech">Python</span><span class="tech">Gradio</span><span class="tech">Groq API</span><span class="tech">Google Maps API</span>
            </div>
            <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="proj-link">
              GitHub <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="proj-item">
        <span class="proj-idx">02</span>
        <div class="proj-content">
          <div class="proj-top">
            <div class="proj-name">SahayLoan &#8212; Micro-Loan Platform</div>
            <span class="proj-tag tag-ft">FinTech</span>
          </div>
          <p class="proj-desc">Full-stack micro-lending platform for loans up to &#8377;1,00,000. Flutter frontend, FastAPI backend, AI credit scoring with Random Forest classifier, digital KYC with Aadhaar &amp; PAN OCR via Tesseract, Stripe EMI integration, Firebase Auth and Firestore multi-role system.</p>
          <div class="proj-row">
            <div class="proj-tech">
              <span class="tech">Flutter</span><span class="tech">FastAPI</span><span class="tech">Scikit-learn</span><span class="tech">Firebase</span><span class="tech">Stripe</span>
            </div>
            <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="proj-link">
              GitHub <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="proj-item">
        <span class="proj-idx">03</span>
        <div class="proj-content">
          <div class="proj-top">
            <div class="proj-name">SikshaSetu &#8212; Rural Education Platform</div>
            <span class="proj-tag tag-fs">Full-Stack</span>
          </div>
          <p class="proj-desc">Education platform bridging the digital divide for rural communities. Role-based access control with Spring Security and JWT/OAuth 2.0, optimized relational schema, responsive React frontend, ZEGOCLOUD real-time video SDK for virtual classrooms.</p>
          <div class="proj-row">
            <div class="proj-tech">
              <span class="tech">React</span><span class="tech">Spring Boot</span><span class="tech">Spring Security</span><span class="tech">JWT</span><span class="tech">MySQL</span>
            </div>
            <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="proj-link">
              GitHub <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="proj-item">
        <span class="proj-idx">04</span>
        <div class="proj-content">
          <div class="proj-top">
            <div class="proj-name">AI-Powered E-Commerce Backend</div>
            <span class="proj-tag tag-ai">AI / Full-Stack</span>
          </div>
          <p class="proj-desc">Intelligent e-commerce backend with AI-driven product recommendations using Spring AI and vector similarity search via Redis Vector DB. Generative AI chatbot for real-time customer support, AI-powered product image generation pipeline, secured with Spring Security and JWT.</p>
          <div class="proj-row">
            <div class="proj-tech">
              <span class="tech">React</span><span class="tech">Spring Boot</span><span class="tech">Spring AI</span><span class="tech">Redis Vector DB</span><span class="tech">Tailwind</span>
            </div>
            <a href="https://github.com/Shravan157" target="_blank" class="proj-link">
              GitHub <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

      <div class="proj-item">
        <span class="proj-idx">05</span>
        <div class="proj-content">
          <div class="proj-top">
            <div class="proj-name">Zomato Review Sentiment Analysis</div>
            <span class="proj-tag tag-ml">ML / NLP</span>
          </div>
          <p class="proj-desc">End-to-end NLP pipeline classifying 10,000+ Zomato restaurant reviews. Extensive EDA with 15 visualizations, hypothesis testing, TF-IDF vectorization, model comparison across Logistic Regression, Random Forest, and Naive Bayes. Logistic Regression achieved the highest F1 score.</p>
          <div class="proj-row">
            <div class="proj-tech">
              <span class="tech">Python</span><span class="tech">Scikit-learn</span><span class="tech">NLTK</span><span class="tech">TF-IDF</span><span class="tech">Pandas</span>
            </div>
            <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="proj-link">
              GitHub <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
            </a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="exp-section" id="experience">
  <div class="wrap">
    <div class="sec-label reveal"><span class="sec-num">03</span> Experience &amp; Education</div>
    <div class="exp-grid reveal">

      <div class="exp-card">
        <div class="exp-period">Apr 2026 &#8212; Present &#183; Remote</div>
        <div class="exp-role">Data Science with Gen AI Intern</div>
        <div class="exp-org">Innovexis</div>
        <ul class="exp-points">
          <li>Selected for Innovexis's competitive Data Science with Gen AI program</li>
          <li>Real-world projects integrating LLMs and generative AI techniques</li>
          <li>Python, NumPy, Pandas, Scikit-learn for data analysis and model building</li>
          <li>Hands-on exposure to production-level Gen AI workflows</li>
        </ul>
        <div class="exp-badge"><div class="nav-dot"></div>Currently Active</div>
      </div>

      <div class="exp-card">
        <div class="exp-period">Jun 2023 &#8212; May 2027 (Expected)</div>
        <div class="exp-role">B.Tech, Computer Science Engineering (AI &amp; ML)</div>
        <div class="exp-org">ViMEET &#183; University of Mumbai</div>
        <ul class="exp-points">
          <li>Specializing in Artificial Intelligence &amp; Machine Learning</li>
          <li>Coursework: DSA, Machine Learning, Cloud Computing, Microservices, System Design</li>
          <li>Building production projects alongside coursework</li>
        </ul>
        <div class="exp-cgpa">CGPA 7.5 / 10.0</div>
      </div>

    </div>
  </div>
</section>

<section class="contact-section" id="contact">
  <div class="wrap">
    <div class="sec-label reveal"><span class="sec-num">04</span> Contact</div>
    <div class="contact-grid reveal">
      <div>
        <h2 class="contact-headline">Let's build<br><em>something.</em></h2>
        <p class="contact-sub">Open to internships, collaborations, and conversations about backend systems, AI, and anything in between.</p>
        <a href="mailto:shravanparthe@gmail.com" class="btn-primary">Send a Message</a>
      </div>
      <div class="contact-cards">
        <div class="contact-card">
          <div class="cc-label">Email</div>
          <div class="cc-val"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div>
        </div>
        <div class="contact-card">
          <div class="cc-label">Phone</div>
          <div class="cc-val">7385813010</div>
        </div>
        <div class="contact-card">
          <div class="cc-label">LinkedIn</div>
          <div class="cc-val"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div>
        </div>
        <div class="contact-card">
          <div class="cc-label">GitHub</div>
          <div class="cc-val"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div>
        </div>
        <div class="contact-card wide">
          <div class="cc-label">Location</div>
          <div class="cc-val">Mumbai, India</div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="quote-wrap">
    <span class="quote-mark">&#8220;</span>
    <p class="quote-body">
      The woods are lovely, dark and deep,<br>
      But I have promises to keep,<br>
      And <strong>miles to go before I sleep,</strong><br>
      And miles to go before I sleep.
    </p>
    <div class="quote-src">&#8212; Robert Frost</div>
  </div>
</div>

<footer>
  <div class="foot-inner">
    <div class="foot-copy">Built by <a href="https://github.com/Shravan157">Shravan Parthe</a> &#183; 2026</div>
    <div class="foot-links">
      <a href="https://github.com/Shravan157" target="_blank">GitHub</a>
      <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn</a>
      <a href="mailto:shravanparthe@gmail.com">Email</a>
    </div>
  </div>
</footer>

<script>
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
document.querySelectorAll('.hero .reveal').forEach((el, i) => {
  setTimeout(() => el.classList.add('in'), i * 120 + 100);
});
</script>
</body>
</html>"""

components.html(HTML, height=7000, scrolling=True)
