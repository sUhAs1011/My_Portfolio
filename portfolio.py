import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import base64
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Suhas Venkata · Portfolio", page_icon="🌐", layout="wide")

# --- LOAD IMAGE ---
def load_and_base64_image(file_path):
    try:
        img = Image.open(file_path)
        buffered = BytesIO()
        img.save(buffered, format="PNG") # Use PNG for transparency if needed
        return base64.b64encode(buffered.getvalue()).decode()
    except FileNotFoundError:
        st.error(f"Error: {file_path} not found. Please ensure the image is in the correct directory.")
        return None # Return None if file is not found

img_b64 = load_and_base64_image("profile.jpg")

# --- CUSTOM STYLES ---
st.markdown("""
<style>
html {
    scroll-behavior: smooth;
}

body {
    background-color: #0e1117;
    color: white; /* Ensure text is visible on dark background */
}

.gradient-text {
    font-size: 48px;
    font-weight: 800;
    /* Corrected: use linear-gradient for standard syntax and -webkit- for webkit browsers */
    background: linear-gradient(90deg, #005BEA, #00C6FB);
    -webkit-background-clip: text;
    -webkit-text-fill-color: white; /* Makes text transparent so gradient background shows through */
    color: white; /* Fallback for browsers that don't support -webkit-text-fill-color */
    margin-bottom: 5px;
}

.gradient-text span {
    -webkit-text-fill-color: white; /* Span within gradient-text should also be transparent to inherit parent's gradient */
}

.subtitle {
    font-size: 20px;
    color: #ccc;
    margin-bottom: 25px;
}

.intro {
    font-size: 17px;
    line-height: 1.6;
    color: white;
    max-width: 550px;
}

.say-hello {
    border: 2px solid white;
    border-radius: 12px;
    padding: 10px 24px;
    background-color: transparent;
    color: white;
    font-size: 16px;
    margin-top: 25px;
    cursor: pointer;
    transition: 0.3s;
}

.say-hello:hover {
    background-color: white;
    color: black;
}

.profile-pic {
    border-radius: 50%;
    width: 300px;
    height: 300px;
    object-fit: cover;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
    transform: translateX(150px);
}

.hero-container {
    padding: 40px 20px 20px 40px;
}

/* Ensure content sections have padding to account for fixed navbar */
.content-section {
    padding-top: 80px; /* Adjust based on navbar height + desired spacing */
    margin-bottom: 40px; /* Add some space between sections */
}

/* Timeline styling (for .timeline-wrapper, .timeline-col, etc. - these are generic and might not be used directly in the final timeline HTML, but good to keep if you have other timeline styles) */
.timeline-wrapper {
    display: flex;
    justify-content: space-between;
    margin-top: 50px;
}

.timeline-col {
    width: 45%;
}

.timeline-block {
    border-left: 2px solid #555;
    margin-left: 20px;
    padding-left: 20px;
    position: relative;
    margin-bottom: 50px;
}

.timeline-block::before {
    content: '';
    position: absolute;
    top: 0;
    left: -8px;
    width: 12px;
    height: 12px;
    background-color: #00C6FB;
    border-radius: 50%;
}

.timeline-title {
    font-weight: 700;
    font-size: 18px;
    color: #1da1f2;
}

.timeline-subtitle {
    color: #aaa;
    font-size: 15px;
}

.timeline-date {
    font-size: 14px;
    color: #888;
    margin-top: 5px;
}

/* Simplified Navigation Bar Styling (navbar-custom) */
.navbar-custom {
    overflow: hidden;
    background-color: #0e1117; /* Match body background for seamless look */
    position: fixed;
    top: 40px;
    width: 100%;
    left: -1.25%;
    z-index: 1000;
    display: flex;
    justify-content: flex-end; /* Align items to the right */
    padding: 15px 40px; /* Adjust padding to match image more closely */
    box-sizing: border-box; /* Include padding in width */
    border-bottom: 1px solid #222; /* Subtle border for separation */
}

.navbar-custom a {
    color: #f2f2f2;
    text-align: center;
    padding: 8px 15px; /* Adjust padding for button size */
    text-decoration: none;
    font-size: 16px;
    transition: color 0.3s, background-color 0.3s;
    margin-left: 12px; /* Space between links */
}

.navbar-custom a:hover {
    color: #00C6FB; /* Highlight color on hover */
    background-color: transparent; /* Keep background transparent */
}

/* Timeline CSS (alternating vertical style) - actual implementation style */
.timeline-container {
    position: relative;
    max-width: 800px;
    margin: 40px auto;
}

.timeline-item {
    padding: 20px 40px;
    position: relative;
    background-color: inherit;
    width: 100%;
}

.timeline-item::after {
    content: "";
    position: absolute;
    width: 6px;
    background-color: #1f77b4;
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -3px;
}

.timeline-content {
    padding: 20px;
    background-color: #0e1117;
    position: relative;
    border-radius: 6px;
    width: 40%;
    color: white;
    box-shadow: 0 0 10px rgba(0, 198, 251, 0.2); /* Subtle glow from cyan */
}

.left {
    left: 0;
}

.right {
    left: 60%;
}

.timeline-content::before {
    content: " ";
    position: absolute;
    top: 20px;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background-color: #00C6FB;
    border: 4px solid white;
    z-index: 1;
}

.left::before {
    left: 95%;
}

.right::before {
    left: -15px;
}

@media screen and (max-width: 768px) {
    .timeline-content {
        width: 90%;
        left: 0 !important;
    }
    .timeline-item::after {
        left: 30px;
    }
    .timeline-content::before {
        left: 15px;
    }
}

/* --- Gradient Button CSS (No underline) --- */
.contact-button {
    display: inline-block;
    padding: 14px 26px;
    margin: 12px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none !important;
    color: white !important;
    background: linear-gradient(90deg, #6e00ff, #c800c8, #0008ff);
    border-radius: 16px;
    border: 2px solid rgba(255, 255, 255, 0.1);
    transition: 0.4s ease-in-out;
    box-shadow: 0 0 10px rgba(200, 0, 255, 0.3);
}
.contact-button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(200, 0, 255, 0.6);
    text-decoration: none !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* your .timeline-container, .timeline-item, .left/right CSS here */
</style>
""", unsafe_allow_html=True)


