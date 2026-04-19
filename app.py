import streamlit as st
import base64
import os

# ─── Page Configuration ───
st.set_page_config(
    page_title="Shravan Parthe — Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Resume Download Helper ───
def get_resume_download_link():
    resume_path = os.path.join(os.path.dirname(__file__), "resume_shravan2.pdf")
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f'<a href="data:application/pdf;base64,{data}" download="Shravan_Parthe_Resume.pdf" class="btn-primary">Download Resume <span class="btn-arrow">↗</span></a>'
    return '<a href="#" class="btn-primary">Resume Coming Soon <span class="btn-arrow">↗</span></a>'

# ─── Custom CSS ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --bg:         #09090f;
  --bg-1:       #0f0f1a;
  --bg-2:       #13131f;
  --bg-3:       #1a1a28;
  --border:     rgba(255,255,255,0.07);
  --border-glow:rgba(212,175,55,0.25);
  --gold:       #d4af37;
  --gold-light: #f0d060;
  --gold-dim:   rgba(212,175,55,0.15);
  --cyan:       #00e5cc;
  --cyan-dim:   rgba(0,229,204,0.12);
  --text-1:     #f0f0f8;
  --text-2:     #9898b8;
  --text-3:     #5a5a7a;
  --purple:     #a78bfa;
  --green:      #34d399;
  --rose:       #fb7185;
  --radius-sm:  8px;
  --radius:     14px;
  --radius-lg:  20px;
  --font-head:  'Syne', sans-serif;
  --font-body:  'DM Sans', sans-serif;
  --font-mono:  'JetBrains Mono', monospace;
}

/* ─── Reset & Base ─── */
* { box-sizing: border-box; margin: 0; padding: 0; }
.stApp {
  background-color: var(--bg) !important;
  color: var(--text-1) !important;
  font-family: var(--font-body) !important;
}
.block-container {
  max-width: 1100px !important;
  padding: 0 2rem 6rem !important;
}
#MainMenu, footer, header, .stDeployButton { visibility: hidden !important; display: none !important; }

/* ─── Dot Grid Background ─── */
.stApp::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: radial-gradient(circle, rgba(212,175,55,0.06) 1px, transparent 1px);
  background-size: 32px 32px;
  pointer-events: none;
  z-index: 0;
}
.block-container { position: relative; z-index: 1; }

/* ─── Animations ─── */
@keyframes fadeUp {
  from { opacity:0; transform:translateY(28px); }
  to   { opacity:1; transform:translateY(0); }
}
@keyframes fadeIn {
  from { opacity:0; } to { opacity:1; }
}
@keyframes shimmer {
  0%   { background-position: -200% center; }
  100% { background-position:  200% center; }
}
@keyframes pulse-ring {
  0%   { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(212,175,55,0.4); }
  70%  { transform: scale(1);    box-shadow: 0 0 0 14px rgba(212,175,55,0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(212,175,55,0); }
}
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-8px); }
}
@keyframes glow-line {
  0%,100% { opacity:0.4; width:40px; }
  50%     { opacity:1;   width:80px; }
}
@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

/* ─── Navigation ─── */
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 0;
  border-bottom: 1px solid var(--border);
  margin-bottom: 0;
  animation: fadeIn 0.6s ease both;
  position: sticky;
  top: 0;
  background: rgba(9,9,15,0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  z-index: 100;
}
.nav-brand {
  font-family: var(--font-head);
  font-weight: 800;
  font-size: 1.25rem;
  color: var(--text-1);
  letter-spacing: -0.5px;
}
.nav-brand .dot { 
  display: inline-block;
  width: 8px; height: 8px;
  background: var(--gold);
  border-radius: 50%;
  margin-left: 3px;
  vertical-align: middle;
  animation: pulse-ring 2.5s ease infinite;
}
.nav-links { display: flex; gap: 2rem; align-items: center; }
.nav-links a {
  color: var(--text-2);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  letter-spacing: 0.3px;
  transition: color 0.2s;
  font-family: var(--font-body);
}
.nav-links a:hover { color: var(--gold); }
.nav-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.9rem;
  background: rgba(52,211,153,0.1);
  border: 1px solid rgba(52,211,153,0.2);
  border-radius: 999px;
  font-size: 0.75rem;
  color: var(--green);
  font-weight: 600;
}
.nav-status::before {
  content: '';
  width: 7px; height: 7px;
  background: var(--green);
  border-radius: 50%;
  animation: pulse-ring 2s ease infinite;
}

