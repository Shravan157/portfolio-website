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

/* ─── Bento Project Grid ─── */
@keyframes dash-flow {
  to { stroke-dashoffset: -20; }
}
@keyframes node-pulse {
  0%,100% { r: 6; opacity: 0.7; }
  50%      { r: 8; opacity: 1;   }
}

.bento {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}
.bento-card {
  background: var(--bg-1);
  border: 1px solid var(--border);
  border-top: 2px solid var(--ca, var(--gold));
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  min-height: 280px;
}
.bento-card::before {
  content: '';
  position: absolute;
  top: 0; right: 0;
  width: 220px; height: 220px;
  background: radial-gradient(circle at top right, var(--cg, rgba(212,175,55,0.06)) 0%, transparent 65%);
  pointer-events: none;
  transition: opacity 0.3s;
}
.bento-card::after {
  content: var(--cn, "01");
  position: absolute;
  bottom: -1.5rem; right: 1.25rem;
  font-family: var(--font-head);
  font-size: 8rem;
  font-weight: 800;
  color: var(--ca, var(--gold));
  opacity: 0.035;
  line-height: 1;
  pointer-events: none;
  user-select: none;
  letter-spacing: -4px;
}
.bento-card:hover {
  transform: translateY(-5px);
  background: var(--bg-2);
  border-color: var(--ca, var(--gold));
  box-shadow: 0 24px 56px rgba(0,0,0,0.55), 0 0 0 1px var(--ca, var(--gold));
}
.bento-card:hover::before { opacity: 1.6; }