# --- NAVIGATION BAR ---
st.markdown("""
<div class="navbar-custom">
    <a href="#about">👨‍💼 About Me</a>
    <a href="#skills">🛠️ Skills</a>
    <a href="#experience">💼 Experience</a>
    <a href="#journey">🚶‍♂️ My Journey</a>
    <a href="#achievements">🏆 Achievements</a>
    <a href="#projects">🚀 Projects</a>
</div>
""", unsafe_allow_html=True)
# --- HERO SECTION ---
st.markdown("<div id='home' class='content-section'>", unsafe_allow_html=True)
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<div class='gradient-text'>Suhas Venkata <span>👋</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>CSE Student at PES University</div>", unsafe_allow_html=True)
    st.markdown("""
<p style='font-size:18px; line-height:1.6;'>
I'm a final-year Computer Science student at PES University, passionate about Machine Learning and Natural Language Processing. 
I recently interned in C3I, gaining ML exposure and hands-on experience. 
Exploring software engineering and always open to new challenges.
</p>
""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if img_b64: 
        st.markdown(f"<img src='data:image/png;base64,{img_b64}' class='profile-pic'/>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True) # End of Home section

# --- STYLE FOR CONTACT BUTTONS ---
# --- STYLE FOR CONTACT BUTTONS ---
st.markdown("""
<style>
.button-row {
  display: flex;
  justify-content: center;   /* Center align */
  gap: 16px;
  margin-top: 20px;
  flex-wrap: wrap;           /* Responsive wrap */
}

.contact-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 0;
  background: linear-gradient(90deg, #9333ea, #3b82f6); /* Purple → Blue gradient */
  border-radius: 8px;
  text-decoration: none;
  color: white;
  font-weight: 600;
  transition: transform 0.15s ease, box-shadow 0.2s ease;
  width: 160px;        /* Fixed equal width */
  height: 45px;        /* Consistent height */
  text-align: center;
}

.contact-button:hover {
  transform: translateY(-3px);
  box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

.contact-icon {
  width: 20px;
  height: 20px;
}
</style>
""", unsafe_allow_html=True)

import base64
buttons_html = """
<div class="button-row">
  <a href="data:application/pdf;base64,{resume_b64}" download="Suhas_Resume.pdf" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=32541&format=png&color=FFFFFF" class="contact-icon">Resume
  </a>
  <a href="mailto:suhas.karamalaputti@gmail.com" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=qyRpAggnV0zH&format=png&color=FFFFFF" class="contact-icon">Email
  </a>
  <a href="https://www.linkedin.com/in/suhas-venkata-b78750348/" target="_blank" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=13930&format=png&color=FFFFFF" class="contact-icon">LinkedIn
  </a>
  <a href="https://github.com/sUhAs1011" target="_blank" class="contact-button">
    <img src="https://img.icons8.com/?size=100&id=SzgQDfObXUbA&format=png&color=FFFFFF" class="contact-icon">GitHub
  </a>
</div>
""".format(resume_b64=base64.b64encode(open("new_resume.pdf","rb").read()).decode())
st.markdown(buttons_html, unsafe_allow_html=True)



# --- ABOUT ME ---
st.markdown("<div id='about' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")

col1, col2 = st.columns([1, 2])

with col1:
    from PIL import Image
    img = Image.open("linked.jpg")
    img = ImageEnhance.Sharpness(img).enhance(1.8)
    img = ImageEnhance.Contrast(img).enhance(1.4)
    img = ImageEnhance.Color(img).enhance(1.2)
    img = img.filter(ImageFilter.SHARPEN)

    st.image(img, width=500)  # ensures correct rendering for local file

with col2:
    st.header("👨‍💼 About Me")
    st.markdown("""
    <div style="font-size:18px; line-height:1.6; text-align: left;">
        I am <strong>Suhas Venkata</strong>, a Senior studying Computer Science & Engineering at PES University, Electronic City.
        I’m deeply passionate about machine learning and deep learning and enjoy exploring cutting-edge tech to solve meaningful problems.
        I embrace new challenges and continuously refine my skills to create real-world impact.
    </div>    
    """, unsafe_allow_html=True)
    st.markdown("    ")
    st.markdown("""
    <div style="font-size:18px; line-height:1.6; text-align: left;">
        The last 2 months, I’ve interned with the Centre for Cognitive Computing Intelligence (C3I), where I devised and deployed an end-to-end career advisory system leveraging dual-tower Deep Structured Semantic Models and ChromaDB for highly accurate job–course matching.
    </div>    
    """, unsafe_allow_html=True)
    st.markdown("    ")
    st.markdown("""
    <div style="font-size:18px; line-height:1.6; text-align: left;">
        I'm always open to challenges, collaboration, and learning—if you're exploring projects in NLP, Machine Learning, or AI, let's connect and build something meaningful together.
    </div>    
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)




# --- Skills Section ---
st.markdown("""
    <style>
    .skill-box {
        background-color: #111827;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 15px;
        transition: transform 0.2s ease-in-out;
    }
    .skill-box:hover {
        transform: scale(1.03);
    }
    .skill-text {
        font-size: 18px;
        font-weight: bold;
        color: #ffffff;
        transition: color 0.3s ease;
        cursor: pointer;
    }
    .skill-text:hover {
        color: #00BFFF;
    }
    </style>
""", unsafe_allow_html=True)



# --- Skills Section ---
st.markdown("<div id='skills' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")
st.markdown("## 🛠️ Skills")

# --- Programming Languages Sub-section ---
st.markdown("#### 👨‍💻 Programming Languages")

# Icon URLs (you can expand for other languages similarly)
icon_map = {
    "Python": "https://img.icons8.com/color/48/000000/python--v1.png",
    "Java": "https://img.icons8.com/color/48/000000/java-coffee-cup-logo--v1.png",
    "C++": "https://img.icons8.com/color/48/000000/c-plus-plus-logo.png",
    "C": "https://img.icons8.com/color/48/000000/c-programming.png",
    "Rust": "https://img.icons8.com/?size=100&id=haeAxVQEIg0F&format=png&color=000000"
}

prog_langs = ["Python", "Java", "C++", "C", "Rust"]
prog_cols = st.columns(3)

for i, lang in enumerate(prog_langs):
    with prog_cols[i % 3]:
        icon_url = icon_map[lang]
        st.markdown(
            f"""
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{icon_url}" alt="{lang} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{lang}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Web Development Sub-section ---
st.markdown("#### 🌐 Web Development")

# Icon URLs for Web Dev
webdev_icon_map = {
    "HTML": "https://img.icons8.com/?size=100&id=20909&format=png&color=000000",
    "CSS": "https://img.icons8.com/?size=100&id=21278&format=png&color=000000",
    "JavaScript": "https://img.icons8.com/?size=100&id=108784&format=png&color=000000",
    "Streamlit": "https://img.icons8.com/?size=100&id=Rffi8qeb2fK5&format=png&color=000000",
    "SpringBoot": "https://img.icons8.com/?size=100&id=90519&format=png&color=000000"
}

webdev_tools = ["HTML", "CSS", "JavaScript", "Streamlit","SpringBoot"]
webdev_cols = st.columns(3)

for i, tool in enumerate(webdev_tools):
    with webdev_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{webdev_icon_map[tool]}" alt="{tool} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- Databases Sub-section ---
st.markdown("#### 🗄️ Databases") 

db_icon_map = {
    "MySQL": "https://img.icons8.com/?size=100&id=9nLaR5KFGjN0&format=png&color=000000",
    "MongoDB": "https://img.icons8.com/?size=100&id=74402&format=png&color=000000",
    "ChromaDB": "https://miro.medium.com/v2/resize:fit:1044/1*d2XUNgrLw7687CDfXx9-Dw.png"  # Placeholder DB icon
}

db_tools = ["MySQL", "MongoDB", "ChromaDB"]
db_cols = st.columns(3)

for i, tool in enumerate(db_tools):
    with db_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{db_icon_map[tool]}" alt="{tool} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- AI/ML Sub-section ---
st.markdown("#### 🤖 AI/ML Library")


# Icon and label
ml_icon_map = {
    "Scikit-learn": "https://quintagroup.com/cms/python/images/scikit-learn-logo.png",
    "Pandas":        "https://img.icons8.com/?size=100&id=xSkewUSqtErH&format=png&color=000000",
    "NumPy":         "https://img.icons8.com/?size=100&id=aR9CXyMagKIS&format=png&color=000000",
    "NLTK":          "https://miro.medium.com/v2/resize%3Afit%3A592/1%2AYM2HXc7f4v02pZBEO8h-qw.png",
    "Spacy":         "https://upload.wikimedia.org/wikipedia/commons/8/88/SpaCy_logo.svg",
    "PyTorch":       "https://img.icons8.com/?size=100&id=jH4BpkMnRrU5&format=png&color=000000",
    "Mathplotlib":   "https://img.icons8.com/?size=100&id=TkX1totjFmAD&format=png&color=000000",
    "Keras": "https://img.icons8.com/?size=100&id=XcSgtbIpgK6W&format=png&color=000000",
    "Seaborn": "https://cdn.worldvectorlogo.com/logos/seaborn-1.svg"
}

ml_tools = ["Scikit-learn", "Pandas", "NumPy", "NLTK", "Spacy", "PyTorch", "Mathplotlib", "Keras", "Seaborn"]
ml_cols = st.columns(3)

for i, tool in enumerate(ml_tools):
    with ml_cols[i % 3]:
        icon_url = ml_icon_map.get(tool, "")
        st.markdown(
            f"""
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{icon_url}" alt="{tool} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- Tools Sub-section ---
st.markdown("#### 🧰 Tools & Platforms")

tool_icon_map = {
    "Git": "https://img.icons8.com/?size=100&id=20906&format=png&color=000000",
    "Docker": "https://img.icons8.com/?size=100&id=22813&format=png&color=000000",
    "Kubernetes": "https://img.icons8.com/?size=100&id=cvzmaEA4kC0o&format=png&color=000000",
    "VSCode": "https://img.icons8.com/?size=100&id=0OQR1FYCuA9f&format=png&color=000000",
    "Jupyter": "https://img.icons8.com/?size=100&id=J0SgMWzAxqFj&format=png&color=000000",  # Using generic Jupyter icon
    "Google Colab": "https://img.icons8.com/?size=100&id=lOqoeP2Zy02f&format=png&color=000000"
}

tools_list = list(tool_icon_map.keys())
tool_cols = st.columns(3)

for i, tool in enumerate(tools_list):
    with tool_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{tool_icon_map[tool]}" alt="{tool} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- Operating Systems Sub-section ---
st.markdown("#### 🖥️ Operating Systems")

os_icon_map = {
    "Windows": "https://img.icons8.com/?size=100&id=108792&format=png&color=000000",
    "Ubuntu": "https://img.icons8.com/?size=100&id=63208&format=png&color=000000",
    "Linux": "https://img.icons8.com/?size=100&id=m6O2bFdG70gw&format=png&color=000000"
}

os_list = list(os_icon_map.keys())
os_cols = st.columns(3)

for i, os in enumerate(os_list):
    with os_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box' style="text-align:center; padding:10px;">
                <img src="{os_icon_map[os]}" alt="{os} icon" style="width:40px; height:40px; margin-bottom:10px;" />
                <div class='skill-text' style="font-weight:bold;">{os}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- EXPERIENCE SECTION ---
st.markdown("<div id='experience' class='content-section'>", unsafe_allow_html=True)
st.markdown("    ")
st.header("💼 Experience")

# --- Company and Date with Location on the right ---
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div>
        <h3>
            <a href="https://research.pes.edu/centre-of-cognitive-computing-and-computational-intelligence-c3i/" target="_blank" style="text-decoration: none; color: inherit;">
                Centre of Cognitive Computing and Computational Intelligence
            </a>
        </h3>
        <div class='subtitle'>Summer Research Intern | June 2025 – August 2025</div>
    </div>
     <div style="text-align: right; font-size: 1.5rem;">Bengaluru, Karnataka</div>
</div>
""", unsafe_allow_html=True)

# --- Experience Details ---
st.write("""
- Architected and deployed a comprehensive career advisory system using **Deep Structured Semantic Model (DSSM)** with dual-tower neural networks for intelligent job-course matching.

- Developed advanced NLP pipeline for multi-format resume processing (PDF & DOCX, via OCR) with sophisticated skill extraction using regex patterns and custom normalization algorithms, successfully extracting relevant technical and business skills in a resume.
 
- Implemented vector database solution using ChromaDB for efficient storage and retrieval of **1,00,000+** job and course embeddings, enabling real-time semantic similarity searches across diverse datasets.

- Built interactive Streamlit application with real-time skill gap analysis, providing personalized course recommendations from Coursera and other platforms based on cosine similarity scoring and semantic matching.

- Optimized system performance through memory-efficient negative sampling, batch processing, and embedding normalization, handling **25,000+** job-course pairs while maintaining sub-second response times.
""")

st.markdown("</div>", unsafe_allow_html=True)  # End of Experience section



# --- MY JOURNEY SECTION ---
st.markdown("<div id='journey' class='content-section'>", unsafe_allow_html=True)
st.markdown("    ")
st.markdown("<h2 style='text-align:center;'>🚶‍♂️ My Journey</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-container">

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>B.Tech CSE</h3>
      <p>PES University</p>
      <p>📅 2022 – Present</p>
      <p>CGPA : 8.06</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content right">
      <h3>12th CBSE</h3>
      <p>Geetanjali Olympiad School</p>
      <p>📅 2020 – 2022</p>
      <p>12th Boards : 86%</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>10th CBSE</h3>
      <p>DPS East</p>
      <p>📅 2006 – 2020</p>
      <p>10th Boards : 90%</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# --- Custom CSS ---
st.markdown("""
<style>
.achievement-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 20px;
}
.achievement-left {
    font-size: 18px;
    font-weight: bold;
}
.achievement-description {
    font-size: 16px;
}
.achievement-date {
    font-size: 16px;
    color: #bbb;
}
</style>
""", unsafe_allow_html=True)

# --- ACHIEVEMENTS SECTION ---
st.markdown("<div id='achievements' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")
st.header("🏆 Achievements")

# Heal-O-Code Hackathon
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <h3 style="margin: 0;">🩺 Heal-O-Code Hackathon</h3>
    <div style="font-size: 24px;font-weight:bold;">March 2025</div>
</div>
""", unsafe_allow_html=True)
st.write("""
Top 10 out of 50+ teams in **Heal-O-Code Hackathon**. Built a healthcare decision support tool using **Multi-Chain Blockchain** and **Ollama** for better drug recommendation.
""")

