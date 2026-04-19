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
        return f'<a href="data:application/pdf;base64,{data}" download="Shravan_Parthe_Resume.pdf" class="btn-resume">📄 Download Resume</a>'
    return '<a href="#" class="btn-resume">📄 Resume Coming Soon</a>'

# ─── Custom CSS ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --bg: #ffffff;
    --bg-alt: #f8f9fc;
    --bg-card: #ffffff;
    --text-primary: #1a1a2e;
    --text-secondary: #4a4a6a;
    --text-muted: #8888a0;
    --accent: #4285f4;
    --accent-light: #e8f0fe;
    --accent-dark: #1a73e8;
    --border: #e8e8ef;
    --border-light: #f0f0f5;
    --green: #34a853;
    --green-light: #e6f4ea;
    --orange: #ea8c00;
    --orange-light: #fef7e0;
    --purple: #9c27b0;
    --purple-light: #f3e5f5;
    --red: #ea4335;
    --red-light: #fce8e6;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
    --shadow-lg: 0 10px 30px rgba(0,0,0,0.1);
    --radius: 12px;
    --font-heading: 'Poppins', sans-serif;
    --font-body: 'Inter', sans-serif;
}

/* Global */
.stApp {
    background-color: var(--bg) !important;
    color: var(--text-primary) !important;
    font-family: var(--font-body) !important;
}
.block-container {
    max-width: 1080px !important;
    padding-top: 1rem !important;
    padding-bottom: 4rem !important;
}
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ─── Navigation ─── */
.nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.25rem 0;
    border-bottom: 1px solid var(--border-light);
    margin-bottom: 2rem;
}
.nav-brand {
    font-family: var(--font-heading);
    font-weight: 800;
    font-size: 1.4rem;
    color: var(--text-primary);
    letter-spacing: -0.5px;
}
.nav-brand span { color: var(--accent); }
.nav-links { display: flex; gap: 1.75rem; }
.nav-links a {
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 0.88rem;
    font-weight: 500;
    transition: color 0.2s;
    font-family: var(--font-body);
}
.nav-links a:hover { color: var(--accent); }

/* ─── Hero ─── */
.hero-section {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 3rem;
    padding: 3.5rem 0 3rem;
}
.hero-text { flex: 1; max-width: 560px; }
.hero-greeting {
    font-family: var(--font-heading);
    font-size: 1rem;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 0.5rem;
    letter-spacing: 0.5px;
}
.hero-name {
    font-family: var(--font-heading);
    font-size: clamp(2rem, 4vw, 2.75rem);
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.15;
    margin-bottom: 0.5rem;
    letter-spacing: -1px;
}
.hero-title {
    font-family: var(--font-heading);
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin-bottom: 1.25rem;
}
.hero-desc {
    font-size: 0.95rem;
    color: var(--text-secondary);
    line-height: 1.75;
    margin-bottom: 1.75rem;
}
.hero-buttons {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    align-items: center;
}
.btn-resume {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.7rem 1.5rem;
    background: var(--accent);
    color: #fff !important;
    border-radius: 8px;
    font-size: 0.88rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s;
    box-shadow: 0 2px 8px rgba(66,133,244,0.3);
}
.btn-resume:hover {
    background: var(--accent-dark);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(66,133,244,0.4);
}
.btn-social {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.65rem 1.25rem;
    background: transparent;
    color: var(--text-secondary) !important;
    border: 1.5px solid var(--border);
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.2s;
}
.btn-social:hover {
    border-color: var(--accent);
    color: var(--accent) !important;
    background: var(--accent-light);
}
.hero-illustration {
    flex-shrink: 0;
    width: 320px;
    height: 320px;
    background: var(--bg-alt);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}