/* Per-card accent palette */
.c-cyan   { --ca:#00e5cc; --cg:rgba(0,229,204,0.07);   --cn:"01"; }
.c-gold   { --ca:#d4af37; --cg:rgba(212,175,55,0.07);  --cn:"02"; }
.c-purple { --ca:#a78bfa; --cg:rgba(167,139,250,0.07); --cn:"03"; }
.c-rose   { --ca:#fb7185; --cg:rgba(251,113,133,0.07); --cn:"04"; }
.c-green  { --ca:#34d399; --cg:rgba(52,211,153,0.07);  --cn:"05"; }

/* Featured card (2-col) */
.bento-feat { grid-column: span 2; }
.bento-feat-inner {
  display: grid;
  grid-template-columns: 1fr 0.85fr;
  gap: 1.75rem;
  flex: 1;
}
.bento-feat-content { display: flex; flex-direction: column; }
.bento-feat-visual {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-3);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem;
  overflow: hidden;
  position: relative;
}
.bento-feat-visual::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 50%, rgba(0,229,204,0.06) 0%, transparent 70%);
}

/* Small domain icon top-right */
.bento-icon {
  position: absolute;
  top: 1.25rem; right: 1.25rem;
  width: 36px; height: 36px;
  opacity: 0.18;
  transition: opacity 0.3s;
}
.bento-card:hover .bento-icon { opacity: 0.35; }

/* Shared card parts */
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

.p-badges { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem; }
.p-title {
  font-family: var(--font-head);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-1);
  margin-bottom: 0.35rem;
  letter-spacing: -0.3px;
  line-height: 1.3;
}
.p-date {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-3);
  letter-spacing: 0.5px;
  margin-bottom: 0.85rem;
}
.p-desc {
  color: var(--text-2);
  font-size: 0.87rem;
  line-height: 1.75;
  font-weight: 300;
  margin-bottom: 1.25rem;
  flex: 1;
}
.p-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}
.chip {
  padding: 0.22rem 0.65rem;
  background: var(--bg-3);
  border: 1px solid var(--border);
  border-radius: 6px;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--text-3);
  transition: all 0.2s;
}
.bento-card:hover .chip {
  border-color: color-mix(in srgb, var(--ca) 30%, transparent);
  color: var(--ca);
}
.p-link {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: var(--ca, var(--gold));
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 600;
  font-family: var(--font-mono);
  transition: all 0.2s;
  margin-top: auto;
}
.p-link:hover { opacity: 0.75; gap: 0.65rem; }

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
  .bento { grid-template-columns: 1fr; }
  .bento-feat { grid-column: span 1; }
  .bento-feat-inner { grid-template-columns: 1fr; }
  .bento-feat-visual { display: none; }
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
  <p class="section-sub">Across healthcare AI, fintech, edtech, and machine learning</p>

  <div class="bento">

    <!-- ═══ 01 MedoraX — Featured 2-col ═══ -->
    <div class="bento-card bento-feat c-cyan">
      <div class="bento-feat-inner">

        <div class="bento-feat-content">
          <div class="p-badges">
            <span class="badge badge-cyan">Healthcare AI</span>
            <span class="badge badge-gold">Multimodal</span>
          </div>
          <div class="p-title">MedoraX AI — Clinical AI Assistant</div>
          <div class="p-date">OCT 2025 — NOV 2026</div>
          <p class="p-desc">
            A multimodal clinical AI assistant supporting voice, image, and text inputs.
            Transcribes symptoms via Whisper-large-v3, analyzes medical images via Llama-4-scout,
            and generates structured diagnostic responses using Llama-3.3-70b.
            Multilingual support in English, Hindi, and Marathi with GPS-based hospital finder
            and real-time AQI monitoring. Deployed on Hugging Face Spaces with 4–7s response times.
          </p>
          <div class="p-chips">
            <span class="chip">Python</span><span class="chip">Gradio</span>
            <span class="chip">Groq API</span><span class="chip">Whisper-v3</span>
            <span class="chip">Llama-4</span><span class="chip">Google Maps</span>
          </div>
          <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="p-link">
            View on GitHub &#8594;
          </a>
        </div>

        <div class="bento-feat-visual">
          <svg viewBox="0 0 210 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:210px;">
            <defs>
              <filter id="glow-c">
                <feGaussianBlur stdDeviation="2.5" result="blur"/>
                <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
            </defs>
            <!-- Input labels -->
            <text x="32" y="11" text-anchor="middle" font-size="7" fill="rgba(0,229,204,0.45)" font-family="monospace" letter-spacing="1">INPUTS</text>
            <!-- Voice node -->
            <circle cx="32" cy="45" r="20" fill="rgba(0,229,204,0.06)" stroke="#00e5cc" stroke-width="1.2" opacity="0.7"/>
            <text x="32" y="42" text-anchor="middle" font-size="9" fill="#00e5cc" font-weight="600">VOICE</text>
            <text x="32" y="53" text-anchor="middle" font-size="7" fill="rgba(0,229,204,0.55)">Whisper</text>
            <!-- Image node -->
            <circle cx="32" cy="100" r="20" fill="rgba(0,229,204,0.06)" stroke="#00e5cc" stroke-width="1.2" opacity="0.7"/>
            <text x="32" y="97" text-anchor="middle" font-size="9" fill="#00e5cc" font-weight="600">IMAGE</text>
            <text x="32" y="108" text-anchor="middle" font-size="7" fill="rgba(0,229,204,0.55)">Llama-4</text>
            <!-- Text node -->
            <circle cx="32" cy="155" r="20" fill="rgba(0,229,204,0.06)" stroke="#00e5cc" stroke-width="1.2" opacity="0.7"/>
            <text x="32" y="152" text-anchor="middle" font-size="9" fill="#00e5cc" font-weight="600">TEXT</text>
            <text x="32" y="163" text-anchor="middle" font-size="7" fill="rgba(0,229,204,0.55)">Direct</text>
            <!-- Dashed lines to hub -->
            <line x1="52" y1="55" x2="98" y2="92" stroke="#00e5cc" stroke-width="1" opacity="0.35" stroke-dasharray="5,4">
              <animate attributeName="stroke-dashoffset" from="0" to="-18" dur="2s" repeatCount="indefinite"/>
            </line>
            <line x1="52" y1="100" x2="98" y2="100" stroke="#00e5cc" stroke-width="1" opacity="0.35" stroke-dasharray="5,4">
              <animate attributeName="stroke-dashoffset" from="0" to="-18" dur="2s" repeatCount="indefinite"/>
            </line>
            <line x1="52" y1="145" x2="98" y2="108" stroke="#00e5cc" stroke-width="1" opacity="0.35" stroke-dasharray="5,4">
              <animate attributeName="stroke-dashoffset" from="0" to="-18" dur="2s" repeatCount="indefinite"/>
            </line>
            <!-- AI Hub -->
            <circle cx="118" cy="100" r="30" fill="rgba(0,229,204,0.08)" stroke="#00e5cc" stroke-width="1.5" filter="url(#glow-c)"/>
            <circle cx="118" cy="100" r="22" fill="none" stroke="rgba(0,229,204,0.3)" stroke-width="0.8" stroke-dasharray="3,3"/>
            <text x="118" y="96" text-anchor="middle" font-size="11" fill="#00e5cc" font-weight="700">AI</text>
            <text x="118" y="109" text-anchor="middle" font-size="7.5" fill="rgba(0,229,204,0.6)">Engine</text>
            <!-- Line to output -->
            <line x1="148" y1="100" x2="168" y2="100" stroke="#00e5cc" stroke-width="1.5" opacity="0.5" stroke-dasharray="5,4">
              <animate attributeName="stroke-dashoffset" from="0" to="-18" dur="1.5s" repeatCount="indefinite"/>
            </line>
            <!-- Output -->
            <rect x="168" y="78" width="38" height="44" rx="9" fill="rgba(0,229,204,0.07)" stroke="#00e5cc" stroke-width="1.2" opacity="0.75"/>
            <text x="187" y="97" text-anchor="middle" font-size="9" fill="#00e5cc" font-weight="700">Dx</text>
            <text x="187" y="109" text-anchor="middle" font-size="6.5" fill="rgba(0,229,204,0.55)">Report</text>
            <!-- Output label -->
            <text x="187" y="136" text-anchor="middle" font-size="7" fill="rgba(0,229,204,0.45)" font-family="monospace" letter-spacing="1">OUTPUT</text>
          </svg>
        </div>

      </div>
    </div>

    <!-- ═══ 02 SahayLoan ═══ -->
    <div class="bento-card c-gold">
      <!-- Domain icon: coin/rupee -->
      <svg class="bento-icon" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="18" cy="18" r="16" stroke="#d4af37" stroke-width="2"/>
        <text x="18" y="23" text-anchor="middle" font-size="14" fill="#d4af37" font-weight="700">&#8377;</text>
      </svg>
      <div class="p-badges">
        <span class="badge badge-gold">FinTech</span>
        <span class="badge badge-green">AI Scoring</span>
      </div>
      <div class="p-title">SahayLoan — Micro-Loan Platform</div>
      <div class="p-date">JAN 2026 — PRESENT</div>
      <p class="p-desc">
        Full-stack micro-lending platform (up to &#8377;1,00,000) with Flutter frontend, FastAPI backend,
        Random Forest credit scoring, Tesseract KYC, and Stripe EMI payments.
        Multi-role system with Firebase Auth and Firestore.
      </p>
      <div class="p-chips">
        <span class="chip">Flutter</span><span class="chip">FastAPI</span>
        <span class="chip">Scikit-learn</span><span class="chip">Firebase</span>
        <span class="chip">Tesseract</span><span class="chip">Stripe</span>
      </div>
      <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="p-link">View on GitHub &#8594;</a>
    </div>

    <!-- ═══ 03 SikshaSetu ═══ -->
    <div class="bento-card c-purple">
      <!-- Domain icon: graduation cap outline -->
      <svg class="bento-icon" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
        <polygon points="18,4 34,13 18,22 2,13" stroke="#a78bfa" stroke-width="1.8" fill="none"/>
        <path d="M8 16 L8 26 Q18 31 28 26 L28 16" stroke="#a78bfa" stroke-width="1.8" fill="none" stroke-linejoin="round"/>
        <line x1="34" y1="13" x2="34" y2="22" stroke="#a78bfa" stroke-width="1.8"/>
      </svg>
      <div class="p-badges">
        <span class="badge badge-purple">Full-Stack</span>
        <span class="badge badge-cyan">EdTech</span>
      </div>
      <div class="p-title">SikshaSetu — Rural Education Platform</div>
      <div class="p-date">JAN 2025 — APR 2025</div>
      <p class="p-desc">
        Education platform bridging the digital divide. RBAC with Spring Security + JWT/OAuth 2.0,
        optimized MySQL schema, React.js frontend, and ZEGOCLOUD real-time video SDK for virtual classrooms.
      </p>
      <div class="p-chips">
        <span class="chip">React</span><span class="chip">Spring Boot</span>
        <span class="chip">JWT</span><span class="chip">MySQL</span>
        <span class="chip">ZEGOCLOUD</span>
      </div>
      <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="p-link">View on GitHub &#8594;</a>
    </div>

    <!-- ═══ 04 AI E-Commerce ═══ -->
    <div class="bento-card c-rose">
      <!-- Domain icon: vector DB / nodes -->
      <svg class="bento-icon" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="10" cy="10" r="5" stroke="#fb7185" stroke-width="1.8"/>
        <circle cx="26" cy="10" r="5" stroke="#fb7185" stroke-width="1.8"/>
        <circle cx="18" cy="26" r="5" stroke="#fb7185" stroke-width="1.8"/>
        <line x1="14" y1="12" x2="22" y2="12" stroke="#fb7185" stroke-width="1.4"/>
        <line x1="12" y1="14" x2="16" y2="22" stroke="#fb7185" stroke-width="1.4"/>
        <line x1="24" y1="14" x2="20" y2="22" stroke="#fb7185" stroke-width="1.4"/>
      </svg>
      <div class="p-badges">
        <span class="badge badge-rose">E-Commerce</span>
        <span class="badge badge-gold">Spring AI</span>
      </div>
      <div class="p-title">AI-Powered E-Commerce Platform</div>
      <div class="p-date">OCT 2024 — JAN 2025</div>
      <p class="p-desc">
        Intelligent backend with Spring AI product recommendations, Redis Vector DB similarity search,
        generative AI chatbot for real-time support, and an AI-powered image generation pipeline.
      </p>
      <div class="p-chips">
        <span class="chip">React</span><span class="chip">Spring Boot</span>
        <span class="chip">Spring AI</span><span class="chip">Redis VectorDB</span>
        <span class="chip">Tailwind</span>
      </div>
      <a href="https://github.com/Shravan157" target="_blank" class="p-link">View on GitHub &#8594;</a>
    </div>

    <!-- ═══ 05 Zomato NLP ═══ -->
    <div class="bento-card c-green">
      <!-- Domain icon: bar chart -->
      <svg class="bento-icon" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="4"  y="22" width="6" height="10" rx="2" stroke="#34d399" stroke-width="1.8"/>
        <rect x="13" y="14" width="6" height="18" rx="2" stroke="#34d399" stroke-width="1.8"/>
        <rect x="22" y="6"  width="6" height="26" rx="2" stroke="#34d399" stroke-width="1.8"/>
        <line x1="2" y1="33" x2="34" y2="33" stroke="#34d399" stroke-width="1.5" opacity="0.5"/>
      </svg>
      <div class="p-badges">
        <span class="badge badge-green">ML / NLP</span>
      </div>
      <div class="p-title">Zomato Sentiment Analysis</div>
      <div class="p-date">DATA SCIENCE PROJECT</div>
      <p class="p-desc">
        End-to-end NLP pipeline classifying 10,000+ restaurant reviews. 15 EDA visualizations,
        hypothesis testing, TF-IDF vectorization, and model comparison (Logistic Regression,
        Random Forest, Naive Bayes) — highest F1 via Logistic Regression.
      </p>
      <div class="p-chips">
        <span class="chip">Python</span><span class="chip">Scikit-learn</span>
        <span class="chip">NLTK</span><span class="chip">TF-IDF</span>
        <span class="chip">Matplotlib</span>
      </div>
      <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="p-link">View on GitHub &#8594;</a>
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
