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
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    .stApp {background: #080809;}
    section[data-testid="stSidebar"] {display: none;}
    iframe {display: block;}
</style>
""", unsafe_allow_html=True)

RESUME_URL = "https://raw.githubusercontent.com/Shravan157/portfolio-website/master/resume_shravan2.pdf"
GITHUB_URL = "https://github.com/Shravan157"
EMAIL     = "shravanparthe@gmail.com"
PHONE     = "+91 73858 13010"

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Shravan Parthe</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:          #080809;
      --surface:     #0F0F12;
      --surface2:    #161619;
      --border:      #1D1D24;
      --border2:     #28282F;
      --text:        #F0F0F4;
      --text2:       #9898A8;
      --text3:       #52525E;
      --accent:      #F97316;
      --accent2:     #FB923C;
      --accent-dim:  rgba(249,115,22,0.10);
      --accent-glow: rgba(249,115,22,0.22);
      --green:       #22C55E;
      --green-dim:   rgba(34,197,94,0.10);
      --blue:        #818CF8;
      --blue-dim:    rgba(129,140,248,0.10);
      --teal:        #2DD4BF;
      --teal-dim:    rgba(45,212,191,0.10);
      --purple-dim:  rgba(167,139,250,0.10);
      --yellow-dim:  rgba(234,179,8,0.10);
      --font-d: 'Syne', sans-serif;
      --font-b: 'Manrope', sans-serif;
      --font-m: 'JetBrains Mono', monospace;
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: var(--font-b);
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* grid bg */
    body::before {
      content: '';
      position: fixed; inset: 0; z-index: 0; pointer-events: none;
      background-image:
        linear-gradient(rgba(255,255,255,0.013) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.013) 1px, transparent 1px);
      background-size: 56px 56px;
    }
    /* ambient glow top-right */
    body::after {
      content: '';
      position: fixed; top: -280px; right: -280px;
      width: 680px; height: 680px; z-index: 0; pointer-events: none;
      background: radial-gradient(circle, rgba(249,115,22,0.055), transparent 65%);
    }

    * { position: relative; z-index: 1; }
    a { color: inherit; text-decoration: none; }

    .container {
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 clamp(1.2rem, 5vw, 2.5rem);
    }

    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: var(--surface); }
    ::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 99px; }

    /* ─────────── NAV ─────────── */
    #nav {
      position: sticky; top: 0; z-index: 999;
      background: rgba(8,8,9,0.82);
      backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
      border-bottom: 1px solid var(--border);
    }
    .nav-inner {
      max-width: 1100px; margin: 0 auto;
      padding: 0.9rem clamp(1.2rem,5vw,2.5rem);
      display: flex; align-items: center; justify-content: space-between;
    }
    .logo {
      display: flex; align-items: center; gap: 0.6rem;
      font-family: var(--font-d); font-weight: 800; font-size: 1rem;
      letter-spacing: -0.4px; color: var(--text);
    }
    .logo-mark {
      width: 30px; height: 30px; border-radius: 7px;
      background: var(--accent); display: flex; align-items: center; justify-content: center;
      font-family: var(--font-m); font-size: 0.62rem; color: #080809; font-weight: 700;
    }
    .nav-links { display: flex; align-items: center; gap: 0.2rem; }
    .nav-links a {
      font-family: var(--font-m); font-size: 0.67rem; color: var(--text2);
      padding: 0.4rem 0.85rem; border-radius: 6px;
      transition: all 0.2s; letter-spacing: 0.2px;
    }
    .nav-links a:hover { color: var(--text); background: var(--surface2); }
    .nav-cta {
      background: var(--accent-dim) !important;
      border: 1px solid rgba(249,115,22,0.28) !important;
      color: var(--accent) !important;
    }
    .nav-cta:hover { background: var(--accent-glow) !important; border-color: var(--accent) !important; }

    /* ─────────── HERO ─────────── */
    #hero { padding: 5rem 0 3.5rem; }
    .hero-grid {
      display: grid; grid-template-columns: 1fr 420px;
      gap: 4rem; align-items: center;
    }
    .hero-badge {
      display: inline-flex; align-items: center; gap: 0.5rem;
      font-family: var(--font-m); font-size: 0.63rem;
      color: var(--green); background: var(--green-dim);
      border: 1px solid rgba(34,197,94,0.2);
      padding: 0.28rem 0.85rem; border-radius: 99px;
      margin-bottom: 1.5rem; letter-spacing: 0.4px;
    }
    .badge-dot {
      width: 6px; height: 6px; border-radius: 50%;
      background: var(--green); animation: pulse-d 2s infinite;
    }
    @keyframes pulse-d {
      0%,100% { opacity:1; transform:scale(1); }
      50%      { opacity:0.45; transform:scale(0.8); }
    }
    .hero-name {
      font-family: var(--font-d); font-weight: 800;
      font-size: clamp(3rem,7vw,5rem);
      line-height: 1.0; letter-spacing: -2px;
      color: var(--text); margin-bottom: 0.5rem;
    }
    .hero-role {
      font-family: var(--font-d); font-weight: 700;
      font-size: clamp(1.2rem,3vw,1.7rem);
      color: var(--accent); letter-spacing: -0.3px;
      margin-bottom: 1.3rem; line-height: 1.2;
    }
    .hero-desc {
      font-size: 0.93rem; color: var(--text2); line-height: 1.8;
      max-width: 510px; margin-bottom: 2rem;
    }
    .hero-desc strong { color: var(--text); font-weight: 600; }
    .hero-actions { display: flex; gap: 0.7rem; flex-wrap: wrap; align-items: center; }
    .btn {
      display: inline-flex; align-items: center; gap: 0.45rem;
      padding: 0.68rem 1.35rem; border-radius: 8px;
      font-family: var(--font-m); font-size: 0.7rem; font-weight: 500;
      transition: all 0.2s; cursor: pointer; border: 1px solid transparent;
      letter-spacing: 0.15px;
    }
    .btn-primary { background: var(--accent); color: #080809; font-weight: 700; }
    .btn-primary:hover {
      background: var(--accent2); transform: translateY(-1px);
      box-shadow: 0 8px 22px var(--accent-glow);
    }
    .btn-ghost { background: var(--surface); border-color: var(--border2); color: var(--text2); }
    .btn-ghost:hover { border-color: var(--text3); color: var(--text); }
    .btn svg { flex-shrink: 0; }
    .hero-meta {
      display: flex; align-items: center; gap: 1.5rem;
      margin-top: 1.8rem; padding-top: 1.5rem;
      border-top: 1px solid var(--border); flex-wrap: wrap;
    }
    .meta-item {
      display: flex; align-items: center; gap: 0.4rem;
      font-family: var(--font-m); font-size: 0.6rem;
      color: var(--text3); letter-spacing: 0.2px;
    }
    .meta-item svg { width: 12px; height: 12px; stroke: var(--text3); fill: none; stroke-width: 2; }

    /* terminal */
    .terminal {
      background: var(--surface); border: 1px solid var(--border2);
      border-radius: 16px; overflow: hidden;
      box-shadow: 0 28px 52px rgba(0,0,0,0.45);
    }
    .term-bar {
      display: flex; align-items: center; gap: 0.5rem;
      padding: 0.8rem 1.2rem; border-bottom: 1px solid var(--border);
      background: var(--surface2);
    }
    .td { width: 10px; height: 10px; border-radius: 50%; }
    .td-r { background: #FF5F57; } .td-y { background: #FFBD2E; } .td-g { background: #28C840; }
    .term-title { font-family: var(--font-m); font-size: 0.6rem; color: var(--text3); margin: 0 auto; }
    .term-body { padding: 1.3rem 1.5rem; font-family: var(--font-m); font-size: 0.7rem; line-height: 2.05; }
    .tl { display: flex; gap: 0.75rem; }
    .tn { color: var(--text3); min-width: 1.4rem; text-align: right; font-size: 0.58rem; user-select: none; }
    .t-kw { color: var(--blue); } .t-str { color: var(--teal); } .t-cm { color: var(--text3); font-style: italic; }
    .t-fn { color: var(--accent2); } .t-pr { color: var(--green); } .t-br { color: var(--text2); }
    .tb { height: 0.5rem; }
    .cursor {
      display: inline-block; width: 2px; height: 1em;
      background: var(--accent); vertical-align: middle;
      animation: blink 1s step-end infinite; margin-left: 2px;
    }
    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
    .term-foot {
      padding: 0.8rem 1.5rem; border-top: 1px solid var(--border);
      display: flex; flex-wrap: wrap; gap: 0.35rem;
    }
    .tbadge {
      font-family: var(--font-m); font-size: 0.57rem;
      padding: 0.12rem 0.55rem; border-radius: 4px;
      border: 1px solid var(--border2); color: var(--text3); background: var(--bg);
    }

    /* ─────────── STATS ─────────── */
    #stats { padding: 1rem 0 4rem; }
    .stats-row {
      display: grid; grid-template-columns: repeat(4,1fr);
      border: 1px solid var(--border); border-radius: 12px;
      overflow: hidden; background: var(--surface);
    }
    .stat-item {
      padding: 1.8rem 1.2rem; text-align: center;
      border-right: 1px solid var(--border); transition: background 0.2s;
    }
    .stat-item:last-child { border-right: none; }
    .stat-item:hover { background: var(--surface2); }
    .stat-num {
      font-family: var(--font-d); font-size: 2.4rem; font-weight: 800;
      color: var(--accent); line-height: 1; margin-bottom: 0.45rem;
    }
    .stat-label {
      font-family: var(--font-m); font-size: 0.57rem;
      letter-spacing: 1.5px; text-transform: uppercase; color: var(--text3);
    }

    /* ─────────── SHARED SECTION HEAD ─────────── */
    .sec-head { margin-bottom: 2.5rem; }
    .sec-tag {
      font-family: var(--font-m); font-size: 0.6rem;
      color: var(--accent); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 0.5rem;
    }
    .sec-title {
      font-family: var(--font-d); font-weight: 800;
      font-size: clamp(1.7rem,3.5vw,2.2rem);
      letter-spacing: -0.7px; color: var(--text); line-height: 1.15;
    }

    /* ─────────── SKILLS ─────────── */
    #skills { padding: 4rem 0; }
    .skills-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 0.75rem; }
    .skill-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; padding: 1.4rem; transition: all 0.25s;
    }
    .skill-card:hover { border-color: var(--border2); background: var(--surface2); transform: translateY(-2px); }
    .skill-head { display: flex; align-items: center; gap: 0.65rem; margin-bottom: 1rem; }
    .sk-ico {
      width: 30px; height: 30px; border-radius: 7px;
      display: flex; align-items: center; justify-content: center; font-size: 0.85rem;
    }
    .ico-o  { background: var(--accent-dim); }
    .ico-b  { background: var(--blue-dim); }
    .ico-t  { background: var(--teal-dim); }
    .ico-p  { background: var(--purple-dim); }
    .ico-g  { background: var(--green-dim); }
    .ico-y  { background: var(--yellow-dim); }
    .sk-name {
      font-family: var(--font-m); font-size: 0.6rem; font-weight: 500;
      color: var(--text2); text-transform: uppercase; letter-spacing: 1.2px;
    }
    .chips { display: flex; flex-wrap: wrap; gap: 0.35rem; }
    .chip {
      font-family: var(--font-m); font-size: 0.64rem;
      padding: 0.2rem 0.65rem; border-radius: 40px;
      border: 1px solid var(--border2); color: var(--text2); background: var(--bg);
      transition: all 0.15s;
    }
    .chip:hover { border-color: var(--accent); color: var(--accent); background: var(--accent-dim); }

    /* ─────────── PROJECTS ─────────── */
    #projects { padding: 4rem 0; }
    .proj-featured { display: grid; grid-template-columns: repeat(2,1fr); gap: 0.85rem; margin-bottom: 0.85rem; }
    .proj-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 14px; padding: 1.8rem; transition: all 0.3s;
      display: flex; flex-direction: column;
    }
    .proj-card:hover {
      border-color: var(--border2); background: var(--surface2);
      transform: translateY(-3px); box-shadow: 0 18px 36px rgba(0,0,0,0.32);
    }
    .proj-card.hi:hover { border-color: rgba(249,115,22,0.38); }
    .proj-top { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 0.85rem; }
    .proj-num { font-family: var(--font-m); font-size: 0.58rem; color: var(--text3); }
    .proj-links { display: flex; gap: 0.4rem; }
    .proj-link {
      display: flex; align-items: center; justify-content: center;
      width: 28px; height: 28px; border-radius: 7px;
      border: 1px solid var(--border2); background: var(--surface2); transition: all 0.2s;
    }
    .proj-link:hover { border-color: var(--accent); background: var(--accent-dim); }
    .proj-link svg { width: 13px; height: 13px; stroke: var(--text3); fill: none; stroke-width: 2; transition: stroke 0.2s; }
    .proj-link:hover svg { stroke: var(--accent); }
    .proj-name {
      font-family: var(--font-d); font-size: 1.12rem; font-weight: 700;
      color: var(--text); letter-spacing: -0.3px; margin-bottom: 0.35rem;
    }
    .proj-period { font-family: var(--font-m); font-size: 0.58rem; color: var(--text3); margin-bottom: 0.75rem; }
    .proj-desc { font-size: 0.85rem; color: var(--text2); line-height: 1.75; margin-bottom: 1.2rem; flex: 1; }
    .proj-stack { display: flex; flex-wrap: wrap; gap: 0.3rem; }
    .s-tag {
      font-family: var(--font-m); font-size: 0.58rem;
      padding: 0.13rem 0.52rem; border-radius: 4px;
      background: var(--surface2); border: 1px solid var(--border); color: var(--text3);
    }

    /* smaller project cards row */
    .proj-row { display: grid; grid-template-columns: repeat(3,1fr); gap: 0.85rem; }
    .proj-sm {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; padding: 1.4rem; transition: all 0.25s;
    }
    .proj-sm:hover { border-color: var(--border2); transform: translateY(-2px); }
    .sm-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.6rem; }
    .sm-name {
      font-family: var(--font-d); font-size: 0.92rem; font-weight: 700;
      color: var(--text); letter-spacing: -0.2px; margin-bottom: 0.4rem;
    }
    .sm-desc { font-size: 0.78rem; color: var(--text3); line-height: 1.65; margin-bottom: 0.85rem; }

    /* other-work subheader */
    .sub-head { margin-top: 3rem; margin-bottom: 1.5rem; }
    .sub-title {
      font-family: var(--font-d); font-size: 1.3rem; font-weight: 700;
      color: var(--text); letter-spacing: -0.3px;
    }

    /* ─────────── EXPERIENCE ─────────── */
    #experience { padding: 4rem 0; }
    .exp-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 14px; padding: 2.2rem;
      display: grid; grid-template-columns: auto 1fr; gap: 2rem;
    }
    .exp-l { display: flex; flex-direction: column; align-items: center; gap: 0.5rem; }
    .exp-logo {
      width: 48px; height: 48px; border-radius: 12px;
      background: var(--accent-dim); border: 1px solid rgba(249,115,22,0.22);
      display: flex; align-items: center; justify-content: center;
      font-family: var(--font-m); font-size: 0.6rem; color: var(--accent); font-weight: 700;
    }
    .exp-vl { flex: 1; width: 1px; background: var(--border); }
    .exp-role { font-family: var(--font-d); font-size: 1.1rem; font-weight: 700; color: var(--text); letter-spacing: -0.3px; }
    .exp-co { font-family: var(--font-m); font-size: 0.7rem; color: var(--accent); margin: 0.3rem 0; }
    .exp-per { font-family: var(--font-m); font-size: 0.6rem; color: var(--text3); margin-bottom: 1.1rem; }
    .exp-ul { list-style: none; }
    .exp-ul li {
      font-size: 0.88rem; color: var(--text2); line-height: 1.75;
      padding-left: 1.3rem; position: relative; margin-bottom: 0.35rem;
    }
    .exp-ul li::before { content: '→'; position: absolute; left: 0; color: var(--accent); font-size: 0.72rem; top: 0.12rem; }
    .exp-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 1rem; }
    .exp-tag {
      font-family: var(--font-m); font-size: 0.58rem;
      padding: 0.18rem 0.62rem; border-radius: 40px;
      border: 1px solid var(--border2); color: var(--text3); background: var(--bg);
    }

    /* ─────────── EDUCATION ─────────── */
    #education { padding: 4rem 0; }
    .edu-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 14px; padding: 2.2rem;
      display: flex; justify-content: space-between; align-items: center; gap: 2rem;
    }
    .edu-l { flex: 1; }
    .edu-degree { font-family: var(--font-d); font-size: 1.1rem; font-weight: 700; color: var(--text); letter-spacing: -0.3px; margin-bottom: 0.3rem; }
    .edu-school { font-family: var(--font-m); font-size: 0.68rem; color: var(--accent); margin-bottom: 0.3rem; line-height: 1.5; }
    .edu-per { font-family: var(--font-m); font-size: 0.6rem; color: var(--text3); margin-bottom: 0.85rem; }
    .edu-desc { font-size: 0.85rem; color: var(--text2); line-height: 1.7; max-width: 580px; }
    .edu-r { text-align: right; flex-shrink: 0; }
    .cgpa-lbl { font-family: var(--font-m); font-size: 0.58rem; color: var(--text3); letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 0.25rem; }
    .cgpa-val { font-family: var(--font-d); font-size: 2.8rem; font-weight: 800; color: var(--accent); line-height: 1; }
    .cgpa-max { font-family: var(--font-m); font-size: 0.68rem; color: var(--text3); }

    /* ─────────── CONTACT ─────────── */
    #contact { padding: 4rem 0 5.5rem; }
    .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }
    .contact-h {
      font-family: var(--font-d); font-weight: 800;
      font-size: clamp(1.8rem,4vw,2.8rem); line-height: 1.15;
      letter-spacing: -1px; margin-bottom: 1rem;
    }
    .contact-h span { color: var(--accent); }
    .contact-sub { font-size: 0.9rem; color: var(--text2); line-height: 1.75; margin-bottom: 1.5rem; }
    .c-cards { display: flex; flex-direction: column; gap: 0.6rem; }
    .c-item {
      display: flex; align-items: center; gap: 1rem;
      padding: 1rem 1.2rem; background: var(--surface);
      border: 1px solid var(--border); border-radius: 12px;
      transition: all 0.2s; color: var(--text);
    }
    .c-item:hover { border-color: var(--accent); background: var(--surface2); transform: translateX(4px); }
    .c-ico {
      width: 36px; height: 36px; border-radius: 9px;
      background: var(--surface2); border: 1px solid var(--border2);
      display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }
    .c-ico svg { width: 16px; height: 16px; stroke: var(--text2); fill: none; stroke-width: 2; }
    .c-meta { flex: 1; }
    .c-lbl { font-family: var(--font-m); font-size: 0.53rem; color: var(--text3); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.18rem; }
    .c-val { font-size: 0.87rem; font-weight: 500; color: var(--text); }
    .c-arr { color: var(--text3); font-size: 0.9rem; transition: all 0.2s; }
    .c-item:hover .c-arr { color: var(--accent); transform: translateX(3px); }
    .resume-blk {
      background: linear-gradient(145deg, var(--accent-dim), rgba(249,115,22,0.04));
      border: 1px solid rgba(249,115,22,0.22); border-radius: 14px; padding: 2rem;
    }
    .res-title { font-family: var(--font-d); font-size: 1.05rem; font-weight: 700; color: var(--text); margin-bottom: 0.45rem; }
    .res-sub { font-size: 0.82rem; color: var(--text2); margin-bottom: 1.3rem; line-height: 1.65; }
    .res-info { margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border); }
    .res-info-lbl { font-family: var(--font-m); font-size: 0.58rem; color: var(--text3); letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 0.8rem; }
    .info-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.55rem; }
    .info-k { font-family: var(--font-m); font-size: 0.67rem; color: var(--text3); }
    .info-v { font-size: 0.82rem; color: var(--text2); }
    .info-v.green { color: var(--green); }

    /* ─────────── DIVIDER ─────────── */
    .div { height: 1px; background: linear-gradient(90deg, transparent, var(--border) 30%, var(--border) 70%, transparent); }

    /* ─────────── FOOTER ─────────── */
    footer { border-top: 1px solid var(--border); padding: 1.5rem 0; }
    .foot-inner {
      max-width: 1100px; margin: 0 auto;
      padding: 0 clamp(1.2rem,5vw,2.5rem);
      display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.8rem;
    }
    .foot-copy { font-family: var(--font-m); font-size: 0.58rem; color: var(--text3); }
    .foot-links { display: flex; gap: 1.5rem; }
    .foot-links a { font-family: var(--font-m); font-size: 0.58rem; color: var(--text3); transition: color 0.2s; }
    .foot-links a:hover { color: var(--accent); }

    /* ─────────── REVEAL ─────────── */
    .reveal { opacity: 0; transform: translateY(22px); transition: opacity 0.55s ease, transform 0.55s ease; }
    .reveal.in { opacity: 1; transform: none; }

    /* ─────────── RESPONSIVE ─────────── */
    @media (max-width: 900px) {
      .hero-grid  { grid-template-columns: 1fr; }
      .terminal   { display: none; }
      .stats-row  { grid-template-columns: repeat(2,1fr); }
      .skills-grid { grid-template-columns: repeat(2,1fr); }
      .proj-featured { grid-template-columns: 1fr; }
      .proj-row   { grid-template-columns: 1fr; }
      .contact-grid { grid-template-columns: 1fr; gap: 2.5rem; }
      .edu-card   { flex-direction: column; gap: 1rem; }
      .edu-r      { text-align: left; }
    }
    @media (max-width: 560px) {
      .nav-links a:not(.nav-cta) { display: none; }
      .stats-row  { grid-template-columns: repeat(2,1fr); }
      .skills-grid { grid-template-columns: 1fr; }
      .hero-meta  { gap: 0.9rem; }
    }
  </style>
</head>
<body>

<!-- ═══════ NAV ═══════ -->
<nav id="nav">
  <div class="nav-inner">
    <div class="logo">
      <div class="logo-mark">SP</div>
      Shravan Parthe
    </div>
    <div class="nav-links">
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#experience">Experience</a>
      <a href="#contact">Contact</a>
      <a href="RESUME_URL_PH" target="_blank" class="nav-cta">Resume ↗</a>
    </div>
  </div>
</nav>

<!-- ═══════ HERO ═══════ -->
<section id="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <div class="hero-badge"><span class="badge-dot"></span>Open to opportunities</div>
        <h1 class="hero-name">Shravan<br>Parthe.</h1>
        <p class="hero-role">Backend + AI/ML Developer</p>
        <p class="hero-desc">
          Final-year B.Tech CSE (AI &amp; ML) student at ViMEET, University of Mumbai.
          I build <strong>production-grade backend systems</strong> with Java &amp; Spring Boot
          and integrate <strong>AI/ML pipelines</strong> that solve real-world problems —
          from clinical diagnostics to micro-lending platforms.
        </p>
        <div class="hero-actions">
          <a href="#projects" class="btn btn-primary">View Projects →</a>
          <a href="GITHUB_URL_PH" target="_blank" class="btn btn-ghost">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
            </svg>
            GitHub
          </a>
          <a href="mailto:EMAIL_PH" class="btn btn-ghost">Email Me</a>
        </div>
        <div class="hero-meta">
          <div class="meta-item">
            <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>
            Mumbai, India
          </div>
          <div class="meta-item">
            <svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>
            ViMEET · CGPA 7.5
          </div>
          <div class="meta-item">
            <svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
            Data Science Intern · Innovexis
          </div>
        </div>
      </div>

      <!-- TERMINAL CARD -->
      <div class="terminal">
        <div class="term-bar">
          <div class="td td-r"></div><div class="td td-y"></div><div class="td td-g"></div>
          <span class="term-title">Shravan.java</span>
        </div>
        <div class="term-body">
          <div class="tl"><span class="tn">1</span><span class="t-cm">// Developer profile · 2026</span></div>
          <div class="tb"></div>
          <div class="tl"><span class="tn">3</span><span class="t-kw">public class&nbsp;</span><span class="t-fn">Shravan</span><span class="t-br"> {</span></div>
          <div class="tb"></div>
          <div class="tl"><span class="tn">5</span><span style="color:var(--text3)">&nbsp;&nbsp;</span><span class="t-kw">String&nbsp;</span><span class="t-pr">name</span><span class="t-br"> = </span><span class="t-str">"Shravan Parthe"</span><span class="t-br">;</span></div>
          <div class="tl"><span class="tn">6</span><span style="color:var(--text3)">&nbsp;&nbsp;</span><span class="t-kw">String&nbsp;</span><span class="t-pr">role</span><span class="t-br"> = </span><span class="t-str">"Backend + AI Dev"</span><span class="t-br">;</span></div>
          <div class="tl"><span class="tn">7</span><span style="color:var(--text3)">&nbsp;&nbsp;</span><span class="t-kw">int&nbsp;</span><span class="t-pr">year</span><span class="t-br"> = </span><span class="t-str">4</span><span class="t-br">;</span><span class="t-cm"> // final year</span></div>
          <div class="tb"></div>
          <div class="tl"><span class="tn">9</span><span style="color:var(--text3)">&nbsp;&nbsp;</span><span class="t-kw">String</span><span class="t-br">[] </span><span class="t-pr">backend</span><span class="t-br"> = {</span></div>
          <div class="tl"><span class="tn">10</span><span style="color:var(--text3)">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="t-str">"Java"</span><span class="t-br">,&nbsp;</span><span class="t-str">"Spring Boot"</span><span class="t-br">,&nbsp;</span><span class="t-str">"Spring AI"</span></div>
          <div class="tl"><span class="tn">11</span><span style="color:var(--text3)">&nbsp;&nbsp;</span><span class="t-br">};</span></div>
          <div class="tb"></div>
          <div class="tl"><span class="tn">13</span><span style="color:var(--text3)">&nbsp;&nbsp;</span><span class="t-kw">String</span><span class="t-br">[] </span><span class="t-pr">aiml</span><span class="t-br"> = {</span></div>
          <div class="tl"><span class="tn">14</span><span style="color:var(--text3)">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="t-str">"Python"</span><span class="t-br">,&nbsp;</span><span class="t-str">"LangChain"</span><span class="t-br">,&nbsp;</span><span class="t-str">"Groq"</span></div>
          <div class="tl"><span class="tn">15</span><span style="color:var(--text3)">&nbsp;&nbsp;</span><span class="t-br">};</span></div>
          <div class="tb"></div>
          <div class="tl"><span class="tn">17</span><span style="color:var(--text3)">&nbsp;&nbsp;</span><span class="t-kw">boolean&nbsp;</span><span class="t-pr">openToWork</span><span class="t-br"> = </span><span class="t-str">true</span><span class="t-br">;</span><span class="cursor"></span></div>
          <div class="tl"><span class="tn">18</span><span class="t-br">}</span></div>
        </div>
        <div class="term-foot">
          <span class="tbadge">Java</span><span class="tbadge">Spring Boot</span><span class="tbadge">Spring AI</span>
          <span class="tbadge">Python</span><span class="tbadge">FastAPI</span><span class="tbadge">LangChain4j</span>
          <span class="tbadge">Flutter</span><span class="tbadge">React</span><span class="tbadge">Redis</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════ STATS ═══════ -->
<section id="stats">
  <div class="container">
    <div class="stats-row reveal">
      <div class="stat-item">
        <div class="stat-num">7+</div>
        <div class="stat-label">Projects Built</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">15+</div>
        <div class="stat-label">Technologies</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">7.5</div>
        <div class="stat-label">CGPA · ViMEET</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">4</div>
        <div class="stat-label">Domains Shipped</div>
      </div>
    </div>
  </div>
</section>

<div class="div"></div>

<!-- ═══════ SKILLS ═══════ -->
<section id="skills">
  <div class="container">
    <div class="sec-head reveal">
      <div class="sec-tag">02 — Capabilities</div>
      <h2 class="sec-title">Tech Stack</h2>
    </div>
    <div class="skills-grid reveal">

      <div class="skill-card">
        <div class="skill-head"><div class="sk-ico ico-o">⚙️</div><span class="sk-name">Backend</span></div>
        <div class="chips">
          <span class="chip">Java</span><span class="chip">Spring Boot</span>
          <span class="chip">Spring Security</span><span class="chip">Spring AI</span>
          <span class="chip">FastAPI</span><span class="chip">REST APIs</span>
          <span class="chip">JWT / OAuth 2.0</span>
        </div>
      </div>

      <div class="skill-card">
        <div class="skill-head"><div class="sk-ico ico-b">🤖</div><span class="sk-name">AI / ML</span></div>
        <div class="chips">
          <span class="chip">Python</span><span class="chip">Scikit-learn</span>
          <span class="chip">LangChain4j</span><span class="chip">Groq API</span>
          <span class="chip">XGBoost</span><span class="chip">NumPy</span>
          <span class="chip">Pandas</span><span class="chip">NLTK</span>
        </div>
      </div>

      <div class="skill-card">
        <div class="skill-head"><div class="sk-ico ico-t">🗄️</div><span class="sk-name">Databases</span></div>
        <div class="chips">
          <span class="chip">MySQL</span><span class="chip">PostgreSQL</span>
          <span class="chip">Redis</span><span class="chip">Redis Vector DB</span>
          <span class="chip">Firebase</span><span class="chip">Firestore</span>
        </div>
      </div>

      <div class="skill-card">
        <div class="skill-head"><div class="sk-ico ico-p">🌐</div><span class="sk-name">Frontend</span></div>
        <div class="chips">
          <span class="chip">React.js</span><span class="chip">JavaScript</span>
          <span class="chip">Tailwind CSS</span><span class="chip">Streamlit</span>
          <span class="chip">Gradio</span>
        </div>
      </div>

      <div class="skill-card">
        <div class="skill-head"><div class="sk-ico ico-g">📱</div><span class="sk-name">Mobile</span></div>
        <div class="chips">
          <span class="chip">Flutter</span><span class="chip">Dart</span>
          <span class="chip">Firebase Auth</span><span class="chip">Stripe SDK</span>
          <span class="chip">Push Notifications</span>
        </div>
      </div>

      <div class="skill-card">
        <div class="skill-head"><div class="sk-ico ico-y">🛠️</div><span class="sk-name">DevOps / Tools</span></div>
        <div class="chips">
          <span class="chip">Docker</span><span class="chip">Git</span>
          <span class="chip">Maven</span><span class="chip">Flyway</span>
          <span class="chip">Hugging Face</span><span class="chip">JPA/Hibernate</span>
        </div>
      </div>

    </div>
  </div>
</section>

<div class="div"></div>

<!-- ═══════ PROJECTS ═══════ -->
<section id="projects">
  <div class="container">
    <div class="sec-head reveal">
      <div class="sec-tag">03 — Work</div>
      <h2 class="sec-title">Featured Projects</h2>
    </div>

    <div class="proj-featured reveal">
      <!-- MedoraX AI -->
      <div class="proj-card hi">
        <div class="proj-top">
          <span class="proj-num">01 / HEALTHCARE AI</span>
          <div class="proj-links">
            <a href="https://github.com/Shravan157/MedX-AI-Clinical-Assistant" target="_blank" class="proj-link">
              <svg viewBox="0 0 24 24"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </div>
        <h3 class="proj-name">MedoraX AI</h3>
        <p class="proj-period">Apr 2026 – May 2026</p>
        <p class="proj-desc">Multimodal clinical AI assistant supporting voice, image, and text inputs. Transcribes symptoms via Whisper-large-v3, analyzes medical images via Llama-4-scout, and generates structured diagnostic responses with Llama-3.3-70b. Supports English, Hindi, and Marathi with Edge TTS output. Integrated GPS-based hospital finder and real-time AQI monitoring. Deployed on Hugging Face Spaces with a three-tier caching system achieving 4–7 second response times.</p>
        <div class="proj-stack">
          <span class="s-tag">Python</span><span class="s-tag">Gradio</span><span class="s-tag">Groq API</span>
          <span class="s-tag">Whisper-v3</span><span class="s-tag">Llama-4-scout</span><span class="s-tag">Google Maps API</span>
          <span class="s-tag">HuggingFace Spaces</span>
        </div>
      </div>

      <!-- SahayLoan -->
      <div class="proj-card">
        <div class="proj-top">
          <span class="proj-num">02 / FINTECH</span>
          <div class="proj-links">
            <a href="https://github.com/Shravan157/Sahay-Loan" target="_blank" class="proj-link">
              <svg viewBox="0 0 24 24"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </div>
        <h3 class="proj-name">SahayLoan</h3>
        <p class="proj-period">Oct 2025 – Nov 2025</p>
        <p class="proj-desc">Full-stack micro-lending platform (₹500–₹1,00,000) built for underserved communities. Flutter mobile app with FastAPI backend. Random Forest ML credit scoring engine evaluates borrower creditworthiness. Tesseract OCR handles Aadhaar/PAN KYC digitally. Multi-role system (Borrower, Admin, Loan Provider) with Firebase Auth, Firestore, push notifications, and Stripe EMI payments.</p>
        <div class="proj-stack">
          <span class="s-tag">Flutter</span><span class="s-tag">Dart</span><span class="s-tag">FastAPI</span>
          <span class="s-tag">Scikit-learn</span><span class="s-tag">Firebase</span>
          <span class="s-tag">Tesseract OCR</span><span class="s-tag">Stripe</span>
        </div>
      </div>

      <!-- SikshaSetu -->
      <div class="proj-card">
        <div class="proj-top">
          <span class="proj-num">03 / EDTECH</span>
          <div class="proj-links">
            <a href="https://github.com/Shravan157/SikshaSetu_Edu_App" target="_blank" class="proj-link">
              <svg viewBox="0 0 24 24"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </div>
        <h3 class="proj-name">SikshaSetu</h3>
        <p class="proj-period">Jan 2025 – Apr 2025</p>
        <p class="proj-desc">Full-stack college management platform bridging the digital divide for rural communities. RBAC with Spring Security + JWT/OAuth 2.0. Virtual classrooms via ZEGOCLOUD real-time video SDK. AI chatbot via Perplexity API with LangChain4j RAG integration. Covers attendance, results, events, faculty notes, and live session scheduling for 3 user roles.</p>
        <div class="proj-stack">
          <span class="s-tag">Spring Boot</span><span class="s-tag">React</span><span class="s-tag">MySQL</span>
          <span class="s-tag">LangChain4j</span><span class="s-tag">ZEGOCLOUD</span><span class="s-tag">JWT</span>
          <span class="s-tag">Spring Security</span>
        </div>
      </div>

      <!-- AI E-Commerce -->
      <div class="proj-card">
        <div class="proj-top">
          <span class="proj-num">04 / E-COMMERCE</span>
          <div class="proj-links">
            <a href="GITHUB_URL_PH" target="_blank" class="proj-link">
              <svg viewBox="0 0 24 24"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </a>
          </div>
        </div>
        <h3 class="proj-name">AI-Powered E-Commerce</h3>
        <p class="proj-period">Oct 2024 – Jan 2025</p>
        <p class="proj-desc">Intelligent e-commerce backend with AI-driven product recommendations using Spring AI and vector similarity search via Redis Vector DB. Generative AI chatbot for real-time customer support. AI-powered product image generation pipeline. Secure authentication with Spring Security + JWT. React frontend with Tailwind CSS.</p>
        <div class="proj-stack">
          <span class="s-tag">Spring Boot</span><span class="s-tag">Spring AI</span>
          <span class="s-tag">Redis Vector DB</span><span class="s-tag">React</span>
          <span class="s-tag">Tailwind CSS</span><span class="s-tag">Spring Security</span>
        </div>
      </div>
    </div>

    <!-- Other projects -->
    <div class="sub-head reveal">
      <div class="sec-tag">03 — More Work</div>
      <h3 class="sub-title">Other Projects</h3>
    </div>
    <div class="proj-row reveal">
      <div class="proj-sm">
        <div class="sm-top">
          <span class="proj-num">05 / DATA SCIENCE</span>
          <a href="https://github.com/Shravan157/tourism_project" target="_blank" class="proj-link">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--text3)" stroke-width="2" width="13" height="13"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
          </a>
        </div>
        <h4 class="sm-name">Tourism Analytics</h4>
        <p class="sm-desc">Streamlit app for tourism experience analytics — attraction rating prediction, visit-mode classification (Solo/Couples/Family/Friends/Business), and collaborative-filtering recommendation using XGBoost.</p>
        <div class="proj-stack">
          <span class="s-tag">Python</span><span class="s-tag">Streamlit</span>
          <span class="s-tag">XGBoost</span><span class="s-tag">Scikit-learn</span>
        </div>
      </div>

      <div class="proj-sm">
        <div class="sm-top">
          <span class="proj-num">06 / NLP</span>
          <a href="https://github.com/Shravan157/Zomato-Restaurant-Review-Sentiment-Analysis" target="_blank" class="proj-link">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--text3)" stroke-width="2" width="13" height="13"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
          </a>
        </div>
        <h4 class="sm-name">Zomato Sentiment Pipeline</h4>
        <p class="sm-desc">End-to-end NLP pipeline classifying Zomato restaurant reviews as Positive/Negative using TF-IDF vectorization, GridSearchCV hyperparameter tuning, and three classifier comparison.</p>
        <div class="proj-stack">
          <span class="s-tag">Python</span><span class="s-tag">NLTK</span>
          <span class="s-tag">TF-IDF</span><span class="s-tag">Scikit-learn</span>
        </div>
      </div>

      <div class="proj-sm">
        <div class="sm-top">
          <span class="proj-num">07 / ANALYTICS</span>
          <a href="https://github.com/Shravan157/phonepe-insights" target="_blank" class="proj-link">
            <svg viewBox="0 0 24 24" fill="none" stroke="var(--text3)" stroke-width="2" width="13" height="13"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
          </a>
        </div>
        <h4 class="sm-name">PhonePe Insights</h4>
        <p class="sm-desc">ETL pipeline ingesting PhonePe transaction CSVs into MySQL with an interactive Streamlit dashboard for transaction volume, geographic distribution, and category analytics via Plotly.</p>
        <div class="proj-stack">
          <span class="s-tag">Python</span><span class="s-tag">MySQL</span>
          <span class="s-tag">Streamlit</span><span class="s-tag">Plotly</span>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="div"></div>

<!-- ═══════ EXPERIENCE ═══════ -->
<section id="experience">
  <div class="container">
    <div class="sec-head reveal">
      <div class="sec-tag">04 — Experience</div>
      <h2 class="sec-title">Work History</h2>
    </div>
    <div class="exp-card reveal">
      <div class="exp-l">
        <div class="exp-logo">INX</div>
        <div class="exp-vl"></div>
      </div>
      <div>
        <p class="exp-role">Data Science with Gen AI Intern</p>
        <p class="exp-co">Innovexis · Remote</p>
        <p class="exp-per">Jan 2026 – Mar 2026</p>
        <ul class="exp-ul">
          <li>Selected for a competitive Data Science with Generative AI internship program, shortlisted from a pool of multiple candidates</li>
          <li>Worked on real-world data science projects integrating large language models and generative AI techniques into production workflows</li>
          <li>Applied Python, NumPy, Pandas, and Scikit-learn for data analysis, preprocessing, feature engineering, and model building</li>
          <li>Gained hands-on exposure to production-level Gen AI workflows, LLM integration patterns, and applied machine learning at scale</li>
        </ul>
        <div class="exp-tags">
          <span class="exp-tag">Python</span><span class="exp-tag">NumPy</span>
          <span class="exp-tag">Pandas</span><span class="exp-tag">Scikit-learn</span>
          <span class="exp-tag">FastAPI</span><span class="exp-tag">LLM Integration</span>
          <span class="exp-tag">Gen AI</span>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="div"></div>

<!-- ═══════ EDUCATION ═══════ -->
<section id="education">
  <div class="container">
    <div class="sec-head reveal">
      <div class="sec-tag">05 — Background</div>
      <h2 class="sec-title">Education</h2>
    </div>
    <div class="edu-card reveal">
      <div class="edu-l">
        <p class="edu-degree">B.Tech — Computer Science Engineering (AI &amp; ML)</p>
        <p class="edu-school">Vishwaniketan's Institute of Management Entrepreneurship &amp; Engineering Technology (ViMEET) · University of Mumbai</p>
        <p class="edu-per">Jun 2023 – Expected May 2027</p>
        <p class="edu-desc">Specializing in Artificial Intelligence and Machine Learning. Coursework spans Neural Networks, Distributed Computing, Data Analytics &amp; Visualization, Cryptography &amp; System Security, and Software Engineering &amp; Project Management. Built 7+ production-grade projects across healthcare, fintech, edtech, and e-commerce domains during the program.</p>
      </div>
      <div class="edu-r">
        <p class="cgpa-lbl">CGPA</p>
        <p class="cgpa-val">7.5</p>
        <p class="cgpa-max">/ 10.0</p>
      </div>
    </div>
  </div>
</section>

<div class="div"></div>

<!-- ═══════ CONTACT ═══════ -->
<section id="contact">
  <div class="container">
    <div class="contact-grid reveal">
      <div>
        <div class="sec-tag">06 — Get In Touch</div>
        <h2 class="contact-h">Let's build<br>something <span>great.</span></h2>
        <p class="contact-sub">Open to backend engineering, AI/ML engineering, and full-stack roles. Whether it's a full-time position, internship, or a project collaboration — I'd love to hear from you.</p>
        <div class="c-cards">
          <a href="mailto:EMAIL_PH" class="c-item">
            <div class="c-ico">
              <svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
            </div>
            <div class="c-meta">
              <p class="c-lbl">Email</p>
              <p class="c-val">EMAIL_PH</p>
            </div>
            <span class="c-arr">→</span>
          </a>
          <a href="GITHUB_URL_PH" target="_blank" class="c-item">
            <div class="c-ico">
              <svg viewBox="0 0 24 24"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
            </div>
            <div class="c-meta">
              <p class="c-lbl">GitHub</p>
              <p class="c-val">github.com/Shravan157</p>
            </div>
            <span class="c-arr">→</span>
          </a>
          <a href="tel:PHONE_PH" class="c-item">
            <div class="c-ico">
              <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 11.5a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.6 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91A16 16 0 0 0 14 15.82l1.27-.76a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            </div>
            <div class="c-meta">
              <p class="c-lbl">Phone</p>
              <p class="c-val">PHONE_PH</p>
            </div>
            <span class="c-arr">→</span>
          </a>
        </div>
      </div>
      <div>
        <div class="resume-blk">
          <p class="res-title">Download Resume</p>
          <p class="res-sub">Full breakdown of experience, projects, and technical skills — formatted for recruiters and engineering teams.</p>
          <a href="RESUME_URL_PH" target="_blank" class="btn btn-primary">Download PDF →</a>
          <div class="res-info">
            <p class="res-info-lbl">Quick Info</p>
            <div class="info-row"><span class="info-k">Location</span><span class="info-v">Mumbai, India</span></div>
            <div class="info-row"><span class="info-k">Availability</span><span class="info-v green">Open to opportunities</span></div>
            <div class="info-row"><span class="info-k">Grad. Year</span><span class="info-v">2027</span></div>
            <div class="info-row"><span class="info-k">Focus Areas</span><span class="info-v">Backend + AI/ML</span></div>
            <div class="info-row"><span class="info-k">Preferred Roles</span><span class="info-v">SDE · MLE · Full-Stack</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════ FOOTER ═══════ -->
<footer>
  <div class="foot-inner">
    <p class="foot-copy">© 2026 Shravan Parthe &mdash; Built with Streamlit &amp; a lot of CSS.</p>
    <div class="foot-links">
      <a href="GITHUB_URL_PH" target="_blank">GitHub</a>
      <a href="mailto:EMAIL_PH">Email</a>
      <a href="RESUME_URL_PH" target="_blank">Resume</a>
    </div>
  </div>
</footer>

<script>
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
  }, { threshold: 0.08 });
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
</script>
</body>
</html>"""

# Inject variables cleanly — no f-string needed
HTML = (
    HTML
    .replace("RESUME_URL_PH", RESUME_URL)
    .replace("GITHUB_URL_PH", GITHUB_URL)
    .replace("EMAIL_PH",      EMAIL)
    .replace("PHONE_PH",      PHONE)
)

components.html(HTML, height=5600, scrolling=True)
