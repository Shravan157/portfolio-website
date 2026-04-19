import streamlit as st

# ─── Page Configuration ───
st.set_page_config(
    page_title="Shravan Parthe — Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ───
st.markdown("""
<style>
@import url('https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&f[]=cabinet-grotesk@700,800&display=swap');

:root {
    --bg: #0d1117;
    --surface: #161b22;
    --surface-2: #1c2129;
    --border: #30363d;
    --text: #e6edf3;
    --text-muted: #8b949e;
    --text-faint: #6e7681;
    --accent: #58a6ff;
    --accent-hover: #79b8ff;
    --accent-subtle: rgba(56, 139, 253, 0.15);
    --green: #3fb950;
    --green-subtle: rgba(63, 185, 80, 0.15);
    --purple: #bc8cff;
    --purple-subtle: rgba(188, 140, 255, 0.15);
    --orange: #f0883e;
    --orange-subtle: rgba(240, 136, 62, 0.15);
    --font-body: 'General Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-display: 'Cabinet Grotesk', 'General Sans', sans-serif;
}

/* Global overrides */
.stApp {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: var(--font-body) !important;
}

.block-container {
    max-width: 1100px !important;
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
}

/* Hide Streamlit defaults */
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

/* Navigation bar */
.nav-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 3rem;
}
.nav-logo {
    font-family: var(--font-display);
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--text);
    letter-spacing: -0.5px;
}
.nav-logo span { color: var(--accent); }
.nav-links {
    display: flex;
    gap: 2rem;
}
.nav-links a {
    color: var(--text-muted);
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    transition: color 0.2s;
}
.nav-links a:hover { color: var(--text); }

/* Hero Section */
.hero {
    padding: 4rem 0 3rem;
    text-align: left;
}
.hero-badge {
    display: inline-block;
    padding: 0.35rem 1rem;
    border-radius: 999px;
    background: var(--green-subtle);
    color: var(--green);
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    letter-spacing: 0.5px;
}
.hero h1 {
    font-family: var(--font-display);
    font-size: clamp(2.5rem, 5vw, 3.75rem);
    font-weight: 800;
    color: var(--text);
    line-height: 1.1;
    letter-spacing: -1.5px;
    margin-bottom: 1.25rem;
}
.hero h1 .accent { color: var(--accent); }
.hero-sub {
    font-size: 1.15rem;
    color: var(--text-muted);
    line-height: 1.7;
    max-width: 640px;
}
.hero-links {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
    flex-wrap: wrap;
}
.hero-links a {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.65rem 1.5rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s;
}
.btn-primary {
    background: var(--accent);
    color: #fff;
}
.btn-primary:hover {
    background: var(--accent-hover);
    transform: translateY(-1px);
}
.btn-outline {
    background: transparent;
    color: var(--text);
    border: 1px solid var(--border);
}
.btn-outline:hover {
    border-color: var(--text-muted);
    background: var(--surface);
}

/* Section Styles */
.section-header {
    margin: 4rem 0 2rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--border);
}
.section-header h2 {
    font-family: var(--font-display);
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.5px;
}
.section-header p {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-top: 0.4rem;
}

/* Stats row */
.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0;
}
.stat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    transition: border-color 0.2s;
}
.stat-card:hover { border-color: var(--accent); }
.stat-value {
    font-family: var(--font-display);
    font-size: 2rem;
    font-weight: 800;
    color: var(--accent);
}
.stat-label {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-top: 0.25rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Skill Tags */
.skills-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-top: 1rem;
}
.skill-tag {
    padding: 0.45rem 1rem;
    border-radius: 8px;
    font-size: 0.82rem;
    font-weight: 600;
    border: 1px solid transparent;
}
.skill-lang { background: var(--accent-subtle); color: var(--accent); border-color: rgba(56,139,253,0.3); }
.skill-frame { background: var(--green-subtle); color: var(--green); border-color: rgba(63,185,80,0.3); }
.skill-tool { background: var(--purple-subtle); color: var(--purple); border-color: rgba(188,140,255,0.3); }
.skill-data { background: var(--orange-subtle); color: var(--orange); border-color: rgba(240,136,62,0.3); }

/* Skill Category Header */
.skill-category {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-faint);
    margin-top: 1.5rem;
    margin-bottom: 0.6rem;
}

/* Project Cards */
.project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.75rem;
    margin-bottom: 1.25rem;
    transition: border-color 0.2s, transform 0.2s;
}
.project-card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
}
.project-card-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 0.75rem;
}
.project-card h3 {
    font-family: var(--font-display);
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--text);
    margin: 0;
}
.project-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 600;
    white-space: nowrap;
}
.badge-ai { background: var(--purple-subtle); color: var(--purple); }
.badge-fullstack { background: var(--green-subtle); color: var(--green); }
.badge-ml { background: var(--orange-subtle); color: var(--orange); }
.badge-fintech { background: var(--accent-subtle); color: var(--accent); }
.project-desc {
    color: var(--text-muted);
    font-size: 0.92rem;
    line-height: 1.65;
    margin-bottom: 1rem;
}
.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
}
.tech-chip {
    padding: 0.25rem 0.65rem;
    border-radius: 6px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 0.78rem;
    font-weight: 500;
}
.project-link {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: var(--accent);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 600;
}
.project-link:hover { color: var(--accent-hover); }

/* Experience / Education Cards */
.timeline-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem 1.75rem;
    margin-bottom: 1rem;
    position: relative;
}
.timeline-card::before {
    content: '';
    position: absolute;
    left: -1px;
    top: 1.5rem;
    bottom: 1.5rem;
    width: 3px;
    border-radius: 2px;
    background: var(--accent);
}
.timeline-role {
    font-family: var(--font-display);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text);
}
.timeline-org {
    color: var(--accent);
    font-size: 0.95rem;
    font-weight: 600;
}
.timeline-meta {
    color: var(--text-faint);
    font-size: 0.82rem;
    margin-top: 0.25rem;
}
.timeline-desc {
    color: var(--text-muted);
    font-size: 0.9rem;
    line-height: 1.6;
    margin-top: 0.6rem;
}

/* Contact Section */
.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
}
.contact-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    transition: border-color 0.2s;
}
.contact-card:hover { border-color: var(--accent); }
.contact-icon {
    font-size: 1.75rem;
    margin-bottom: 0.5rem;
}
.contact-label {
    font-size: 0.78rem;
    color: var(--text-faint);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
}
.contact-value {
    color: var(--text);
    font-size: 0.95rem;
    font-weight: 500;
    margin-top: 0.25rem;
}
.contact-value a {
    color: var(--accent);
    text-decoration: none;
}
.contact-value a:hover { color: var(--accent-hover); }

/* Footer */
.footer {
    text-align: center;
    padding: 3rem 0 2rem;
    border-top: 1px solid var(--border);
    margin-top: 4rem;
}
.footer p {
    color: var(--text-faint);
    font-size: 0.85rem;
}
.footer a {
    color: var(--text-muted);
    text-decoration: none;
}

/* Responsive */
@media (max-width: 768px) {
    .stats-row { grid-template-columns: repeat(2, 1fr); }
    .hero h1 { font-size: 2.25rem; }
    .nav-links { gap: 1rem; }
    .contact-grid { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)


# ─── Navigation ───
st.markdown("""
<div class="nav-bar">
    <div class="nav-logo">&lt;SP<span>/</span>&gt;</div>
    <div class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#experience">Experience</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Hero Section ───
st.markdown("""
<div class="hero">
    <div class="hero-badge">● Available for Internships & Collaborations</div>
    <h1>Hi, I'm <span class="accent">Shravan Parthe</span></h1>
    <p class="hero-sub">
        Computer Science & Engineering student at the University of Mumbai, building scalable 
        software systems at the intersection of <strong style="color:#e6edf3;">AI/ML</strong>, 
        <strong style="color:#e6edf3;">backend engineering</strong>, and 
        <strong style="color:#e6edf3;">full-stack development</strong>. 
        Currently interning as a Data Science Intern at Innovexis.
    </p>
    <div class="hero-links">
        <a href="https://github.com/Shravan157" target="_blank" class="btn-primary">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            GitHub
        </a>
        <a href="https://www.linkedin.com/in/shravan-parthe-00946b2ab" target="_blank" class="btn-outline">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            LinkedIn
        </a>
        <a href="mailto:shravanparthe@gmail.com" class="btn-outline">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 7L2 7"/></svg>
            Email
        </a>
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
        <div class="stat-value">6+</div>
        <div class="stat-label">Technologies</div>
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
</div>

<div class="skill-category">Languages</div>
<div class="skills-grid">
    <span class="skill-tag skill-lang">Python</span>
    <span class="skill-tag skill-lang">Java</span>
    <span class="skill-tag skill-lang">JavaScript</span>
    <span class="skill-tag skill-lang">Dart</span>
    <span class="skill-tag skill-lang">SQL</span>
    <span class="skill-tag skill-lang">HTML / CSS</span>
</div>

<div class="skill-category">Frameworks & Libraries</div>
<div class="skills-grid">
    <span class="skill-tag skill-frame">Spring Boot</span>
    <span class="skill-tag skill-frame">FastAPI</span>
    <span class="skill-tag skill-frame">React</span>
    <span class="skill-tag skill-frame">Flutter</span>
    <span class="skill-tag skill-frame">Gradio</span>
    <span class="skill-tag skill-frame">Tailwind CSS</span>
    <span class="skill-tag skill-frame">scikit-learn</span>
    <span class="skill-tag skill-frame">NLTK</span>
</div>

<div class="skill-category">Tools & Platforms</div>
<div class="skills-grid">
    <span class="skill-tag skill-tool">Git / GitHub</span>
    <span class="skill-tag skill-tool">Firebase</span>
    <span class="skill-tag skill-tool">MySQL</span>
    <span class="skill-tag skill-tool">Hugging Face</span>
    <span class="skill-tag skill-tool">Google Colab</span>
    <span class="skill-tag skill-tool">Vercel</span>
    <span class="skill-tag skill-tool">VS Code</span>
    <span class="skill-tag skill-tool">Stripe API</span>
</div>

<div class="skill-category">AI / ML & Data Science</div>
<div class="skills-grid">
    <span class="skill-tag skill-data">Machine Learning</span>
    <span class="skill-tag skill-data">NLP</span>
    <span class="skill-tag skill-data">Data Science</span>
    <span class="skill-tag skill-data">Data Intelligence</span>
    <span class="skill-tag skill-data">Computer Vision</span>
    <span class="skill-tag skill-data">TF-IDF / Text Classification</span>
</div>
""", unsafe_allow_html=True)


# ─── Projects ───
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2>Featured Projects</h2>
    <p>A selection of projects showcasing my work across AI, full-stack, and mobile development</p>
</div>
""", unsafe_allow_html=True)

# Project 1: MedoraX
st.markdown("""
<div class="project-card">
    <div class="project-card-header">
        <h3>🏥 MedoraX — AI Clinical Assistant</h3>
        <span class="project-badge badge-ai">Healthcare AI</span>
    </div>
    <p class="project-desc">
        An AI-powered multimodal healthcare diagnostic system providing real-time medical guidance through voice, 
        image, and text. Supports English, Hindi, and Marathi with speech-to-text via Whisper, medical image 
        analysis via Llama-4, and AI consultation via Llama-3.3-70b. Includes GPS-based hospital finder, 
        air quality monitoring, and emergency detection.
    </p>
    <div class="project-tech">
        <span class="tech-chip">Python</span>
        <span class="tech-chip">Gradio</span>
        <span class="tech-chip">Groq API</span>
        <span class="tech-chip">Llama 3.3 / 4</span>
        <span class="tech-chip">Whisper</span>
        <span class="tech-chip">Google Maps API</span>
        <span class="tech-chip">Edge TTS</span>
    </div>
    <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="project-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# Project 2: SikshaSetu
st.markdown("""
<div class="project-card">
    <div class="project-card-header">
        <h3>🎓 SikshaSetu — Education Portal</h3>
        <span class="project-badge badge-fullstack">Full-Stack</span>
    </div>
    <p class="project-desc">
        A modern full-stack college portal with user management, attendance tracking, results, events, notes, 
        notifications, and an AI chatbot. Features a virtual classroom powered by ZEGOCLOUD for real-time 
        video conferencing. Supports role-based access for Admin, Faculty, and Students.
    </p>
    <div class="project-tech">
        <span class="tech-chip">Java</span>
        <span class="tech-chip">Spring Boot 3</span>
        <span class="tech-chip">React 18</span>
        <span class="tech-chip">MySQL</span>
        <span class="tech-chip">JWT Auth</span>
        <span class="tech-chip">Tailwind CSS</span>
        <span class="tech-chip">ZEGOCLOUD</span>
    </div>
    <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="project-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# Project 3: Sahay Loan
st.markdown("""
<div class="project-card">
    <div class="project-card-header">
        <h3>🏦 SAHAY — Micro-Loan Platform</h3>
        <span class="project-badge badge-fintech">FinTech</span>
    </div>
    <p class="project-desc">
        A full-stack micro-lending platform for underserved communities in India. Users can apply for micro-loans 
        up to ₹1,00,000, get AI-powered credit scoring via a Random Forest ML model, complete digital KYC 
        with Aadhaar/PAN OCR, and repay EMIs via Stripe. Cross-platform Flutter app with FastAPI backend.
    </p>
    <div class="project-tech">
        <span class="tech-chip">Flutter</span>
        <span class="tech-chip">FastAPI</span>
        <span class="tech-chip">Firebase</span>
        <span class="tech-chip">scikit-learn</span>
        <span class="tech-chip">Stripe</span>
        <span class="tech-chip">Tesseract OCR</span>
    </div>
    <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="project-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# Project 4: Zomato Sentiment
st.markdown("""
<div class="project-card">
    <div class="project-card-header">
        <h3>🍽️ Zomato Sentiment Analysis</h3>
        <span class="project-badge badge-ml">ML / NLP</span>
    </div>
    <p class="project-desc">
        End-to-end NLP project to classify 10,000+ Zomato restaurant reviews as positive or negative. 
        Includes extensive EDA (15 visualizations), hypothesis testing (Mann-Whitney U, Spearman), 
        TF-IDF vectorization, and model comparison (Logistic Regression, Random Forest, Naive Bayes). 
        Logistic Regression achieved the highest F1 score.
    </p>
    <div class="project-tech">
        <span class="tech-chip">Python</span>
        <span class="tech-chip">scikit-learn</span>
        <span class="tech-chip">NLTK</span>
        <span class="tech-chip">TF-IDF</span>
        <span class="tech-chip">Pandas</span>
        <span class="tech-chip">Matplotlib</span>
    </div>
    <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="project-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# Project 5: Real Estate
st.markdown("""
<div class="project-card">
    <div class="project-card-header">
        <h3>🏠 Real Estate Investment Advisor</h3>
        <span class="project-badge badge-ai">AI / Data</span>
    </div>
    <p class="project-desc">
        An AI-powered real estate investment advisory tool built with Python. Helps users analyze 
        properties, assess investment potential, and make data-driven real estate decisions.
    </p>
    <div class="project-tech">
        <span class="tech-chip">Python</span>
        <span class="tech-chip">Data Analysis</span>
        <span class="tech-chip">Machine Learning</span>
    </div>
    <a href="https://github.com/Shravan157/Real-Estate-Investment-Advisor" target="_blank" class="project-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        View on GitHub
    </a>
</div>
""", unsafe_allow_html=True)


# ─── Experience ───
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2>Experience</h2>
    <p>Professional and academic journey</p>
</div>

<div class="timeline-card">
    <div class="timeline-role">Data Science Intern</div>
    <div class="timeline-org">Innovexis</div>
    <div class="timeline-meta">April 2026 — Present · India</div>
    <div class="timeline-desc">
        Working on data science and machine learning projects, applying statistical analysis, 
        NLP techniques, and predictive modeling to solve real-world problems.
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Education ───
st.markdown("""
<div class="section-header">
    <h2>Education</h2>
</div>

<div class="timeline-card">
    <div class="timeline-role">B.Tech — Computer Engineering</div>
    <div class="timeline-org">University of Mumbai</div>
    <div class="timeline-meta">2023 — 2027</div>
    <div class="timeline-desc">
        Coursework in data structures, algorithms, machine learning, cloud computing, 
        virtualization, system design, and software engineering.
    </div>
</div>

<div class="timeline-card">
    <div class="timeline-role">Bachelor of Science</div>
    <div class="timeline-org">Vishwaniketan iMEET</div>
    <div class="timeline-meta">Vishwaniketan Institute of Management Entrepreneurship and Engineering Technology</div>
</div>
""", unsafe_allow_html=True)


# ─── Contact ───
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <h2>Get in Touch</h2>
    <p>Feel free to reach out for collaborations, opportunities, or just a chat</p>
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
        <div class="contact-value">Mumbai, Maharashtra, India</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Footer ───
st.markdown("""
<div class="footer">
    <p>Designed & built by <a href="https://github.com/Shravan157" target="_blank">Shravan Parthe</a> · 2026</p>
</div>
""", unsafe_allow_html=True)
