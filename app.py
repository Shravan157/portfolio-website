import streamlit as st
import base64
import os

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Shravan Parthe — Portfolio",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Resume download helper ────────────────────────────────────────────────────
def get_resume_link():
    resume_path = os.path.join(os.path.dirname(__file__), "resume_shravan2.pdf")
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f'<a href="data:application/pdf;base64,{data}" download="Shravan_Parthe_Resume.pdf" class="mc-btn-primary">Download Resume →</a>'
    return '<a href="#" class="mc-btn-primary">Resume Coming Soon →</a>'

# ── Mastercard Design System CSS ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sofia+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap');

/* ── Tokens ── */
:root {
  --canvas:   #F3F0EE;
  --lifted:   #FCFBFA;
  --ink:      #141413;
  --white:    #FFFFFF;
  --slate:    #696969;
  --signal:   #CF4500;
  --orbit:    #F37338;
  --r-btn:    20px;
  --r-hero:   40px;
  --r-pill:   999px;
}

/* ── Base ── */
html, body, [class*="css"] {
  font-family: 'Sofia Sans', SofiaSans, Arial, sans-serif !important;
  background: var(--canvas) !important;
  color: var(--ink) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
section.main > div { padding-top: 0 !important; }
.block-container {
  max-width: 1280px !important;
  padding: 0 52px 80px 52px !important;
  margin: 0 auto !important;
}
[data-testid="stVerticalBlock"] > div { gap: 0 !important; }

/* ── Floating nav pill ── */
.mc-nav {
  position: sticky; top: 20px; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  background: var(--white);
  border-radius: var(--r-pill);
  padding: 14px 40px;
  box-shadow: rgba(0,0,0,0.04) 0px 4px 24px 0px;
  margin: 24px 0 96px 0;
}
.mc-nav-logo {
  font-size: 17px; font-weight: 700;
  letter-spacing: -0.04em; color: var(--ink);
}
.mc-nav-logo .dot { color: var(--orbit); font-size: 22px; vertical-align: -2px; }
.mc-nav-links { display: flex; gap: 44px; list-style: none; margin: 0; padding: 0; }
.mc-nav-links a {
  font-size: 15px; font-weight: 500; letter-spacing: -0.02em;
  color: var(--ink); text-decoration: none; transition: color 0.15s;
}
.mc-nav-links a:hover { color: var(--orbit); }
.mc-nav-avail {
  display: flex; align-items: center; gap: 8px;
  font-size: 13px; font-weight: 500; color: var(--slate);
}
.mc-nav-dot {
  width: 8px; height: 8px; background: #22C55E;
  border-radius: 50%; box-shadow: 0 0 6px #22C55E;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0%,100% { opacity:1; transform:scale(1); }
  50%      { opacity:0.5; transform:scale(0.85); }
}

/* ── Eyebrow ── */
.mc-eyebrow {
  font-size: 13px; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: var(--ink);
  display: inline-flex; align-items: center; gap: 7px; margin-bottom: 18px;
}
.mc-eyebrow::before { content:'●'; font-size: 7px; color: var(--orbit); }

/* ── Ghost watermark ── */
.mc-ghost {
  font-size: clamp(56px, 9vw, 112px); font-weight: 700;
  letter-spacing: -0.03em; color: #E4DDD7;
  line-height: 1; margin: 0; user-select: none; pointer-events: none;
}

/* ── Buttons ── */
.mc-btn-primary {
  display: inline-block;
  background: var(--ink); color: var(--canvas) !important;
  border: 1.5px solid var(--ink); border-radius: var(--r-btn);
  padding: 11px 28px; font-size: 15px; font-weight: 500;
  letter-spacing: -0.02em; text-decoration: none; cursor: pointer;
  transition: opacity .15s; white-space: nowrap;
}
.mc-btn-primary:hover { opacity: .82; }
.mc-btn-secondary {
  display: inline-block;
  background: var(--white); color: var(--ink) !important;
  border: 1.5px solid var(--ink); border-radius: var(--r-btn);
  padding: 11px 28px; font-size: 15px; font-weight: 450;
  letter-spacing: -0.02em; text-decoration: none; cursor: pointer;
  transition: background .15s; white-space: nowrap;
}
.mc-btn-secondary:hover { background: var(--canvas); }

/* ── Hero ── */
.mc-hero { padding: 0 0 120px 0; }
.mc-hero-headline {
  font-size: clamp(40px,5.5vw,72px); font-weight: 500;
  letter-spacing: -0.025em; line-height: 1.0; color: var(--ink);
  margin: 0 0 28px 0; max-width: 700px;
}
.mc-hero-headline em { font-style: normal; color: var(--orbit); }
.mc-hero-sub {
  font-family: 'Sofia Sans', monospace; font-size: 15px; font-weight: 500;
  color: var(--slate); letter-spacing: 0.01em; margin-bottom: 20px;
}
.mc-hero-body {
  font-size: 17px; font-weight: 400; line-height: 1.65;
  color: var(--slate); max-width: 500px; margin: 0 0 40px 0;
}
/* Code card */
.mc-code-card {
  background: var(--ink); border-radius: var(--r-hero);
  padding: 36px 36px 32px; color: var(--canvas);
  font-family: 'Sofia Sans', monospace; font-size: 14px;
  line-height: 2.1; position: relative; overflow: hidden;
}
.mc-code-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--orbit) 0%, transparent 100%);
}
.mc-code-bar {
  display: flex; gap: 7px; align-items: center;
  margin-bottom: 24px; padding-bottom: 16px;
  border-bottom: 1px solid rgba(243,240,238,0.1);
}
.mc-code-dot { width: 10px; height: 10px; border-radius: 50%; }
.dot-r { background: #FF5F57; }
.dot-y { background: #FFBD2E; }
.dot-g { background: #28CA41; box-shadow: 0 0 6px rgba(40,202,65,0.8); }
.mc-code-filename {
  margin-left: auto; font-size: 12px;
  color: rgba(243,240,238,0.35); letter-spacing: 0.04em;
}
.kw  { color: #B99EF5; }
.fn  { color: #7DD3FC; }
.str { color: #86EFAC; }
.cm  { color: rgba(243,240,238,0.35); }
.nm  { color: var(--orbit); }

/* ── Stats ── */
.mc-stats {
  display: grid; grid-template-columns: repeat(4,1fr); gap: 16px;
  margin: 0 0 120px 0;
}
.mc-stat {
  background: var(--lifted); border-radius: 28px; padding: 32px 24px;
  text-align: center; transition: transform .2s, box-shadow .2s;
  position: relative; overflow: hidden;
}
.mc-stat::after {
  content: ''; position: absolute; bottom: 0; left: 50%;
  transform: translateX(-50%); height: 3px; width: 36px;
  border-radius: 2px; background: var(--orbit); transition: width .25s;
}
.mc-stat:hover { transform: translateY(-5px); box-shadow: rgba(0,0,0,0.08) 0px 20px 40px; }
.mc-stat:hover::after { width: 72px; }
.mc-stat-num {
  font-size: 44px; font-weight: 500; letter-spacing: -0.04em;
  color: var(--ink); line-height: 1;
}
.mc-stat-num .accent { color: var(--orbit); }
.mc-stat-label {
  font-size: 12px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.06em; color: var(--slate); margin-top: 6px;
}

/* ── Section header ── */
.mc-sec-head { position: relative; margin-bottom: 56px; }
.mc-sec-title {
  font-size: clamp(32px,3.5vw,48px); font-weight: 500;
  letter-spacing: -0.025em; line-height: 1.1;
  color: var(--ink); margin: 0 0 14px 0;
}
.mc-sec-sub {
  font-size: 16px; font-weight: 400; line-height: 1.6;
  color: var(--slate); max-width: 460px; margin: 0;
}

/* ── Skills ── */
.mc-skills-wrap { margin-bottom: 128px; }
.mc-skill-cat {
  font-size: 12px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.07em; color: var(--slate); margin: 28px 0 10px 4px;
}
.mc-skill-cat:first-child { margin-top: 0; }
.mc-pill-group { display: flex; flex-wrap: wrap; gap: 8px; }
.mc-pill {
  display: inline-block; background: var(--white);
  border: 1.5px solid var(--ink); border-radius: var(--r-pill);
  padding: 8px 20px; font-size: 14px; font-weight: 500;
  color: var(--ink); transition: background .15s, color .15s; cursor: default;
}
.mc-pill:hover { background: var(--ink); color: var(--canvas); }

/* ── Project cards ── */
.mc-projects-wrap { margin-bottom: 128px; }
.mc-proj {
  background: var(--lifted); border-radius: 40px;
  padding: 44px 44px 40px; margin-bottom: 20px;
  transition: transform .2s, box-shadow .2s;
  position: relative; overflow: hidden;
}
.mc-proj:hover {
  transform: translateY(-4px);
  box-shadow: rgba(0,0,0,0.08) 0px 24px 48px;
}
.mc-proj-num {
  position: absolute; bottom: -28px; right: 44px;
  font-size: 96px; font-weight: 700; color: #E4DDD7;
  line-height: 1; user-select: none; letter-spacing: -0.04em;
}
.mc-proj-arrow {
  position: absolute; top: 44px; right: 44px;
  width: 50px; height: 50px; background: var(--ink); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: var(--canvas); font-size: 18px; text-decoration: none;
  transition: background .15s;
}
.mc-proj-arrow:hover { background: var(--orbit); }
.mc-proj-icon { font-size: 28px; margin-bottom: 14px; }
.mc-proj-badge {
  display: inline-block; border: 1.5px solid var(--ink);
  border-radius: var(--r-pill); padding: 3px 14px;
  font-size: 11px; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; color: var(--ink);
  background: var(--white); margin-bottom: 16px;
}
.mc-proj-title {
  font-size: 22px; font-weight: 500; letter-spacing: -0.02em;
  color: var(--ink); margin: 0 0 12px 0; line-height: 1.2;
  max-width: calc(100% - 80px);
}
.mc-proj-desc {
  font-size: 15px; font-weight: 400; line-height: 1.7;
  color: var(--slate); margin: 0 0 24px 0;
}
.mc-proj-tech { display: flex; flex-wrap: wrap; gap: 6px; }
.mc-proj-chip {
  display: inline-block; background: rgba(20,20,19,0.06);
  border-radius: var(--r-pill); padding: 5px 14px;
  font-size: 12px; font-weight: 500; color: var(--ink);
  border: 1px solid rgba(20,20,19,0.15);
}

/* ── Experience & Education ── */
.mc-timeline-wrap { margin-bottom: 128px; }
.mc-tl-item {
  display: flex; gap: 32px; margin-bottom: 52px; position: relative;
}
.mc-tl-year {
  font-size: 13px; font-weight: 700; color: var(--orbit);
  min-width: 96px; padding-top: 5px; text-align: right; flex-shrink: 0;
}
.mc-tl-connector {
  display: flex; flex-direction: column; align-items: center;
  padding-top: 6px; flex-shrink: 0;
}
.mc-tl-dot {
  width: 10px; height: 10px; background: var(--orbit);
  border-radius: 50%; box-shadow: 0 0 8px rgba(243,115,56,0.5);
  flex-shrink: 0;
}
.mc-tl-line {
  width: 1px; flex: 1; background: linear-gradient(to bottom, var(--orbit), rgba(243,115,56,0));
  margin-top: 6px; min-height: 60px;
}
.mc-tl-body {}
.mc-tl-role {
  font-size: 19px; font-weight: 500; letter-spacing: -0.02em;
  color: var(--ink); margin: 0 0 4px 0;
}
.mc-tl-org { font-size: 14px; font-weight: 500; color: var(--orbit); margin: 0 0 6px 0; }
.mc-tl-meta { font-size: 13px; font-weight: 400; color: var(--slate); margin: 0 0 12px 0; }
.mc-tl-bullets {
  font-size: 15px; font-weight: 400; line-height: 1.75;
  color: var(--slate); padding-left: 18px; margin: 0;
}
.mc-tl-bullets li { margin-bottom: 4px; }
.mc-cgpa {
  display: inline-block; margin-top: 8px;
  background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.3);
  border-radius: var(--r-pill); padding: 4px 16px;
  font-size: 13px; font-weight: 600; color: #16A34A;
}

/* ── Contact ── */
.mc-contact-wrap {
  background: var(--ink); border-radius: 40px;
  padding: 80px 80px 72px; margin-bottom: 80px;
  position: relative; overflow: hidden;
}
.mc-contact-wrap::after {
  content: 'Hello'; position: absolute;
  bottom: -40px; right: -10px;
  font-size: 180px; font-weight: 700; letter-spacing: -0.05em;
  color: rgba(243,240,238,0.04); line-height: 1; user-select: none;
}
.mc-contact-eyebrow {
  font-size: 12px; font-weight: 700; letter-spacing: 0.07em;
  text-transform: uppercase; color: rgba(243,240,238,0.4);
  display: inline-flex; align-items: center; gap: 7px; margin-bottom: 20px;
}
.mc-contact-eyebrow::before { content:'●'; font-size:7px; color: var(--orbit); }
.mc-contact-headline {
  font-size: clamp(28px,3.5vw,48px); font-weight: 500;
  letter-spacing: -0.025em; line-height: 1.1;
  color: var(--canvas); margin: 0 0 18px 0; max-width: 560px;
}
.mc-contact-sub {
  font-size: 16px; font-weight: 400; line-height: 1.6;
  color: rgba(243,240,238,0.55); max-width: 440px; margin: 0 0 44px 0;
}
.mc-contact-btn {
  display: inline-block; background: var(--canvas); color: var(--ink) !important;
  border-radius: var(--r-btn); padding: 12px 32px;
  font-size: 15px; font-weight: 500; letter-spacing: -0.02em;
  text-decoration: none; transition: opacity .15s; margin-right: 12px;
}
.mc-contact-btn:hover { opacity: .85; }
.mc-contact-links { display: flex; gap: 28px; margin-top: 40px; flex-wrap: wrap; }
.mc-contact-link {
  color: rgba(243,240,238,0.5) !important; font-size: 13px;
  font-weight: 400; text-decoration: none; letter-spacing: 0.02em;
  transition: color .15s;
}
.mc-contact-link:hover { color: var(--canvas) !important; }
.mc-contact-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 14px; margin-top: 0;
}
.mc-contact-item {
  background: rgba(243,240,238,0.05);
  border: 1px solid rgba(243,240,238,0.1);
  border-radius: 20px; padding: 22px 20px; text-align: center;
  transition: background .15s;
}
.mc-contact-item:hover { background: rgba(243,240,238,0.09); }
.mc-contact-item-icon { font-size: 22px; margin-bottom: 6px; }
.mc-contact-item-label {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.07em; color: rgba(243,240,238,0.35); margin-bottom: 4px;
}
.mc-contact-item-val {
  font-size: 13px; font-weight: 400; color: rgba(243,240,238,0.75);
}
.mc-contact-item-val a {
  color: var(--orbit) !important; text-decoration: none;
}

/* ── Quote ── */
.mc-quote {
  text-align: center; padding: 60px 40px 0; margin-bottom: 48px;
  position: relative;
}
.mc-quote-text {
  font-size: clamp(15px, 2vw, 18px); font-weight: 400;
  line-height: 2; color: var(--slate); max-width: 500px;
  margin: 0 auto 12px; font-style: italic;
}
.mc-quote-highlight { color: var(--orbit); font-style: italic; font-weight: 500; }
.mc-quote-author {
  font-size: 12px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.07em; color: #C4BEB8;
}

/* ── Footer ── */
.mc-footer {
  border-top: 1px solid rgba(20,20,19,0.12);
  padding: 28px 0 40px;
  display: flex; justify-content: space-between;
  align-items: center; flex-wrap: wrap; gap: 12px;
}
.mc-footer-copy { font-size: 13px; font-weight: 400; color: var(--slate); }
.mc-footer-dot {
  display: inline-block; width: 8px; height: 8px;
  background: var(--orbit); border-radius: 50%;
  margin-right: 8px; vertical-align: middle;
}

/* ── SVG orbital arcs ── */
.mc-arc { display: block; width: 100%; overflow: visible; }

/* ── Responsive ── */
@media (max-width: 768px) {
  .block-container { padding: 0 20px 60px !important; }
  .mc-nav-links { display: none; }
  .mc-stats { grid-template-columns: repeat(2,1fr); }
  .mc-contact-wrap { padding: 48px 32px; }
  .mc-contact-wrap::after { font-size: 80px; }
  .mc-tl-item { flex-direction: column; gap: 12px; }
  .mc-tl-year { text-align: left; }
}
</style>
""", unsafe_allow_html=True)

# ── Nav ───────────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="mc-nav">
  <span class="mc-nav-logo">Shravan<span class="dot">●</span>Dev</span>
  <ul class="mc-nav-links">
    <li><a href="#skills">Skills</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <div class="mc-nav-avail">
    <span class="mc-nav-dot"></span> Open to work
  </div>
</nav>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
col1, col2 = st.columns([55, 45], gap="large")

with col1:
    resume_link = get_resume_link()
    st.markdown(f"""
    <section class="mc-hero">
      <p class="mc-eyebrow">Backend Engineer · AI/ML Developer · B.Tech CSE 2027</p>
      <h1 class="mc-hero-headline">I'm <em>Shravan</em> Parthe.<br>I build intelligent systems.</h1>
      <p class="mc-hero-sub">// Java · Spring Boot · Python · AI/ML · Flutter</p>
      <p class="mc-hero-body">
        Results-driven CS student specialising in AI & ML with hands-on expertise in backend
        development. I build scalable, production-ready applications spanning fintech,
        healthcare, and edtech — bridging robust backends with intelligent AI features.
      </p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
        {resume_link}
        <a class="mc-btn-secondary" href="https://github.com/Shravan157" target="_blank">GitHub ↗</a>
        <a class="mc-btn-secondary" href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">LinkedIn ↗</a>
      </div>
    </section>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="padding-top:40px;">
    <div class="mc-code-card">
      <div class="mc-code-bar">
        <span class="mc-code-dot dot-r"></span>
        <span class="mc-code-dot dot-y"></span>
        <span class="mc-code-dot dot-g"></span>
        <span class="mc-code-filename">Developer.java</span>
      </div>
      <div><span class="cm">// open to work ✓</span></div>
      <div><span class="kw">class</span> <span class="fn">Developer</span> {</div>
      <div>&nbsp;&nbsp;<span class="kw">String</span> name = <span class="str">"Shravan"</span>;</div>
      <div>&nbsp;&nbsp;<span class="kw">int</span> year = <span class="nm">3</span>;</div>
      <div>&nbsp;&nbsp;<span class="kw">String[]</span> stack = {</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Java"</span>, <span class="str">"SpringBoot"</span>,</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Python"</span>, <span class="str">"Flutter"</span>,</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"React"</span>, <span class="str">"FastAPI"</span></div>
      <div>&nbsp;&nbsp;};</div>
      <div>&nbsp;&nbsp;<span class="kw">boolean</span> hireable = <span class="nm">true</span>;</div>
      <div>}</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="mc-stats">
  <div class="mc-stat">
    <div class="mc-stat-num">5<span class="accent">+</span></div>
    <div class="mc-stat-label">Projects Shipped</div>
  </div>
  <div class="mc-stat">
    <div class="mc-stat-num">7<span class="accent">.</span>5</div>
    <div class="mc-stat-label">CGPA</div>
  </div>
  <div class="mc-stat">
    <div class="mc-stat-num">3<span class="accent">rd</span></div>
    <div class="mc-stat-label">Year B.Tech</div>
  </div>
  <div class="mc-stat">
    <div class="mc-stat-num">1<span class="accent">+</span></div>
    <div class="mc-stat-label">Internship</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Orbital arc ───────────────────────────────────────────────────────────────
st.markdown("""
<svg class="mc-arc" height="48" viewBox="0 0 1200 48" fill="none" preserveAspectRatio="none" style="margin-bottom:80px;">
  <path d="M0 40 Q300 4 600 24 Q900 44 1200 8" stroke="#F37338" stroke-width="1.5" fill="none" opacity="0.55"/>
</svg>
""", unsafe_allow_html=True)

# ── Skills ────────────────────────────────────────────────────────────────────
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

SKILLS = {
    "Languages":       ["Java", "Python", "JavaScript", "Dart", "SQL"],
    "Frameworks":      ["Spring Boot", "Spring Security", "Spring AI", "FastAPI", "React", "Flutter"],
    "AI / ML":         ["Scikit-learn", "NumPy", "Pandas", "NLTK", "TF-IDF", "Groq API", "LLM Integration"],
    "Tools & DevOps":  ["Docker", "GitHub", "Firebase", "Tesseract OCR", "Redis", "Stripe"],
    "Databases":       ["MySQL", "PostgreSQL", "Firebase Firestore", "Redis Vector DB"],
}

st.markdown("""
<div class="mc-skills-wrap">
  <div class="mc-sec-head">
    <p class="mc-ghost" aria-hidden="true">Stack</p>
    <p class="mc-eyebrow" style="margin-top:-20px;">Skills & Tools</p>
    <h2 class="mc-sec-title">My technical toolkit.</h2>
    <p class="mc-sec-sub">Technologies I reach for when building production-grade, intelligent software.</p>
  </div>
""", unsafe_allow_html=True)

sc1, sc2 = st.columns(2, gap="large")
items = list(SKILLS.items())
for i, (cat, pills) in enumerate(items):
    pills_html = "".join(f'<span class="mc-pill">{p}</span>' for p in pills)
    block = f'<div class="mc-skill-cat">{cat}</div><div class="mc-pill-group">{pills_html}</div><br>'
    if i < 3:
        with sc1:
            st.markdown(block, unsafe_allow_html=True)
    else:
        with sc2:
            st.markdown(block, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── Orbital arc ───────────────────────────────────────────────────────────────
st.markdown("""
<svg class="mc-arc" height="40" viewBox="0 0 1200 40" fill="none" preserveAspectRatio="none" style="margin-bottom:80px;">
  <path d="M1200 32 Q900 4 600 22 Q300 40 0 8" stroke="#F37338" stroke-width="1" fill="none" opacity="0.4"/>
</svg>
""", unsafe_allow_html=True)

# ── Projects ─────────────────────────────────────────────────────────────────
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="mc-projects-wrap">
  <div class="mc-sec-head">
    <p class="mc-ghost" aria-hidden="true">Work</p>
    <p class="mc-eyebrow" style="margin-top:-20px;">Featured Projects</p>
    <h2 class="mc-sec-title">Things I've built that I'm proud of.</h2>
    <p class="mc-sec-sub">Spanning healthcare AI, fintech, edtech, and data science — each project is production-minded.</p>
  </div>
""", unsafe_allow_html=True)

PROJECTS = [
    {
        "icon": "🏥",
        "badge": "Healthcare AI",
        "title": "MedoraX AI — Clinical AI Assistant",
        "date": "Oct 2025 — Nov 2026",
        "desc": "Multimodal clinical AI assistant supporting voice, image & text inputs — transcribing symptoms via Whisper-large-v3, analysing medical images via Llama-4-scout, generating structured diagnostic responses via Llama-3.3-70b. Multilingual support (English, Hindi, Marathi) with GPS-based hospital finder and real-time AQI monitoring.",
        "tech": ["Python", "Gradio", "Groq API", "Google Maps API", "Whisper"],
        "link": "https://github.com/Shravan157/MedX-AI-Clinical-Assistant",
    },
    {
        "icon": "🏦",
        "badge": "FinTech",
        "title": "SahayLoan — Micro-Loan Platform",
        "date": "Jan 2026 — Present",
        "desc": "Full-stack micro-lending platform (loans up to ₹1,00,000) with Flutter frontend and FastAPI backend. AI credit scoring via Random Forest, digital KYC with Aadhaar & PAN OCR via Tesseract, Stripe EMI integration, and multi-role system with Firebase Auth and Firestore.",
        "tech": ["Flutter", "Dart", "FastAPI", "Scikit-learn", "Firebase", "Tesseract OCR", "Stripe"],
        "link": "https://github.com/Shravan157/Sahay-Loan",
    },
    {
        "icon": "🎓",
        "badge": "Full-Stack",
        "title": "SikshaSetu — Rural Education Platform",
        "date": "Jan 2025 — Apr 2025",
        "desc": "Full-stack platform bridging the digital divide for rural communities. Role-based access with Spring Security & JWT/OAuth 2.0, Spring Data JPA, responsive React frontend, and ZEGOCLOUD real-time video SDK for virtual classrooms.",
        "tech": ["React", "Spring Boot", "Spring Security", "JWT", "MySQL", "Spring Data JPA"],
        "link": "https://github.com/Shravan157/SikshaSetu_Edu_App",
    },
    {
        "icon": "🛒",
        "badge": "AI / Full-Stack",
        "title": "AI-Powered E-Commerce Platform",
        "date": "Oct 2024 — Jan 2025",
        "desc": "Intelligent e-commerce backend with AI-driven product recommendations using Spring AI and vector similarity search via Redis Vector DB. Generative AI chatbot for real-time customer support and AI-powered product image generation pipeline.",
        "tech": ["React", "Spring Boot", "Spring AI", "Redis Vector DB", "JWT", "Tailwind CSS"],
        "link": "https://github.com/Shravan157",
    },
    {
        "icon": "🍽️",
        "badge": "ML / NLP",
        "title": "Zomato Sentiment Analysis",
        "date": "Data Science Project",
        "desc": "End-to-end NLP project classifying 10,000+ Zomato restaurant reviews. EDA with 15 visualisations, TF-IDF vectorisation, model comparison (Logistic Regression, Random Forest, Naive Bayes). Logistic Regression achieved the highest F1 score.",
        "tech": ["Python", "Scikit-learn", "NLTK", "TF-IDF", "Pandas", "Matplotlib"],
        "link": "https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis",
    },
]

pc1, pc2 = st.columns(2, gap="large")
for i, proj in enumerate(PROJECTS):
    tech_html = "".join(f'<span class="mc-proj-chip">{t}</span>' for t in proj["tech"])
    card = f"""
    <div class="mc-proj">
      <a class="mc-proj-arrow" href="{proj['link']}" target="_blank">↗</a>
      <div class="mc-proj-icon">{proj['icon']}</div>
      <span class="mc-proj-badge">{proj['badge']}</span>
      <h3 class="mc-proj-title">{proj['title']}</h3>
      <p style="font-size:12px;color:var(--orbit);font-weight:600;margin:0 0 12px;letter-spacing:0.02em;">📅 {proj['date']}</p>
      <p class="mc-proj-desc">{proj['desc']}</p>
      <div class="mc-proj-tech">{tech_html}</div>
      <div class="mc-proj-num">0{i+1}</div>
    </div>
    """
    if i % 2 == 0:
        with pc1:
            st.markdown(card, unsafe_allow_html=True)
    else:
        with pc2:
            st.markdown(card, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── Orbital arc ───────────────────────────────────────────────────────────────
st.markdown("""
<svg class="mc-arc" height="44" viewBox="0 0 1200 44" fill="none" preserveAspectRatio="none" style="margin-bottom:80px;">
  <path d="M0 36 Q400 6 700 28 Q950 44 1200 12" stroke="#F37338" stroke-width="1.5" fill="none" opacity="0.5"/>
</svg>
""", unsafe_allow_html=True)

# ── Experience ────────────────────────────────────────────────────────────────
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="mc-timeline-wrap">
  <div class="mc-sec-head">
    <p class="mc-ghost" aria-hidden="true">Journey</p>
    <p class="mc-eyebrow" style="margin-top:-20px;">Experience & Education</p>
    <h2 class="mc-sec-title">Where I've worked & learned.</h2>
  </div>

  <div class="mc-tl-item">
    <div class="mc-tl-year">Apr 2026<br>— Present</div>
    <div class="mc-tl-connector"><div class="mc-tl-dot"></div><div class="mc-tl-line"></div></div>
    <div class="mc-tl-body">
      <p class="mc-tl-role">Data Science with Gen AI Intern</p>
      <p class="mc-tl-org">@ Innovexis</p>
      <p class="mc-tl-meta">Remote · Present</p>
      <ul class="mc-tl-bullets">
        <li>Selected for Innovexis's competitive Data Science with Generative AI internship after shortlisting from multiple applicants.</li>
        <li>Working on real-world projects integrating large language models and generative AI techniques.</li>
        <li>Applying Python, NumPy, Pandas, and Scikit-learn for data analysis, preprocessing, and model building.</li>
        <li>Gaining hands-on exposure to production-level Gen AI workflows and applied machine learning.</li>
      </ul>
    </div>
  </div>

  <div class="mc-tl-item">
    <div class="mc-tl-year">Jun 2023<br>— May 2027</div>
    <div class="mc-tl-connector"><div class="mc-tl-dot"></div><div class="mc-tl-line"></div></div>
    <div class="mc-tl-body">
      <p class="mc-tl-role">B.Tech in Computer Science Engineering (AI & ML)</p>
      <p class="mc-tl-org">@ ViMEET, University of Mumbai</p>
      <p class="mc-tl-meta">Mumbai, India · Expected May 2027</p>
      <p style="font-size:15px;font-weight:400;line-height:1.75;color:var(--slate);margin:0;">
        Specialising in Artificial Intelligence & Machine Learning. Coursework includes
        Data Structures & Algorithms, Machine Learning, Cloud Computing,
        Microservices Architecture, and System Design.
      </p>
      <span class="mc-cgpa">✦ CGPA: 7.5 / 10.0</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Contact ───────────────────────────────────────────────────────────────────
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="mc-contact-wrap">
  <p class="mc-contact-eyebrow">Let's work together</p>
  <h2 class="mc-contact-headline">Have a project or opportunity in mind?</h2>
  <p class="mc-contact-sub">
    Whether it's a backend system, an AI feature, or a full product build — drop me a message
    and let's figure it out together.
  </p>
  <div>
    <a class="mc-contact-btn" href="mailto:shravanparthe@gmail.com">Send an email →</a>
  </div>

  <div class="mc-contact-grid" style="margin-top:40px;">
    <div class="mc-contact-item">
      <div class="mc-contact-item-icon">📧</div>
      <div class="mc-contact-item-label">Email</div>
      <div class="mc-contact-item-val"><a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a></div>
    </div>
    <div class="mc-contact-item">
      <div class="mc-contact-item-icon">📱</div>
      <div class="mc-contact-item-label">Phone</div>
      <div class="mc-contact-item-val">7385813010</div>
    </div>
    <div class="mc-contact-item">
      <div class="mc-contact-item-icon">💼</div>
      <div class="mc-contact-item-label">LinkedIn</div>
      <div class="mc-contact-item-val"><a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe ↗</a></div>
    </div>
    <div class="mc-contact-item">
      <div class="mc-contact-item-icon">🐙</div>
      <div class="mc-contact-item-label">GitHub</div>
      <div class="mc-contact-item-val"><a href="https://github.com/Shravan157" target="_blank">Shravan157 ↗</a></div>
    </div>
    <div class="mc-contact-item">
      <div class="mc-contact-item-icon">📍</div>
      <div class="mc-contact-item-label">Location</div>
      <div class="mc-contact-item-val">Mumbai, India</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Quote ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="mc-quote">
  <p class="mc-quote-text">
    The woods are lovely, dark and deep,<br>
    But I have promises to keep,<br>
    And <span class="mc-quote-highlight">miles to go before I sleep,</span><br>
    And miles to go before I sleep.
  </p>
  <div class="mc-quote-author">— Robert Frost · Stopping by Woods on a Snowy Evening</div>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<footer class="mc-footer">
  <span class="mc-footer-copy">
    <span class="mc-footer-dot"></span>
    © 2026 Shravan Parthe. Built with Streamlit.
  </span>
  <span class="mc-footer-copy">Designed with care, shipped with confidence.</span>
</footer>
""", unsafe_allow_html=True)
