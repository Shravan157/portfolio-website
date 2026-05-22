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
  .stApp { background: #fbfdfe !important; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { border: none !important; display: block !important; }
  section[data-testid="stAppViewContainer"] > div { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

RESUME_URL = "https://raw.githubusercontent.com/Shravan157/portfolio-website/master/resume_shravan2.pdf"

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Shravan Parthe - Backend & AI Developer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Clash+Display:wght@400;500;600;700&family=Bricolage+Grotesque:opsz,wght@12..96,300;12..96,400;12..96,500;12..96,600;12..96,700&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; font-size: 16px; }
  
  :root {
    /* Light theme — clean, modern, recruiter-friendly */
    --bg: #fbfdfe;
    --bg1: #ffffff;
    --bg2: #f1f5f9;
    --bg3: rgba(0, 0, 0, 0.02);
    --bg4: rgba(0, 0, 0, 0.04);
    --bd: #e2e8f0;
    --bd2: #cbd5e1;
    --bd3: #94a3b8;
    --text: #0f172a;
    --text2: #334155;
    --text3: #64748b;
    --accent: #4f46e5;
    --accent2: #6366f1;
    --accent3: rgba(79, 70, 229, 0.08);
    --accent4: rgba(79, 70, 229, 0.16);
    --gold: #d97706;
    --gold2: rgba(217, 119, 6, 0.08);
    --green: #059669;
    --green2: rgba(5, 150, 105, 0.08);
    --H: 'Clash Display', sans-serif;
    --B: 'Bricolage Grotesque', sans-serif;
    --M: 'JetBrains Mono', monospace;
    --r: 8px;
    --r2: 12px;
    --r3: 16px;
  }
  
  body {
    font-family: var(--B);
    background: var(--bg);
    color: var(--text);
    line-height: 1.5;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
  }
  
  ::selection { background: var(--accent3); color: var(--accent); }
  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: var(--bd); }
  ::-webkit-scrollbar-thumb { background: var(--accent2); border-radius: 99px; }
  
  a { color: inherit; text-decoration: none; }
  
  /* subtle noise (barely visible) */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    opacity: 0.2;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.012'/%3E%3C/svg%3E");
  }
  
  /* light ambient orbs */
  .glow-orb {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    filter: blur(80px);
    opacity: 0.3;
  }
  .g1 { width: 500px; height: 500px; background: radial-gradient(circle, rgba(99,102,241,0.12), transparent); top: -150px; left: -150px; }
  .g2 { width: 450px; height: 450px; background: radial-gradient(circle, rgba(5,150,105,0.08), transparent); bottom: -100px; right: -100px; }
  .g3 { width: 400px; height: 400px; background: radial-gradient(circle, rgba(217,119,6,0.06), transparent); top: 40%; right: 10%; }
  
  #root { position: relative; z-index: 2; }
  .container {
    max-width: 1120px;
    margin: 0 auto;
    padding: 0 clamp(1rem, 4vw, 2.5rem);
  }
  
  /* ---------- NAVIGATION ---------- */
  #nav {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(251, 253, 254, 0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--bd);
    padding: 0.75rem 0;
  }
  .nav-inner {
    max-width: 1120px;
    margin: 0 auto;
    padding: 0 clamp(1rem, 4vw, 2.5rem);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .logo {
    font-family: var(--H);
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: -0.3px;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .logo-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--accent);
  }
  .nav-links {
    display: flex;
    align-items: center;
    gap: 0.2rem;
  }
  .nav-links a {
    font-family: var(--M);
    font-size: 0.7rem;
    letter-spacing: 0.3px;
    color: var(--text2);
    padding: 0.45rem 0.9rem;
    border-radius: var(--r);
    transition: all 0.2s;
  }
  .nav-links a:hover {
    color: var(--text);
    background: var(--bg3);
  }
  .nav-cta {
    background: var(--accent3);
    border: 1px solid var(--accent4);
    color: var(--accent) !important;
    border-radius: var(--r) !important;
  }
  .nav-cta:hover {
    background: var(--accent4) !important;
    color: var(--accent2) !important;
  }
  
  /* ---------- HERO (compact, no full viewport) ---------- */
  #hero {
    padding: 3rem 0 2rem;
  }
  .hero-grid {
    display: grid;
    grid-template-columns: 1fr 400px;
    gap: 3rem;
    align-items: center;
  }
  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-family: var(--M);
    font-size: 0.68rem;
    color: var(--accent);
    background: var(--accent3);
    border: 1px solid var(--accent4);
    padding: 0.28rem 0.85rem;
    border-radius: 99px;
    margin-bottom: 1.2rem;
  }
  .eyebrow-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--green);
    animation: pulse 2s infinite;
  }
  @keyframes pulse { 0%,100%{opacity:1}50%{opacity:0.4} }
  
  h1 {
    font-family: var(--H);
    font-weight: 700;
    font-size: clamp(2.8rem, 6vw, 4.6rem);
    line-height: 1.05;
    letter-spacing: -1.5px;
    margin-bottom: 1rem;
  }
  .ht-name { color: var(--text); }
  .ht-line { color: var(--text3); font-weight: 500; }
  .ht-accent {
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .role {
    font-family: var(--M);
    font-size: 0.75rem;
    color: var(--text3);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
  }
  .role-bar {
    display: inline-block;
    width: 28px;
    height: 1px;
    background: var(--accent);
    margin-right: 0.7rem;
    vertical-align: middle;
  }
  .desc {
    font-size: 0.95rem;
    color: var(--text2);
    line-height: 1.7;
    max-width: 500px;
    margin-bottom: 1.8rem;
  }
  .desc strong {
    color: var(--text);
    font-weight: 600;
  }
  .hero-actions {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
  }
  
  /* Buttons */
  .btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.7rem 1.4rem;
    border-radius: var(--r);
    font-family: var(--M);
    font-size: 0.68rem;
    font-weight: 500;
    transition: all 0.2s;
    cursor: pointer;
  }
  .btn-primary {
    background: var(--accent);
    color: white;
    box-shadow: 0 2px 8px rgba(79, 70, 229, 0.2);
  }
  .btn-primary:hover {
    background: #4338ca;
    transform: translateY(-2px);
  }
  .btn-ghost {
    border: 1px solid var(--bd2);
    color: var(--text2);
    background: transparent;
  }
  .btn-ghost:hover {
    border-color: var(--accent2);
    color: var(--accent);
    background: var(--accent3);
  }
  .btn-outline {
    border: 1px solid var(--gold2);
    color: var(--gold);
    background: var(--gold2);
  }
  .btn-outline:hover {
    border-color: var(--gold);
    background: rgba(217, 119, 6, 0.12);
  }
  
  /* Code card (light mode) */
  .code-card {
    background: var(--bg1);
    border: 1px solid var(--bd);
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.04);
    transition: all 0.2s;
  }
  .code-card:hover {
    box-shadow: 0 20px 35px rgba(0, 0, 0, 0.08);
  }
  .card-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding-bottom: 1rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid var(--bd);
  }
  .dots {
    display: flex;
    gap: 0.35rem;
  }
  .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }
  .d1 { background: #ef4444; }
  .d2 { background: #f59e0b; }
  .d3 { background: #10b981; }
  .card-title {
    font-family: var(--M);
    font-size: 0.65rem;
    color: var(--text3);
    margin-left: 0.4rem;
  }
  .code-block {
    font-family: var(--M);
    font-size: 0.72rem;
    line-height: 1.8;
  }
  .line {
    display: flex;
    gap: 0.75rem;
    align-items: baseline;
  }
  .ln {
    color: var(--text3);
    font-size: 0.6rem;
    min-width: 1.2rem;
    text-align: right;
  }
  .kw { color: #4f46e5; }
  .str { color: #059669; }
  .cm { color: var(--text3); font-style: italic; }
  .fn { color: #7c3aed; }
  .pr { color: #d97706; }
  .blink {
    display: inline-block;
    width: 2px;
    height: 0.85em;
    background: var(--accent);
    animation: blinkCursor 0.9s step-end infinite;
  }
  @keyframes blinkCursor { 0%,100%{opacity:1} 50%{opacity:0} }
  
  .card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 1.2rem;
    padding-top: 1rem;
    border-top: 1px solid var(--bd);
  }
  .tag {
    font-family: var(--M);
    font-size: 0.6rem;
    padding: 0.2rem 0.7rem;
    border-radius: 40px;
    border: 1px solid var(--bd);
    background: var(--bg3);
    color: var(--text2);
  }
  
  /* Stats bar */
  #stats {
    padding: 2rem 0 3rem;
  }
  .stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border: 1px solid var(--bd);
    border-radius: var(--r2);
    overflow: hidden;
    background: var(--bg1);
  }
  .stat-item {
    padding: 1.5rem 1rem;
    text-align: center;
    border-right: 1px solid var(--bd);
    transition: background 0.2s;
  }
  .stat-item:last-child { border-right: none; }
  .stat-item:hover { background: var(--bg2); }
  .stat-num {
    font-family: var(--H);
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.2;
  }
  .stat-label {
    font-family: var(--M);
    font-size: 0.6rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--text3);
  }
  
  /* Section headers */
  .section-header {
    margin-bottom: 2rem;
  }
  .section-top {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 0.5rem;
  }
  .section-idx {
    font-family: var(--M);
    font-size: 0.65rem;
    color: var(--accent2);
  }
  .section-line {
    flex: 1;
    height: 1px;
    background: var(--bd);
  }
  .section-title {
    font-family: var(--H);
    font-size: 1.6rem;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-bottom: 0.2rem;
  }
  .section-sub {
    color: var(--text2);
    font-size: 0.85rem;
  }
  
  /* Skills grid */
  #skills { padding: 3rem 0; }
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
  }
  .skill-card {
    border: 1px solid var(--bd);
    border-radius: var(--r2);
    padding: 1.2rem;
    background: var(--bg1);
    transition: all 0.2s;
  }
  .skill-card:hover {
    border-color: var(--accent4);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
  }
  .skill-label {
    font-family: var(--M);
    font-size: 0.6rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.8rem;
  }
  .chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }
  .chip {
    font-family: var(--M);
    font-size: 0.68rem;
    padding: 0.2rem 0.7rem;
    border-radius: 40px;
    border: 1px solid var(--bd2);
    background: var(--bg3);
    color: var(--text2);
    transition: all 0.1s;
  }
  .chip:hover {
    transform: translateY(-1px);
    border-color: var(--accent2);
    background: var(--accent3);
  }
  
  /* Projects */
  #projects { padding: 3rem 0; }
  .project-list { display: flex; flex-direction: column; }
  .project-row {
    display: grid;
    grid-template-columns: 60px 1fr auto;
    gap: 1.2rem;
    padding: 1.5rem 0;
    border-bottom: 1px solid var(--bd);
    align-items: start;
  }
  .project-row:first-child { border-top: 1px solid var(--bd); }
  .project-idx {
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--text3);
    padding-top: 0.2rem;
  }
  .project-title {
    font-family: var(--H);
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.3rem;
  }
  .project-desc {
    font-size: 0.85rem;
    color: var(--text2);
    line-height: 1.6;
    margin-bottom: 0.6rem;
  }
  .project-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
  }
  .stack-badge {
    font-family: var(--M);
    font-size: 0.58rem;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    border: 1px solid var(--bd);
    color: var(--text3);
  }
  .project-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 0.5rem;
  }
  .project-tag {
    font-family: var(--M);
    font-size: 0.58rem;
    padding: 0.2rem 0.7rem;
    border-radius: 99px;
    background: var(--accent3);
    color: var(--accent);
    border: 1px solid var(--accent4);
    white-space: nowrap;
  }
  .project-link {
    display: inline-flex;
    align-items: center;
    gap: 0.2rem;
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--text3);
    transition: color 0.2s;
  }
  .project-link:hover { color: var(--accent); }
  
  /* Experience */
  #experience { padding: 3rem 0; }
  .exp-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.9rem;
  }
  .exp-card {
    border: 1px solid var(--bd);
    border-radius: var(--r2);
    padding: 1.5rem;
    background: var(--bg1);
    transition: all 0.2s;
  }
  .exp-card:hover {
    border-color: var(--accent4);
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.04);
  }
  .exp-period {
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--text3);
    margin-bottom: 0.6rem;
  }
  .exp-role {
    font-family: var(--H);
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
  }
  .exp-company {
    font-family: var(--M);
    font-size: 0.7rem;
    color: var(--gold);
    margin-bottom: 1rem;
  }
  .exp-list {
    list-style: none;
  }
  .exp-list li {
    font-size: 0.85rem;
    color: var(--text2);
    line-height: 1.6;
    padding-left: 1.1rem;
    position: relative;
    margin-bottom: 0.2rem;
  }
  .exp-list li::before {
    content: '▹';
    position: absolute;
    left: 0;
    color: var(--accent);
  }
  .exp-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    margin-top: 1rem;
    padding: 0.2rem 0.8rem;
    border-radius: 99px;
    font-family: var(--M);
    font-size: 0.6rem;
  }
  .pill-green {
    background: var(--green2);
    color: var(--green);
    border: 1px solid rgba(5,150,105,0.2);
  }
  .pill-amber {
    background: var(--gold2);
    color: var(--gold);
    border: 1px solid rgba(217,119,6,0.2);
  }
  .pulse-dot {
    width: 6px;
    height: 6px;
    background: var(--green);
    border-radius: 50%;
    animation: pulse 2s infinite;
  }
  
  /* Contact */
  #contact { padding: 3rem 0 4rem; }
  .contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
  }
  .contact-title {
    font-family: var(--H);
    font-size: clamp(1.6rem, 3.5vw, 2.2rem);
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1rem;
  }
  .contact-title span {
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .contact-sub {
    color: var(--text2);
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
  }
  .contact-links {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
  }
  .contact-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.9rem 1.2rem;
    border: 1px solid var(--bd);
    border-radius: var(--r2);
    background: var(--bg1);
    transition: all 0.2s;
  }
  .contact-card:hover {
    border-color: var(--accent4);
    background: var(--bg2);
    transform: translateX(4px);
  }
  .contact-left {
    display: flex;
    align-items: center;
    gap: 0.8rem;
  }
  .contact-icon {
    width: 34px;
    height: 34px;
    border-radius: var(--r);
    background: var(--bg3);
    border: 1px solid var(--bd);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .contact-icon svg {
    width: 16px;
    height: 16px;
    stroke: var(--text3);
  }
  .contact-label {
    font-family: var(--M);
    font-size: 0.55rem;
    color: var(--text3);
    text-transform: uppercase;
  }
  .contact-value {
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--text);
  }
  .contact-arrow {
    color: var(--text3);
    font-size: 0.8rem;
  }
  
  /* Footer */
  footer {
    border-top: 1px solid var(--bd);
    padding: 1.2rem 0;
  }
  .footer-inner {
    max-width: 1120px;
    margin: 0 auto;
    padding: 0 clamp(1rem, 4vw, 2.5rem);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.8rem;
  }
  .footer-copy {
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--text3);
  }
  .footer-links {
    display: flex;
    gap: 1.2rem;
  }
  .footer-links a {
    font-family: var(--M);
    font-size: 0.6rem;
    color: var(--text3);
  }
  .footer-links a:hover { color: var(--accent); }
  
  /* reveal animation */
  .reveal {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  .reveal.in {
    opacity: 1;
    transform: none;
  }
  
  /* Responsive */
  @media (max-width: 850px) {
    .hero-grid { grid-template-columns: 1fr; gap: 2rem; }
    .code-card { max-width: 500px; margin: 0 auto; }
    .stats-row { grid-template-columns: repeat(2, 1fr); }
    .stat-item:nth-child(2) { border-right: none; }
    .skills-grid { grid-template-columns: 1fr; }
    .exp-grid { grid-template-columns: 1fr; }
    .contact-grid { grid-template-columns: 1fr; gap: 2rem; }
    .project-row { grid-template-columns: 48px 1fr; }
    .project-right { display: none; }
    .nav-links a:not(.nav-cta) { display: none; }
  }
  @media (max-width: 550px) {
    .stats-row { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>

<div class="glow-orb g1"></div>
<div class="glow-orb g2"></div>
<div class="glow-orb g3"></div>

<div id="root">
  <!-- Navigation -->
  <nav id="nav">
    <div class="nav-inner">
      <a href="#hero" class="logo">
        <div class="logo-dot"></div>
        Shravan Parthe
      </a>
      <div class="nav-links">
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#experience">Experience</a>
        <a href="#contact" class="nav-cta">Contact</a>
      </div>
    </div>
  </nav>

  <!-- Hero Section (compact, no full viewport) -->
  <section id="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <div class="eyebrow">
            <div class="eyebrow-dot"></div>
            Available for internships & collaborations
          </div>
          <h1>
            <span class="ht-name">Shravan</span><br>
            <span class="ht-line">Parthe<span class="ht-accent">.</span></span>
          </h1>
          <div class="role">
            <span class="role-bar"></span>
            Backend & AI Developer · B.Tech CSE AI/ML
          </div>
          <p class="desc">
            I build <strong>production-grade backends</strong> in Java & Spring Boot,
            cross-platform apps in Flutter, and integrate <strong>Gen AI</strong> into real systems.
            Currently interning at <strong>Innovexis</strong> — deploying ML pipelines to production.
          </p>
          <div class="hero-actions">
            <a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">📧 Get in Touch</a>
            <a href="https://github.com/Shravan157" target="_blank" class="btn btn-ghost">🐙 GitHub</a>
            <a href="https://raw.githubusercontent.com/Shravan157/portfolio-website/master/resume_shravan2.pdf" target="_blank" download class="btn btn-outline">📄 Resume</a>
          </div>
        </div>

        <!-- Code card (light theme) -->
        <div class="code-card">
          <div class="card-header">
            <div class="dots">
              <div class="dot d1"></div>
              <div class="dot d2"></div>
              <div class="dot d3"></div>
            </div>
            <span class="card-title">shravan.java</span>
          </div>
          <div class="code-block">
            <div class="line"><span class="ln">1</span><span class="cm">// Developer profile</span></div>
            <div class="line"><span class="ln">2</span><span class="kw">public class </span><span class="fn">Shravan</span> {</div>
            <div class="line"><span class="ln">3</span>&nbsp;</div>
            <div class="line"><span class="ln">4</span>&nbsp;&nbsp;<span class="kw">String</span> <span class="pr">name</span> = <span class="str">"Shravan Parthe"</span>;</div>
            <div class="line"><span class="ln">5</span>&nbsp;&nbsp;<span class="kw">String</span> <span class="pr">role</span> = <span class="str">"Backend + AI Dev"</span>;</div>
            <div class="line"><span class="ln">6</span>&nbsp;&nbsp;<span class="kw">int</span> <span class="pr">year</span> = <span class="str">3</span>;</div>
            <div class="line"><span class="ln">7</span>&nbsp;</div>
            <div class="line"><span class="ln">8</span>&nbsp;&nbsp;<span class="kw">String</span>[] <span class="pr">stack</span> = {</div>
            <div class="line"><span class="ln">9</span>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Java"</span>, <span class="str">"Spring Boot"</span>,</div>
            <div class="line"><span class="ln">10</span>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Python"</span>, <span class="str">"Flutter"</span>,</div>
            <div class="line"><span class="ln">11</span>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"FastAPI"</span>, <span class="str">"Spring AI"</span></div>
            <div class="line"><span class="ln">12</span>&nbsp;&nbsp;};</div>
            <div class="line"><span class="ln">13</span>&nbsp;</div>
            <div class="line"><span class="ln">14</span>&nbsp;&nbsp;<span class="fn">boolean</span> <span class="pr">openToWork</span> = <span class="str">true</span>;<span class="blink"></span></div>
            <div class="line"><span class="ln">15</span>}</div>
          </div>
          <div class="card-tags">
            <span class="tag">Java</span><span class="tag">Spring Boot</span><span class="tag">Python</span><span class="tag">Flutter</span><span class="tag">FastAPI</span><span class="tag">Spring AI</span><span class="tag">MySQL</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Stats -->
  <section id="stats">
    <div class="container">
      <div class="stats-row reveal">
        <div class="stat-item"><div class="stat-num">6+</div><div class="stat-label">Projects</div></div>
        <div class="stat-item"><div class="stat-num">7.5</div><div class="stat-label">CGPA</div></div>
        <div class="stat-item"><div class="stat-num">3rd</div><div class="stat-label">Year</div></div>
        <div class="stat-item"><div class="stat-num">2027</div><div class="stat-label">Graduation</div></div>
      </div>
    </div>
  </section>

  <!-- Skills -->
  <section id="skills">
    <div class="container">
      <div class="section-header reveal">
        <div class="section-top"><span class="section-idx">01</span><div class="section-line"></div></div>
        <div class="section-title">Tech Stack</div>
        <div class="section-sub">Languages, frameworks, and tools I use daily</div>
      </div>
      <div class="skills-grid reveal">
        <div class="skill-card"><div class="skill-label">Languages</div><div class="chips"><span class="chip">Java</span><span class="chip">Python</span><span class="chip">JavaScript</span><span class="chip">Dart</span><span class="chip">SQL</span></div></div>
        <div class="skill-card"><div class="skill-label">Frameworks</div><div class="chips"><span class="chip">Spring Boot</span><span class="chip">FastAPI</span><span class="chip">Flutter</span><span class="chip">React</span><span class="chip">Spring AI</span></div></div>
        <div class="skill-card"><div class="skill-label">ML / Data</div><div class="chips"><span class="chip">Scikit-learn</span><span class="chip">Pandas</span><span class="chip">NumPy</span><span class="chip">NLTK</span><span class="chip">TF-IDF</span></div></div>
        <div class="skill-card"><div class="skill-label">Infra & DB</div><div class="chips"><span class="chip">Docker</span><span class="chip">MySQL</span><span class="chip">PostgreSQL</span><span class="chip">Redis</span><span class="chip">Firebase</span></div></div>
      </div>
    </div>
  </section>

  <!-- Projects -->
  <section id="projects">
    <div class="container">
      <div class="section-header reveal">
        <div class="section-top"><span class="section-idx">02</span><div class="section-line"></div></div>
        <div class="section-title">Selected Work</div>
        <div class="section-sub">Production-grade projects from scratch</div>
      </div>
      <div class="project-list reveal">
        <div class="project-row"><div class="project-idx">01</div><div><div class="project-title">MedoraX AI — Clinical Assistant</div><div class="project-desc">Multimodal assistant with voice, image analysis, structured diagnostics. Whisper, Llama-4-scout, multilingual support.</div><div class="project-stack"><span class="stack-badge">Python</span><span class="stack-badge">Gradio</span><span class="stack-badge">Groq API</span></div></div><div class="project-right"><span class="project-tag">Healthcare AI</span><a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="project-link">GitHub ↗</a></div></div>
        <div class="project-row"><div class="project-idx">02</div><div><div class="project-title">SahayLoan — Micro-Lending</div><div class="project-desc">Flutter + FastAPI, Random Forest credit scoring, OCR KYC, Stripe EMI. Full-stack lending platform.</div><div class="project-stack"><span class="stack-badge">Flutter</span><span class="stack-badge">FastAPI</span><span class="stack-badge">Scikit-learn</span></div></div><div class="project-right"><span class="project-tag">FinTech</span><a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="project-link">GitHub ↗</a></div></div>
        <div class="project-row"><div class="project-idx">03</div><div><div class="project-title">SikshaSetu — Rural Education</div><div class="project-desc">Spring Boot + React, JWT/OAuth, role-based access, video SDK for virtual classrooms.</div><div class="project-stack"><span class="stack-badge">React</span><span class="stack-badge">Spring Boot</span><span class="stack-badge">MySQL</span></div></div><div class="project-right"><span class="project-tag">Full-Stack</span><a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="project-link">GitHub ↗</a></div></div>
        <div class="project-row"><div class="project-idx">04</div><div><div class="project-title">AI E-Commerce Backend</div><div class="project-desc">Spring AI + Redis Vector DB for recommendations, GenAI chatbot, JWT auth.</div><div class="project-stack"><span class="stack-badge">Spring Boot</span><span class="stack-badge">Spring AI</span><span class="stack-badge">Redis</span></div></div><div class="project-right"><span class="project-tag">AI/Full-Stack</span><a href="https://github.com/Shravan157" target="_blank" class="project-link">GitHub ↗</a></div></div>
        <div class="project-row"><div class="project-idx">05</div><div><div class="project-title">Zomato Sentiment Analysis</div><div class="project-desc">NLP pipeline on 10k+ reviews: EDA, TF-IDF, Logistic Regression (best F1).</div><div class="project-stack"><span class="stack-badge">Python</span><span class="stack-badge">Scikit-learn</span><span class="stack-badge">NLTK</span></div></div><div class="project-right"><span class="project-tag">ML/NLP</span><a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="project-link">GitHub ↗</a></div></div>
      </div>
    </div>
  </section>

  <!-- Experience -->
  <section id="experience">
    <div class="container">
      <div class="section-header reveal">
        <div class="section-top"><span class="section-idx">03</span><div class="section-line"></div></div>
        <div class="section-title">Experience & Education</div>
        <div class="section-sub">Where I've worked and what I'm studying</div>
      </div>
      <div class="exp-grid reveal">
        <div class="exp-card"><div class="exp-period">APR 2026 — PRESENT · REMOTE</div><div class="exp-role">Data Science with Gen AI Intern</div><div class="exp-company">Innovexis</div><ul class="exp-list"><li>Real-world LLM & generative AI integrations</li><li>Python, Pandas, Scikit-learn for data analysis & models</li><li>Production-level Gen AI workflows</li></ul><div class="exp-pill pill-green"><div class="pulse-dot"></div> Active Mission</div></div>
        <div class="exp-card"><div class="exp-period">JUN 2023 — MAY 2027 (EXPECTED)</div><div class="exp-role">B.Tech, Computer Science (AI & ML)</div><div class="exp-company">ViMEET · University of Mumbai</div><ul class="exp-list"><li>Specialization in AI/ML, DSA, Cloud, Microservices</li><li>Production projects alongside rigorous coursework</li></ul><div class="exp-pill pill-amber">CGPA 7.5 / 10.0</div></div>
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section id="contact">
    <div class="container">
      <div class="section-header reveal">
        <div class="section-top"><span class="section-idx">04</span><div class="section-line"></div></div>
        <div class="section-title">Let's Connect</div>
      </div>
      <div class="contact-grid reveal">
        <div><div class="contact-title">Open to <span>opportunities</span><br>and collaboration</div><p class="contact-sub">Looking for backend, mobile, or AI engineering internships. Also open to project collaborations. If you're building something interesting, let's talk.</p><div class="hero-actions"><a href="mailto:shravanparthe@gmail.com" class="btn btn-primary">Send a Message</a><a href="https://raw.githubusercontent.com/Shravan157/portfolio-website/master/resume_shravan2.pdf" target="_blank" download class="btn btn-outline">Download Resume</a></div></div>
        <div class="contact-links">
          <a href="mailto:shravanparthe@gmail.com" class="contact-card"><div class="contact-left"><div class="contact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg></div><div><div class="contact-label">Email</div><div class="contact-value">shravanparthe@gmail.com</div></div></div><span class="contact-arrow">↗</span></a>
          <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank" class="contact-card"><div class="contact-left"><div class="contact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></div><div><div class="contact-label">LinkedIn</div><div class="contact-value">Shravan Parthe</div></div></div><span class="contact-arrow">↗</span></a>
          <a href="https://github.com/Shravan157" target="_blank" class="contact-card"><div class="contact-left"><div class="contact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg></div><div><div class="contact-label">GitHub</div><div class="contact-value">Shravan157</div></div></div><span class="contact-arrow">↗</span></a>
          <div class="contact-card" style="cursor:default"><div class="contact-left"><div class="contact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div><div><div class="contact-label">Location</div><div class="contact-value">Nagpur, Maharashtra, India</div></div></div></div>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <div class="footer-inner"><div class="footer-copy">Built by Shravan Parthe · 2026</div><div class="footer-links"><a href="https://github.com/Shravan157" target="_blank">GitHub</a><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn</a><a href="mailto:shravanparthe@gmail.com">Email</a></div></div>
  </footer>
</div>

<script>
  (function() {
    // scroll reveal
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); observer.unobserve(e.target); } });
    }, { threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    // smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
      });
    });
  })();
</script>
</body>
</html>"""

components.html(HTML, height=3800, scrolling=True)