/* ─── Hero ─── */
.hero-wrap {
  padding: 5rem 0 4rem;
  animation: fadeUp 0.7s 0.1s ease both;
}
.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  color: var(--gold);
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}
.hero-eyebrow::before {
  content: '';
  display: block;
  width: 28px; height: 1px;
  background: var(--gold);
}
.hero-name {
  font-family: var(--font-head);
  font-size: clamp(3rem, 6vw, 5rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -2px;
  color: var(--text-1);
  margin-bottom: 0.35rem;
}
.hero-name .gradient-text {
  background: linear-gradient(135deg, var(--gold-light) 0%, var(--gold) 40%, #c8962b 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 4s linear infinite;
}
.hero-subtitle {
  font-family: var(--font-head);
  font-size: 1.15rem;
  font-weight: 500;
  color: var(--text-2);
  margin-bottom: 1.5rem;
  letter-spacing: -0.3px;
}
.hero-desc {
  font-size: 1rem;
  color: var(--text-2);
  line-height: 1.8;
  max-width: 560px;
  font-weight: 300;
  margin-bottom: 2.5rem;
}
.hero-desc strong { color: var(--text-1); font-weight: 500; }
.hero-cta {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  align-items: center;
  margin-bottom: 3.5rem;
}
.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.85rem 2rem;
  background: var(--gold);
  color: #09090f !important;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 700;
  text-decoration: none !important;
  transition: all 0.25s;
  font-family: var(--font-body);
  letter-spacing: 0.2px;
}
.btn-primary:hover {
  background: var(--gold-light);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(212,175,55,0.35);
}
.btn-arrow {
  display: inline-block;
  transition: transform 0.2s;
}
.btn-primary:hover .btn-arrow { transform: translate(2px,-2px); }
.btn-outline {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.82rem 1.75rem;
  background: transparent;
  color: var(--text-2) !important;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 500;
  text-decoration: none !important;
  transition: all 0.25s;
}
.btn-outline:hover {
  border-color: var(--gold);
  color: var(--gold) !important;
  background: var(--gold-dim);
}

/* ─── Hero Stats Strip ─── */
.stats-strip {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  animation: fadeUp 0.7s 0.3s ease both;
}
.stat-item {
  background: var(--bg-1);
  padding: 1.5rem 1.25rem;
  text-align: center;
  transition: background 0.2s;
}
.stat-item:hover { background: var(--bg-2); }
.stat-num {
  font-family: var(--font-head);
  font-size: 2rem;
  font-weight: 800;
  color: var(--gold);
  letter-spacing: -1px;
  line-height: 1;
}
.stat-lbl {
  font-size: 0.72rem;
  color: var(--text-3);
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
  margin-top: 0.35rem;
}

/* ─── Section ─── */
.section {
  padding: 5rem 0 0;
  animation: fadeUp 0.7s ease both;
}
.section-label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--gold);
  letter-spacing: 2.5px;
  text-transform: uppercase;
  margin-bottom: 0.75rem;
}
.section-label::before {
  content:'';
  width:20px; height:1px;
  background: var(--gold);
}
.section-title {
  font-family: var(--font-head);
  font-size: 2.25rem;
  font-weight: 800;
  color: var(--text-1);
  letter-spacing: -1px;
  line-height: 1.1;
  margin-bottom: 0.5rem;
}
.section-sub {
  color: var(--text-3);
  font-size: 0.9rem;
  font-weight: 400;
  margin-bottom: 2.5rem;
}

