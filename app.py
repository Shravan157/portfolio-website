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
        return f'<a href="data:application/pdf;base64,{data}" download="Shravan_Parthe_Resume.pdf" class="btn-primary">📄 Download Resume</a>'
    return '<a href="#" class="btn-primary">📄 Resume Coming Soon</a>'

# ─── Custom CSS ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg: #080b14;
    --bg-alt: #0d1117;
    --glass: rgba(255,255,255,0.04);
    --glass-hover: rgba(255,255,255,0.07);
    --glass-border: rgba(255,255,255,0.08);
    --glass-border-hover: rgba(99,179,237,0.4);
    --text-primary: #e8eaf0;
    --text-secondary: #9aa5b4;
    --text-muted: #5a6478;
    --accent: #63b3ed;
    --accent-glow: rgba(99,179,237,0.15);
    --accent-bright: #90cdf4;
    --purple: #b794f4;
    --purple-glow: rgba(183,148,244,0.15);
    --green: #68d391;
    --green-glow: rgba(104,211,145,0.15);
    --orange: #fbd38d;
    --orange-glow: rgba(251,211,141,0.15);
    --pink: #fc8181;
    --pink-glow: rgba(252,129,129,0.15);
    --font: 'Space Grotesk', sans-serif;
    --mono: 'JetBrains Mono', monospace;
    --radius: 14px;
    --radius-sm: 8px;
    --blur: blur(16px);
}

/* ── Reset & Base ── */
.stApp {
    background-color: var(--bg) !important;
    color: var(--text-primary) !important;
    font-family: var(--font) !important;
}
.block-container {
    max-width: 1100px !important;
    padding-top: 0.5rem !important;
    padding-bottom: 5rem !important;
}
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Animated Background ── */
.stApp::before {
    content: '';
    position: fixed;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background:
        radial-gradient(ellipse 600px 600px at 15% 20%, rgba(99,179,237,0.06) 0%, transparent 70%),
        radial-gradient(ellipse 500px 500px at 85% 75%, rgba(183,148,244,0.05) 0%, transparent 70%),
        radial-gradient(ellipse 400px 400px at 50% 50%, rgba(104,211,145,0.03) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* ── Navigation ── */
.nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.5rem 0 1.25rem;
    border-bottom: 1px solid var(--glass-border);
    margin-bottom: 0;
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: var(--blur);
    background: rgba(8,11,20,0.8);
}
.nav-brand {
    font-family: var(--mono);
    font-size: 1.15rem;
    font-weight: 500;
    color: var(--text-primary);
    letter-spacing: -0.3px;
}
.nav-brand .accent { color: var(--accent); }
.nav-brand .dim { color: var(--text-muted); }
.nav-links { display: flex; gap: 2rem; align-items: center; }
.nav-links a {
    color: var(--text-muted);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 0.3px;
    transition: color 0.2s;
    position: relative;
}
.nav-links a::after {
    content: '';
    position: absolute;
    bottom: -3px; left: 0;
    width: 0; height: 1.5px;
    background: var(--accent);
    transition: width 0.2s;
    border-radius: 2px;
}
.nav-links a:hover { color: var(--accent); }
.nav-links a:hover::after { width: 100%; }
.nav-dot {
    width: 8px; height: 8px;
    background: var(--green);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--green);
    animation: pulse-dot 2s infinite;
    display: inline-block;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.6; transform: scale(0.8); }
}

