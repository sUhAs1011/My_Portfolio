import streamlit as st
from PIL import Image
import base64
from io import BytesIO


st.set_page_config(page_title="Suhas Venkata", page_icon="📁", layout="wide")


profile_pic = Image.open("profile.jpg")


def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

img_b64 = image_to_base64(profile_pic)


st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.gradient-text {
    font-size: 48px;
    font-weight: 800;
    background: -webkit-linear-gradient(90deg, #005BEA, #00C6FB);
    -webkit-background-clip: text;
    color: white;
    margin-bottom: 5px;
}

.gradient-text span {
    -webkit-text-fill-color: inherit;
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
    width: 280px;
    height: 280px;
    object-fit: cover;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
}

.hero-container {
    padding: 40px 20px 20px 40px;
}

/* Timeline styling */
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
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<div class='gradient-text'>Suhas Venkata <span>👋</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>B.Tech CSE Student</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='intro'>
        Hey! I'm Suhas and I'm a student passionate about building secure, intelligent systems.  
        My interests lie in AI, Machine Learning, Blockchain, and Cybersecurity.  
        Welcome to my portfolio! 😊
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<img src='data:image/png;base64,{img_b64}' class='profile-pic'/>", unsafe_allow_html=True)

# --- SKILLS SECTION ---
st.markdown("---")
st.header("🛠️ Skills")
st.write("""
- **Languages**: Python, Java, C++, JavaScript  
- **Web Development**: HTML, CSS, React, Node.js, Spring Boot  
- **Database**: MySQL, MongoDB  
- **AI/ML**: scikit-learn, Pandas, Numpy, Streamlit  
- **Security**: SSL, Network Protocols, Cryptography  
- **Tools**: Git, Postman, Docker, VS Code
""")

# --- JOURNEY SECTION ---
st.markdown("---")
st.markdown("<h2 style='text-align:center;'>My Journey</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Here is my personal journey 🧾</p>", unsafe_allow_html=True)

# --- Timeline CSS (alternating vertical style) ---
st.markdown("""
<style>
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
</style>
""", unsafe_allow_html=True)

# --- Timeline Content ---
st.markdown("""
<div class="timeline-container">

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>B.Tech CSE</h3>
      <p>PES University</p>
      <p>📅 2022 – Present</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content right">
      <h3>12th PUC</h3>
      <p>Geetanjali Olympiad School</p>
      <p>📅 2020 – 2022</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>10th CBSE</h3>
      <p>DPS EAST</p>
      <p>📅 2006 – 2020</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)


# --- PROJECTS SECTION ---
st.markdown("---")
st.header("🚀 Projects")

st.subheader("🗳️ Electronic Voting System")
st.write("""
Built a secure and role-based electronic voting system using Java Spring Boot and MySQL, with React frontend and dynamic result visualization.
""")
st.write("**Tech Stack**: Spring Boot, MySQL, React, Chart.js")

st.subheader("🧠 Emotion Classifier (ML Hackathon)")
st.write("""
Built an ML model to classify sentiments into Positive, Negative, and Neutral from text data, achieving high accuracy.
""")
st.write("**Tech Stack**: scikit-learn, Pandas, CSV")

st.subheader("💬 LegalBot")
st.write("""
A chatbot for mining law compliance using Sentence Transformers and MongoDB. Handles user queries, detects contradictions, and suggests alternatives.
""")
st.write("**Tech Stack**: NLP, MongoDB, Tkinter GUI")

# --- Custom Footer with Styling ---
st.markdown("""
    <div style='text-align: center; padding-top: 20px; font-size: 40px; font-weight: 500; color: #ffffff;'>
        Made with ❤️ by <strong>Suhas Venkata</strong>
    </div>
""", unsafe_allow_html=True)



# --- Gradient Button CSS (No underline) ---
st.markdown("""
<style>
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

# --- Centered Contact Buttons ---
st.markdown("""
<div style='text-align: center; margin-top: 20px;'>
    <a href="mailto:suhas.karamalaputti@gmail.com" class="contact-button">📧 Email</a>
    <a href="https://www.linkedin.com/in/suhas-venkata-b78750348/" target="_blank" class="contact-button">🔗 LinkedIn</a>
    <a href="https://github.com/sUhAs1011" target="_blank" class="contact-button">💻 GitHub</a>
</div>
""", unsafe_allow_html=True)

