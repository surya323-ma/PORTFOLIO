import streamlit as st
import base64
import os

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="𝓢𝓾𝓻𝔂𝓪 𝓞𝓶𝓪𝓻 | AI & ML Engineer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Outfit:wght@300;400;500;700;900&display=swap');

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}

html,body,[data-testid="stAppViewContainer"]{
    background:#050b14 !important;
    color:#e8f4ff !important;
    font-family:'Outfit',sans-serif !important;
}
[data-testid="stAppViewContainer"]::before{
    content:'';position:fixed;inset:0;z-index:0;
    background-image:
        linear-gradient(rgba(0,210,255,0.04) 1px,transparent 1px),
        linear-gradient(90deg,rgba(0,210,255,0.04) 1px,transparent 1px);
    background-size:40px 40px;pointer-events:none;
}
#MainMenu,footer,header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebarNav"],
.stDeployButton{display:none !important;}
[data-testid="stAppViewContainer"]>div{position:relative;z-index:1;}
[data-testid="block-container"]{
    max-width: 100% !important;
    padding: 0 40px 60px !important;
    margin: 0 auto !important;
}
[data-testid="stSidebar"]{
    background:#0a1628 !important;
    border-right:1px solid rgba(0,210,255,0.15) !important;
}
::-webkit-scrollbar{width:6px;}
::-webkit-scrollbar-track{background:#050b14;}
::-webkit-scrollbar-thumb{background:rgba(0,210,255,0.3);border-radius:3px;}

.stButton>button{
    background:transparent !important;
    border:1px solid rgba(0,210,255,0.4) !important;
    color:#00d2ff !important;
    font-family:'Space Mono',monospace !important;
    font-size:11px !important;letter-spacing:2px !important;
    padding:8px 20px !important;border-radius:6px !important;
    transition:all 0.2s !important;
}
.stButton>button:hover{background:rgba(0,210,255,0.1) !important;}

.stRadio>div{display:flex;gap:4px;flex-direction:row !important;}
.stRadio>div>label{
    background:transparent !important;
    border:1px solid rgba(0,210,255,0.2) !important;
    color:#7a9bb5 !important;
    font-family:'Space Mono',monospace !important;
    font-size:10px !important;letter-spacing:1.2px !important;
    padding:7px 12px !important;border-radius:5px !important;
    cursor:pointer !important;transition:all 0.2s !important;
}
.stRadio>div>label:has(input:checked){
    border-color:#00d2ff !important;color:#00d2ff !important;
    background:rgba(0,210,255,0.08) !important;
}

[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea{
    background:#0f1f38 !important;
    border:1px solid rgba(0,210,255,0.2) !important;
    color:#e8f4ff !important;border-radius:7px !important;
    font-family:'Outfit',sans-serif !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus{
    border-color:#00d2ff !important;
    box-shadow:0 0 0 1px rgba(0,210,255,0.2) !important;
}
label[data-testid="stWidgetLabel"] p{
    color:#7a9bb5 !important;
    font-family:'Space Mono',monospace !important;
    font-size:11px !important;letter-spacing:1.5px !important;
}
hr{border-color:rgba(0,210,255,0.15) !important;margin:0 !important;}

[data-testid="stExpander"]{
    background:#0a1628 !important;
    border:1px solid rgba(0,210,255,0.2) !important;
    border-radius:10px !important;
}
[data-testid="stExpander"] summary{
    color:#7a9bb5 !important;
    font-family:'Space Mono',monospace !important;
    font-size:11px !important;
}

@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.3}}
@keyframes orbit{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
</style>
""", unsafe_allow_html=True)

# ─── LOAD PROFILE PHOTO FROM FILE ─────────────────────────────────────────────
@st.cache_data
def load_profile_photo():
    photo_path = "my_photo.jpg"
    if os.path.exists(photo_path):
        with open(photo_path, "rb") as f:
            raw = f.read()
        b64 = base64.b64encode(raw).decode()
        ext = photo_path.rsplit(".", 1)[-1].lower()
        mime = "image/jpeg" if ext in ("jpg", "jpeg") else "image/png"
        return b64, mime
    return None, None

profile_img_b64, profile_img_mime = load_profile_photo()

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def sec_hdr(title):
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:12px;margin:32px 0 20px;">
      <span style="font-family:'Space Mono',monospace;font-size:11px;
                   letter-spacing:3px;color:#7a9bb5;white-space:nowrap;">{title}</span>
      <div style="flex:1;height:1px;background:rgba(0,210,255,0.15);"></div>
    </div>""", unsafe_allow_html=True)

def tag_html(text, color="#00d2ff", bg="rgba(0,210,255,0.08)", border="rgba(0,210,255,0.2)"):
    return (f'<span style="font-size:10px;padding:3px 10px;border-radius:4px;'
            f'background:{bg};color:{color};border:1px solid {border};'
            f'font-family:\'Space Mono\',monospace;margin:3px 3px 0 0;">{text}</span>')

# ─── NAV BAR ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="display:flex;align-items:center;justify-content:space-between;
            padding:18px 0;border-bottom:1px solid rgba(0,210,255,0.15);
            margin-bottom:0;">
  <span style="font-family:'Space Mono',monospace;font-size:13px;
               color:#00d2ff;letter-spacing:2px;">
    𝓢𝓾𝓻𝔂𝓪 𝓞𝓶𝓪𝓻<span style="color:#ff3d7a;">.</span>
  </span>
  <span style="font-family:'Space Mono',monospace;font-size:10px;
               color:#7a9bb5;letter-spacing:2px;">
    AI &amp; ML ENGINEER
  </span>
</div>
""", unsafe_allow_html=True)
# ─── NAVIGATION ──────────────────────────────────────────────────────────────

col_nav, _ = st.columns([5, 1])
with col_nav:
    page = st.radio(
        "nav",
        ["HOME", "PROJECTS", "CERTIFICATES", "SKILLS", "DEPLOY LINKS", "CONTACT"],
        horizontal=True, label_visibility="collapsed", key="main_nav"
    )

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════════════════════════════════════════
if page == "HOME":

    # HERO
    col_text, col_photo = st.columns([3, 1], gap="large")

    with col_text:
        st.markdown("""
        <div style="padding:36px 0 20px;">
          <div style="display:inline-flex;align-items:center;gap:8px;
                      background:rgba(0,210,255,0.08);
                      border:1px solid rgba(0,210,255,0.25);
                      padding:5px 16px;border-radius:100px;margin-bottom:22px;">
            <span style="width:7px;height:7px;border-radius:50%;background:#00ff9d;
                         display:inline-block;animation:pulse 2s infinite;"></span>
            <span style="font-family:'Space Mono',monospace;font-size:11px;
                         color:#00d2ff;letter-spacing:1.5px;">OPEN TO OPPORTUNITIES</span>
          </div>
          <div style="font-family:'Outfit',sans-serif;font-weight:900;
                      font-size:clamp(34px,5.5vw,56px);line-height:1.05;
                      letter-spacing:-1.5px;margin-bottom:10px;">
            <span style="color:#e8f4ff;">𝓢𝓾𝓻𝔂𝓪 𝓞𝓶𝓪𝓻</span><br>
            <span style="background:linear-gradient(90deg,#00d2ff,#7b2fff);
                         -webkit-background-clip:text;-webkit-text-fill-color:transparent;"></span>
          </div>
          <div style="font-family:'Space Mono',monospace;font-size:11px;
                      letter-spacing:1.5px;margin-bottom:16px;">
            <span style="color:#7a9bb5;">AI Engineer</span>
            <span style="color:#ff3d7a;margin:0 8px;">/</span>
            <span style="color:#7a9bb5;">ML Researcher</span>
            <span style="color:#ff3d7a;margin:0 8px;">/</span>
            <span style="color:#7a9bb5;">Data Scientist</span>
          </div>
          <div style="font-size:14px;color:#7a9bb5;line-height:1.8;max-width:900px;margin-bottom:26px;">
                Final-year B.Tech (AI & ML) student and aspiring Data Scientist with hands-on internship experience in machine learning, statistical analysis, and data analytics. Proficient in Python, SQL, and scikit-learn with demonstrated ability to build predictive models, automate data workflows, and communicate insights via Power BI and Streamlit dashboards. Knowledgeable in Generative AI concepts, Agentic AI frameworks, and Model Context Protocol (MCP). Experienced in translating complex datasets into actionable business decisions for cross-functional stakeholders. deep learning, data pipelines, and production ML. 
          </div>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <a href="https://www.linkedin.com/in/surya-omar-3538a527b" target="_blank"
               style="display:inline-flex;align-items:center;gap:6px;background:#00d2ff;
                      color:#050b14;font-weight:700;font-family:'Outfit',sans-serif;
                      font-size:12px;padding:9px 20px;border-radius:7px;text-decoration:none;">
              💼 LinkedIn ↗
            </a>
            <a href="https://github.com/surya323-ma" target="_blank"
               style="display:inline-flex;align-items:center;gap:6px;background:transparent;
                      color:#e8f4ff;border:1px solid rgba(0,210,255,0.3);
                      font-family:'Outfit',sans-serif;font-size:12px;
                      padding:9px 20px;border-radius:7px;text-decoration:none;">
              🐙 GitHub ↗
            </a>
            <a href="https://codolio.com/profile/surya323" target="_blank"
               style="display:inline-flex;align-items:center;gap:6px;background:transparent;
                      color:#a67dff;border:1px solid rgba(123,47,255,0.35);
                      font-family:'Outfit',sans-serif;font-size:12px;
                      padding:9px 20px;border-radius:7px;text-decoration:none;">
              🏆 Codolio ↗
            </a>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_photo:
        st.markdown("<div style='height:44px'></div>", unsafe_allow_html=True)
        if profile_img_b64:
            st.markdown(f"""
            <div style="display:flex;justify-content:center;flex-direction:column;align-items:center;">
              <div style="position:relative;display:inline-block;width:300px;height:300px;">
                <div style="position:absolute;inset:-8px;border-radius:50%;
                            border:2px solid transparent;
                            border-top-color:#00d2ff;border-right-color:#7b2fff;
                            animation:orbit 4s linear infinite;"></div>
                <img src="data:{profile_img_mime};base64,{profile_img_b64}"
                      style="width:300px;height:300px;border-radius:50%;
                            object-fit:cover;object-position: top;
                            box-shadow:0 0 40px rgba(0,210,255,0.5);display:block;" />
              </div>
              <div style="margin-top:14px;text-align:center;">
                <div style="font-family:'Space Mono',monospace;font-size:11px;
                            color:#00d2ff;letter-spacing:1px;">SURYA OMAR</div>
                <div style="font-size:11px;color:#7a9bb5;margin-top:4px;">AI &amp; ML ENGINEER</div>
              </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="display:flex;justify-content:center;flex-direction:column;align-items:center;">
              <div style="width:165px;height:165px;border-radius:50%;
                          background:linear-gradient(135deg,#0a1628,#0f1f38);
                          border:3px solid rgba(0,210,255,0.4);
                          display:flex;flex-direction:column;align-items:center;
                          justify-content:center;
                          box-shadow:0 0 30px rgba(0,210,255,0.12);">
                <span style="font-size:52px;">🧠</span>
                <span style="font-family:'Space Mono',monospace;font-size:8px;
                             color:#7a9bb5;margin-top:10px;letter-spacing:1px;">SURYA OMAR</span>
              </div>
              <div style="margin-top:14px;text-align:center;">
                <div style="font-family:'Space Mono',monospace;font-size:11px;
                            color:#00d2ff;letter-spacing:1px;">SURYA OMAR</div>
                <div style="font-size:11px;color:#7a9bb5;margin-top:4px;">AI &amp; ML ENGINEER</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    # STATS
    for col, val, lbl, color in zip(
        st.columns(4, gap="small"),
        ["30+","𝓑.𝓣𝓮𝓬𝓱","95%","2025"],
        ["𝓟𝓡𝓞𝓙𝓔𝓒𝓣𝓢","𝓓𝓔𝓖𝓡𝓔𝓔","𝓐𝓒𝓒𝓤𝓡𝓐𝓒𝓨","𝓑𝓐𝓣𝓒𝓗"],
        ["#00d2ff","#a67dff","#ff3d7a","#00ff9d"]
    ):
        with col:
            st.markdown(f"""
            <div style="background:#0a1628;border:1px solid rgba(0,210,255,0.15);
                        border-radius:10px;padding:20px 12px;text-align:center;margin:6px 0;">
              <div style="font-family:'Space Mono',monospace;font-size:22px;
                          font-weight:700;color:{color};">{val}</div>
              <div style="font-size:10px;color:#7a9bb5;letter-spacing:1.5px;
                          margin-top:5px;font-family:'Space Mono',monospace;">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    # EDUCATION
    sec_hdr("𝓔𝓓𝓤𝓒𝓐𝓣𝓘𝓞𝓝")
    st.markdown("""
    <div style="background:#0a1628;border:1px solid rgba(0,210,255,0.15);
                border-radius:12px;padding:22px;position:relative;overflow:hidden;">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;
                  background:linear-gradient(90deg,#00d2ff,#7b2fff);"></div>
      <div style="display:flex;align-items:flex-start;gap:16px;">
        <div style="width:50px;height:50px;border-radius:12px;flex-shrink:0;
                    background:linear-gradient(135deg,rgba(0,210,255,0.12),rgba(123,47,255,0.12));
                    border:1px solid rgba(0,210,255,0.2);
                    display:flex;align-items:center;justify-content:center;font-size:22px;">🎓</div>
        <div>
          <div style="font-size:16px;font-weight:700;color:#e8f4ff;">
            B.Tech — Artificial Intelligence &amp; Machine Learning
          </div>
          <div style="font-family:'Space Mono',monospace;font-size:11px;
                      color:#00d2ff;margin-top:4px;letter-spacing:1px;">
            ALLENHOUSE INSTITUTE OF TECHNOLOGY
          </div>
          <div style="font-size:12px;color:#7a9bb5;margin-top:4px;">
            Kanpur, Uttar Pradesh &nbsp;·&nbsp; 2021 – 2025
          </div>
          <div style="margin-top:10px;display:flex;gap:6px;flex-wrap:wrap;">
            <span style="font-size:10px;padding:3px 10px;border-radius:4px;background:rgba(0,210,255,0.08);color:#00d2ff;border:1px solid rgba(0,210,255,0.2);font-family:'Space Mono',monospace;">DEEP LEARNING</span>
            <span style="font-size:10px;padding:3px 10px;border-radius:4px;background:rgba(123,47,255,0.1);color:#a67dff;border:1px solid rgba(123,47,255,0.2);font-family:'Space Mono',monospace;">NEURAL NETWORKS</span>
            <span style="font-size:10px;padding:3px 10px;border-radius:4px;background:rgba(0,255,157,0.07);color:#00ff9d;border:1px solid rgba(0,255,157,0.2);font-family:'Space Mono',monospace;">DATA SCIENCE</span>
            <span style="font-size:10px;padding:3px 10px;border-radius:4px;background:rgba(255,61,122,0.08);color:#ff7aaa;border:1px solid rgba(255,61,122,0.2);font-family:'Space Mono',monospace;">NLP</span>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    sec_hdr("𝓐𝓑𝓞𝓤𝓣 𝓜𝓔")
    st.markdown("""
    <div style="background:#0a1628;border:1px solid rgba(0,210,255,0.15);
                border-radius:12px;padding:22px;">
      <p style="font-size:18px;color:#9ab8d0;line-height:1.8;margin-bottom:12px;">
        Hey! I'm <strong style="color:#e8f4ff;">Surya Omar</strong>, an AI & ML engineering student at Allenhouse Institute of Technology. I build intelligent systems using machine learning, data analytics, and modern AI tools.
Skilled in Python, SQL, and ML frameworks, I focus on developing scalable solutions, from predictive modeling to deploying real-world applications. I’m especially interested in Generative AI and LLM-based systems.</p>
      <p style="font-size:14px;color:#9ab8d0;line-height:1.8;">
        My expertise spans <span style="color:#00d2ff;">Large Language Models</span>, 
<span style="color:#a67dff;">Computer Vision</span>, 
<span style="color:#ff7aaa;">NLP</span>, and 
<span style="color:#00ff9d;">Data Analytics</span> — focused on building scalable and impactful AI solutions.
      </p>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PROJECTS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "PROJECTS":
    sec_hdr("FEATURED PROJECTS")

    projects = [
        {
            "type": "AI / OLLAMA", "type_color": "#00d2ff", "type_bg": "rgba(0,210,255,0.08)",
            "type_border": "rgba(0,210,255,0.2)", "gradient": "linear-gradient(90deg,#00d2ff,#7b2fff)",
            "title": "BotTrainer — Local LLM NLU Studio (Ollama)", "emoji": "🤖",
            "desc": "BotTrainer provides accurate, scalable, and user-friendly intent detection using LLMs, with support for voice input and performance evaluation.",
            "metrics": [("94%", "RELEVANCE"), ("180ms", "LATENCY"), ("RAG", "ARCH")],
            "tags": ["LangChain", "Ollama", "FAISS", "FastAPI"],
            "tag_color": "#00d2ff", "tag_bg": "rgba(0,210,255,0.08)", "tag_border": "rgba(0,210,255,0.2)",

        },
        {
            "type": "MACHINE LEARNING", "type_color": "#a67dff", "type_bg": "rgba(123,47,255,0.1)",
            "type_border": "rgba(123,47,255,0.2)", "gradient": "linear-gradient(90deg,#7b2fff,#ff3d7a)",
            "title": "CardioSense AI", "emoji": "🫀",
            "desc": "CardioSense AI is an advanced Machine Learning-powered web application that predicts cardiovascular disease risk based on patient clinical data.",
            "metrics": [("78%", "mAP"), ("30fps", "SPEED"), ("ANN", "MODEL")],
            "tags": ["ML","WEB APP"],
            "tag_color": "#a67dff", "tag_bg": "rgba(123,47,255,0.1)", "tag_border": "rgba(123,47,255,0.2)",
            "demo": "https://cardiosens.streamlit.app/",
        },
        {
            "type": "CYBERSECURITY  ", "type_color": "#00ff9d", "type_bg": "rgba(0,255,157,0.07)",
            "type_border": "rgba(0,255,157,0.2)", "gradient": "linear-gradient(90deg,#00ff9d,#00d2ff)",
            "title": "AI-Based Network Intrusion Detection System", "emoji": "📊",
            "desc": "This project demonstrates how to use Machine Learning (Random Forest) and Generative AI (Grok) to detect and explain network attacks (specifically DDoS).",
            "metrics": [("88%", "ACCURACY"), ("LSTM", "MODEL"), ("40+", "FEATURES")],
            "tags": ["ML", "GROK", "Streamlit", "NETWORK"],
            "tag_color": "#00ff9d", "tag_bg": "rgba(0,255,157,0.07)", "tag_border": "rgba(0,255,157,0.2)",
            "demo": "https://network-intrusion-detection-system0.streamlit.app/",
        },
        {
            "type": "Data analytics", "type_color": "#ff7aaa", "type_bg": "rgba(255,61,122,0.08)",
            "type_border": "rgba(255,61,122,0.2)", "gradient": "linear-gradient(90deg,#ff3d7a,#ffb800)",
            "title": "EV-Vehicle-Charging-Demand-Prediction", "emoji": "🚗",
            "desc": "This forecasting model helps urban planners anticipate infrastructure needs, particularly for EV charging stations, supporting sustainability goals and enhancing user experience.",
            "metrics": [("91%", "F1 SCORE"), ("3", "LANGUAGES"), ("Forecast", "MODEL")],
            "tags": ["Forecast EV",  "Visualize" ],
            "tag_color": "#ff7aaa", "tag_bg": "rgba(255,61,122,0.08)", "tag_border": "rgba(255,61,122,0.2)",
            "demo":  "https://evadoption.streamlit.app/",
        },
        {
            "type": "Data analytics", "type_color": "#ff7aaa", "type_bg": "rgba(255,61,122,0.08)",
            "type_border": "rgba(255,61,122,0.2)", "gradient": "linear-gradient(90deg,#ff3d7a,#ffb800)",
            "title": "StockSense", "emoji": "🚗",
            "desc": "Real-time NSE/BSE stock analysis with Deep Learning predictions, technical indicators, and Buy/Hold/Sell signals.",
            "metrics": [("91%", "F1 SCORE"),  ("Lstm", "MODEL")],
            "tags": ["Yfinance","Flask"],
            "tag_color": "#ff7aaa", "tag_bg": "rgba(255,61,122,0.08)", "tag_border": "rgba(255,61,122,0.2)",
            "demo":  "https://stocksense ∙ main ∙ streamlit_app.py/",
        },
        {
            "type": "MACHINE LEARNING", "type_color": "#a67dff", "type_bg": "rgba(123,47,255,0.1)",
            "type_border": "rgba(123,47,255,0.2)", "gradient": "linear-gradient(90deg,#7b2fff,#ff3d7a)",
            "title": "MovieMind – AI-Driven Movie Discovery Platform", "emoji": "🎞️",
            "desc": "MovieMind – AI Driven Movie Discovery Platform is an intelligent movie recommendation system designed to help users discover movies based on their interests. The system uses content-based filtering techniques such as TF-IDF text similarity and genre-based recommendations to provide accurate and personalized movie suggestions.",
            "metrics": [("78%", "mAP"), ("30fps", "SPEED"), ("ANN", "MODEL")],
            "tags": ["ML","WEB APP"],
            "tag_color": "#a67dff", "tag_bg": "rgba(123,47,255,0.1)", "tag_border": "rgba(123,47,255,0.2)",
            "demo": "https://moviemind0.streamlit.app/",
        },

    ]

    for i in range(0, len(projects), 2):
        cols = st.columns(2, gap="medium")
        for j, col in enumerate(cols):
            if i+j < len(projects):
                p = projects[i+j]
                tags_html = "".join([
                    f'<span style="font-size:10px;padding:3px 9px;border-radius:4px;'
                    f'background:{p["tag_bg"]};color:{p["tag_color"]};'
                    f'border:1px solid {p["tag_border"]};'
                    f'font-family:\'Space Mono\',monospace;">{t}</span>'
                    for t in p["tags"]
                ])
                metrics_html = "".join([
                    f'<div style="text-align:center;">'
                    f'<div style="font-family:\'Space Mono\',monospace;font-size:15px;'
                    f'font-weight:700;color:{p["type_color"]};">{mv}</div>'
                    f'<div style="font-size:9px;color:#7a9bb5;letter-spacing:1px;">{ml}</div>'
                    f'</div>'
                    for mv, ml in p["metrics"]
                ])
                with col:
                    st.markdown(f"""
                    <div style="background:#0a1628;border:1px solid rgba(0,210,255,0.15);
                                border-radius:12px;padding:20px;margin-bottom:16px;
                                position:relative;overflow:hidden;height:100%;">
                      <div style="position:absolute;top:0;left:0;right:0;height:2px;
                                  background:{p['gradient']};"></div>
                      <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
                        <span style="font-size:22px;">{p['emoji']}</span>
                        <span style="font-size:10px;padding:3px 10px;border-radius:4px;
                                     background:{p['type_bg']};color:{p['type_color']};
                                     border:1px solid {p['type_border']};
                                     font-family:'Space Mono',monospace;letter-spacing:1px;">
                          {p['type']}
                        </span>
                      </div>
                      <div style="font-size:17px;font-weight:700;color:#e8f4ff;margin-bottom:10px;">
                        {p['title']}
                      </div>
                      <div style="font-size:13px;color:#7a9bb5;line-height:1.65;margin-bottom:16px;">
                        {p['desc']}
                      </div>
                      <div style="display:flex;justify-content:space-around;
                                  background:#0f1f38;border-radius:8px;
                                  padding:12px;margin-bottom:14px;">
                        {metrics_html}
                      </div>
                      <div style="display:flex;flex-wrap:wrap;gap:6px;">
                        {tags_html}
                      </div>
                      {"<a href='" + p['demo'] + "' target='_blank' style='display:inline-block;margin-top:12px;padding:8px 18px;border-radius:6px;border:1px solid #00d2ff;color:#00d2ff;text-decoration:none;font-size:12px;letter-spacing:1px;'>🚀 Live Demo</a>" if "demo" in p else ""}
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)



# ═══════════════════════════════════════════════════════════════════════════════
# CERTIFICATES
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "CERTIFICATES":
    sec_hdr("𝒞𝐸𝑅𝒯𝐼𝐹𝐼𝒞𝒜𝒯𝐼𝒪𝒩𝒮 & 𝒜𝒞𝐻𝐼𝐸𝒱𝐸𝑀𝐸𝒩𝒯𝒮")
    st.markdown("""
                <p style="font-size:20px;color:#7a9bb5;line-height:1.7;margin-bottom:24px;max-width:600px;font-weight:700;">
                        𝓥𝓮𝓻𝓲𝓯𝓲𝓮𝓭 𝓬𝓻𝓮𝓭𝓮𝓷𝓽𝓲𝓪𝓵𝓼 𝓯𝓻𝓸𝓶 𝓽𝓸𝓹 𝓹𝓵𝓪𝓽𝓯𝓸𝓻𝓶𝓼 𝓲𝓷 𝓐𝓘, 𝓜𝓛 &amp; 𝓓𝓪𝓽𝓪 𝓢𝓬𝓲𝓮𝓷𝓬𝓮.
                    </p>
                      """, unsafe_allow_html=True)


    certs = [
        {"org": "NPTEL / IIT MADRAS","color": "#ff7aaa","bg": "rgba(255,61,122,0.08)","bdr": "rgba(255,61,122,0.2)",
        "grad": "linear-gradient(90deg,#ff3d7a,#a67dff)","icon": "🐍","badge": "DATA SCIENCE","year": "2025",
        "title": "Python for Data Science",
        "desc": "Completed NPTEL course covering Python fundamentals, data analysis, and real-world data science workflows with assignments and proctored exam."},
        {"org": "DELOITTE","color":"#ffb800","bg":"rgba(255,184,0,0.08)","bdr":"rgba(255,184,0,0.2)",
         "grad":"linear-gradient(90deg,#ffb800,#ff3d7a)","icon":"📊","badge":"ANALYTICS","year":"2025",
         "title":"Data Analytics Job Simulation",
         "desc": "Completed Deloitte’s virtual job simulation involving real-world tasks in data analysis and forensic technology, gaining hands-on experience in business insights and problem solving."},
        {"org":"MetaEdSchool /Aws User group Kanpur","color":"#00d2ff","bg":"rgba(0,210,255,0.08)","bdr":"rgba(0,210,255,0.2)",
         "grad":"linear-gradient(90deg,#00d2ff,#0080ff)","icon":"🔷","badge":"VERIFIED","year":"2025",
         "title":"Chat Code Create  CERTIFICATE",
         "desc":"By MetaEdSchool in collaboration with 'Aws User group Kanpur' and 'Jagran Institute of Management'"},
        {"org":" GeeksforGeeks","color":"#a67dff","bg":"rgba(123,47,255,0.1)","bdr":"rgba(123,47,255,0.2)",
         "grad":"linear-gradient(90deg,#7b2fff,#ff3d7a)","icon":"🧠","badge":"22-week course","year":"2025",
         "title":"GfG 160 - 160 Days of Problem Solving",
         "desc":"160 Days of Problem Solving (DSA): 22-week structured program with workshops — GeeksforGeeks."},
         {"org": "ALLENHOUSE / RCPL","color": "#7b2fff","bg": "rgba(123,47,255,0.08)","bdr": "rgba(123,47,255,0.2)","grad": "linear-gradient(90deg,#7b2fff,#00d2ff)","icon": "💻",
    "badge": "FULL STACK",
    "year": "2025",
    "title": "Web Application Development (MERN Stack)",
    "desc": "Completed value-added course on MERN stack covering MongoDB, Express, React, and Node.js for full-stack web development."
},
        {"org":"IBM / COURSERA","color":"#00ff9d","bg":"rgba(0,255,157,0.07)","bdr":"rgba(0,255,157,0.2)",
         "grad":"linear-gradient(90deg,#00ff9d,#00d2ff)","icon":"📊","badge":"IBM","year":"2023",
         "title":"Machine Learning with Python",
         "desc":"Hands-on ML with Scikit-learn: supervised, unsupervised learning, regression, classification."},
        {"org": "CODECHEF","color": "#b37a2a","bg": "rgba(179,122,42,0.08)","bdr": "rgba(179,122,42,0.25)","grad": "linear-gradient(90deg,#b37a2a,#ffb347)",
        "icon": "👨‍🍳","badge": "SQL","year": "2025",
"title": "SQL Practice Queries",
"desc": "Completed all SQL practice problems on CodeChef, strengthening query writing, data retrieval, and database problem-solving skills."},
{"org": "AKTU / GUVI / HCL","color": "#00c853","bg": "rgba(0,200,83,0.08)","bdr": "rgba(0,200,83,0.2)","grad": "linear-gradient(90deg,#00c853,#00d2ff)","icon": "🤖",
    "badge": "AI EVENT","year": "2025","title": "AI Tech Confluence 2025",
"desc": "Participated in AKTU AI Tech Confluence powered by GUVI & HCL, gaining exposure to industry trends, AI applications, and emerging technologies."
},
{"org": "IIT KANPUR / EDUFABRICA","color": "#0077b6","bg": "rgba(0,119,182,0.08)","bdr": "rgba(0,119,182,0.2)","grad": "linear-gradient(90deg,#0077b6,#00b4d8)","icon": "🎯",
    "badge": "WORKSHOP","year": "2024","title": "AI & ML with Data Science",
"desc": "Completed 2-day workshop on AI, Machine Learning, and Data Science at IIT Kanpur, covering practical applications and industry use cases."
},
{"org": "IBM SKILLSBUILD","color": "#0f62fe","bg": "rgba(15,98,254,0.08)","bdr": "rgba(15,98,254,0.2)","grad": "linear-gradient(90deg,#0f62fe,#42a5f5)","icon": "🌐",
    "badge": "WEB DEV","year": "2025","title": "Web Development Fundamentals",
"desc": "Learned core web development concepts including HTML, CSS, and fundamentals of building responsive web applications."
},
{"org": "SOFTPRO INDIA / AKTU","color": "#ff6f00","bg": "rgba(255,111,0,0.08)","bdr": "rgba(255,111,0,0.2)","grad": "linear-gradient(90deg,#ff6f00,#ff9800)",
  "icon": "🧠","badge": "ML","year": "2025",
  "title": "Machine Learning Workshop",
"desc": "Participated in machine learning workshop organized by Softpro India, covering ML concepts and practical implementation."
},
{"org": "HACKERRANK","color": "#00ff9d","bg": "rgba(0,255,157,0.07)","bdr": "rgba(0,255,157,0.2)","grad": "linear-gradient(90deg,#00ff9d,#00d2ff)",
    "icon": "🧠","badge": "ADVANCED","year": "2025",
    "title": "SQL (Advanced)",
"desc": "Cleared HackerRank SQL (Advanced) certification demonstrating strong skills in complex queries, joins, and database problem solving."
},
{"org": "OPEN SOURCE CONNECT INDIA","color": "#ff8c00","bg": "rgba(255,140,0,0.08)","bdr": "rgba(255,140,0,0.2)","grad": "linear-gradient(90deg,#ff8c00,#00ff9d)",
    "icon": "🌍","badge": "CONTRIBUTOR","year": "2025",
    "title": "Open Source Connect India 2025", "desc": "Contributed to open-source projects during OSCI 2025, collaborating on real-world development and strengthening community-driven software skills."
},
{"org": "HACKERRANK","color": "#00ff9d","bg": "rgba(0,255,157,0.07)","bdr": "rgba(0,255,157,0.2)","grad": "linear-gradient(90deg,#00ff9d,#00d2ff)","icon": "⚡",
    "badge": "INTERMEDIATE","year": "2025",
"title": "Node.js (Intermediate)",
    "desc": "Validated backend development skills including Node.js fundamentals, APIs, and asynchronous programming through HackerRank certification."
}
    ]

    for i in range(0, len(certs), 2):
        cols = st.columns(2, gap="medium")
        for j, col in enumerate(cols):
            if i+j < len(certs):
                c = certs[i+j]
                with col:
                    st.markdown(f"""
                    <div style="background:#0a1628;border:1px solid {c['bdr']};
                                border-radius:12px;padding:20px;margin-bottom:14px;
                                position:relative;overflow:hidden;">
                      <div style="position:absolute;top:0;left:0;right:0;height:2px;background:{c['grad']};"></div>
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
                        <div style="display:flex;align-items:center;gap:12px;">
                          <span style="font-size:26px;">{c['icon']}</span>
                          <div>
                            <div style="font-family:'Space Mono',monospace;font-size:9px;
                                        color:{c['color']};letter-spacing:1.5px;">{c['org']}</div>
                            <div style="font-size:14px;font-weight:700;color:#e8f4ff;margin-top:3px;">
                              {c['title']}
                            </div>
                          </div>
                        </div>
                        <div style="display:flex;flex-direction:column;align-items:flex-end;gap:5px;">
                          <span style="font-size:9px;padding:2px 8px;border-radius:4px;
                                       background:{c['bg']};color:{c['color']};
                                       border:1px solid {c['bdr']};
                                       font-family:'Space Mono',monospace;">{c['badge']}</span>
                          <span style="font-family:'Space Mono',monospace;font-size:9px;color:#7a9bb5;">{c['year']}</span>
                        </div>
                      </div>
                      <div style="font-size:12px;color:#7a9bb5;line-height:1.65;">{c['desc']}</div>
                    </div>
                    """, unsafe_allow_html=True)

    sec_hdr("ACHIEVEMENT HIGHLIGHTS")
    for col, (ico, t, s, c) in zip(
        st.columns(4, gap="small"),
        [("🥇","NPTEL","Python for Data Science -- IIT Madras ","#ff7aaa"),
         ("⚡","HackerRank 5★","Python ,Java ,Node. js ,SQL (Advanced) & Problem Solving (Advanced) ","#00ff9d"),
         ("🏆","Codolio","Competitive coding","#00d2ff"),
         ("📜","10+ Certs","IBM, Deloitte, CodeChef, GUVI","#a67dff")
         ]
    ):
        with col:
            st.markdown(f"""
            <div style="background:#0a1628;border:1px solid rgba(0,210,255,0.12);
                        border-radius:10px;padding:16px 12px;text-align:center;">
              <div style="font-size:26px;margin-bottom:8px;">{ico}</div>
              <div style="font-size:12px;font-weight:600;color:#e8f4ff;margin-bottom:4px;">{t}</div>
              <div style="font-size:11px;color:#7a9bb5;">{s}</div>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# SKILLS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "SKILLS":
    sec_hdr("𝓣𝓔𝓒𝓗𝓝𝓘𝓒𝓐𝓛 𝓢𝓚𝓘𝓛𝓛s")
    skill_cats = [
        ("🤖","AI / LLMs",["GPT-4","LLaMA","LangChain","RAG","LoRA","Prompt Eng"],"#00d2ff","rgba(0,210,255,0.08)","rgba(0,210,255,0.2)"),
        ("🧮","Machine Learning",["PyTorch","TensorFlow","Sklearn","XGBoost","CNN","LSTM"],"#a67dff","rgba(123,47,255,0.1)","rgba(123,47,255,0.2)"),
        ("👁️","Computer Vision",["YOLOv8","OpenCV","SAM","ViT","Diffusion"],"#ff7aaa","rgba(255,61,122,0.08)","rgba(255,61,122,0.2)"),
        ("💬","NLP",["BERT","Transformers","spaCy","HuggingFace","NLTK"],"#00ff9d","rgba(0,255,157,0.07)","rgba(0,255,157,0.2)"),
        ("📊","Data Science",["Pandas","NumPy","Matplotlib","Plotly","Seaborn"],"#ffb800","rgba(255,184,0,0.08)","rgba(255,184,0,0.2)"),
        ("🌐","Computer Networks",["OSI Model","TCP/IP","HTTP/HTTPS","DNS","Routing","Network Security"],"#00bcd4","rgba(0,188,212,0.08)","rgba(0,188,212,0.2)"),
        ("☁️","MLOps & Cloud",["Docker","FastAPI","MLflow","AWS","Streamlit","Airflow"],"#00d2ff","rgba(0,210,255,0.08)","rgba(0,210,255,0.2)"),
        ("🗄️","Databases",["MySQL","PostgreSQL","MongoDB","SQL","NoSQL","Firebase"],"#ffb800","rgba(255,184,0,0.08)","rgba(255,184,0,0.2)"),
        ("☕","Java Development",["Core Java","OOPs","Collections","JDBC","Exception Handling","DSA in Java"],"#ff7aaa","rgba(255,122,170,0.08)","rgba(255,122,170,0.2)"),
        ("⚛️","MERN Stack",["MongoDB","Express.js","React.js","Node.js","REST APIs","JWT Auth"],"#00ff9d","rgba(0,255,157,0.08)","rgba(0,255,157,0.2)")
    ]
    for i in range(0, len(skill_cats), 3):
        cols = st.columns(3, gap="medium")
        for j, col in enumerate(cols):
            if i+j < len(skill_cats):
                ico,name,tags,tc,tbg,tb = skill_cats[i+j]
                tags_h = "".join([tag_html(t,tc,tbg,tb) for t in tags])
                with col:
                    st.markdown(f"""
                    <div style="background:#0a1628;border:1px solid rgba(0,210,255,0.15);
                                border-radius:10px;padding:16px;margin-bottom:12px;">
                      <div style="display:flex;align-items:center;gap:8px;margin-bottom:12px;">
                        <span style="font-size:18px;">{ico}</span>
                        <span style="font-size:13px;font-weight:600;color:#e8f4ff;">{name}</span>
                      </div>
                      <div style="display:flex;flex-wrap:wrap;">{tags_h}</div>
                    </div>
                    """, unsafe_allow_html=True)
        st.markdown("<div style='height:2px'></div>", unsafe_allow_html=True)

    sec_hdr("PROFICIENCY")
    for skill, pct, color in [
        ("Python",95,"#00d2ff"),("Machine Learning",88,"#a67dff"),
        ("Deep Learning / PyTorch",85,"#ff7aaa"),("NLP / Transformers",80,"#00ff9d"),
        ("Data Analysis",90,"#ffb800"),("MLOps / Deployment",75,"#00d2ff"),("MERN Stack Development", 70, "#00ff9d"),
    ("Java & OOPs", 50, "#ff7aaa"),("Databases (SQL + NoSQL)", 78, "#ffb800")
    ]:
        st.markdown(f"""
        <div style="margin-bottom:14px;">
          <div style="display:flex;justify-content:space-between;margin-bottom:5px;">
            <span style="font-size:13px;color:#e8f4ff;">{skill}</span>
            <span style="font-family:'Space Mono',monospace;font-size:11px;color:{color};">{pct}%</span>
          </div>
          <div style="background:#0f1f38;border-radius:100px;height:5px;border:1px solid rgba(0,210,255,0.1);">
            <div style="width:{pct}%;height:100%;border-radius:100px;
                        background:linear-gradient(90deg,{color}44,{color});"></div>
          </div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# DEPLOY LINKS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "DEPLOY LINKS":
    sec_hdr("𝓛𝓘𝓥𝓔 𝓟𝓡𝓞𝓕𝓘𝓛𝓔𝓢 & 𝓓𝓔𝓟𝓛𝓞𝓨𝓜𝓔𝓝𝓣𝓢")

    st.markdown("""
    <p style="font-size:14px;color:#7a9bb5;line-height:1.7;margin-bottom:24px;max-width:600px;">
      𝓐𝓵𝓵 𝓵𝓲𝓿𝓮 𝓭𝓮𝓹𝓵𝓸𝔂𝓮𝓭 𝓪𝓹𝓹𝓼, 𝓬𝓸𝓭𝓲𝓷𝓰 𝓹𝓻𝓸𝓯𝓲𝓵𝓮𝓼, 𝓪𝓷𝓭 𝓹𝓸𝓻𝓽𝓯𝓸𝓵𝓲𝓸 𝓵𝓲𝓷𝓴𝓼 — 𝓭𝓲𝓻𝓮𝓬𝓽𝓵𝔂 𝓪𝓬𝓬𝓮𝓼𝓼𝓲𝓫𝓵𝓮 𝓱𝓮𝓻𝓮.
    </p>
    """, unsafe_allow_html=True)

    sec_hdr("𝓟𝓞𝓡𝓣𝓕𝓞𝓛𝓘𝓞 𝓟𝓡𝓞𝓕𝓘𝓛𝓔𝓢")

    profiles = [
        {"icon":"💼","platform":"LINKEDIN","label":"Professional Network",
         "url":"https://www.linkedin.com/in/surya-omar-3538a527b","handle":"surya-omar-3538a527b",
         "color":"#00d2ff","bg":"rgba(0,210,255,0.08)","bdr":"rgba(0,210,255,0.2)",
         "grad":"linear-gradient(90deg,#00d2ff,#0080ff)",
         "desc":"Professional experience, skills endorsements & recommendations."},
        {"icon":"🐙","platform":"GITHUB","label":"Source Code & Repos",
         "url":"https://github.com/surya323-ma","handle":"surya323-ma",
         "color":"#a67dff","bg":"rgba(123,47,255,0.1)","bdr":"rgba(123,47,255,0.2)",
         "grad":"linear-gradient(90deg,#7b2fff,#ff3d7a)",
         "desc":"All project repositories, contributions & open-source work."},
        {"icon":"🏆","platform":"CODOLIO","label":"Competitive Coding",
         "url":"https://codolio.com/profile/surya323","handle":"surya323",
         "color":"#00ff9d","bg":"rgba(0,255,157,0.07)","bdr":"rgba(0,255,157,0.2)",
         "grad":"linear-gradient(90deg,#00ff9d,#00d2ff)",
         "desc":"DSA stats, problem-solving & competitive programming profile."},
         {"icon":"⭐","platform":"HACKERRANK","label":"Coding Practice","url":"https://www.hackerrank.com/profile/suryaomar323","handle":"suryaomar323",
    "color":"#00ff9d", "bg":"rgba(0,255,157,0.07)", "bdr":"rgba(0,255,157,0.2)",
    "grad":"linear-gradient(90deg,#00ff9d,#00d2ff)",
    "desc":"Solved problems in Python, SQL & problem solving. Earned certifications and badges in coding challenges."
},
{"icon":"🧩","platform":"LEETCODE","label":"DSA Practice","url":"https://leetcode.com/u/Surya323/","handle":"Surya323","color":"#ffa116","bg":"rgba(255,161,22,0.08)",
  "bdr":"rgba(255,161,22,0.2)","grad":"linear-gradient(90deg,#ffa116,#ff7a00)",
    "desc":"Solved DSA problems covering arrays, strings, trees & dynamic programming for interview preparation."
}
    ]

    for p in profiles:
        st.markdown(f"""
        <div style="background:#0a1628;border:1px solid {p['bdr']};
                    border-radius:12px;padding:18px 20px;margin-bottom:12px;
                    position:relative;overflow:hidden;">
          <div style="position:absolute;top:0;left:0;right:0;height:2px;background:{p['grad']};"></div>
          <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;">
            <div style="display:flex;align-items:center;gap:14px;">
              <div style="width:48px;height:48px;border-radius:10px;flex-shrink:0;
                          background:{p['bg']};border:1px solid {p['bdr']};
                          display:flex;align-items:center;justify-content:center;font-size:22px;">
                {p['icon']}
              </div>
              <div>
                <div style="font-family:'Space Mono',monospace;font-size:9px;
                            color:{p['color']};letter-spacing:1.5px;">{p['platform']}</div>
                <div style="font-size:15px;font-weight:700;color:#e8f4ff;margin-top:2px;">{p['label']}</div>
                <div style="font-size:11px;color:#7a9bb5;margin-top:2px;">@{p['handle']}</div>
              </div>
            </div>
            <div style="display:flex;flex-direction:column;align-items:flex-end;gap:6px;">
              <a href="{p['url']}" target="_blank"
                 style="display:inline-flex;align-items:center;gap:5px;
                        background:{p['bg']};color:{p['color']};
                        border:1px solid {p['bdr']};
                        font-family:'Space Mono',monospace;font-size:10px;letter-spacing:1px;
                        padding:7px 16px;border-radius:6px;text-decoration:none;">
                VISIT ↗
              </a>
              <div style="font-size:11px;color:#7a9bb5;text-align:right;max-width:200px;">
                {p['desc']}
              </div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    sec_hdr("𝓓𝓔𝓟𝓛𝓞𝓨𝓔𝓓 𝓟𝓡𝓞𝓙𝓔𝓒𝓣𝓢")

    
    deployed = [
    {
        "name":"NeuroRoute AI",
        "type":"STREAMLIT CLOUD",
        "emoji":"🧠",
        "desc":"AI-powered intelligent routing and decision system with smart predictions.",
        "url":"https://neuroroute-ai.streamlit.app/",
        "stack":["Streamlit","AI","ML"],
        "color":"#00d2ff","bg":"rgba(0,210,255,0.08)","bdr":"rgba(0,210,255,0.2)"
    },

    {
        "name":"Network Intrusion Detection",
        "type":"STREAMLIT CLOUD",
        "emoji":"🛡️",
        "desc":"ML-based intrusion detection system to identify cyber attacks like DDoS.",
        "url":"https://network-intrusion-detection-system0.streamlit.app/",
        "stack":["Machine Learning","Security","Streamlit"],
        "color":"#00ff9d","bg":"rgba(0,255,157,0.07)","bdr":"rgba(0,255,157,0.2)"
    },

    {
        "name":"CardioSense AI",
        "type":"STREAMLIT CLOUD",
        "emoji":"🫀",
        "desc":"AI system for predicting cardiovascular disease risk using patient data.",
        "url":"https://cardiosens.streamlit.app/",
        "stack":["ML","Healthcare","Streamlit"],
        "color":"#ff7aaa","bg":"rgba(255,61,122,0.08)","bdr":"rgba(255,61,122,0.2)"
    },

    {
        "name":"EV Adoption Analytics",
        "type":"STREAMLIT CLOUD",
        "emoji":"🚗",
        "desc":"Forecasting EV adoption trends and charging demand using data analytics.",
        "url":"https://evadoption.streamlit.app/",
        "stack":["Forecasting","Data Science","Streamlit"],
        "color":"#ffb800","bg":"rgba(255,184,0,0.08)","bdr":"rgba(255,184,0,0.2)"
    },

    {
        "name":"FashionIQ",
        "type":"STREAMLIT CLOUD",
        "emoji":"👗",
        "desc":"AI-based fashion recommendation system for personalized outfit suggestions.",
        "url":"https://fashioniq.streamlit.app/",
        "stack":["AI","Recommendation System","Streamlit"],
        "color":"#a67dff","bg":"rgba(123,47,255,0.08)","bdr":"rgba(123,47,255,0.2)"
    },

    {
        "name":"MovieMind AI",
        "type":"STREAMLIT CLOUD",
        "emoji":"🎬",
        "desc":"AI movie recommendation system using content-based filtering techniques.",
        "url":"https://moviemind0.streamlit.app/",
        "stack":["ML","Recommendation","Streamlit"],
        "color":"#00d2ff","bg":"rgba(0,210,255,0.08)","bdr":"rgba(0,210,255,0.2)"
    },

    {
        "name":"StockSense AI",
        "type":"STREAMLIT CLOUD",
        "emoji":"📈",
        "desc":"Stock market prediction system with technical indicators and ML insights.",
        "url":"https://appapppy-l7pp3qlk9gtlhrkpezut8v.streamlit.app/",
        "stack":["Finance","ML","Streamlit"],
        "color":"#00ff9d","bg":"rgba(0,255,157,0.07)","bdr":"rgba(0,255,157,0.2)"
    }


    ]

    cols = st.columns(2, gap="medium")
    for idx, d in enumerate(deployed):
        with cols[idx%2]:
            stk = "".join([tag_html(s, d["color"], d["bg"], d["bdr"]) for s in d["stack"]])
            st.markdown(f"""
            <div style="background:#0a1628;border:1px solid {d['bdr']};
                        border-radius:10px;padding:16px;margin-bottom:12px;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
                <div>
                  <div style="font-family:'Space Mono',monospace;font-size:9px;
                              color:{d['color']};letter-spacing:1.5px;margin-bottom:3px;">{d['type']}</div>
                  <div style="font-size:14px;font-weight:700;color:#e8f4ff;">{d['emoji']} {d['name']}</div>
                </div>
                <span style="font-size:9px;padding:3px 8px;border-radius:100px;
                             background:rgba(0,255,157,0.1);color:#00ff9d;
                             border:1px solid rgba(0,255,157,0.25);
                             font-family:'Space Mono',monospace;white-space:nowrap;">● LIVE</span>
              </div>
              <div style="font-size:12px;color:#7a9bb5;margin-bottom:10px;">{d['desc']}</div>
              <div style="display:flex;flex-wrap:wrap;margin-bottom:10px;">{stk}</div>
              <a href="{d['url']}" target="_blank"
                 style="color:{d['color']};text-decoration:none;
                        font-family:'Space Mono',monospace;font-size:10px;letter-spacing:1px;">
                VIEW LIVE ↗
              </a>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "CONTACT":
    sec_hdr("𝓖𝓔𝓣 𝓘𝓝 𝓣𝓞𝓤𝓒𝓗")
    st.markdown("""
    <p style="font-size:14px;color:#7a9bb5;line-height:1.75;max-width:540px;margin-bottom:26px;">
      𝓞𝓹𝓮𝓷 𝓽𝓸 𝓲𝓷𝓽𝓮𝓻𝓷𝓼𝓱𝓲𝓹𝓼, 𝓐𝓘/𝓜𝓛 𝓬𝓸𝓵𝓵𝓪𝓫𝓸𝓻𝓪𝓽𝓲𝓸𝓷𝓼, 𝓻𝓮𝓼𝓮𝓪𝓻𝓬𝓱 & 𝓮𝓷𝓰𝓲𝓷𝓮𝓮𝓻𝓲𝓷𝓰 𝓻𝓸𝓵𝓮𝓼. 𝓛𝓮𝓽'𝓼 𝓫𝓾𝓲𝓵𝓭 𝓼𝓸𝓶𝓮𝓽𝓱𝓲𝓷𝓰 𝓲𝓷𝓽𝓮𝓵𝓵𝓲𝓰𝓮𝓷𝓽 𝓽𝓸𝓰𝓮𝓽𝓱𝓮𝓻! 
    </p>""", unsafe_allow_html=True)

    contact_data = [
        ("💼","LINKEDIN","surya-omar-3538a527b","https://www.linkedin.com/in/surya-omar-3538a527b","#00d2ff"),
        ("🐙","GITHUB","surya323-ma","https://github.com/surya323-ma","#a67dff"),
        ("🏆","CODOLIO","surya323","https://codolio.com/profile/surya323","#00ff9d"),
        ("📞","PHONE","+91-9794667615","tel:+91XXXXXXXXXX","#00ff9d"),
        ("📧","EMAIL","suryaomar323@gmail.com","mailto:suryaomar323@gmail.com","#ff7aaa"),
        
        ("🎓","INSTITUTION","Allenhouse Institute of Technology","#","#ffb800"),
    ]
    cols = st.columns(2, gap="medium")
    for idx,(ico,lbl,val,url,color) in enumerate(contact_data):
        with cols[idx%2]:
            link = (f'<a href="{url}" target="_blank" style="color:{color};text-decoration:none;font-size:13px;font-weight:500;">{val} ↗</a>'
                    if url!="#" else f'<span style="color:#e8f4ff;font-size:13px;font-weight:500;">{val}</span>')
            st.markdown(f"""
            <div style="background:#0a1628;border:1px solid rgba(0,210,255,0.15);
                        border-radius:10px;padding:16px 18px;margin-bottom:10px;
                        display:flex;align-items:center;gap:12px;">
              <span style="font-size:22px;">{ico}</span>
              <div>
                <div style="font-family:'Space Mono',monospace;font-size:9px;
                            color:#7a9bb5;letter-spacing:1.5px;margin-bottom:4px;">{lbl}</div>
                {link}
              </div>
            </div>
            """, unsafe_allow_html=True)

    sec_hdr("𝓢𝓔𝓝𝓓 𝓐 𝓜𝓔𝓢𝓢𝓐𝓖𝓔")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        name_in = st.text_input("YOUR NAME", placeholder="Your name")
    with col2:
        email_in = st.text_input("YOUR EMAIL", placeholder="your@email.com")
    msg_in = st.text_area("MESSAGE", placeholder="Tell me about your project or opportunity...", height=120)
    col_btn, _ = st.columns([1,3])
    import urllib.parse

if st.button("SEND ↗"):
    if name_in and email_in and msg_in:

        # 📧 Gmail link
        subject = urllib.parse.quote(f"Portfolio Contact from {name_in}")
        body = urllib.parse.quote(f"Name: {name_in}\nEmail: {email_in}\n\nMessage:\n{msg_in}")

        gmail_url = f"mailto:Suryaomar323@gmail.com?subject={subject}&body={body}"

        # 💬 WhatsApp link
        whatsapp_url = f"https://wa.me/919794667615?text={body}"

        st.markdown(f"""
        <a href="{gmail_url}" target="_blank"
           style="display:inline-block;margin:10px 10px 0 0;
                  padding:10px 18px;border-radius:6px;
                  background:#ff7aaa;color:white;text-decoration:none;">
            📧 Send via Gmail
        </a>

        <a href="{whatsapp_url}" target="_blank"
           style="display:inline-block;margin-top:10px;
                  padding:10px 18px;border-radius:6px;
                  background:#25D366;color:white;text-decoration:none;">
            💬 Send via WhatsApp
        </a>
        """, unsafe_allow_html=True)

    else:
        st.warning("Please fill all fields.")

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
st.markdown("""
<div style="border-top:1px solid rgba(0,210,255,0.15);padding:24px 0;
            display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
  <span style="font-family:'Space Mono',monospace;font-size:11px;color:#7a9bb5;">
    © 2025 𝓢𝓾𝓻𝔂𝓪 𝓞𝓶𝓪𝓻 · AI &amp; ML ENGINEER
  </span>
  <span style="font-family:'Space Mono',monospace;font-size:11px;color:rgba(0,210,255,0.4);">
    BUILT WITH STREAMLIT · PYTHON
  </span>
</div>
""", unsafe_allow_html=True)