/* ── Hero ── */
.hero-section {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 4rem;
    align-items: center;
    padding: 5rem 0 4rem;
}
.hero-label {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.35rem 0.85rem;
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: 999px;
    font-size: 0.78rem;
    color: var(--accent);
    font-family: var(--mono);
    margin-bottom: 1.5rem;
    backdrop-filter: var(--blur);
}
.hero-name {
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1.1;
    letter-spacing: -1.5px;
    margin-bottom: 0.6rem;
}
.hero-name .highlight {
    background: linear-gradient(135deg, var(--accent) 0%, var(--purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-title {
    font-size: 1rem;
    color: var(--text-secondary);
    font-weight: 500;
    margin-bottom: 1.5rem;
    font-family: var(--mono);
}
.hero-desc {
    font-size: 0.93rem;
    color: var(--text-secondary);
    line-height: 1.8;
    max-width: 520px;
    margin-bottom: 2.25rem;
}
.hero-cta {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    align-items: center;
}
.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.75rem 1.6rem;
    background: linear-gradient(135deg, var(--accent) 0%, #4299e1 100%);
    color: #0a0e1a !important;
    border-radius: var(--radius-sm);
    font-size: 0.875rem;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.25s;
    box-shadow: 0 0 20px rgba(99,179,237,0.35);
    letter-spacing: 0.2px;
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 30px rgba(99,179,237,0.55);
}
.btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.72rem 1.35rem;
    background: var(--glass);
    color: var(--text-secondary) !important;
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-sm);
    font-size: 0.85rem;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.25s;
    backdrop-filter: var(--blur);
}
.btn-outline:hover {
    border-color: var(--glass-border-hover);
    color: var(--accent) !important;
    background: var(--accent-glow);
}

/* ── Hero Card ── */
.hero-card {
    width: 300px;
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 1.75rem;
    backdrop-filter: var(--blur);
    box-shadow: 0 8px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.06);
    position: relative;
    overflow: hidden;
}
.hero-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0.6;
}
.hero-card-top {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 1.25rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--glass-border);
}
.hero-card-dot { width: 10px; height: 10px; border-radius: 50%; }
.dot-red { background: #fc8181; }
.dot-yellow { background: #fbd38d; }
.dot-green { background: #68d391; box-shadow: 0 0 6px rgba(104,211,145,0.8); }
.hero-card-title {
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--text-muted);
    margin-left: auto;
}
.code-line { font-family: var(--mono); font-size: 0.78rem; line-height: 2; }
.kw { color: var(--purple); }
.fn { color: var(--accent); }
.str { color: var(--green); }
.cm { color: var(--text-muted); }
.num { color: var(--orange); }

/* ── Section Header ── */
.section-header {
    margin: 5rem 0 2.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}
.section-num {
    font-family: var(--mono);
    font-size: 0.78rem;
    color: var(--accent);
    opacity: 0.7;
}
.section-header h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: -0.5px;
    margin: 0;
}
.section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--glass-border), transparent);
}

