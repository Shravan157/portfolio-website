<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Shravan Parthe — Backend Engineer & AI Developer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
/* ─── Design Tokens ─── */
:root {
  --parchment: #f5f4ed;
  --ivory: #faf9f5;
  --near-black: #141413;
  --dark-surface: #30302e;
  --terracotta: #c96442;
  --coral: #d97757;
  --olive-gray: #5e5d59;
  --stone-gray: #87867f;
  --charcoal-warm: #4d4c48;
  --warm-silver: #b0aea5;
  --border-cream: #f0eee6;
  --border-warm: #e8e6dc;
  --warm-sand: #e8e6dc;
  --muted-green: #6b7c5e;

  --serif: 'Playfair Display', Georgia, serif;
  --sans: 'DM Sans', Arial, sans-serif;
  --mono: 'DM Mono', 'Courier New', monospace;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-xl: 32px;
}

/* ─── Reset ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--parchment);
  color: var(--near-black);
  font-family: var(--sans);
  font-size: 16px;
  line-height: 1.6;
  overflow-x: hidden;
}

/* ─── Scrollbar ─── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--parchment); }
::-webkit-scrollbar-thumb { background: var(--border-warm); border-radius: 99px; }

/* ─── Nav ─── */
nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(245,244,237,0.92);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-cream);
  padding: 0 clamp(1.5rem, 5vw, 4rem);
}
.nav-inner {
  max-width: 1160px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between;
  height: 64px;
}
.nav-logo {
  font-family: var(--serif);
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--near-black);
  text-decoration: none;
  letter-spacing: -0.3px;
}
.nav-logo span { color: var(--terracotta); }
.nav-links { display: flex; gap: 2rem; align-items: center; }
.nav-links a {
  color: var(--olive-gray);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  transition: color 0.2s;
}
.nav-links a:hover { color: var(--near-black); }
.nav-cta {
  display: inline-flex; align-items: center; gap: 0.4rem;
  padding: 0.55rem 1.1rem;
  background: var(--terracotta);
  color: var(--ivory) !important;
  border-radius: var(--radius-md);
  font-size: 0.85rem; font-weight: 500;
  transition: opacity 0.2s;
}
.nav-cta:hover { opacity: 0.88; }
.nav-dot {
  width: 7px; height: 7px;
  background: #6ab187;
  border-radius: 50%;
  box-shadow: 0 0 7px #6ab187;
  animation: pulse 2.2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.5;transform:scale(.75)} }

/* ─── Container ─── */
.container { max-width: 1160px; margin: 0 auto; padding: 0 clamp(1.5rem, 5vw, 4rem); }

/* ─── Hero ─── */
.hero {
  background: var(--parchment);
  padding: 6rem 0 5rem;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute; top: 0; right: 0;
  width: 55%; height: 100%;
  background: radial-gradient(ellipse 70% 80% at 80% 40%, rgba(201,100,66,0.07) 0%, transparent 70%);
  pointer-events: none;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 5rem;
  align-items: center;
}
.hero-overline {
  display: inline-flex; align-items: center; gap: 0.5rem;
  font-size: 0.75rem; font-weight: 500;
  color: var(--terracotta);
  letter-spacing: 0.8px; text-transform: uppercase;
  margin-bottom: 1.5rem;
  font-family: var(--mono);
}
.hero-overline::before {
  content: '';
  width: 20px; height: 1px;
  background: var(--terracotta);
}
.hero-name {
  font-family: var(--serif);
  font-size: clamp(2.8rem, 5vw, 4rem);
  font-weight: 500;
  color: var(--near-black);
  line-height: 1.1;
  letter-spacing: -1px;
  margin-bottom: 0.5rem;
}
.hero-name em {
  font-style: italic;
  color: var(--terracotta);
}
.hero-role {
  font-family: var(--mono);
  font-size: 0.9rem;
  color: var(--stone-gray);
  margin-bottom: 1.75rem;
  letter-spacing: 0.3px;
}
.hero-desc {
  font-size: 1.05rem;
  color: var(--olive-gray);
  line-height: 1.75;
  max-width: 480px;
  margin-bottom: 2.5rem;
}
.hero-cta { display: flex; gap: 0.75rem; flex-wrap: wrap; }
.btn-terra {
  display: inline-flex; align-items: center; gap: 0.45rem;
  padding: 0.75rem 1.5rem;
  background: var(--terracotta);
  color: var(--ivory) !important;
  border-radius: var(--radius-md);
  font-size: 0.875rem; font-weight: 500;
  text-decoration: none;
  transition: all 0.2s;
  box-shadow: 0 0 0 1px var(--terracotta);
}
.btn-terra:hover { opacity: 0.88; transform: translateY(-1px); }
.btn-ghost {
  display: inline-flex; align-items: center; gap: 0.45rem;
  padding: 0.72rem 1.3rem;
  background: var(--warm-sand);
  color: var(--charcoal-warm) !important;
  border: 1px solid var(--border-warm);
  border-radius: var(--radius-md);
  font-size: 0.875rem; font-weight: 500;
  text-decoration: none;
  transition: all 0.2s;
  box-shadow: 0 0 0 1px #d1cfc5;
}
.btn-ghost:hover { background: var(--border-warm); color: var(--near-black) !important; }