/* ─── Skills ─── */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
}
.skill-cell {
  background: var(--bg-1);
  padding: 1.75rem 1.5rem;
  transition: background 0.2s;
  position: relative;
  overflow: hidden;
}
.skill-cell::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, var(--gold-dim) 0%, transparent 60%);
  opacity: 0;
  transition: opacity 0.3s;
}
.skill-cell:hover { background: var(--bg-2); }
.skill-cell:hover::before { opacity: 1; }
.skill-cell-icon {
  font-size: 1.6rem;
  margin-bottom: 0.75rem;
  display: block;
}
.skill-cell-name {
  font-family: var(--font-head);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-3);
  margin-bottom: 1rem;
}
.pill-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}
.pill {
  padding: 0.28rem 0.75rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 500;
  border: 1px solid;
  font-family: var(--font-mono);
  transition: all 0.2s;
  cursor: default;
}
.pill-gold  { color: var(--gold);   border-color: rgba(212,175,55,0.3);  background: rgba(212,175,55,0.07); }
.pill-cyan  { color: var(--cyan);   border-color: rgba(0,229,204,0.3);   background: rgba(0,229,204,0.07); }
.pill-purple{ color: var(--purple); border-color: rgba(167,139,250,0.3); background: rgba(167,139,250,0.07); }
.pill-rose  { color: var(--rose);   border-color: rgba(251,113,133,0.3); background: rgba(251,113,133,0.07); }
.pill-green { color: var(--green);  border-color: rgba(52,211,153,0.3);  background: rgba(52,211,153,0.07); }
.pill:hover { transform: translateY(-1px); filter: brightness(1.2); }

/* ─── Projects ─── */
.project-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
}
.project-card {
  background: var(--bg-1);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.project-card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--radius-lg);
  padding: 1px;
  background: linear-gradient(135deg, rgba(212,175,55,0) 0%, rgba(212,175,55,0.4) 50%, rgba(0,229,204,0) 100%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.3s;
}
.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 48px rgba(0,0,0,0.5);
  background: var(--bg-2);
}
.project-card:hover::after { opacity: 1; }
.project-card.featured {
  grid-column: span 2;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}
.project-featured-content { display: flex; flex-direction: column; }
.project-featured-visual {
  background: var(--bg-3);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--cyan);
  line-height: 1.9;
  overflow: hidden;
  position: relative;
}
.project-featured-visual::before {
  content: '';
  position: absolute;
  top: -20px; right: -20px;
  width: 100px; height: 100px;
  background: radial-gradient(circle, rgba(0,229,204,0.15) 0%, transparent 70%);
}
.kw  { color: var(--purple); }
.fn  { color: var(--gold); }
.str { color: var(--green); }
.cm  { color: var(--text-3); }
.num { color: var(--cyan); }

.project-badge-wrap {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}
.badge {
  padding: 0.22rem 0.7rem;
  border-radius: 999px;
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  font-family: var(--font-mono);
}
.badge-gold   { background: rgba(212,175,55,0.15); color: var(--gold);   border: 1px solid rgba(212,175,55,0.3); }
.badge-cyan   { background: rgba(0,229,204,0.12);  color: var(--cyan);   border: 1px solid rgba(0,229,204,0.25); }
.badge-purple { background: rgba(167,139,250,0.12);color: var(--purple); border: 1px solid rgba(167,139,250,0.25);}
.badge-green  { background: rgba(52,211,153,0.12); color: var(--green);  border: 1px solid rgba(52,211,153,0.25); }
.badge-rose   { background: rgba(251,113,133,0.12);color: var(--rose);   border: 1px solid rgba(251,113,133,0.25); }

.project-title {
  font-family: var(--font-head);
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text-1);
  margin-bottom: 0.4rem;
  letter-spacing: -0.3px;
  line-height: 1.3;
}
.project-date {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-3);
  margin-bottom: 0.85rem;
  letter-spacing: 0.5px;
}
.project-desc {
  color: var(--text-2);
  font-size: 0.88rem;
  line-height: 1.75;
  flex: 1;
  font-weight: 300;
  margin-bottom: 1.25rem;
}
.project-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}
.chip {
  padding: 0.22rem 0.65rem;
  background: var(--bg-3);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-3);
  transition: all 0.2s;
}
.chip:hover { border-color: rgba(212,175,55,0.3); color: var(--gold); }
.project-link {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: var(--gold);
  text-decoration: none;
  font-size: 0.82rem;
  font-weight: 600;
  font-family: var(--font-mono);
  transition: all 0.2s;
  margin-top: auto;
}
.project-link:hover { color: var(--gold-light); gap: 0.65rem; }