/* ── Stats ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.85rem;
    margin-bottom: 1rem;
}
.stat-card {
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    padding: 1.5rem 1.25rem;
    text-align: center;
    transition: all 0.25s;
    backdrop-filter: var(--blur);
    position: relative;
    overflow: hidden;
}
.stat-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 50%;
    transform: translateX(-50%);
    width: 40%;
    height: 2px;
    border-radius: 2px;
    transition: width 0.3s;
}
.stat-card:nth-child(1)::after { background: var(--accent); }
.stat-card:nth-child(2)::after { background: var(--purple); }
.stat-card:nth-child(3)::after { background: var(--green); }
.stat-card:nth-child(4)::after { background: var(--orange); }
.stat-card:hover {
    border-color: var(--glass-border-hover);
    background: var(--glass-hover);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}
.stat-card:hover::after { width: 80%; }
.stat-value {
    font-size: 2rem;
    font-weight: 700;
    font-family: var(--mono);
    background: linear-gradient(135deg, var(--text-primary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
}
.stat-label {
    font-size: 0.7rem;
    color: var(--text-muted);
    margin-top: 0.3rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* ── Skills ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 0.85rem;
}
.skill-group {
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    padding: 1.4rem;
    transition: all 0.25s;
    backdrop-filter: var(--blur);
}
.skill-group:hover {
    border-color: var(--glass-border-hover);
    background: var(--glass-hover);
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
}
.skill-group-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 1rem;
}
.skill-group-icon { font-size: 1.1rem; }
.skill-group-title {
    font-family: var(--mono);
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
}
.skill-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.skill-tag {
    padding: 0.3rem 0.75rem;
    border-radius: 6px;
    font-size: 0.77rem;
    font-weight: 500;
    font-family: var(--mono);
    border: 1px solid transparent;
    transition: all 0.2s;
}
.skill-tag:hover { transform: translateY(-1px); }
.tag-blue { background: rgba(99,179,237,0.1); color: var(--accent); border-color: rgba(99,179,237,0.2); }
.tag-purple { background: rgba(183,148,244,0.1); color: var(--purple); border-color: rgba(183,148,244,0.2); }
.tag-green { background: rgba(104,211,145,0.1); color: var(--green); border-color: rgba(104,211,145,0.2); }
.tag-orange { background: rgba(251,211,141,0.1); color: var(--orange); border-color: rgba(251,211,141,0.2); }

/* ── Projects ── */
.project-card {
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    padding: 1.75rem;
    margin-bottom: 0.85rem;
    transition: all 0.3s;
    backdrop-filter: var(--blur);
    position: relative;
    overflow: hidden;
}
.project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, var(--accent), var(--purple));
    opacity: 0;
    transition: opacity 0.3s;
    border-radius: 2px 0 0 2px;
}
.project-card:hover {
    border-color: var(--glass-border-hover);
    background: var(--glass-hover);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35), 0 0 0 1px rgba(99,179,237,0.08);
    transform: translateX(4px);
}
.project-card:hover::before { opacity: 1; }
.project-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 0.5rem;
}
.project-header h3 {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
    letter-spacing: -0.3px;
}
.project-badge {
    padding: 0.2rem 0.7rem;
    border-radius: 999px;
    font-size: 0.68rem;
    font-weight: 600;
    white-space: nowrap;
    font-family: var(--mono);
    border: 1px solid transparent;
    flex-shrink: 0;
}
.badge-ai { background: var(--purple-glow); color: var(--purple); border-color: rgba(183,148,244,0.3); }
.badge-fullstack { background: var(--green-glow); color: var(--green); border-color: rgba(104,211,145,0.3); }
.badge-ml { background: var(--orange-glow); color: var(--orange); border-color: rgba(251,211,141,0.3); }
.badge-fintech { background: var(--accent-glow); color: var(--accent); border-color: rgba(99,179,237,0.3); }
.project-date {
    font-family: var(--mono);
    font-size: 0.73rem;
    color: var(--text-muted);
    margin-bottom: 0.75rem;
}
.project-desc {
    color: var(--text-secondary);
    font-size: 0.875rem;
    line-height: 1.75;
    margin-bottom: 1rem;
}
.project-tech { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1rem; }
.tech-chip {
    padding: 0.2rem 0.6rem;
    border-radius: 5px;
    background: rgba(255,255,255,0.04);
    border: 1px solid var(--glass-border);
    color: var(--text-muted);
    font-size: 0.72rem;
    font-weight: 500;
    font-family: var(--mono);
    transition: all 0.2s;
}
.tech-chip:hover { color: var(--accent); border-color: rgba(99,179,237,0.25); }
.project-link {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: var(--accent);
    text-decoration: none;
    font-size: 0.8rem;
    font-weight: 600;
    font-family: var(--mono);
    opacity: 0.8;
    transition: opacity 0.2s;
}
.project-link:hover { opacity: 1; }

/* ── Timeline ── */
.timeline-card {
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    padding: 1.5rem 1.75rem;
    margin-bottom: 0.85rem;
    backdrop-filter: var(--blur);
    transition: all 0.25s;
    position: relative;
}
.timeline-card:hover {
    border-color: var(--glass-border-hover);
    background: var(--glass-hover);
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
}
.timeline-glow {
    position: absolute;
    top: 1.5rem; left: -1px;
    width: 3px; height: 2rem;
    border-radius: 0 2px 2px 0;
    background: linear-gradient(180deg, var(--accent), var(--purple));
    box-shadow: 0 0 10px var(--accent);
}
.timeline-role {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: -0.3px;
}
.timeline-org {
    color: var(--accent);
    font-size: 0.88rem;
    font-weight: 600;
    margin-top: 0.15rem;
    font-family: var(--mono);
}
.timeline-meta {
    font-family: var(--mono);
    font-size: 0.73rem;
    color: var(--text-muted);
    margin-top: 0.15rem;
}
.timeline-bullets {
    color: var(--text-secondary);
    font-size: 0.85rem;
    line-height: 1.75;
    margin-top: 0.75rem;
    padding-left: 1.1rem;
}
.timeline-bullets li { margin-bottom: 0.35rem; }
.timeline-cgpa {
    display: inline-block;
    padding: 0.2rem 0.65rem;
    background: var(--green-glow);
    color: var(--green);
    border-radius: 6px;
    border: 1px solid rgba(104,211,145,0.25);
    font-size: 0.75rem;
    font-weight: 600;
    font-family: var(--mono);
    margin-top: 0.5rem;
}