# MRD Scholarship
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <h3 style="margin: 0;">🎓 MRD Scholarship</h3>
    <div style="font-size: 24px;font-weight:bold;">March 2023</div>
</div>
""", unsafe_allow_html=True)
st.write("""
Awarded the prestigious **MRD Scholarship** in Semester 1 by **PES University**, receiving a 20% tuition fee reimbursement in recognition of academic excellence.
""")

# DAC Scholarship
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center;">
    <h3 style="margin: 0;">🏅 DAC Scholarship</h3>
    <div style="font-size: 24px;font-weight:bold;">August 2025</div>
</div>
""", unsafe_allow_html=True)
st.write("""
Received **Distinction Scholarship** of ₹ 2000 for achieving SGPA above **7.75** in **Semesters 2–6** at **PES University**.
""")
st.markdown("</div>", unsafe_allow_html=True)





# --- PROJECTS SECTION ---
st.markdown("<div id='projects' class='content-section'>", unsafe_allow_html=True)
st.markdown("   ")
st.header("🚀 Projects")


# --- Blockchain Healthcare Project with Image ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/HoC2_PS9_Hash_Bros' target='_blank' style='text-decoration: none; color: white;'>⚕️ Blockchain-Powered Healthcare Insights</a></h3>",
        unsafe_allow_html=True
    )

    st.write("""
    Designed and developed a secure, scalable system to extract actionable insights from **Electronic Health Records (EHRs)** stored in **Inter Planetary File System (IPFS)**, with unique identifiers maintained on a **multi-chain blockchain** to ensure end-to-end data integrity and traceability.

    Key features include:
    - Analyzing patient histories
    - Predict adverse drug reactions
    - Recommend personalized treatment plans based on patient's history

    **Tech Stack**: Streamlit, Chart.js, IPFS, Multi-Chain Blockchain
    """)

