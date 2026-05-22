import streamlit as st
import streamlit.components.v1 as components

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Shravan Parthe | Orbital Portfolio",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================
# HIDE STREAMLIT DEFAULT UI
# ============================================
st.markdown("""
<style>
  /* Hide Streamlit branding and default elements */
  #MainMenu, header, footer, [data-testid="stToolbar"],
  [data-testid="stDecoration"], [data-testid="stStatusWidget"],
  .stDeployButton { visibility: hidden !important; display: none !important; }
  
  /* Full bleed background and container */
  .stApp { background: #02040e !important; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  
  /* Iframe styling */
  iframe { border: none !important; display: block !important; }
  section[data-testid="stAppViewContainer"] > div { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ============================================
# RESUME URL (RAW GITHUB LINK)
# ============================================
RESUME_URL = "https://raw.githubusercontent.com/Shravan157/portfolio-website/master/resume_shravan2.pdf"

# ============================================
# HTML / CSS / JS PORTFOLIO (SPACE THEME)
# ============================================
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Shravan Parthe · Orbital Engineer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Sora:wght@300;400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
  /* ---------- RESET & VARIABLES ---------- */
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  :root {
    --void: #02040e;
    --surf: rgba(255, 255, 255, 0.032);
    --surf2: rgba(255, 255, 255, 0.062);
    --bd: rgba(122, 162, 255, 0.12);
    --bd2: rgba(122, 162, 255, 0.22);
    --text: #eef5ff;
    --muted: #8b9bc2;
    --sub: #4a5a82;
    --cyan: #5ef3ff;
    --gold: #ffd966;
    --violet: #b794f4;
    --green: #34d399;
    --pink: #f472b6;
    --blue: #60a5fa;
    --H: 'Orbitron', monospace;
    --B: 'Sora', sans-serif;
    --M: 'Space Mono', monospace;
  }
  body {
    font-family: var(--B);
    background: var(--void);
    color: var(--text);
    line-height: 1.65;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
  }
  ::selection { background: var(--violet); color: #fff; }
  ::-webkit-scrollbar { width: 3px; }
  ::-webkit-scrollbar-track { background: var(--void); }
  ::-webkit-scrollbar-thumb { background: var(--violet); border-radius: 99px; }
  a { color: inherit; text-decoration: none; }

  /* ---------- CANVAS STARS + COSMIC DUST ---------- */
  #cosmic-canvas {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
  }

  /* ---------- NEBULA GLOWS ---------- */
  .nebula {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 1;
    animation: drift 20s ease-in-out infinite alternate;
    filter: blur(80px);
  }
  .nb1 { width: 700px; height: 700px; background: radial-gradient(circle, rgba(167,139,250,.18), transparent); top: -200px; left: -200px; }
  .nb2 { width: 600px; height: 600px; background: radial-gradient(circle, rgba(94,243,255,.14), transparent); top: 20%; right: -180px; animation-delay: -7s; }
  .nb3 { width: 550px; height: 550px; background: radial-gradient(circle, rgba(96,165,250,.1), transparent); bottom: -120px; left: 20%; animation-delay: -14s; }
  .nb4 { width: 380px; height: 380px; background: radial-gradient(circle, rgba(244,114,182,.1), transparent); top: 55%; left: 5%; animation-delay: -4s; }
  @keyframes drift {
    from { transform: translate(0, 0) scale(1); }
    to { transform: translate(35px, 55px) scale(1.1); }
  }

  /* ---------- GRAIN TEXTURE ---------- */
  body::after {
    content: '';
    position: fixed;
    inset: 0;
    z-index: 2;
    pointer-events: none;
    opacity: 0.45;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.028'/%3E%3C/svg%3E");
  }

  /* ---------- MAIN LAYOUT ---------- */
  #root { position: relative; z-index: 3; }
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 clamp(1.2rem, 5vw, 3.5rem);
  }

  /* ---------- NAVIGATION ---------- */
  #nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999;
    padding: 0.9rem 0;
    background: rgba(2, 4, 14, 0.68);
    backdrop-filter: blur(18px);
    border-bottom: 1px solid rgba(94, 243, 255, 0.06);
    transition: all 0.3s ease;
  }
  #nav.scrolled {
    background: rgba(2, 4, 14, 0.92);
    border-bottom-color: rgba(94, 243, 255, 0.18);
    backdrop-filter: blur(24px);
  }
  .nav-inner {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 clamp(1.2rem, 5vw, 3.5rem);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .logo {
    font-family: var(--H);
    font-weight: 900;
    font-size: 0.95rem;
    letter-spacing: 3px;
    color: var(--text);
  }
  .logo em { color: var(--cyan); font-style: normal; }
  .nav-links {
    display: flex;
    align-items: center;
    gap: 2rem;
  }
  .nav-links a {
    font-family: var(--M);
    font-size: 0.6rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--muted);
    transition: color 0.2s;
    position: relative;
  }
  .nav-links a::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 0;
    height: 1px;
    background: var(--cyan);
    transition: width 0.3s;
  }
  .nav-links a:hover { color: var(--cyan); }
  .nav-links a:hover::after { width: 100%; }
  .live-badge {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.3rem 0.85rem;
    border: 1px solid rgba(52, 211, 153, 0.22);
    border-radius: 99px;
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--green);
    background: rgba(52, 211, 153, 0.06);
    transition: all 0.2s;
  }
  .live-badge:hover {
    background: rgba(52, 211, 153, 0.12);
    border-color: rgba(52, 211, 153, 0.4);
  }
  .pulse-dot {
    width: 6px;
    height: 6px;
    background: var(--green);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--green);
    animation: pulse 1.8s ease-in-out infinite;
  }
  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.3; transform: scale(0.7); }
  }

  /* ---------- HERO SECTION ---------- */
  #hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 8rem 0 5rem;
  }
  .hero-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 4rem;
    align-items: center;
  }
  .coord {
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--cyan);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 1.4rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
    opacity: 0;
    animation: fadeUp 0.8s ease forwards 0.15s;
  }
  .coord::before {
    content: '';
    width: 40px;
    height: 1px;
    background: linear-gradient(90deg, var(--cyan), transparent);
  }
  h1 {
    font-family: var(--H);
    font-weight: 900;
    text-transform: uppercase;
    font-size: clamp(2.6rem, 6.5vw, 5.2rem);
    line-height: 1.04;
    letter-spacing: -1px;
    margin-bottom: 1.2rem;
    opacity: 0;
    animation: fadeUp 0.9s ease forwards 0.3s;
  }
  .glow-text { color: var(--cyan); text-shadow: 0 0 30px rgba(94, 243, 255, 0.35); }
  .role {
    font-family: var(--M);
    font-size: 0.7rem;
    color: var(--gold);
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 1.8rem;
    opacity: 0;
    animation: fadeUp 0.9s ease forwards 0.45s;
  }
  .role::before { content: '// '; color: var(--sub); }
  .desc {
    color: var(--muted);
    font-size: 0.95rem;
    line-height: 1.95;
    max-width: 520px;
    margin-bottom: 2.2rem;
    opacity: 0;
    animation: fadeUp 0.9s ease forwards 0.6s;
  }
  .desc strong { color: var(--text); font-weight: 600; }
  .hero-actions {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    opacity: 0;
    animation: fadeUp 0.9s ease forwards 0.75s;
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(28px); }
    to { opacity: 1; transform: none; }
  }

  /* ---------- BUTTONS (PROFESSIONAL) ---------- */
  .btn {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    padding: 0.78rem 1.6rem;
    border-radius: 4px;
    font-family: var(--M);
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
  }
  .btn-primary {
    background: linear-gradient(135deg, var(--cyan), #26c6da);
    color: #000;
    box-shadow: 0 4px 24px rgba(94, 243, 255, 0.2);
    position: relative;
    overflow: hidden;
  }
  .btn-primary::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, transparent, rgba(255, 255, 255, 0.28), transparent);
    transform: translateX(-100%);
    transition: transform 0.55s ease;
  }
  .btn-primary:hover { transform: translateY(-3px); box-shadow: 0 8px 36px rgba(94, 243, 255, 0.35); }
  .btn-primary:hover::before { transform: translateX(100%); }
  .btn-ghost {
    border: 1px solid var(--bd2);
    color: var(--muted);
    background: rgba(94, 243, 255, 0.03);
  }
  .btn-ghost:hover { border-color: var(--cyan); color: var(--cyan); background: rgba(94, 243, 255, 0.08); transform: translateY(-3px); }
  .btn-resume {
    border: 1px solid rgba(255, 201, 77, 0.25);
    color: var(--gold);
    background: rgba(255, 201, 77, 0.04);
  }
  .btn-resume:hover { border-color: var(--gold); background: rgba(255, 201, 77, 0.1); transform: translateY(-3px); }

  /* ---------- 3D ORBIT SCENE ---------- */
  .scene {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0;
    animation: fadeUp 1s ease forwards 0.5s;
  }
  .orbit-card {
    width: 100%;
    max-width: 420px;
    min-height: 500px;
    border: 1px solid var(--bd);
    border-radius: 32px;
    background: linear-gradient(160deg, rgba(10, 16, 42, 0.92), rgba(4, 8, 22, 0.8));
    position: relative;
    overflow: hidden;
    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(2px);
  }
  .orbit-ring {
    position: absolute;
    border: 1px dashed rgba(94, 243, 255, 0.12);
    border-radius: 50%;
    top: 50%;
    left: 50%;
  }
  .ring1 { width: 380px; height: 380px; margin: -190px 0 0 -190px; animation: spin 60s linear infinite; }
  .ring2 { width: 260px; height: 260px; margin: -130px 0 0 -130px; animation: spin 40s linear infinite reverse; }
  .ring3 { width: 160px; height: 160px; margin: -80px 0 0 -80px; animation: spin 25s linear infinite; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .orbit-dot {
    position: absolute;
    border-radius: 50%;
    top: 0;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .dot1 { width: 7px; height: 7px; background: var(--cyan); box-shadow: 0 0 14px var(--cyan); }
  .dot2 { width: 5px; height: 5px; background: var(--gold); box-shadow: 0 0 10px var(--gold); }
  .dot3 { width: 9px; height: 9px; background: var(--pink); box-shadow: 0 0 16px var(--pink); }
  .planet-core {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 88px;
    height: 88px;
    border-radius: 50%;
    transform: translate(-50%, -65%);
    background: radial-gradient(circle at 32% 28%, #9ecfff, #4a80d0 45%, #1a3a7a 80%, #0d1f44);
    box-shadow: 0 0 50px rgba(94, 163, 255, 0.3), inset -8px -8px 20px rgba(0, 0, 0, 0.35);
    animation: floatPlanet 4s ease-in-out infinite;
  }
  @keyframes floatPlanet {
    0%, 100% { transform: translate(-50%, -65%); }
    50% { transform: translate(-50%, -70%); }
  }
  .rocket-icon, .astro-icon { position: absolute; z-index: 5; filter: drop-shadow(0 0 18px rgba(94, 243, 255, 0.3)); }
  .rocket-icon { right: 28px; top: 28px; animation: rocketFloat 5s ease-in-out infinite; }
  .astro-icon { left: 50%; top: 60%; transform: translate(-50%, -10%); animation: astroFloat 6s ease-in-out infinite; }
  @keyframes rocketFloat {
    0%, 100% { transform: translateY(0) rotate(20deg); }
    50% { transform: translateY(-12px) rotate(15deg); }
  }
  @keyframes astroFloat {
    0%, 100% { transform: translate(-50%, -10%) rotate(-2deg); }
    50% { transform: translate(-50%, 2%) rotate(2deg); }
  }
  .stat-badge {
    position: absolute;
    bottom: 20px;
    left: 18px;
    right: 18px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    z-index: 6;
  }
  .stat-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 18px;
    padding: 1rem 1rem;
    transition: all 0.2s;
  }
  .stat-card:hover { background: rgba(255, 255, 255, 0.09); border-color: rgba(94, 243, 255, 0.2); transform: translateY(-2px); }
  .stat-label {
    font-family: var(--M);
    font-size: 0.55rem;
    color: var(--sub);
    text-transform: uppercase;
    letter-spacing: 1.5px;
  }
  .stat-value {
    font-size: 0.8rem;
    font-weight: 500;
    margin-top: 4px;
    color: var(--text);
  }

  /* SECTION HEADER */
  .section-header {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 2.8rem;
  }
  .sec-num {
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--cyan);
    letter-spacing: 2px;
  }
  .sec-title {
    font-family: var(--H);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
  }
  .sec-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--bd2), transparent);
  }

  /* STATS GRID */
  #stats { padding: 4rem 0; }
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: var(--bd);
    border: 1px solid var(--bd);
    border-radius: 12px;
    overflow: hidden;
  }
  .stat-item {
    background: var(--surf);
    padding: 2rem 1rem;
    text-align: center;
    transition: background 0.2s;
  }
  .stat-item:hover { background: var(--surf2); }
  .stat-number {
    font-family: var(--H);
    font-size: 2.3rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--cyan), var(--blue));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .stat-label2 {
    font-family: var(--M);
    font-size: 0.55rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* SKILLS */
  #skills { padding: 5rem 0; }
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.9rem;
  }
  .skill-card {
    border: 1px solid var(--bd);
    border-radius: 16px;
    padding: 1.6rem;
    background: var(--surf);
    transition: all 0.2s;
  }
  .skill-card:hover { border-color: rgba(94, 243, 255, 0.25); background: var(--surf2); }
  .skill-header {
    font-family: var(--M);
    font-size: 0.6rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--cyan);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }
  .chip-container { display: flex; flex-wrap: wrap; gap: 0.4rem; }
  .chip {
    padding: 0.25rem 0.7rem;
    border-radius: 40px;
    font-family: var(--M);
    font-size: 0.65rem;
    transition: 0.1s linear;
  }
  .chip:hover { transform: translateY(-2px); }
  .chip-cyan { background: rgba(94, 243, 255, 0.08); color: var(--cyan); border: 1px solid rgba(94, 243, 255, 0.2); }
  .chip-violet { background: rgba(167, 139, 250, 0.08); color: #c4b5fd; border: 1px solid rgba(167, 139, 250, 0.2); }
  .chip-blue { background: rgba(96, 165, 250, 0.08); color: #93c5fd; border: 1px solid rgba(96, 165, 250, 0.2); }
  .chip-green { background: rgba(52, 211, 153, 0.08); color: #6ee7b7; border: 1px solid rgba(52, 211, 153, 0.2); }

  /* PROJECTS (MISSIONS) */
  #missions { padding: 5rem 0; }
  .project-list { display: flex; flex-direction: column; }
  .project-row {
    display: grid;
    grid-template-columns: 72px 1fr;
    border-top: 1px solid var(--bd);
    padding: 2rem 0;
    transition: 0.2s;
  }
  .project-row:last-child { border-bottom: 1px solid var(--bd); }
  .project-meta { font-family: var(--M); font-size: 0.6rem; color: var(--sub); letter-spacing: 1px; }
  .project-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }
  .project-name {
    font-family: var(--H);
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--text);
  }
  .project-tag {
    padding: 0.2rem 0.65rem;
    border-radius: 40px;
    font-size: 0.55rem;
    font-family: var(--M);
    text-transform: uppercase;
    background: rgba(167, 139, 250, 0.1);
    color: #c4b5fd;
    border: 1px solid rgba(167, 139, 250, 0.2);
  }
  .project-desc {
    color: var(--muted);
    font-size: 0.85rem;
    line-height: 1.8;
    margin: 0.8rem 0;
  }
  .project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 0.6rem;
  }
  .tech-badge {
    font-family: var(--M);
    font-size: 0.6rem;
    padding: 0.15rem 0.6rem;
    border-radius: 40px;
    background: var(--surf);
    border: 1px solid var(--bd);
    color: var(--muted);
  }
  .project-link {
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--muted);
    transition: color 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
  }
  .project-link:hover { color: var(--cyan); }

  /* EXPERIENCE */
  #log { padding: 5rem 0; }
  .exp-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.2rem;
  }
  .exp-card {
    border: 1px solid var(--bd);
    border-radius: 20px;
    padding: 2rem;
    background: var(--surf);
    transition: 0.2s;
  }
  .exp-card:hover { border-color: rgba(94, 243, 255, 0.2); background: var(--surf2); }
  .exp-period {
    font-family: var(--M);
    font-size: 0.55rem;
    color: var(--cyan);
    letter-spacing: 1.5px;
    margin-bottom: 0.7rem;
  }
  .exp-title {
    font-family: var(--H);
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
  }
  .exp-org {
    font-family: var(--M);
    font-size: 0.7rem;
    color: var(--gold);
    margin-bottom: 1.2rem;
  }
  .exp-list { list-style: none; }
  .exp-list li {
    color: var(--muted);
    font-size: 0.82rem;
    line-height: 1.8;
    padding-left: 1.2rem;
    position: relative;
  }
  .exp-list li::before {
    content: '▹';
    position: absolute;
    left: 0;
    color: var(--cyan);
  }
  .status-badge {
    display: inline-flex;
    margin-top: 1rem;
    padding: 0.25rem 0.9rem;
    border-radius: 40px;
    font-family: var(--M);
    font-size: 0.55rem;
    gap: 0.4rem;
    align-items: center;
  }
  .badge-active { background: rgba(52, 211, 153, 0.08); border: 1px solid rgba(52, 211, 153, 0.2); color: var(--green); }

  /* CONTACT SECTION */
  #contact { padding: 5rem 0 8rem; }
  .contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
  }
  .contact-title {
    font-family: var(--H);
    font-size: clamp(1.9rem, 4vw, 2.8rem);
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 1.2rem;
  }
  .contact-title em { color: var(--cyan); font-style: normal; text-shadow: 0 0 25px rgba(94, 243, 255, 0.3); }
  .contact-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem;
  }
  .contact-card {
    border: 1px solid var(--bd);
    border-radius: 12px;
    padding: 1rem;
    background: var(--surf);
    transition: 0.2s;
  }
  .contact-card:hover { border-color: rgba(94, 243, 255, 0.2); background: var(--surf2); transform: translateY(-2px); }
  .contact-label {
    font-family: var(--M);
    font-size: 0.55rem;
    letter-spacing: 2px;
    color: var(--cyan);
    margin-bottom: 0.3rem;
  }
  .contact-value a { color: var(--muted); transition: 0.2s; }
  .contact-value a:hover { color: var(--cyan); }

  /* QUOTE */
  .quote-wrap {
    border-top: 1px solid var(--bd);
    padding: 5rem 0;
    text-align: center;
    position: relative;
  }
  .quote-mark {
    font-family: var(--H);
    font-size: 3rem;
    line-height: 1;
    color: var(--sub);
    display: block;
    margin-bottom: 1rem;
  }
  .quote-text {
    font-size: 1rem;
    line-height: 2.1;
    max-width: 600px;
    margin: 0 auto 1rem;
    color: var(--muted);
  }
  .quote-author {
    font-family: var(--M);
    font-size: 0.6rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--sub);
  }

  /* FOOTER */
  footer {
    border-top: 1px solid var(--bd);
    padding: 1.6rem 0;
  }
  .footer-inner {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 clamp(1.2rem, 5vw, 3.5rem);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .footer-copy {
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--sub);
  }
  .footer-links {
    display: flex;
    gap: 1.5rem;
  }
  .footer-links a {
    font-family: var(--M);
    font-size: 0.6rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--sub);
    transition: 0.2s;
  }
  .footer-links a:hover { color: var(--cyan); }

  /* REVEAL ANIMATION */
  .reveal {
    opacity: 0;
    transform: translateY(28px);
    transition: opacity 0.7s ease, transform 0.7s ease;
  }
  .reveal.in {
    opacity: 1;
    transform: none;
  }

  @media (max-width: 900px) {
    .hero-grid { grid-template-columns: 1fr; }
    .scene { display: none; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .skills-grid { grid-template-columns: 1fr; }
    .exp-grid { grid-template-columns: 1fr; }
    .contact-grid { grid-template-columns: 1fr; gap: 2rem; }
    .nav-links a:not(.live-badge) { display: none; }
  }
  @media (max-width: 560px) {
    .contact-cards { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<canvas id="cosmic-canvas"></canvas>
<div class="nebula nb1"></div>
<div class="nebula nb2"></div>
<div class="nebula nb3"></div>
<div class="nebula nb4"></div>

<div id="root">
  <!-- NAVIGATION -->
  <nav id="nav">
    <div class="nav-inner">
      <a href="#hero" class="logo">SHRAVAN<span style="color: #5ef3ff;">.</span></a>
      <div class="nav-links">
        <a href="#skills">Arsenal</a>
        <a href="#missions">Missions</a>
        <a href="#log">Flight Log</a>
        <a href="#contact">Transmit</a>
        <div class="live-badge"><div class="pulse-dot"></div> Signal Active</div>
      </div>
    </div>
  </nav>

  <!-- HERO SECTION -->
  <section id="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="coord">⏣ 19.0760°N · 72.8777°E · ORBIT ALT</div>
          <h1><span class="glow-text">Shravan</span><br>Parthe.</h1>
          <div class="role">Backend Engineer & AI Developer</div>
          <p class="desc"><strong>3rd year B.Tech CSE (AI&ML)</strong> building production‑grade systems in Java, Spring Boot, Python. Active mission at <strong>Innovexis</strong> — deploying real‑world Gen AI integrations. Every commit is a stage separation.</p>
          <div class="hero-actions">
            <a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">📡 Launch Contact</a>
            <a href="https://github.com/Shravan157" target="_blank" class="btn btn-ghost">⚡ GitHub</a>
            <a href="__RESUME_URL__" target="_blank" download="Shravan_Parthe_Resume.pdf" class="btn btn-resume">📄 Resume</a>
          </div>
        </div>
        <!-- 3D ORBIT SCENE -->
        <div class="scene">
          <div class="orbit-card">
            <div class="orbit-ring ring1"><div class="orbit-dot dot1"></div></div>
            <div class="orbit-ring ring2"><div class="orbit-dot dot2"></div></div>
            <div class="orbit-ring ring3"><div class="orbit-dot dot3"></div></div>
            <div class="planet-core"></div>
            <div class="rocket-icon">
              <svg width="52" viewBox="0 0 55 100" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="rb" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1e3a5f"/><stop offset="100%" stop-color="#0a1628"/></linearGradient><radialGradient id="rf" cx="50%" cy="0%"><stop offset="0%" stop-color="#5ef3ff"/><stop offset="50%" stop-color="#2979ff"/><stop offset="100%" stop-color="transparent"/></radialGradient></defs><ellipse cx="27.5" cy="86" rx="10" ry="18" fill="url(#rf)" opacity=".9"><animate attributeName="ry" values="18;22;15;20;18" dur=".32s" repeatCount="indefinite"/></ellipse><path d="M12 62 L2 80 L16 70 Z" fill="#1a3a6a"/><path d="M43 62 L53 80 L39 70 Z" fill="#1a3a6a"/><rect x="14" y="22" width="27" height="48" rx="6" fill="url(#rb)" stroke="#3d6080"/><path d="M14 27 Q27.5 4 41 27 Z" fill="#1a3a6a"/><circle cx="27.5" cy="50" r="7.5" fill="#0d2240" stroke="#5ef3ff" stroke-width="1.2"/><circle cx="27.5" cy="50" r="4.5" fill="#163560"/><circle cx="26" cy="48.5" r="1.5" fill="white" opacity=".2"/><line x1="27.5" y1="18" x2="27.5" y2="7" stroke="#5ef3ff" stroke-width="1.2" opacity=".7"/><circle cx="27.5" cy="5" r="3" fill="#5ef3ff" opacity=".85"><animate attributeName="opacity" values=".85;.3;.85" dur="1.1s" repeatCount="indefinite"/></circle></svg>
            </div>
            <div class="astro-icon">
              <svg width="140" viewBox="0 0 160 220" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="vg" cx="36%" cy="30%"><stop offset="0%" stop-color="#82b4ff"/><stop offset="100%" stop-color="#0d3a8a"/></radialGradient><radialGradient id="sg2" cx="33%" cy="28%"><stop offset="0%" stop-color="#1e2a3e"/><stop offset="100%" stop-color="#07101e"/></radialGradient></defs><ellipse cx="80" cy="67" rx="44" ry="48" fill="url(#sg2)" stroke="#44607a" stroke-width="1.5"/><ellipse cx="80" cy="70" rx="30" ry="32" fill="url(#vg)" stroke="#2979ff" stroke-width="1"/><circle cx="76" cy="72" r="1.2" fill="#5ef3ff" opacity=".7"/><circle cx="86" cy="66" r="1" fill="#5ef3ff" opacity=".6"/><path d="M39 60 Q80 44 121 60" stroke="#5ef3ff" stroke-width="1" fill="none" opacity=".4"/><circle cx="80" cy="130" r="14" fill="none" stroke="#5ef3ff" stroke-width="1.2" opacity=".5"/><text x="80" y="135" text-anchor="middle" fill="#5ef3ff" font-size="8" font-family="Orbitron" font-weight="700">SP</text><line x1="80" y1="19" x2="80" y2="8" stroke="#5ef3ff" stroke-width="1" opacity=".7"/><circle cx="80" cy="5" r="3" fill="#5ef3ff" opacity=".85"><animate attributeName="opacity" values=".85;.25;.85" dur="1.3s" repeatCount="indefinite"/></circle></svg>
            </div>
            <div class="stat-badge">
              <div class="stat-card"><div class="stat-label">Trajectory</div><div class="stat-value">Backend + AI · Real‑world Gen AI</div></div>
              <div class="stat-card"><div class="stat-label">Status</div><div class="stat-value">Building, shipping, iterating</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- STATS SECTION -->
  <section id="stats">
    <div class="container">
      <div class="stats-grid reveal">
        <div class="stat-item"><div class="stat-number">6+</div><div class="stat-label2">Missions</div></div>
        <div class="stat-item"><div class="stat-number">7.5</div><div class="stat-label2">CGPA</div></div>
        <div class="stat-item"><div class="stat-number">3rd</div><div class="stat-label2">Year</div></div>
        <div class="stat-item"><div class="stat-number">2027</div><div class="stat-label2">Graduation</div></div>
      </div>
    </div>
  </section>

  <!-- SKILLS (ARSENAL) -->
  <section id="skills">
    <div class="container">
      <div class="section-header reveal"><span class="sec-num">01</span> <span class="sec-title">TECH ARSENAL</span><div class="sec-line"></div></div>
      <div class="skills-grid reveal">
        <div class="skill-card"><div class="skill-header">⌨️ Languages</div><div class="chip-container"><span class="chip chip-cyan">Java</span><span class="chip chip-cyan">Python</span><span class="chip chip-cyan">JavaScript</span><span class="chip chip-cyan">Dart</span><span class="chip chip-cyan">SQL</span></div></div>
        <div class="skill-card"><div class="skill-header">⚙️ Frameworks</div><div class="chip-container"><span class="chip chip-violet">Spring Boot</span><span class="chip chip-violet">React</span><span class="chip chip-violet">Flutter</span><span class="chip chip-violet">FastAPI</span><span class="chip chip-violet">Spring AI</span></div></div>
        <div class="skill-card"><div class="skill-header">🛠️ Tools & Libs</div><div class="chip-container"><span class="chip chip-blue">Docker</span><span class="chip chip-blue">GitHub</span><span class="chip chip-blue">NumPy</span><span class="chip chip-blue">Pandas</span><span class="chip chip-blue">Scikit-learn</span><span class="chip chip-blue">NLTK</span></div></div>
        <div class="skill-card"><div class="skill-header">🗄️ Databases</div><div class="chip-container"><span class="chip chip-green">MySQL</span><span class="chip chip-green">PostgreSQL</span><span class="chip chip-green">Firebase</span><span class="chip chip-green">Redis</span></div></div>
      </div>
    </div>
  </section>

  <!-- PROJECTS / MISSION LOG -->
  <section id="missions">
    <div class="container">
      <div class="section-header reveal"><span class="sec-num">02</span> <span class="sec-title">MISSION LOG</span><div class="sec-line"></div></div>
      <div class="project-list reveal">
        <div class="project-row"><div class="project-meta">M-01</div><div><div class="project-header"><div class="project-name">MedoraX AI — Clinical Assistant</div><div class="project-tag">Healthcare AI</div></div><div class="project-desc">Multimodal clinical assistant with voice, image, text. Transcribes symptoms, analyzes medical images, generates structured diagnostics. Multilingual with GPS hospital finder.</div><div class="project-tech"><span class="tech-badge">Python</span><span class="tech-badge">Gradio</span><span class="tech-badge">Groq API</span></div><div><a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="project-link">GitHub ↗</a></div></div></div>
        <div class="project-row"><div class="project-meta">M-02</div><div><div class="project-header"><div class="project-name">SahayLoan — Micro‑Loan Platform</div><div class="project-tag">FinTech</div></div><div class="project-desc">Full‑stack lending platform with Flutter frontend, FastAPI backend, AI credit scoring (Random Forest), KYC OCR, Stripe EMI integration.</div><div class="project-tech"><span class="tech-badge">Flutter</span><span class="tech-badge">FastAPI</span><span class="tech-badge">Scikit-learn</span></div><div><a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="project-link">GitHub ↗</a></div></div></div>
        <div class="project-row"><div class="project-meta">M-03</div><div><div class="project-header"><div class="project-name">SikshaSetu — Rural Education</div><div class="project-tag">Full‑Stack</div></div><div class="project-desc">Education platform bridging digital divide. Spring Security + JWT/OAuth 2.0, optimized schema, React + ZEGOCLOUD for virtual classrooms.</div><div class="project-tech"><span class="tech-badge">React</span><span class="tech-badge">Spring Boot</span><span class="tech-badge">MySQL</span></div><div><a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="project-link">GitHub ↗</a></div></div></div>
        <div class="project-row"><div class="project-meta">M-04</div><div><div class="project-header"><div class="project-name">AI E‑Commerce Backend</div><div class="project-tag">AI/Full‑Stack</div></div><div class="project-desc">Intelligent backend with AI recommendations using Spring AI + Redis Vector DB, GenAI chatbot, image generation pipeline, JWT secured.</div><div class="project-tech"><span class="tech-badge">Spring Boot</span><span class="tech-badge">Spring AI</span><span class="tech-badge">Redis</span></div><div><a href="https://github.com/Shravan157" target="_blank" class="project-link">GitHub ↗</a></div></div></div>
        <div class="project-row"><div class="project-meta">M-05</div><div><div class="project-header"><div class="project-name">Zomato Sentiment Analysis</div><div class="project-tag">ML/NLP</div></div><div class="project-desc">End‑to‑end NLP pipeline on 10k+ reviews: EDA, TF‑IDF, model comparison (Logistic Regression, Random Forest, Naive Bayes).</div><div class="project-tech"><span class="tech-badge">Python</span><span class="tech-badge">Scikit-learn</span><span class="tech-badge">NLTK</span></div><div><a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="project-link">GitHub ↗</a></div></div></div>
        <div class="project-row"><div class="project-meta">M-06</div><div><div class="project-header"><div class="project-name">PhonePe Insights</div><div class="project-tag">Data Engineering</div></div><div class="project-desc">ETL + dashboard for PhonePe data. MySQL backend with SQLAlchemy, interactive Streamlit dashboard, Plotly visualizations.</div><div class="project-tech"><span class="tech-badge">Streamlit</span><span class="tech-badge">MySQL</span><span class="tech-badge">Plotly</span></div><div><a href="https://github.com/Shravan157/phonepe-insights" target="_blank" class="project-link">GitHub ↗</a></div></div></div>
      </div>
    </div>
  </section>

  <!-- EXPERIENCE / FLIGHT LOG -->
  <section id="log">
    <div class="container">
      <div class="section-header reveal"><span class="sec-num">03</span> <span class="sec-title">FLIGHT RECORD</span><div class="sec-line"></div></div>
      <div class="exp-grid reveal">
        <div class="exp-card"><div class="exp-period">APR 2026 — PRESENT · REMOTE</div><div class="exp-title">Data Science with Gen AI Intern</div><div class="exp-org">Innovexis</div><ul class="exp-list"><li>Real‑world LLM & generative AI integrations</li><li>Python, NumPy, Pandas, Scikit‑learn for data analysis & models</li><li>Production‑level Gen AI workflows</li></ul><div class="status-badge badge-active"><div class="pulse-dot"></div> Active Mission</div></div>
        <div class="exp-card"><div class="exp-period">JUN 2023 — MAY 2027 (EXPECTED)</div><div class="exp-title">B.Tech, Computer Science (AI & ML)</div><div class="exp-org">ViMEET · University of Mumbai</div><ul class="exp-list"><li>Specialization in AI/ML, DSA, Cloud, Microservices</li><li>Production projects alongside rigorous coursework</li></ul><div class="status-badge" style="background:rgba(255,201,77,0.08); border-color:rgba(255,201,77,0.2); color:var(--gold);">CGPA 7.5 / 10.0</div></div>
      </div>
    </div>
  </section>

  <!-- CONTACT -->
  <section id="contact">
    <div class="container">
      <div class="section-header reveal"><span class="sec-num">04</span> <span class="sec-title">ESTABLISH CONTACT</span><div class="sec-line"></div></div>
      <div class="contact-grid reveal">
        <div><h2 class="contact-title">Ready to<br><em>Launch?</em></h2><p class="desc" style="margin-bottom: 1.8rem;">Open for SDE/AI internships, collaborations. Transmission line open.</p><div class="hero-actions"><a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">📡 Send Transmission</a><a href="__RESUME_URL__" target="_blank" download="Shravan_Parthe_Resume.pdf" class="btn btn-resume">📄 Download Resume</a></div></div>
        <div class="contact-cards"><div class="contact-card"><div class="contact-label">Email</div><div class="contact-value"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div></div><div class="contact-card"><div class="contact-label">Phone</div><div class="contact-value">+91 73858 13010</div></div><div class="contact-card"><div class="contact-label">LinkedIn</div><div class="contact-value"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div></div><div class="contact-card"><div class="contact-label">GitHub</div><div class="contact-value"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div></div><div class="contact-card" style="grid-column: span 2;"><div class="contact-label">Base of Operations</div><div class="contact-value">Mumbai, India · Earth · Solar System</div></div></div>
      </div>
    </div>
  </section>

  <!-- QUOTE (PROFESSIONAL & SPACE THEMED) -->
  <div class="container">
    <div class="quote-wrap reveal">
      <span class="quote-mark">“</span>
      <p class="quote-text">The best code is like a stable orbit — precise, efficient, and endlessly re‑usable.</p>
      <div class="quote-author">Shravan Parthe — Engineer & Explorer</div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer>
    <div class="footer-inner"><div class="footer-copy">Built by <a href="https://github.com/Shravan157">Shravan Parthe</a> · 2026 · Earth</div><div class="footer-links"><a href="https://github.com/Shravan157" target="_blank">GitHub</a><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn</a><a href="mailto:shravanparthe@gmail.com">Email</a></div></div>
  </footer>
</div>

<script>
  (function() {
    // STARFIELD + COSMIC DUST
    const canvas = document.getElementById('cosmic-canvas');
    let ctx = canvas.getContext('2d');
    let width = window.innerWidth, height = window.innerHeight;
    function resizeCanvas() { width = window.innerWidth; height = window.innerHeight; canvas.width = width; canvas.height = height; }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    
    const colors = ['#ffffff', '#ccd6f6', '#5ef3ff', '#ffd966', '#c4b5fd', '#93c5fd', '#6ee7b7'];
    let stars = [];
    for (let i = 0; i < 340; i++) {
      stars.push({ x: Math.random() * width, y: Math.random() * height, r: Math.random() * 1.8 + 0.2, a: Math.random(), spd: Math.random() * 0.008 + 0.002, phase: Math.random() * Math.PI * 2, col: colors[Math.floor(Math.random() * colors.length)] });
    }
    let meteors = [];
    function addMeteor() { if (meteors.length < 4) { meteors.push({ x: Math.random() * width * 0.7, y: Math.random() * height * 0.4, len: Math.random() * 130 + 50, speed: Math.random() * 8 + 6, alpha: 1, angle: Math.PI / 4 + (Math.random() - 0.5) * 0.6 }); } }
    setInterval(addMeteor, 2800);
    
    let dust = [];
    for (let d = 0; d < 70; d++) { dust.push({ x: Math.random() * width, y: Math.random() * height, r: Math.random() * 2.2 + 0.6, alpha: Math.random() * 0.15, vx: (Math.random() - 0.5) * 0.2, vy: (Math.random() - 0.5) * 0.2, col: ['#7c4dff','#2979ff','#5ef3ff','#f472b6'][Math.floor(Math.random()*4)] }); }
    
    function animate() {
      ctx.clearRect(0, 0, width, height);
      for (let p of dust) { p.x += p.vx; p.y += p.vy; if (p.x < 0) p.x = width; if (p.x > width) p.x = 0; if (p.y < 0) p.y = height; if (p.y > height) p.y = 0; ctx.save(); ctx.globalAlpha = p.alpha; ctx.fillStyle = p.col; ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI*2); ctx.fill(); ctx.restore(); }
      for (let s of stars) { s.phase += s.spd; s.a = 0.25 + 0.75 * (Math.sin(s.phase) * 0.5 + 0.5); ctx.save(); ctx.globalAlpha = s.a; ctx.fillStyle = s.col; ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI*2); ctx.fill(); if (s.r > 1.4 && s.a > 0.8) { ctx.globalAlpha = s.a * 0.3; ctx.strokeStyle = s.col; ctx.lineWidth = 0.5; ctx.beginPath(); ctx.moveTo(s.x - s.r * 3, s.y); ctx.lineTo(s.x + s.r * 3, s.y); ctx.moveTo(s.x, s.y - s.r * 3); ctx.lineTo(s.x, s.y + s.r * 3); ctx.stroke(); } ctx.restore(); }
      for (let i=meteors.length-1; i>=0; i--) { let m=meteors[i]; let dx=Math.cos(m.angle)*m.len, dy=Math.sin(m.angle)*m.len; let grad=ctx.createLinearGradient(m.x, m.y, m.x-dx, m.y-dy); grad.addColorStop(0, `rgba(94,243,255,${m.alpha})`); grad.addColorStop(0.4, `rgba(96,165,250,${m.alpha*0.6})`); grad.addColorStop(1, 'transparent'); ctx.save(); ctx.strokeStyle=grad; ctx.lineWidth=1.8; ctx.shadowBlur=6; ctx.shadowColor='#5ef3ff'; ctx.beginPath(); ctx.moveTo(m.x, m.y); ctx.lineTo(m.x-dx, m.y-dy); ctx.stroke(); ctx.restore(); m.x += m.speed * Math.cos(m.angle); m.y += m.speed * Math.sin(m.angle); m.alpha -= 0.012; if (m.alpha <= 0 || m.x > width || m.y > height) meteors.splice(i,1); }
      requestAnimationFrame(animate);
    }
    animate();

    // SCROLL REVEAL
    const observer = new IntersectionObserver(entries => { entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); observer.unobserve(e.target); } }); }, { threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    
    // NAV SCROLL EFFECT
    const nav = document.getElementById('nav');
    window.addEventListener('scroll', () => { if (window.scrollY > 60) nav.classList.add('scrolled'); else nav.classList.remove('scrolled'); });
    
    // SMOOTH SCROLL INTERNAL
    document.querySelectorAll('a[href^="#"]').forEach(anchor => { anchor.addEventListener('click', function(e) { let target = document.querySelector(this.getAttribute('href')); if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); } }); });
  })();
</script>
</body>
</html>"""

# Replace placeholder with actual resume URL
html_final = HTML_TEMPLATE.replace("__RESUME_URL__", RESUME_URL)

# Render the HTML portfolio inside Streamlit
components.html(html_final, height=6800, scrolling=True)