/* ── Contact ── */
.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 0.85rem;
}
.contact-card {
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    padding: 1.5rem 1.25rem;
    text-align: center;
    transition: all 0.25s;
    backdrop-filter: var(--blur);
}
.contact-card:hover {
    border-color: var(--glass-border-hover);
    background: var(--glass-hover);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3), 0 0 20px var(--accent-glow);
}
.contact-icon { font-size: 1.5rem; margin-bottom: 0.4rem; }
.contact-label {
    font-family: var(--mono);
    font-size: 0.68rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 600;
}
.contact-value {
    color: var(--text-primary);
    font-size: 0.875rem;
    font-weight: 500;
    margin-top: 0.2rem;
}
.contact-value a { color: var(--accent); text-decoration: none; }
.contact-value a:hover { color: var(--accent-bright); }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 3rem 0 1.5rem;
    border-top: 1px solid var(--glass-border);
    margin-top: 4rem;
}
.footer p {
    font-family: var(--mono);
    color: var(--text-muted);
    font-size: 0.78rem;
}
.footer a { color: var(--accent); text-decoration: none; }

/* ── Responsive ── */
@media (max-width: 768px) {
    .hero-section { grid-template-columns: 1fr; }
    .hero-card { display: none; }
    .stats-row { grid-template-columns: repeat(2, 1fr); }
    .nav-links { gap: 1rem; }
    .skills-grid { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)


# ─── Navigation ───
st.markdown("""
<div class="nav">
    <div class="nav-brand">
        <span class="dim">&lt;</span>shravan<span class="accent">.</span>dev<span class="dim">/&gt;</span>
    </div>
    <div class="nav-links">
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#experience">Experience</a>
        <a href="#education">Education</a>
        <a href="#contact">Contact</a>
        <span class="nav-dot" title="Open to work"></span>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Hero ───
resume_link = get_resume_download_link()

st.markdown(f"""
<div class="hero-section">
    <div class="hero-text">
        <div class="hero-label">
            <span>👋</span> Available for opportunities
        </div>
        <div class="hero-name">
            I'm <span class="highlight">Shravan Parthe</span>
        </div>
        <div class="hero-title">// Backend Engineer · AI/ML Developer · B.Tech CSE 2027</div>
        <p class="hero-desc">
            Results-driven CS student specializing in AI & ML with hands-on expertise in 
            backend development using Java and Spring Boot. I build scalable, production-ready 
            applications spanning fintech, healthcare, and edtech — bridging backend systems 
            with intelligent AI features.
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
    <div class="hero-card">
        <div class="hero-card-top">
            <span class="hero-card-dot dot-red"></span>
            <span class="hero-card-dot dot-yellow"></span>
            <span class="hero-card-dot dot-green"></span>
            <span class="hero-card-title">shravan.java</span>
        </div>
        <div class="code-line"><span class="cm">// open to work ✓</span></div>
        <div class="code-line"><span class="kw">class</span> <span class="fn">Developer</span> &#123;</div>
        <div class="code-line">&nbsp;&nbsp;<span class="kw">String</span> name = <span class="str">"Shravan"</span>;</div>
        <div class="code-line">&nbsp;&nbsp;<span class="kw">int</span> year = <span class="num">3</span>;</div>
        <div class="code-line">&nbsp;&nbsp;<span class="kw">String[]</span> stack = &#123;</div>
        <div class="code-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Java"</span>, <span class="str">"Python"</span>,</div>
        <div class="code-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Spring Boot"</span>,</div>
        <div class="code-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"React"</span>, <span class="str">"Flutter"</span></div>
        <div class="code-line">&nbsp;&nbsp;&#125;;</div>
        <div class="code-line">&nbsp;&nbsp;<span class="kw">boolean</span> hireable = <span class="str">true</span>;</div>
        <div class="code-line">&#125;</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Stats ───
st.markdown("""
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-value">5+</div>
        <div class="stat-label">Projects</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">7.5</div>
        <div class="stat-label">CGPA</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">3rd</div>
        <div class="stat-label">Year BTech</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">1</div>
        <div class="stat-label">Internship</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Skills ───
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-num">01.</span>
    <h2>Technical Skills</h2>
    <div class="section-line"></div>
</div>

<div class="skills-grid">
    <div class="skill-group">
        <div class="skill-group-header">
            <span class="skill-group-icon">💻</span>
            <span class="skill-group-title">Languages</span>
        </div>
        <div class="skill-tags">
            <span class="skill-tag tag-blue">Java</span>
            <span class="skill-tag tag-blue">Python</span>
            <span class="skill-tag tag-blue">JavaScript</span>
            <span class="skill-tag tag-blue">Dart</span>
            <span class="skill-tag tag-blue">SQL</span>
        </div>
    </div>
    <div class="skill-group">
        <div class="skill-group-header">
            <span class="skill-group-icon">⚙️</span>
            <span class="skill-group-title">Frameworks</span>
        </div>
        <div class="skill-tags">
            <span class="skill-tag tag-green">React</span>
            <span class="skill-tag tag-green">Spring Boot</span>
            <span class="skill-tag tag-green">Flutter</span>
            <span class="skill-tag tag-green">FastAPI</span>
            <span class="skill-tag tag-green">Spring Security</span>
            <span class="skill-tag tag-green">Spring AI</span>
        </div>
    </div>
    <div class="skill-group">
        <div class="skill-group-header">
            <span class="skill-group-icon">🛠️</span>
            <span class="skill-group-title">Tools & Platforms</span>
        </div>
        <div class="skill-tags">
            <span class="skill-tag tag-purple">Docker</span>
            <span class="skill-tag tag-purple">GitHub</span>
            <span class="skill-tag tag-purple">NumPy</span>
            <span class="skill-tag tag-purple">Pandas</span>
            <span class="skill-tag tag-purple">Scikit-learn</span>
        </div>
    </div>
    <div class="skill-group">
        <div class="skill-group-header">
            <span class="skill-group-icon">🗄️</span>
            <span class="skill-group-title">Databases</span>
        </div>
        <div class="skill-tags">
            <span class="skill-tag tag-orange">MySQL</span>
            <span class="skill-tag tag-orange">PostgreSQL</span>
            <span class="skill-tag tag-orange">Firebase</span>
            <span class="skill-tag tag-orange">Redis</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Projects ───
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-num">02.</span>
    <h2>Featured Projects</h2>
    <div class="section-line"></div>
</div>
""", unsafe_allow_html=True)

projects = [
    {
        "icon": "🏥", "title": "MedoraX AI — Clinical AI Assistant",
        "badge": "badge-ai", "badge_label": "Healthcare AI",
        "date": "Oct 2025 — Nov 2026",
        "desc": "Multimodal clinical AI assistant supporting voice, image, and text inputs — transcribing symptoms via Whisper-large-v3, analyzing medical images via Llama-4-scout, and generating structured diagnostic responses using Llama-3.3-70b. Multilingual support (English, Hindi, Marathi) with GPS-based hospital finder and real-time AQI monitoring.",
        "tech": ["Python", "Gradio", "Groq API", "Google Maps API", "Google Places API"],
        "link": "https://github.com/Shravan157/MedX-AI-Clinical-Assistant"
    },
    {
        "icon": "🏦", "title": "SahayLoan — Micro-Loan Platform",
        "badge": "badge-fintech", "badge_label": "FinTech",
        "date": "Jan 2026 — Present",
        "desc": "Full-stack micro-lending platform (loans up to ₹1,00,000) with Flutter frontend and FastAPI backend. AI credit scoring engine using Random Forest classifier, digital KYC with Aadhaar & PAN OCR via Tesseract, Stripe EMI integration, and multi-role system with Firebase Auth and Firestore.",
        "tech": ["Flutter", "Dart", "FastAPI", "Scikit-learn", "Firebase", "Tesseract OCR", "Stripe"],
        "link": "https://github.com/Shravan157/Sahay-Loan"
    },
    {
        "icon": "🎓", "title": "SikshaSetu — Rural Education Platform",
        "badge": "badge-fullstack", "badge_label": "Full-Stack",
        "date": "Jan 2025 — Apr 2025",
        "desc": "Full-stack education platform bridging the digital divide for rural communities. Role-based access control with Spring Security and JWT/OAuth 2.0, optimized relational schema with Spring Data JPA, responsive React.js frontend, and ZEGOCLOUD real-time video SDK for virtual classrooms.",
        "tech": ["React", "Spring Boot", "Spring Security", "JWT", "MySQL", "Spring Data JPA"],
        "link": "https://github.com/Shravan157/SikshaSetu_Edu_App"
    },
    {
        "icon": "🛒", "title": "AI-Powered E-Commerce Platform",
        "badge": "badge-ai", "badge_label": "AI / Full-Stack",
        "date": "Oct 2024 — Jan 2025",
        "desc": "Intelligent e-commerce backend with AI-driven product recommendations using Spring AI and vector similarity search via Redis Vector DB. Generative AI chatbot for real-time customer support, AI-powered product image generation pipeline, secured with Spring Security and JWT.",
        "tech": ["React", "Spring Boot", "Spring AI", "Redis Vector DB", "Tailwind CSS"],
        "link": "https://github.com/Shravan157"
    },
    {
        "icon": "🍽️", "title": "Zomato Sentiment Analysis",
        "badge": "badge-ml", "badge_label": "ML / NLP",
        "date": "Data Science Project",
        "desc": "End-to-end NLP project classifying 10,000+ Zomato restaurant reviews. Extensive EDA with 15 visualizations, hypothesis testing, TF-IDF vectorization, and model comparison (Logistic Regression, Random Forest, Naive Bayes). Logistic Regression achieved highest F1 score.",
        "tech": ["Python", "Scikit-learn", "NLTK", "TF-IDF", "Pandas", "Matplotlib"],
        "link": "https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis"
    }
]

for p in projects:
    tech_html = "".join([f'<span class="tech-chip">{t}</span>' for t in p["tech"]])
    st.markdown(f"""
<div class="project-card">
    <div class="project-header">
        <h3>{p['icon']} {p['title']}</h3>
        <span class="project-badge {p['badge']}">{p['badge_label']}</span>
    </div>
    <div class="project-date">📅 {p['date']}</div>
    <p class="project-desc">{p['desc']}</p>
    <div class="project-tech">{tech_html}</div>
    <a href="{p['link']}" target="_blank" class="project-link">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/>e x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub →
    </a>
</div>
""", unsafe_allow_html=True)


# ─── Experience ───
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-num">03.</span>
    <h2>Work Experience</h2>
    <div class="section-line"></div>
</div>

<div class="timeline-card">
    <div class="timeline-glow"></div>
    <div class="timeline-role">Data Science with Gen AI Intern</div>
    <div class="timeline-org">@ Innovexis</div>
    <div class="timeline-meta">Apr 2026 — Present · Remote</div>
    <ul class="timeline-bullets">
        >Selected for Innovexis's competitive Data Science with Generative AI internship after shortlisting from multiple applicants</li>
        >Working on real-world data science projects integrating large language models and generative AI techniques</li>
        >Applying Python, NumPy, Pandas, and Scikit-learn for data analysis, preprocessing, and model building</li>
        >Gaining hands-on exposure to production-level Gen AI workflows, LLM integration, and applied machine learning</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# ─── Education ───
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-num">04.</span>
    <h2>Education</h2>
    <div class="section-line"></div>
</div>

<div class="timeline-card">
    <div class="timeline-glow"></div>
    <div class="timeline-role">B.Tech in Computer Science Engineering (AI & ML)</div>
    <div class="timeline-org">@ ViMEET, University of Mumbai</div>
    <div class="timeline-meta">Jun 2023 — Expected May 2027</div>
    <div style="color: var(--text-secondary); font-size: 0.875rem; margin-top: 0.6rem; line-height: 1.7;">
        Specializing in Artificial Intelligence & Machine Learning. Coursework includes 
        Data Structures & Algorithms, Machine Learning, Cloud Computing, Microservices Architecture, 
        and System Design.
    </div>
    <div class="timeline-cgpa">✦ CGPA: 7.5 / 10.0</div>
</div>
""", unsafe_allow_html=True)


# ─── Contact ───
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <span class="section-num">05.</span>
    <h2>Get in Touch</h2>
    <div class="section-line"></div>
</div>

<div class="contact-grid">
    <div class="contact-card">
        <div class="contact-icon">📧</div>
        <div class="contact-label">Email</div>
        <div class="contact-value">
            <a href="mailto:shravanparthe@gmail.com">shravanparthe@gmail.com</a>
        </div>
    </div>
    <div class="contact-card">
        <div class="contact-icon">📱</div>
        <div class="contact-label">Phone</div>
        <div class="contact-value">7385813010</div>
    </div>
    <div class="contact-card">
        <div class="contact-icon">💼</div>
        <div class="contact-label">LinkedIn</div>
        <div class="contact-value">
            <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank">Shravan Parthe</a>
        </div>
    </div>
    <div class="contact-card">
        <div class="contact-icon">🐙</div>
        <div class="contact-label">GitHub</div>
        <div class="contact-value">
            <a href="https://github.com/Shravan157" target="_blank">Shravan157</a>
        </div>
    </div>
    <div class="contact-card">
        <div class="contact-icon">📍</div>
        <div class="contact-label">Location</div>
        <div class="contact-value">Mumbai, India</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Footer ───
st.markdown("""
<style>
.quote-section {
    margin-top: 4rem;
    padding: 3rem 2rem;
    text-align: center;
    position: relative;
    border-top: 1px solid var(--glass-border);
}
.quote-section::before {
    content: '"';
    position: absolute;
    top: 1.5rem;
    left: 50%;
    transform: translateX(-50%);
    font-size: 5rem;
    font-family: Georgia, serif;
    color: var(--accent);
    opacity: 0.12;
    line-height: 1;
    pointer-events: none;
}
.quote-text {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(1rem, 2vw, 1.25rem);
    font-style: italic;
    color: var(--text-secondary);
    line-height: 1.9;
    max-width: 560px;
    margin: 0 auto 0.75rem;
    position: relative;
    z-index: 1;
}
.quote-text .line-highlight {
    background: linear-gradient(135deg, var(--accent) 0%, var(--purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 600;
    font-style: italic;
}
.quote-author {
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 0.25rem;
}
.quote-author span {
    color: var(--accent);
    opacity: 0.7;
}
.footer {
    text-align: center;
    padding: 1.75rem 0 1.5rem;
    border-top: 1px solid var(--glass-border);
}
.footer p {
    font-family: var(--mono);
    color: var(--text-muted);
    font-size: 0.78rem;
}
.footer a { color: var(--accent); text-decoration: none; }
</style>

<div class="quote-section">
    <p class="quote-text">
        The woods are lovely, dark and deep,<br>
        But I have promises to keep,<br>
        And <span class="line-highlight">miles to go before I sleep,</span><br>
        And miles to go before I sleep.
    </p>
    <div class="quote-author">— Robert Frost <span>· Stopping by Woods on a Snowy Evening</span></div>
</div>

<div class="footer">
    <p>Designed & built by <a href="https://github.com/Shravan157" target="_blank">Shravan Parthe</a> · 2026 · Made with ❤️ &amp; ☕</p>
</div>
""", unsafe_allow_html=True)