.hero-illustration .code-visual {
    font-size: 0.75rem;
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent);
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.5rem;
    line-height: 1.8;
    box-shadow: var(--shadow-md);
    text-align: left;
    max-width: 260px;
}
.hero-illustration .code-visual .kw { color: #9c27b0; }
.hero-illustration .code-visual .fn { color: #ea8c00; }
.hero-illustration .code-visual .str { color: #34a853; }
.hero-illustration .code-visual .cm { color: #8888a0; }

/* ─── Section Header ─── */
.section-header {
    margin: 3.5rem 0 1.75rem;
    text-align: center;
}
.section-header h2 {
    font-family: var(--font-heading);
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.4rem;
    letter-spacing: -0.5px;
}
.section-header p {
    color: var(--text-muted);
    font-size: 0.92rem;
}
.section-divider {
    width: 50px;
    height: 3px;
    background: var(--accent);
    border-radius: 2px;
    margin: 0.75rem auto 0;
}

/* ─── Stats ─── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0 1rem;
}
.stat-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem;
    text-align: center;
    transition: all 0.2s;
}
.stat-card:hover {
    border-color: var(--accent);
    box-shadow: var(--shadow-sm);
}
.stat-value {
    font-family: var(--font-heading);
    font-size: 1.75rem;
    font-weight: 800;
    color: var(--accent);
}
.stat-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    margin-top: 0.2rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ─── Skills ─── */
.skills-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
}
.skill-group {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem;
    transition: all 0.2s;
}
.skill-group:hover {
    box-shadow: var(--shadow-sm);
    border-color: var(--accent);
}
.skill-group-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}
.skill-group-title {
    font-family: var(--font-heading);
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
}
.skill-tag {
    padding: 0.3rem 0.7rem;
    border-radius: 6px;
    font-size: 0.78rem;
    font-weight: 500;
}
.tag-lang { background: var(--accent-light); color: var(--accent-dark); }
.tag-frame { background: var(--green-light); color: #1e7e34; }
.tag-tool { background: var(--purple-light); color: var(--purple); }
.tag-db { background: var(--orange-light); color: #b36b00; }
.tag-soft { background: var(--red-light); color: var(--red); }

/* ─── Projects ─── */
.project-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: all 0.25s;
}
.project-card:hover {
    box-shadow: var(--shadow-md);
    border-color: var(--accent);
    transform: translateY(-2px);
}
.project-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 0.6rem;
    gap: 1rem;
}
.project-header h3 {
    font-family: var(--font-heading);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
}
.project-badge {
    padding: 0.2rem 0.65rem;
    border-radius: 999px;
    font-size: 0.7rem;
    font-weight: 600;
    white-space: nowrap;
    flex-shrink: 0;
}
.badge-ai { background: var(--purple-light); color: var(--purple); }
.badge-fullstack { background: var(--green-light); color: #1e7e34; }
.badge-ml { background: var(--orange-light); color: #b36b00; }
.badge-fintech { background: var(--accent-light); color: var(--accent-dark); }
.project-date {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-bottom: 0.5rem;
}
.project-desc {
    color: var(--text-secondary);
    font-size: 0.88rem;
    line-height: 1.7;
    margin-bottom: 0.75rem;
}
.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 0.75rem;
}
.tech-chip {
    padding: 0.2rem 0.6rem;
    border-radius: 5px;
    background: var(--bg-alt);
    border: 1px solid var(--border);
    color: var(--text-secondary);
    font-size: 0.75rem;
    font-weight: 500;
}
.project-link {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    color: var(--accent);
    text-decoration: none;
    font-size: 0.82rem;
    font-weight: 600;
}
.project-link:hover { color: var(--accent-dark); }

/* ─── Experience / Education ─── */
.timeline-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem 1.5rem;
    margin-bottom: 0.75rem;
    border-left: 3px solid var(--accent);
    transition: all 0.2s;
}
.timeline-card:hover {
    box-shadow: var(--shadow-sm);
}
.timeline-role {
    font-family: var(--font-heading);
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-primary);
}
.timeline-org {
    color: var(--accent);
    font-size: 0.9rem;
    font-weight: 600;
}
.timeline-meta {
    color: var(--text-muted);
    font-size: 0.8rem;
    margin-top: 0.15rem;
}
.timeline-desc {
    color: var(--text-secondary);
    font-size: 0.88rem;
    line-height: 1.65;
    margin-top: 0.5rem;
}
.timeline-bullets {
    color: var(--text-secondary);
    font-size: 0.85rem;
    line-height: 1.65;
    margin-top: 0.5rem;
    padding-left: 1.1rem;
}
.timeline-bullets li { margin-bottom: 0.35rem; }
.timeline-cgpa {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    background: var(--green-light);
    color: #1e7e34;
    border-radius: 6px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-top: 0.4rem;
}

/* ─── Contact ─── */
.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 0.75rem;
    margin-top: 1.25rem;
}
.contact-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem;
    text-align: center;
    transition: all 0.2s;
}
.contact-card:hover {
    border-color: var(--accent);
    box-shadow: var(--shadow-sm);
}
.contact-icon { font-size: 1.5rem; margin-bottom: 0.35rem; }
.contact-label {
    font-size: 0.72rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
}
.contact-value {
    color: var(--text-primary);
    font-size: 0.9rem;
    font-weight: 500;
    margin-top: 0.15rem;
}
.contact-value a {
    color: var(--accent);
    text-decoration: none;
}
.contact-value a:hover { color: var(--accent-dark); }