with col2:
    st.image("healthcare.jpg", caption="Healthcare Blockchain System", use_container_width=True)


# Alarm Burglar System with image on the left and content on the right
st.markdown("---")
col_left, col_right = st.columns([1, 2])

with col_left:
    st.image("arduino.jpg", caption="Arduino-Based Security System", use_container_width=True)

with col_right:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/UE22CS251B-ALARM-BURGLAR-SYSTEM' target='_blank' style='text-decoration: none; color: white;'>🚨 Alarm Burglar System with Arduino</a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Engineered a **real-time intrusion detection system** using Arduino, designed to enhance home security through automated alerts and physical deterrents.

    Key features include:
    - Utilized an **ultrasonic sensor** to detect unauthorized entry, triggering a red LED, buzzer alarm, and **GSM-based alert notifications**.
    - Programmed using **C++** with `SoftwareSerial.h` to manage GSM module communication.
    - Configured the Arduino IDE and implemented serial communication to ensure seamless system performance and real-time responsiveness.

    **Tech Stack**: Arduino, C++, Ultrasonic Sensor, GSM Module, SoftwareSerial, Arduino IDE
    """)


# LegalBot with image on the right and content on the left
st.markdown("---")
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/UE22CS342B-NLP_Mini_Project-' target='_blank' style='text-decoration: none; color: white;'>⚖️ LegalBot: AI-Powered Mining Law Chatbot</a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Developed an intelligent legal chatbot to respond to text-based queries related to **Acts, Rules, and Regulations** in the mining industry.

    Key features include:
    - Analyzed and interpreted mining laws to deliver precise legal responses based on user input.
    - Utilized **Sentence Transformer models** and **cosine similarity** to match user queries with the most relevant legal provisions.
    - Identified contradictions between overlapping laws and suggested alternative documents when conflicts were found.

    This solution streamlines legal compliance and enhances accessibility to complex regulatory frameworks.

    **Tech Stack**: Sentence Transformers, Python, MongoDB, Tkinter GUI
    """)