/* ─── Hero Code Card ─── */
.hero-card {
  background: var(--near-black);
  border-radius: var(--radius-xl);
  border: 1px solid var(--dark-surface);
  overflow: hidden;
  box-shadow: rgba(0,0,0,0.18) 0px 12px 40px;
}
.card-topbar {
  display: flex; align-items: center; gap: 0.5rem;
  padding: 0.9rem 1.25rem;
  background: var(--dark-surface);
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.dot { width: 10px; height: 10px; border-radius: 50%; }
.dot-r { background: #ff5f56; }
.dot-y { background: #ffbd2e; }
.dot-g { background: #27c93f; box-shadow: 0 0 5px #27c93f; }
.card-filename {
  font-family: var(--mono); font-size: 0.7rem;
  color: var(--stone-gray); margin-left: auto;
}
.card-body { padding: 1.5rem 1.75rem; }
.code-line {
  font-family: var(--mono); font-size: 0.8rem;
  line-height: 1.95; white-space: pre;
}
.kw { color: #b794f4; }
.fn { color: #63b3ed; }
.st { color: #68d391; }
.cm { color: #4a5568; }
.nm { color: #fbd38d; }
.card-footer {
  display: flex; align-items: center; gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: rgba(255,255,255,0.025);
  border-top: 1px solid rgba(255,255,255,0.05);
}
.status-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: #68d391; box-shadow: 0 0 6px #68d391;
  animation: pulse 2s infinite;
}
.status-text { font-family: var(--mono); font-size: 0.68rem; color: #4a5568; }
.status-ok { color: #68d391; }

/* ─── Stats Strip ─── */
.stats-strip {
  background: var(--near-black);
  padding: 3rem 0;
}
.stats-grid {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--dark-surface);
  border: 1px solid var(--dark-surface);
  border-radius: var(--radius-lg);
  overflow: hidden;
}
.stat-item {
  background: var(--near-black);
  padding: 2rem 1.5rem;
  text-align: center;
  position: relative;
}
.stat-item::after {
  content: '';
  position: absolute; bottom: 0; left: 50%;
  transform: translateX(-50%);
  width: 0; height: 2px;
  background: var(--terracotta);
  transition: width 0.4s;
}
.stat-item:hover::after { width: 60%; }
.stat-num {
  font-family: var(--serif);
  font-size: 2.5rem; font-weight: 500;
  color: var(--ivory);
  line-height: 1;
  margin-bottom: 0.4rem;
}
.stat-label {
  font-size: 0.72rem; font-weight: 500;
  color: var(--stone-gray);
  text-transform: uppercase; letter-spacing: 1px;
  font-family: var(--mono);
}

/* ─── Section Header ─── */
.section-tag {
  display: inline-flex; align-items: center; gap: 0.5rem;
  font-family: var(--mono); font-size: 0.72rem;
  color: var(--terracotta); text-transform: uppercase; letter-spacing: 1px;
  margin-bottom: 1rem;
}
.section-tag::before { content: ''; width: 16px; height: 1px; background: var(--terracotta); }
.section-heading {
  font-family: var(--serif);
  font-size: clamp(1.8rem, 3.5vw, 2.5rem);
  font-weight: 500; line-height: 1.2;
  letter-spacing: -0.5px;
  color: var(--near-black);
  margin-bottom: 0.75rem;
}
.section-heading-light { color: var(--ivory); }
.section-sub {
  font-size: 1rem; color: var(--olive-gray);
  max-width: 440px; line-height: 1.65;
}
.section-sub-light { color: var(--warm-silver); }

/* ─── Skills Section ─── */
.skills-section { background: var(--parchment); padding: 6rem 0; }
.skills-layout { display: grid; grid-template-columns: 280px 1fr; gap: 5rem; align-items: start; }
.skills-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; }
.skill-group {
  background: var(--ivory);
  border: 1px solid var(--border-cream);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: rgba(0,0,0,0.04) 0 4px 20px;
  transition: box-shadow 0.25s, border-color 0.25s;
}
.skill-group:hover {
  box-shadow: rgba(0,0,0,0.08) 0 8px 28px;
  border-color: var(--border-warm);
}
.skill-group-title {
  font-family: var(--mono); font-size: 0.68rem;
  color: var(--stone-gray); text-transform: uppercase; letter-spacing: 1.2px;
  margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;
}
.skill-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.skill-chip {
  padding: 0.28rem 0.7rem;
  border-radius: 6px; font-size: 0.775rem; font-weight: 500;
  font-family: var(--mono);
  transition: transform 0.15s;
}
.skill-chip:hover { transform: translateY(-1px); }
.chip-terra { background: rgba(201,100,66,0.1); color: var(--terracotta); border: 1px solid rgba(201,100,66,0.2); }
.chip-olive { background: rgba(107,124,94,0.1); color: var(--muted-green); border: 1px solid rgba(107,124,94,0.2); }
.chip-stone { background: rgba(135,134,127,0.1); color: var(--charcoal-warm); border: 1px solid var(--border-warm); }
.chip-warm { background: rgba(78,76,72,0.08); color: var(--olive-gray); border: 1px solid var(--border-cream); }

/* ─── Projects Section ─── */
.projects-section { background: var(--near-black); padding: 6rem 0; }
.projects-grid { display: grid; gap: 1px; margin-top: 3rem; }
.project-card {
  background: var(--near-black);
  border: 1px solid var(--dark-surface);
  border-radius: var(--radius-lg);
  padding: 2rem;
  transition: all 0.3s;
  position: relative; overflow: hidden;
  margin-bottom: 0.75rem;
}
.project-card::before {
  content: '';
  position: absolute; left: 0; top: 0; bottom: 0;
  width: 3px;
  background: linear-gradient(180deg, var(--terracotta), var(--coral));
  border-radius: 3px 0 0 3px;
  opacity: 0; transition: opacity 0.3s;
}
.project-card:hover {
  border-color: rgba(201,100,66,0.3);
  background: rgba(20,20,19,0.98);
  transform: translateX(6px);
  box-shadow: rgba(0,0,0,0.4) 0 8px 32px;
}
.project-card:hover::before { opacity: 1; }
.project-top {
  display: flex; align-items: flex-start;
  justify-content: space-between; gap: 1rem;
  margin-bottom: 0.75rem;
}
.project-title {
  font-family: var(--serif); font-size: 1.15rem; font-weight: 500;
  color: var(--ivory); letter-spacing: -0.3px;
}
.project-badge {
  padding: 0.2rem 0.65rem;
  border-radius: 99px; font-size: 0.68rem; font-weight: 500;
  font-family: var(--mono); white-space: nowrap; flex-shrink: 0;
}
.badge-ai { background: rgba(183,148,244,0.12); color: #b794f4; border: 1px solid rgba(183,148,244,0.25); }
.badge-ft { background: rgba(99,179,237,0.1); color: #63b3ed; border: 1px solid rgba(99,179,237,0.2); }
.badge-fs { background: rgba(104,211,145,0.1); color: #68d391; border: 1px solid rgba(104,211,145,0.2); }
.badge-ml { background: rgba(251,211,141,0.1); color: #fbd38d; border: 1px solid rgba(251,211,141,0.2); }
.project-date {
  font-family: var(--mono); font-size: 0.72rem;
  color: var(--stone-gray); margin-bottom: 0.75rem;
}
.project-desc {
  color: var(--warm-silver); font-size: 0.875rem;
  line-height: 1.75; margin-bottom: 1.1rem;
}
.project-tech { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1.1rem; }
.tech-tag {
  padding: 0.2rem 0.55rem;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 5px; color: var(--stone-gray);
  font-size: 0.72rem; font-family: var(--mono);
  transition: color 0.2s, border-color 0.2s;
}
.project-card:hover .tech-tag { color: var(--warm-silver); border-color: rgba(255,255,255,0.12); }
.project-link {
  display: inline-flex; align-items: center; gap: 0.35rem;
  color: var(--terracotta); text-decoration: none;
  font-size: 0.8rem; font-weight: 500; font-family: var(--mono);
  transition: color 0.2s;
}
.project-link:hover { color: var(--coral); }
.project-link svg { transition: transform 0.2s; }
.project-link:hover svg { transform: translate(2px, -2px); }

/* ─── Experience ─── */
.experience-section { background: var(--parchment); padding: 6rem 0; }
.exp-layout { display: grid; grid-template-columns: 280px 1fr; gap: 5rem; align-items: start; }
.timeline { display: flex; flex-direction: column; gap: 0.85rem; }
.exp-card {
  background: var(--ivory);
  border: 1px solid var(--border-cream);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  box-shadow: rgba(0,0,0,0.04) 0 4px 20px;
  position: relative;
  transition: all 0.25s;
}
.exp-card:hover {
  border-color: rgba(201,100,66,0.3);
  box-shadow: rgba(0,0,0,0.08) 0 8px 28px;
}
.exp-glow {
  position: absolute; left: 0; top: 1.75rem;
  width: 3px; height: 2.25rem;
  background: linear-gradient(180deg, var(--terracotta), var(--coral));
  border-radius: 0 3px 3px 0;
  box-shadow: 0 0 8px rgba(201,100,66,0.5);
}
.exp-role {
  font-family: var(--serif); font-size: 1.1rem; font-weight: 500;
  color: var(--near-black); margin-bottom: 0.15rem;
}
.exp-org { color: var(--terracotta); font-size: 0.9rem; font-weight: 500; font-family: var(--mono); }
.exp-meta {
  font-family: var(--mono); font-size: 0.72rem;
  color: var(--stone-gray); margin-top: 0.15rem; margin-bottom: 0.9rem;
}
.exp-bullets {
  color: var(--olive-gray); font-size: 0.875rem;
  line-height: 1.8; padding-left: 1.1rem;
}
.exp-bullets li { margin-bottom: 0.3rem; }
.edu-cgpa {
  display: inline-block; margin-top: 0.75rem;
  padding: 0.22rem 0.7rem;
  background: rgba(107,124,94,0.1); color: var(--muted-green);
  border: 1px solid rgba(107,124,94,0.25);
  border-radius: 6px; font-size: 0.75rem; font-weight: 500; font-family: var(--mono);
}

/* ─── Contact ─── */
.contact-section { background: var(--near-black); padding: 6rem 0; }
.contact-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: start; }
.contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; }
.contact-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--dark-surface);
  border-radius: var(--radius-md);
  padding: 1.5rem 1.25rem;
  text-align: center;
  transition: all 0.25s;
}
.contact-card:hover {
  background: rgba(255,255,255,0.05);
  border-color: rgba(201,100,66,0.35);
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.4), 0 0 20px rgba(201,100,66,0.08);
}
.contact-icon { font-size: 1.4rem; margin-bottom: 0.35rem; }
.contact-lbl {
  font-family: var(--mono); font-size: 0.65rem;
  color: var(--stone-gray); text-transform: uppercase; letter-spacing: 1px;
}
.contact-val {
  color: var(--warm-silver); font-size: 0.85rem; margin-top: 0.2rem;
}
.contact-val a { color: var(--coral); text-decoration: none; }
.contact-val a:hover { color: #e08a70; }
.contact-message {
  font-family: var(--serif); font-style: italic;
  font-size: 1.25rem; line-height: 1.75;
  color: var(--warm-silver); margin-bottom: 2rem;
}
.contact-message em { color: var(--coral); font-style: italic; }

/* ─── Footer ─── */
footer {
  background: var(--near-black);
  border-top: 1px solid var(--dark-surface);
  padding: 2rem 0;
}
.footer-inner {
  max-width: 1160px; margin: 0 auto;
  padding: 0 clamp(1.5rem, 5vw, 4rem);
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 1rem;
}
.footer-copy {
  font-family: var(--mono); font-size: 0.75rem;
  color: var(--stone-gray);
}
.footer-copy a { color: var(--coral); text-decoration: none; }
.footer-links { display: flex; gap: 1.25rem; }
.footer-links a {
  color: var(--stone-gray); text-decoration: none;
  font-size: 0.8rem; transition: color 0.2s;
}
.footer-links a:hover { color: var(--warm-silver); }

/* ─── Quote Section ─── */
.quote-section {
  background: var(--near-black);
  padding: 4rem 0;
  border-top: 1px solid var(--dark-surface);
  text-align: center;
  position: relative; overflow: hidden;
}
.quote-bg-letter {
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-family: var(--serif); font-size: 18rem;
  color: rgba(255,255,255,0.015);
  pointer-events: none; user-select: none;
  line-height: 1;
}
.quote-text {
  font-family: var(--serif); font-style: italic;
  font-size: clamp(1rem, 2.5vw, 1.3rem);
  color: var(--warm-silver);
  line-height: 1.9; max-width: 520px;
  margin: 0 auto 0.75rem;
  position: relative; z-index: 1;
}
.quote-text strong { color: var(--coral); font-weight: 500; }
.quote-author {
  font-family: var(--mono); font-size: 0.7rem;
  color: var(--stone-gray); letter-spacing: 1.5px;
  text-transform: uppercase;
}

/* ─── Fade-in Animation ─── */
.fade-in { opacity: 0; transform: translateY(22px); transition: opacity 0.65s ease, transform 0.65s ease; }
.fade-in.visible { opacity: 1; transform: translateY(0); }
.fade-in:nth-child(2) { transition-delay: 0.1s; }
.fade-in:nth-child(3) { transition-delay: 0.2s; }
.fade-in:nth-child(4) { transition-delay: 0.3s; }

/* ─── Divider ─── */
.divider { width: 40px; height: 2px; background: var(--terracotta); margin: 1.5rem 0; border-radius: 2px; }
.divider-light { background: rgba(201,100,66,0.5); }

/* ─── Responsive ─── */
@media (max-width: 900px) {
  .hero-grid, .skills-layout, .exp-layout, .contact-layout { grid-template-columns: 1fr; gap: 3rem; }
  .hero-card { display: none; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
  .nav-links a:not(.nav-cta) { display: none; }
}
@media (max-width: 580px) {
  .skills-grid, .contact-grid { grid-template-columns: 1fr; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>
</head>
<body>

<!-- ─── Navigation ─── -->
<nav>
  <div class="nav-inner">
    <a href="#" class="nav-logo">Shravan<span>.</span>dev</a>
    <div class="nav-links">
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#experience">Experience</a>
      <a href="#contact">Contact</a>
      <div class="nav-dot" title="Open to work"></div>
      <a href="#contact" class="nav-cta">Hire me →</a>
    </div>
  </div>
</nav>

<!-- ─── Hero ─── -->
<section class="hero" id="home">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-text fade-in">
        <div class="hero-overline">Available for opportunities</div>
        <h1 class="hero-name">I'm <em>Shravan</em><br>Parthe.</h1>
        <div class="hero-role">// Backend Engineer · AI/ML Developer · B.Tech CSE 2027</div>
        <p class="hero-desc">
          CS student specializing in AI & ML with hands-on expertise in backend development using Java and Spring Boot. Building scalable, production-ready applications across fintech, healthcare, and edtech.
        </p>
        <div class="hero-cta">
          <a href="mailto:shravanparthe@gmail.com" class="btn-terra">📄 Get in touch</a>
          <a href="https://github.com/Shravan157" target="_blank" class="btn-ghost">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            GitHub
          </a>
          <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank" class="btn-ghost">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            LinkedIn
          </a>
        </div>
      </div>

      <!-- Code Card -->
      <div class="hero-card fade-in">
        <div class="card-topbar">
          <span class="dot dot-r"></span>
          <span class="dot dot-y"></span>
          <span class="dot dot-g"></span>
          <span class="card-filename">shravan.java</span>
        </div>
        <div class="card-body">
          <div class="code-line"><span class="cm">// open to work ✓</span></div>
          <div class="code-line"><span class="kw">class</span> <span class="fn">Developer</span> {</div>
          <div class="code-line">  <span class="kw">String</span> name = <span class="st">"Shravan"</span>;</div>
          <div class="code-line">  <span class="kw">int</span> year = <span class="nm">3</span>;</div>
          <div class="code-line">  <span class="kw">String[]</span> stack = {</div>
          <div class="code-line">    <span class="st">"Java"</span>, <span class="st">"Python"</span>,</div>
          <div class="code-line">    <span class="st">"Spring Boot"</span>,</div>
          <div class="code-line">    <span class="st">"React"</span>, <span class="st">"Flutter"</span></div>
          <div class="code-line">  };</div>
          <div class="code-line">  <span class="kw">boolean</span> hireable = <span class="fn">true</span>;</div>
          <div class="code-line">}</div>
        </div>
        <div class="card-footer">
          <div class="status-dot"></div>
          <span class="status-text">status: <span class="status-ok">available</span></span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ─── Stats ─── -->
<section class="stats-strip">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-item">
        <div class="stat-num">5+</div>
        <div class="stat-label">Projects</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">7.5</div>
        <div class="stat-label">CGPA</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">3rd</div>
        <div class="stat-label">Year B.Tech</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">1</div>
        <div class="stat-label">Internship</div>
      </div>
    </div>
  </div>
</section>

<!-- ─── Skills ─── -->
<section class="skills-section" id="skills">
  <div class="container">
    <div class="skills-layout">
      <div class="fade-in">
        <div class="section-tag">01. Skills</div>
        <h2 class="section-heading">What I work<br><em style="font-style:italic;color:var(--terracotta)">with.</em></h2>
        <div class="divider"></div>
        <p class="section-sub">
          From backend systems to AI pipelines — a full-spectrum toolkit built through real projects, not just coursework.
        </p>
      </div>
      <div class="skills-grid fade-in">
        <div class="skill-group">
          <div class="skill-group-title">💻 Languages</div>
          <div class="skill-tags">
            <span class="skill-chip chip-terra">Java</span>
            <span class="skill-chip chip-terra">Python</span>
            <span class="skill-chip chip-terra">JavaScript</span>
            <span class="skill-chip chip-terra">Dart</span>
            <span class="skill-chip chip-terra">SQL</span>
          </div>
        </div>
        <div class="skill-group">
          <div class="skill-group-title">⚙️ Frameworks</div>
          <div class="skill-tags">
            <span class="skill-chip chip-olive">Spring Boot</span>
            <span class="skill-chip chip-olive">React</span>
            <span class="skill-chip chip-olive">Flutter</span>
            <span class="skill-chip chip-olive">FastAPI</span>
            <span class="skill-chip chip-olive">Spring AI</span>
          </div>
        </div>
        <div class="skill-group">
          <div class="skill-group-title">🛠️ Tools</div>
          <div class="skill-tags">
            <span class="skill-chip chip-stone">Docker</span>
            <span class="skill-chip chip-stone">GitHub</span>
            <span class="skill-chip chip-stone">NumPy</span>
            <span class="skill-chip chip-stone">Pandas</span>
            <span class="skill-chip chip-stone">Scikit-learn</span>
          </div>
        </div>
        <div class="skill-group">
          <div class="skill-group-title">🗄️ Databases</div>
          <div class="skill-tags">
            <span class="skill-chip chip-warm">MySQL</span>
            <span class="skill-chip chip-warm">PostgreSQL</span>
            <span class="skill-chip chip-warm">Firebase</span>
            <span class="skill-chip chip-warm">Redis</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ─── Projects ─── -->
<section class="projects-section" id="projects">
  <div class="container">
    <div style="margin-bottom:3rem;" class="fade-in">
      <div class="section-tag" style="color:var(--coral)">02. Projects</div>
      <h2 class="section-heading section-heading-light">Featured <em style="color:var(--coral);font-style:italic">work.</em></h2>
      <div class="divider divider-light"></div>
      <p class="section-sub section-sub-light">Five projects that span healthcare AI, fintech, education, and NLP.</p>
    </div>

    <div class="projects-grid fade-in">

      <div class="project-card">
        <div class="project-top">
          <div class="project-title">🏥 MedoraX AI — Clinical AI Assistant</div>
          <span class="project-badge badge-ai">Healthcare AI</span>
        </div>
        <div class="project-date">📅 Oct 2025 — Nov 2026</div>
        <p class="project-desc">Multimodal clinical AI assistant supporting voice, image, and text inputs — transcribing symptoms via Whisper-large-v3, analyzing medical images via Llama-4-scout, and generating structured diagnostic responses using Llama-3.3-70b. Multilingual support (English, Hindi, Marathi) with GPS-based hospital finder and real-time AQI monitoring.</p>
        <div class="project-tech">
          <span class="tech-tag">Python</span><span class="tech-tag">Gradio</span><span class="tech-tag">Groq API</span><span class="tech-tag">Google Maps API</span><span class="tech-tag">Google Places API</span>
        </div>
        <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="project-link">
          View on GitHub
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
        </a>
      </div>

      <div class="project-card">
        <div class="project-top">
          <div class="project-title">🏦 SahayLoan — Micro-Loan Platform</div>
          <span class="project-badge badge-ft">FinTech</span>
        </div>
        <div class="project-date">📅 Jan 2026 — Present</div>
        <p class="project-desc">Full-stack micro-lending platform (loans up to ₹1,00,000) with Flutter frontend and FastAPI backend. AI credit scoring engine using Random Forest classifier, digital KYC with Aadhaar & PAN OCR via Tesseract, Stripe EMI integration, and multi-role system with Firebase Auth and Firestore.</p>
        <div class="project-tech">
          <span class="tech-tag">Flutter</span><span class="tech-tag">FastAPI</span><span class="tech-tag">Scikit-learn</span><span class="tech-tag">Firebase</span><span class="tech-tag">Tesseract OCR</span><span class="tech-tag">Stripe</span>
        </div>
        <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="project-link">
          View on GitHub
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
        </a>
      </div>

      <div class="project-card">
        <div class="project-top">
          <div class="project-title">🎓 SikshaSetu — Rural Education Platform</div>
          <span class="project-badge badge-fs">Full-Stack</span>
        </div>
        <div class="project-date">📅 Jan 2025 — Apr 2025</div>
        <p class="project-desc">Full-stack education platform bridging the digital divide for rural communities. Role-based access control with Spring Security and JWT/OAuth 2.0, optimized relational schema, responsive React.js frontend, and ZEGOCLOUD real-time video SDK for virtual classrooms.</p>
        <div class="project-tech">
          <span class="tech-tag">React</span><span class="tech-tag">Spring Boot</span><span class="tech-tag">Spring Security</span><span class="tech-tag">JWT</span><span class="tech-tag">MySQL</span>
        </div>
        <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="project-link">
          View on GitHub
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
        </a>
      </div>

      <div class="project-card">
        <div class="project-top">
          <div class="project-title">🛒 AI-Powered E-Commerce Platform</div>
          <span class="project-badge badge-ai">AI / Full-Stack</span>
        </div>
        <div class="project-date">📅 Oct 2024 — Jan 2025</div>
        <p class="project-desc">Intelligent e-commerce backend with AI-driven product recommendations using Spring AI and vector similarity search via Redis Vector DB. Generative AI chatbot for real-time customer support, AI-powered product image generation pipeline, secured with Spring Security and JWT.</p>
        <div class="project-tech">
          <span class="tech-tag">React</span><span class="tech-tag">Spring Boot</span><span class="tech-tag">Spring AI</span><span class="tech-tag">Redis Vector DB</span><span class="tech-tag">Tailwind CSS</span>
        </div>
        <a href="https://github.com/Shravan157" target="_blank" class="project-link">
          View on GitHub
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
        </a>
      </div>

      <div class="project-card">
        <div class="project-top">
          <div class="project-title">🍽️ Zomato Sentiment Analysis</div>
          <span class="project-badge badge-ml">ML / NLP</span>
        </div>
        <div class="project-date">📅 Data Science Project</div>
        <p class="project-desc">End-to-end NLP project classifying 10,000+ Zomato restaurant reviews. Extensive EDA with 15 visualizations, hypothesis testing, TF-IDF vectorization, and model comparison (Logistic Regression, Random Forest, Naive Bayes). Logistic Regression achieved highest F1 score.</p>
        <div class="project-tech">
          <span class="tech-tag">Python</span><span class="tech-tag">Scikit-learn</span><span class="tech-tag">NLTK</span><span class="tech-tag">TF-IDF</span><span class="tech-tag">Pandas</span><span class="tech-tag">Matplotlib</span>
        </div>
        <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="project-link">
          View on GitHub
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17L17 7M7 7h10v10"/></svg>
        </a>
      </div>

    </div>
  </div>
</section>

<!-- ─── Experience & Education ─── -->
<section class="experience-section" id="experience">
  <div class="container">
    <div class="exp-layout">
      <div class="fade-in">
        <div class="section-tag">03. Experience</div>
        <h2 class="section-heading">Where I've<br><em style="font-style:italic;color:var(--terracotta)">worked.</em></h2>
        <div class="divider"></div>
        <p class="section-sub">Building real-world experience alongside my degree.</p>
      </div>
      <div class="timeline fade-in">

        <div class="exp-card">
          <div class="exp-glow"></div>
          <div class="exp-role">Data Science with Gen AI Intern</div>
          <div class="exp-org">@ Innovexis</div>
          <div class="exp-meta">Apr 2026 — Present · Remote</div>
          <ul class="exp-bullets">
            <li>Selected for Innovexis's competitive Data Science with Generative AI internship</li>
            <li>Working on real-world projects integrating LLMs and generative AI techniques</li>
            <li>Applying Python, NumPy, Pandas, and Scikit-learn for data analysis and model building</li>
            <li>Gaining hands-on exposure to production-level Gen AI workflows and LLM integration</li>
          </ul>
        </div>

        <div class="exp-card" id="education">
          <div class="exp-glow"></div>
          <div class="exp-role">B.Tech in Computer Science Engineering (AI & ML)</div>
          <div class="exp-org">@ ViMEET, University of Mumbai</div>
          <div class="exp-meta">Jun 2023 — Expected May 2027</div>
          <p style="color:var(--olive-gray);font-size:0.875rem;line-height:1.7;margin-top:0.6rem;">
            Specializing in Artificial Intelligence & Machine Learning. Coursework includes Data Structures & Algorithms, Machine Learning, Cloud Computing, Microservices Architecture, and System Design.
          </p>
          <div class="edu-cgpa">✦ CGPA: 7.5 / 10.0</div>
        </div>

      </div>
    </div>
  </div>
</section>

<!-- ─── Contact ─── -->
<section class="contact-section" id="contact">
  <div class="container">
    <div class="contact-layout">
      <div class="fade-in">
        <div class="section-tag" style="color:var(--coral)">05. Contact</div>
        <h2 class="section-heading section-heading-light">Let's build<br><em style="color:var(--coral);font-style:italic">something.</em></h2>
        <div class="divider divider-light"></div>
        <p class="contact-message">
          Whether it's a <em>collaboration</em>, an <em>internship</em>, or just a conversation about AI and systems — I'd love to connect.
        </p>
        <a href="mailto:shravanparthe@gmail.com" class="btn-terra">✉️ Send a message</a>
      </div>
      <div class="contact-grid fade-in">
        <div class="contact-card">
          <div class="contact-icon">📧</div>
          <div class="contact-lbl">Email</div>
          <div class="contact-val"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div>
        </div>
        <div class="contact-card">
          <div class="contact-icon">📱</div>
          <div class="contact-lbl">Phone</div>
          <div class="contact-val">7385813010</div>
        </div>
        <div class="contact-card">
          <div class="contact-icon">💼</div>
          <div class="contact-lbl">LinkedIn</div>
          <div class="contact-val"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div>
        </div>
        <div class="contact-card">
          <div class="contact-icon">🐙</div>
          <div class="contact-lbl">GitHub</div>
          <div class="contact-val"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div>
        </div>
        <div class="contact-card" style="grid-column:span 2">
          <div class="contact-icon">📍</div>
          <div class="contact-lbl">Location</div>
          <div class="contact-val">Mumbai, India</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ─── Quote ─── -->
<div class="quote-section">
  <div class="quote-bg-letter">"</div>
  <p class="quote-text">
    The woods are lovely, dark and deep,<br>
    But I have promises to keep,<br>
    And <strong>miles to go before I sleep,</strong><br>
    And miles to go before I sleep.
  </p>
  <div class="quote-author">— Robert Frost · Stopping by Woods on a Snowy Evening</div>
</div>

<!-- ─── Footer ─── -->
<footer>
  <div class="footer-inner">
    <div class="footer-copy">
      Designed & built by <a href="https://github.com/Shravan157" target="_blank">Shravan Parthe</a> · 2026 · Made with ❤️ &amp; ☕
    </div>
    <div class="footer-links">
      <a href="https://github.com/Shravan157" target="_blank">GitHub</a>
      <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn</a>
      <a href="mailto:shravanparthe@gmail.com">Email</a>
    </div>
  </div>
</footer>

<script>
// Fade-in on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// Trigger hero immediately
document.querySelectorAll('.hero .fade-in').forEach(el => {
  setTimeout(() => el.classList.add('visible'), 100);
});
</script>
</body>
</html>