/* ─── Timeline ─── */
.timeline { display: flex; flex-direction: column; gap: 1.25rem; }
.tl-card {
  background: var(--bg-1);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.75rem 2rem;
  position: relative;
  transition: all 0.25s;
  overflow: hidden;
}
.tl-card::before {
  content: '';
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 3px;
  background: linear-gradient(180deg, var(--gold) 0%, var(--cyan) 100%);
  border-radius: 0 2px 2px 0;
}
.tl-card:hover {
  border-color: var(--border-glow);
  background: var(--bg-2);
  box-shadow: 0 8px 30px rgba(0,0,0,0.4);
}
.tl-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.5rem;
}
.tl-role {
  font-family: var(--font-head);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-1);
  letter-spacing: -0.3px;
}
.tl-org {
  font-size: 0.9rem;
  color: var(--gold);
  font-weight: 500;
  margin-bottom: 0.2rem;
}
.tl-meta {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-3);
  letter-spacing: 0.5px;
  margin-bottom: 1rem;
}
.tl-tag {
  padding: 0.22rem 0.75rem;
  border-radius: 999px;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  flex-shrink: 0;
}
.tl-bullets {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.tl-bullets li {
  color: var(--text-2);
  font-size: 0.88rem;
  font-weight: 300;
  line-height: 1.65;
  padding-left: 1.25rem;
  position: relative;
}
.tl-bullets li::before {
  content: '▸';
  position: absolute;
  left: 0;
  color: var(--gold);
  font-size: 0.7rem;
  top: 0.2rem;
}
.tl-cgpa {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.3rem 0.85rem;
  background: rgba(52,211,153,0.1);
  border: 1px solid rgba(52,211,153,0.25);
  border-radius: 999px;
  color: var(--green);
  font-size: 0.78rem;
  font-weight: 600;
  font-family: var(--font-mono);
  margin-top: 0.75rem;
  display: inline-flex;
}

/* ─── Contact ─── */
.contact-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
}
.contact-item {
  background: var(--bg-1);
  padding: 1.5rem 1rem;
  text-align: center;
  transition: background 0.2s;
  position: relative;
  overflow: hidden;
}
.contact-item:hover { background: var(--bg-2); }
.contact-item::before {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--gold), var(--cyan));
  transform: scaleX(0);
  transition: transform 0.3s;
}
.contact-item:hover::before { transform: scaleX(1); }
.contact-icon { font-size: 1.35rem; margin-bottom: 0.5rem; }
.contact-lbl {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--text-3);
  text-transform: uppercase;
  letter-spacing: 1.5px;
  font-weight: 600;
  margin-bottom: 0.35rem;
}
.contact-val {
  font-size: 0.83rem;
  color: var(--text-1);
  font-weight: 500;
  word-break: break-all;
}
.contact-val a {
  color: var(--gold);
  text-decoration: none;
  transition: color 0.2s;
}
.contact-val a:hover { color: var(--gold-light); }

/* ─── Footer ─── */
.footer {
  padding: 3rem 0 1.5rem;
  border-top: 1px solid var(--border);
  margin-top: 5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.footer-left p { color: var(--text-3); font-size: 0.82rem; }
.footer-left a { color: var(--gold); text-decoration: none; }
.footer-right {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--text-3);
}

/* ─── Responsive ─── */
@media (max-width: 768px) {
  .block-container { padding: 0 1rem 4rem !important; }
  .hero-name { font-size: 2.5rem; }
  .project-grid { grid-template-columns: 1fr; }
  .project-card.featured { grid-column: span 1; grid-template-columns: 1fr; }
  .project-featured-visual { display: none; }
  .stats-strip { grid-template-columns: repeat(2,1fr); }
  .contact-grid { grid-template-columns: repeat(2,1fr); }
  .skills-grid { grid-template-columns: 1fr 1fr; }
  .footer { flex-direction: column; gap: 0.75rem; text-align: center; }
  .nav-links { gap: 1rem; }
}
</style>
""", unsafe_allow_html=True)

# ─── Navigation ───
st.markdown("""
<nav class="nav">
  <div class="nav-brand">SHRAVAN<span class="dot"></span></div>
  <div class="nav-links">
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#education">Education</a>
    <a href="#contact">Contact</a>
    <span class="nav-status">Open to Work</span>
  </div>