with col_right:
    st.image("chatbot.jpg", caption="LegalBot - AI Chatbot for Mining Compliance", use_container_width=True)

# Cloud Storage with image on the left and content on the right
st.markdown("---")
col_left, col_right = st.columns([1, 2])

with col_left:
    st.image("udp.jpg", caption="UDP-Based Cloud Storage System", use_container_width=True)

with col_right:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/UE22CS252B-Cloud_Storage_Using_UDP' target='_blank' style='text-decoration: none; color: white;'>☁️ Cloud Storage System using UDP</a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Built a secure, network-based **cloud storage system** using **Python** and **UDP** (User Datagram Protocol), enabling efficient file transfer and command execution across systems.

    Key features include:
    - Developed a **client-server architecture** using Python **socket programming** for file upload, download, and listing operations.
    - Integrated **SSL certificates** for secure communication between client and server.
    - Implemented **dynamic IP handling** to support both localhost and distributed multi-system deployments.
    - Enabled execution of remote shell commands and ensured seamless file transfers across networked devices.

    **Tech Stack**: Python, UDP, Socket Programming, SSL, File Handling
    """)

# Portfolio Project with image on the right and content on the left
st.markdown("---")
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/My_Portfolio' target='_blank' style='text-decoration: none; color: white;'>🌐 Personal Portfolio Website</a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Designed and developed an interactive personal portfolio website using **Streamlit**, showcasing my projects, skills, and educational background.

    Key features include:
    - Animated hero section with a circular profile picture and gradient headers
    - Skill badges, project showcases with GitHub integration
    - A vertical educational timeline
    - Downloadable resume and aesthetic contact buttons

    The portfolio is fully responsive and easy to maintain, serving as a central hub for professional representation.

    **Tech Stack**: Streamlit, Python, HTML/CSS, PIL
    """)