/* ─── Footer ─── */
.footer {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
    border-top: 1px solid var(--border-light);
    margin-top: 3rem;
}
.footer p {
    color: var(--text-muted);
    font-size: 0.82rem;
}
.footer a { color: var(--accent); text-decoration: none; }

/* ─── Responsive ─── */
@media (max-width: 768px) {
    .hero-section { flex-direction: column; text-align: center; padding: 2rem 0; }
    .hero-text { max-width: 100%; }
    .hero-buttons { justify-content: center; }
    .hero-illustration { width: 240px; height: 240px; margin: 0 auto; }
    .stats-row { grid-template-columns: repeat(2, 1fr); }
    .nav-links { gap: 1rem; }
    .skills-container { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)


# ─── Navigation ───
st.markdown("""
<div class="nav">
    <div class="nav-brand">&lt;Shravan<span>/</span>&gt;</div>
    <div class="nav-links">
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#experience">Experience</a>
        <a href="#education">Education</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Hero Section ───
resume_link = get_resume_download_link()

st.markdown(f"""
<div class="hero-section">
    <div class="hero-text">
        <div class="hero-greeting">Hello !!!</div>
        <div class="hero-name">I'm Shravan Parthe</div>
        <div class="hero-title">B.Tech CSE (AI & ML) · University of Mumbai, 2027</div>
        <p class="hero-desc">
            Results-driven Computer Science & Engineering student with hands-on expertise in 
            backend development using Java and Spring Boot, and AI/ML integration using Python. 
            Experienced in building scalable, production-ready applications spanning fintech, 
            healthcare, and edtech domains. Passionate about bridging backend systems with 
            intelligent AI features.
        </p>
        <div class="hero-buttons">
            {resume_link}
            <a href="https://github.com/Shravan157" target="_blank" class="btn-social">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                GitHub
            </a>
            <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank" class="btn-social">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                LinkedIn
            </a>
        </div>
    </div>
    <div class="hero-illustration">
        <div class="code-visual">
            <span class="cm">// shravan.java</span><br>
            <span class="kw">class</span> <span class="fn">Developer</span> &#123;<br>
            &nbsp;&nbsp;<span class="kw">String</span> name = <span class="str">"Shravan"</span>;<br>
            &nbsp;&nbsp;<span class="kw">String[]</span> skills = &#123;<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Java"</span>, <span class="str">"Python"</span>,<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"Spring Boot"</span>,<br>
            &nbsp;&nbsp;&nbsp;&nbsp;<span class="str">"React"</span>, <span class="str">"Flutter"</span><br>
            &nbsp;&nbsp;&#125;;<br>
            &nbsp;&nbsp;<span class="kw">boolean</span> hireable = <span class="str">true</span>;<br>
            &#125;
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Stats ───
st.markdown("""
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-value">5+</div>
        <div class="stat-label">Projects Built</div>
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
    <h2>Technical Skills</h2>
    <p>Technologies and tools I work with</p>
    <div class="section-divider"></div>
</div>

<div class="skills-container">
    <div class="skill-group">
        <div class="skill-group-icon">💻</div>
        <div class="skill-group-title">Languages</div>
        <div class="skill-tags">
            <span class="skill-tag tag-lang">Java</span>
            <span class="skill-tag tag-lang">Python</span>
            <span class="skill-tag tag-lang">JavaScript</span>
            <span class="skill-tag tag-lang">Dart</span>
            <span class="skill-tag tag-lang">SQL</span>
        </div>
    </div>
    <div class="skill-group">
        <div class="skill-group-icon">⚙️</div>
        <div class="skill-group-title">Frameworks</div>
        <div class="skill-tags">
            <span class="skill-tag tag-frame">React</span>
            <span class="skill-tag tag-frame">Spring Boot</span>
            <span class="skill-tag tag-frame">Flutter</span>
            <span class="skill-tag tag-frame">FastAPI</span>
            <span class="skill-tag tag-frame">Spring Security</span>
            <span class="skill-tag tag-frame">Spring AI</span>
        </div>
    </div>
    <div class="skill-group">
        <div class="skill-group-icon">🛠️</div>
        <div class="skill-group-title">Tools & Platforms</div>
        <div class="skill-tags">
            <span class="skill-tag tag-tool">Docker</span>
            <span class="skill-tag tag-tool">GitHub</span>
            <span class="skill-tag tag-tool">NumPy</span>
            <span class="skill-tag tag-tool">Pandas</span>
            <span class="skill-tag tag-tool">Scikit-learn</span>
        </div>
    </div>
    <div class="skill-group">
        <div class="skill-group-icon">🗄️</div>
        <div class="skill-group-title">Databases</div>
        <div class="skill-tags">
            <span class="skill-tag tag-db">MySQL</span>
            <span class="skill-tag tag-db">PostgreSQL</span>
            <span class="skill-tag tag-db">Firebase</span>
            <span class="skill-tag tag-db">Redis</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Projects ───
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2>Featured Projects</h2>
    <p>A selection of projects across AI, full-stack, and mobile development</p>
    <div class="section-divider"></div>
</div>
""", unsafe_allow_html=True)

# Project 1: MedoraX
st.markdown("""
<div class="project-card">
    <div class="project-header">
        <h3>🏥 MedoraX AI — Clinical AI Assistant</h3>
        <span class="project-badge badge-ai">Healthcare AI</span>
    </div>
    <div class="project-date">Oct 2025 — Nov 2026</div>
    <p class="project-desc">
        Built a multimodal clinical AI assistant supporting voice, image, and text inputs — transcribing 
        symptoms via Whisper-large-v3, analyzing medical images via Llama-4-scout, and generating structured 
        diagnostic responses using Llama-3.3-70b. Multilingual support in English, Hindi, and Marathi with 
        GPS-based hospital finder and real-time AQI monitoring. Deployed on Hugging Face Spaces with 4–7s response times.
    </p>
    <div class="project-tech">
        <span class="tech-chip">Python</span>
        <span class="tech-chip">Gradio</span>
        <span class="tech-chip">Groq API</span>
        <span class="tech-chip">Google Maps API</span>
        <span class="tech-chip">Google Places API</span>
    </div>
    <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="project-link">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# Project 2: SahayLoan
st.markdown("""
<div class="project-card">
    <div class="project-header">
        <h3>🏦 SahayLoan — Micro-Loan Platform</h3>
        <span class="project-badge badge-fintech">FinTech</span>
    </div>
    <div class="project-date">Jan 2026 — Present</div>
    <p class="project-desc">
        Built a full-stack micro-lending platform (loans up to ₹1,00,000) with a Flutter frontend and 
        FastAPI Python backend. Developed an AI credit scoring engine using a Random Forest classifier 
        to automate loan eligibility decisions. Implemented digital KYC with Aadhaar & PAN OCR via 
        Tesseract and integrated Stripe for online EMI repayments. Multi-role system with Firebase Auth and Firestore.
    </p>
    <div class="project-tech">
        <span class="tech-chip">Flutter</span>
        <span class="tech-chip">Dart</span>
        <span class="tech-chip">FastAPI</span>
        <span class="tech-chip">Scikit-learn</span>
        <span class="tech-chip">Firebase</span>
        <span class="tech-chip">Tesseract OCR</span>
        <span class="tech-chip">Stripe</span>
    </div>
    <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="project-link">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# Project 3: SikshaSetu
st.markdown("""
<div class="project-card">
    <div class="project-header">
        <h3>🎓 SikshaSetu — Rural Education Platform</h3>
        <span class="project-badge badge-fullstack">Full-Stack</span>
    </div>
    <div class="project-date">Jan 2025 — Apr 2025</div>
    <p class="project-desc">
        Developed a full-stack education platform to bridge the digital divide for rural communities. 
        Implemented role-based access control with Spring Security and JWT/OAuth 2.0. Designed optimized 
        relational database schema with Spring Data JPA and MySQL. Built responsive React.js frontend 
        and integrated ZEGOCLOUD's real-time video SDK for virtual classrooms.
    </p>
    <div class="project-tech">
        <span class="tech-chip">React</span>
        <span class="tech-chip">Spring Boot</span>
        <span class="tech-chip">Spring Security</span>
        <span class="tech-chip">JWT</span>
        <span class="tech-chip">MySQL</span>
        <span class="tech-chip">Spring Data JPA</span>
    </div>
    <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="project-link">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# Project 4: AI E-Commerce
st.markdown("""
<div class="project-card">
    <div class="project-header">
        <h3>🛒 AI-Powered E-Commerce Platform</h3>
        <span class="project-badge badge-ai">AI / Full-Stack</span>
    </div>
    <div class="project-date">Oct 2024 — Jan 2025</div>
    <p class="project-desc">
        Engineered an intelligent e-commerce backend with AI-driven product recommendations using 
        Spring AI and vector similarity search via Redis Vector DB. Integrated a generative AI chatbot 
        for real-time customer support and built an AI-powered product image generation pipeline. 
        Secured with Spring Security and JWT authentication.
    </p>
    <div class="project-tech">
        <span class="tech-chip">React</span>
        <span class="tech-chip">Spring Boot</span>
        <span class="tech-chip">Spring AI</span>
        <span class="tech-chip">Redis Vector DB</span>
        <span class="tech-chip">Tailwind CSS</span>
    </div>
    <a href="https://github.com/Shravan157" target="_blank" class="project-link">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# Project 5: Zomato Sentiment
st.markdown("""
<div class="project-card">
    <div class="project-header">
        <h3>🍽️ Zomato Sentiment Analysis</h3>
        <span class="project-badge badge-ml">ML / NLP</span>
    </div>
    <div class="project-date">Data Science Project</div>
    <p class="project-desc">
        End-to-end NLP project to classify 10,000+ Zomato restaurant reviews as positive or negative. 
        Includes extensive EDA (15 visualizations), hypothesis testing, TF-IDF vectorization, and 
        model comparison (Logistic Regression, Random Forest, Naive Bayes). Logistic Regression 
        achieved the highest F1 score.
    </p>
    <div class="project-tech">
        <span class="tech-chip">Python</span>
        <span class="tech-chip">Scikit-learn</span>
        <span class="tech-chip">NLTK</span>
        <span class="tech-chip">TF-IDF</span>
        <span class="tech-chip">Pandas</span>
        <span class="tech-chip">Matplotlib</span>
    </div>
    <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="project-link">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)


# ─── Experience ───
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2>Work Experience</h2>
    <div class="section-divider"></div>
</div>

<div class="timeline-card">
    <div class="timeline-role">Data Science with Gen AI Intern</div>
    <div class="timeline-org">Innovexis</div>
    <div class="timeline-meta">Apr 2026 — Present · Remote</div>
    <ul class="timeline-bullets">
        <li>Selected for Innovexis's competitive Data Science with Generative AI internship after shortlisting from multiple applicants</li>
        <li>Working on real-world data science projects integrating large language models and generative AI techniques</li>
        <li>Applying Python, NumPy, Pandas, and Scikit-learn for data analysis, preprocessing, and model building</li>
        <li>Gaining hands-on exposure to production-level Gen AI workflows, LLM integration, and applied machine learning</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# ─── Education ───
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2>Education</h2>
    <div class="section-divider"></div>
</div>

<div class="timeline-card">
    <div class="timeline-role">B.Tech in Computer Science Engineering (AI & ML)</div>
    <div class="timeline-org">Vishwaniketan's Institute of Management Entrepreneurship and Engineering Technology (ViMEET)</div>
    <div class="timeline-meta">Jun 2023 — Present (Expected 2027)</div>
    <div class="timeline-desc">
        Currently pursuing a B.Tech in Computer Science Engineering, specializing in Artificial Intelligence & Machine Learning.
    </div>
    <div class="timeline-cgpa">CGPA: 7.5 / 10.0</div>
</div>
""", unsafe_allow_html=True)


# ─── Contact ───
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2>Get in Touch</h2>
    <p>Feel free to reach out for collaborations, opportunities, or just a chat</p>
    <div class="section-divider"></div>
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
<div class="footer">
    <p>Designed & built by <a href="https://github.com/Shravan157" target="_blank">Shravan Parthe</a> · 2026</p>
</div>
""", unsafe_allow_html=True)