</nav>
""", unsafe_allow_html=True)

# ─── Hero ───
resume_link = get_resume_download_link()
st.markdown(f"""
<div class="hero-wrap">
  <div class="hero-eyebrow">Mumbai, India · B.Tech CSE AI&amp;ML · Class of 2027</div>
  <h1 class="hero-name">
    Building the<br><span class="gradient-text">Future of Tech</span>
  </h1>
  <div class="hero-subtitle">Full-Stack Engineer & AI/ML Developer</div>
  <p class="hero-desc">
    Results-driven CS student with hands-on expertise in 
    <strong>Java · Spring Boot · Python</strong> and cutting-edge AI/ML integration. 
    I craft scalable, production-ready applications spanning 
    <strong>fintech, healthcare, and edtech</strong> — bridging intelligent backend systems with real-world impact.
  </p>
  <div class="hero-cta">
    {resume_link}
    <a href="https://github.com/Shravan157" target="_blank" class="btn-outline">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
      GitHub
    </a>
    <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank" class="btn-outline">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      LinkedIn
    </a>
  </div>
</div>

<div class="stats-strip">
  <div class="stat-item">
    <div class="stat-num">5+</div>
    <div class="stat-lbl">Projects Built</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">7.5</div>
    <div class="stat-lbl">CGPA / 10</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">3rd</div>
    <div class="stat-lbl">Year B.Tech</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">1</div>
    <div class="stat-lbl">Internship</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Skills ───
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Expertise</div>
  <h2 class="section-title">Technical Skills</h2>
  <p class="section-sub">Languages, frameworks, and tools in my arsenal</p>
  <div class="skills-grid">
    <div class="skill-cell">
      <span class="skill-cell-icon">💻</span>
      <div class="skill-cell-name">Languages</div>
      <div class="pill-row">
        <span class="pill pill-gold">Java</span>
        <span class="pill pill-gold">Python</span>
        <span class="pill pill-gold">JavaScript</span>
        <span class="pill pill-gold">Dart</span>
        <span class="pill pill-gold">SQL</span>
      </div>
    </div>
    <div class="skill-cell">
      <span class="skill-cell-icon">⚙️</span>
      <div class="skill-cell-name">Frameworks</div>
      <div class="pill-row">
        <span class="pill pill-cyan">Spring Boot</span>
        <span class="pill pill-cyan">Spring AI</span>
        <span class="pill pill-cyan">Spring Security</span>
        <span class="pill pill-cyan">React</span>
        <span class="pill pill-cyan">Flutter</span>
        <span class="pill pill-cyan">FastAPI</span>
      </div>
    </div>
    <div class="skill-cell">
      <span class="skill-cell-icon">🛠️</span>
      <div class="skill-cell-name">Tools & Platforms</div>
      <div class="pill-row">
        <span class="pill pill-purple">Docker</span>
        <span class="pill pill-purple">GitHub</span>
        <span class="pill pill-purple">NumPy</span>
        <span class="pill pill-purple">Pandas</span>
        <span class="pill pill-purple">Scikit-learn</span>
      </div>
    </div>
    <div class="skill-cell">
      <span class="skill-cell-icon">🗄️</span>
      <div class="skill-cell-name">Databases</div>
      <div class="pill-row">
        <span class="pill pill-rose">MySQL</span>
        <span class="pill pill-rose">PostgreSQL</span>
        <span class="pill pill-rose">Firebase</span>
        <span class="pill pill-rose">Redis</span>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Projects ───
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Work</div>
  <h2 class="section-title">Featured Projects</h2>
  <p class="section-sub">Across AI, full-stack, mobile, and machine learning</p>

  <div class="project-grid">

    <!-- Featured: MedoraX -->
    <div class="project-card featured">
      <div class="project-featured-content">
        <div class="project-badge-wrap">
          <span class="badge badge-cyan">Healthcare AI</span>
          <span class="badge badge-gold">Multimodal</span>
        </div>
        <div class="project-title">🏥 MedoraX AI — Clinical AI Assistant</div>
        <div class="project-date">Oct 2025 — Nov 2026</div>
        <p class="project-desc">
          A multimodal clinical AI assistant supporting voice, image, and text inputs. Transcribes symptoms via 
          Whisper-large-v3, analyzes medical images via Llama-4-scout, and generates structured diagnostic responses 
          using Llama-3.3-70b. Multilingual support in English, Hindi, and Marathi with GPS-based hospital finder 
          and real-time AQI monitoring. Deployed on Hugging Face Spaces with 4–7s response times.
        </p>
        <div class="project-chips">
          <span class="chip">Python</span><span class="chip">Gradio</span>
          <span class="chip">Groq API</span><span class="chip">Google Maps API</span>
          <span class="chip">Whisper</span><span class="chip">Llama-4</span>
        </div>
        <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="project-link">
          View on GitHub →
        </a>
      </div>
      <div class="project-featured-visual">
        <div>
          <span class="cm"># medorax_ai.py</span><br>
          <span class="kw">class</span> <span class="fn">ClinicalAI</span>:<br>
          &nbsp;&nbsp;<span class="fn">def</span> <span class="fn">analyze</span>(self, inp):<br>
          &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">if</span> inp.type == <span class="str">"voice"</span>:<br>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text = whisper.<span class="fn">transcribe</span>()<br>
          &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">elif</span> inp.type == <span class="str">"image"</span>:<br>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text = llama4.<span class="fn">vision</span>()<br>
          &nbsp;&nbsp;&nbsp;&nbsp;diagnosis = llama3.<span class="fn">generate</span>(<br>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text, lang=<span class="str">"auto"</span><br>
          &nbsp;&nbsp;&nbsp;&nbsp;)<br>
          &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">return</span> diagnosis
        </div>
      </div>
    </div>

    <!-- SahayLoan -->
    <div class="project-card">
      <div class="project-badge-wrap">
        <span class="badge badge-gold">FinTech</span>
        <span class="badge badge-green">AI Credit Scoring</span>
      </div>
      <div class="project-title">🏦 SahayLoan — Micro-Loan Platform</div>
      <div class="project-date">Jan 2026 — Present</div>
      <p class="project-desc">
        Full-stack micro-lending platform (loans up to ₹1,00,000) with Flutter frontend, FastAPI backend, 
        AI credit scoring via Random Forest, digital KYC with Tesseract OCR, and Stripe EMI payments. 
        Multi-role system with Firebase Auth and Firestore.
      </p>
      <div class="project-chips">
        <span class="chip">Flutter</span><span class="chip">FastAPI</span>
        <span class="chip">Scikit-learn</span><span class="chip">Firebase</span>
        <span class="chip">Tesseract</span><span class="chip">Stripe</span>
      </div>
      <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="project-link">View on GitHub →</a>
    </div>

    <!-- SikshaSetu -->
    <div class="project-card">
      <div class="project-badge-wrap">
        <span class="badge badge-purple">Full-Stack</span>
        <span class="badge badge-cyan">EdTech</span>
      </div>
      <div class="project-title">🎓 SikshaSetu — Rural Education Platform</div>
      <div class="project-date">Jan 2025 — Apr 2025</div>
      <p class="project-desc">
        Education platform bridging the digital divide for rural communities. RBAC with Spring Security + 
        JWT/OAuth 2.0, optimized MySQL schema, React.js frontend, and ZEGOCLOUD real-time video SDK 
        for virtual classrooms.
      </p>
      <div class="project-chips">
        <span class="chip">React</span><span class="chip">Spring Boot</span>
        <span class="chip">Spring Security</span><span class="chip">JWT</span>
        <span class="chip">MySQL</span><span class="chip">ZEGOCLOUD</span>
      </div>
      <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="project-link">View on GitHub →</a>
    </div>

    <!-- AI E-Commerce -->
    <div class="project-card">
      <div class="project-badge-wrap">
        <span class="badge badge-gold">AI-Powered</span>
        <span class="badge badge-rose">E-Commerce</span>
      </div>
      <div class="project-title">🛒 AI E-Commerce Platform</div>
      <div class="project-date">Oct 2024 — Jan 2025</div>
      <p class="project-desc">
        Intelligent e-commerce backend with AI-driven product recommendations using Spring AI and 
        vector similarity search via Redis Vector DB, generative AI chatbot for real-time support, 
        and AI-powered image generation pipeline.
      </p>
      <div class="project-chips">
        <span class="chip">React</span><span class="chip">Spring Boot</span>
        <span class="chip">Spring AI</span><span class="chip">Redis Vector DB</span>
        <span class="chip">Tailwind CSS</span>
      </div>
      <a href="https://github.com/Shravan157" target="_blank" class="project-link">View on GitHub →</a>
    </div>

    <!-- Zomato Sentiment -->
    <div class="project-card">
      <div class="project-badge-wrap">
        <span class="badge badge-green">ML / NLP</span>
      </div>
      <div class="project-title">🍽️ Zomato Sentiment Analysis</div>
      <div class="project-date">Data Science Project</div>
      <p class="project-desc">
        End-to-end NLP pipeline classifying 10,000+ restaurant reviews. 15 EDA visualizations, hypothesis 
        testing, TF-IDF vectorization, and model comparison (Logistic Regression, Random Forest, Naive Bayes). 
        Logistic Regression achieved the highest F1 score.
      </p>
      <div class="project-chips">
        <span class="chip">Python</span><span class="chip">Scikit-learn</span>
        <span class="chip">NLTK</span><span class="chip">TF-IDF</span>
        <span class="chip">Matplotlib</span>
      </div>
      <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="project-link">View on GitHub →</a>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ─── Experience ───
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Career</div>
  <h2 class="section-title">Work Experience</h2>
  <p class="section-sub">Real-world industry exposure</p>
  <div class="timeline">
    <div class="tl-card">
      <div class="tl-header">
        <div>
          <div class="tl-role">Data Science with Gen AI Intern</div>
          <div class="tl-org">Innovexis</div>
          <div class="tl-meta">Apr 2026 — Present · Remote</div>
        </div>
        <span class="tl-tag badge badge-green">Active</span>
      </div>
      <ul class="tl-bullets">
        <li>Selected from a competitive applicant pool for Innovexis's Data Science with Generative AI internship program</li>
        <li>Working on real-world data science projects integrating large language models and generative AI techniques</li>
        <li>Applying Python, NumPy, Pandas, and Scikit-learn for data analysis, preprocessing, and model building</li>
        <li>Gaining hands-on exposure to production-level Gen AI workflows, LLM integration, and applied machine learning</li>
      </ul>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Education ───
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Academia</div>
  <h2 class="section-title">Education</h2>
  <p class="section-sub">Academic background and credentials</p>
  <div class="timeline">
    <div class="tl-card">
      <div class="tl-header">
        <div>
          <div class="tl-role">B.Tech in CSE — Artificial Intelligence &amp; Machine Learning</div>
          <div class="tl-org">ViMEET — University of Mumbai</div>
          <div class="tl-meta">Jun 2023 — Present (Expected May 2027)</div>
        </div>
        <span class="tl-tag badge badge-cyan">In Progress</span>
      </div>
      <p style="color:var(--text-2); font-size:0.88rem; font-weight:300; line-height:1.7; margin-bottom:0.5rem;">
        Pursuing B.Tech in Computer Science Engineering with specialization in Artificial Intelligence &amp; Machine Learning 
        at Vishwaniketan's Institute of Management Entrepreneurship and Engineering Technology.
      </p>
      <span class="tl-cgpa">✦ CGPA: 7.5 / 10.0</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Contact ───
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Connect</div>
  <h2 class="section-title">Get in Touch</h2>
  <p class="section-sub">Open to collaborations, internships, and interesting conversations</p>
  <div class="contact-grid">
    <div class="contact-item">
      <div class="contact-icon">📧</div>
      <div class="contact-lbl">Email</div>
      <div class="contact-val"><a href="mailto:shravanparthe@gmail.com">shravanparthe<br>@gmail.com</a></div>
    </div>
    <div class="contact-item">
      <div class="contact-icon">📱</div>
      <div class="contact-lbl">Phone</div>
      <div class="contact-val">7385813010</div>
    </div>
    <div class="contact-item">
      <div class="contact-icon">💼</div>
      <div class="contact-lbl">LinkedIn</div>
      <div class="contact-val"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a></div>
    </div>
    <div class="contact-item">
      <div class="contact-icon">🐙</div>
      <div class="contact-lbl">GitHub</div>
      <div class="contact-val"><a href="https://github.com/Shravan157" target="_blank">Shravan157</a></div>
    </div>
    <div class="contact-item">
      <div class="contact-icon">📍</div>
      <div class="contact-lbl">Location</div>
      <div class="contact-val">Mumbai<br>India</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Footer ───
st.markdown("""
<div class="footer">
  <div class="footer-left">
    <p>Designed &amp; built by <a href="https://github.com/Shravan157" target="_blank">Shravan Parthe</a> · 2026</p>
  </div>
  <div class="footer-right">
    Mumbai, India · Open to opportunities
  </div>
</div>
""", unsafe_allow_html=True)