with col_right:
    st.image("portfolio.jpg", caption="Streamlit Portfolio", use_container_width=True)

# Analyzing job posting trends, skill gaps, and recommend reskilling programs in  employment sectors
st.markdown("---")
col_left, col_right = st.columns([1, 2])

with col_left:
    st.image("career.jpg", caption="Career Pilot", use_container_width=True)

with col_right:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/AI-Powered-Skill-Gap-Analysis-Reskilling-for-Employment-Trends' target='_blank' style='text-decoration: none; color: white;'>🤖 AI-Powered Skill Gap Analysis & Reskilling for Employment Trends </a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Analyzing job trends, mapping skill gaps, and recommending targeted reskilling programs across sectors.

    Key features include:
    - Utilized all-MiniLM-L6-v2 to generate and push refined job and course embeddings into ChromaDB for efficient semantic search.
    - Employed a Deep Structured Semantic Model (DSSM) for training to learn enhanced semantic relationships.
    - Developed a Streamlit web application as a user-friendly frontend interface, facilitating interactive skill gap analysis and course recommendations.
    - Provided intelligent course suggestions directly addressing identified skill gaps relevant to a specific job position, leveraging both pre-computed mappings and the trained DSSM.
    

    **Tech Stack**: Python, Sentence Transformers, ChromaDB, DSSM, Streamlit, Tesseract 
    """)

st.markdown("</div>", unsafe_allow_html=True) # End of Projects section

# --- Custom Footer with Styling ---
st.markdown("""
    <div style='text-align: center; padding-top: 20px; font-size: 40px; font-weight: 500; color: #ffffff;'>
        Made by Suhas Venkata
    </div>
""", unsafe_allow_html=True)



