import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Suhas_Portfolio", page_icon="📁", layout="wide")

# --- LOAD IMAGE ---
profile_pic = Image.open("profile.jpg")

# Convert image to base64 for inline HTML
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

img_b64 = image_to_base64(profile_pic)

# --- CUSTOM STYLES ---
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
    st.markdown("<div class='subtitle'>CSE Student at PES University</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='intro'>
            I am Suhas Venkata, a Junior at PES University(Electronic City), currently pursuing a Bachelor's degree in Computer Science and Engineering.My academic journey is driven by a deep interest in machine learning and deep learning. I am always eager to expand my knowledge, embrace new challenges, and refine my technical skills to contribute meaningfully to the field.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<img src='data:image/png;base64,{img_b64}' class='profile-pic'/>", unsafe_allow_html=True)

# --- SKILLS SECTION ---
st.markdown("---")
st.header("🛠️ Skills")
st.write("""
- **Languages**: Python, Java, C++, C, Rust  
- **Web Development**: HTML, CSS, JavaScript, Streamlit
- **Database**: MySQL, MongoDB, ChromaDB
- **AI/ML**: Scikit-learn, Pandas, Numpy, NLTK, Spacy, pytorch
- **Tools**: Git, Docker, Kubernetes, VSCode, Jupyter, Colab
- **Operating Systems**: Windows, Ubuntu, Linux
""")

# --- EXPERIENCE SECTION ---
st.markdown("---")
st.header("💼 Experience")

st.subheader("C3I(Centre of Cognitive Computing and Computational Intelligence) June 2025 – August 2025 ")
st.write(""" 
 - Built a career advisory platform leveraging NLP, vector search, and data analytics to identify gaps between user resume skills and target job
requirements. 
 - Recommended personalized online courses (primarily from Coursera) to help users bridge skill gaps and upskill effectively based on job
description analysis.
""")


# --- JOURNEY SECTION ---
st.markdown("---")
st.markdown("<h2 style='text-align:center;'>My Journey</h2>", unsafe_allow_html=True)

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
      <p>CGPA:8.06</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content right">
      <h3>12th CBSE</h3>
      <p>Geetanjali Olympiad School</p>
      <p>📅 2020 – 2022</p>
      <p>86% (12th boards) </p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>10th CBSE</h3>
      <p>DPS EAST</p>
      <p>📅 2006 – 2020</p>
      <p>90%(10th boards)</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# --- ACHIEVEMENTS SECTION ---
st.markdown("---")
st.header("🏆 Achievements")

# Heal-O-Code Hackathon
st.subheader("🧠 Heal-O-Code Hackathon – March 2025")
st.write("""
Top 10 out of 50+ teams in **Heal-O-Code Hackathon**  
Built a healthcare decision support tool using **Blockchain** and **Machine Learning** for faster clinical decision-making.
""")

# MRD Scholarship
st.subheader("🎓 MRD Scholarship – March 2023")
st.write("""
Awarded the prestigious **MRD Scholarship** in Semester 1 by **PES University**, receiving a 20% tuition fee reimbursement in recognition of academic excellence.
""")

# Distinction Scholarship
st.subheader("🎖️ Distinction Scholarship ")
st.write("""
Received **Distinction Scholarship** of 2000 Rs for achieving above 7.75 SGPA in **Semesters 2, 3, 4, and 5** at **PES University**.
""")

# --- PROJECTS SECTION ---
st.markdown("---")
st.header("🚀 Projects")


# --- Blockchain Healthcare Project with Image ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        "<h3><a href='https://github.com/sUhAs1011/HoC2_PS9_Hash_Bros' target='_blank' style='text-decoration: none; color: white;'>🗳️ Blockchain-Powered Healthcare Insights</a></h3>",
        unsafe_allow_html=True
    )

    st.write("""
    Designed and developed a secure, scalable system to extract actionable insights from **Electronic Health Records (EHRs)** stored in **IPFS**, with unique identifiers maintained on a **multi-chain blockchain** to ensure end-to-end data integrity and traceability.

    Leveraged machine learning to:
    - Analyze patient histories  
    - Predict adverse drug reactions  
    - Recommend personalized treatment plans  

    This system significantly improved the speed and accuracy of clinical decision-making.

    **Tech Stack**: Spring Boot, MySQL, React, Chart.js, IPFS, Blockchain, ML
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
        "<h3><a href='https://github.com/sUhAs1011/UE22CS251B-ALARM-BURGLAR-SYSTEM' target='_blank' style='text-decoration: none; color: white;'>🔐 Alarm Burglar System with Arduino</a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Engineered a **real-time intrusion detection system** using Arduino (April 2024), designed to enhance home security through automated alerts and physical deterrents.

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
        "<h3><a href='https://github.com/sUhAs1011/UE22CS342B-NLP_Mini_Project-' target='_blank' style='text-decoration: none; color: white;'>💬 LegalBot: AI-Powered Mining Law Chatbot</a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Developed an intelligent legal chatbot to respond to text-based queries related to **Acts, Rules, and Regulations** in the mining industry.

    Key features include:
    - Analyzed and interpreted mining laws to deliver precise legal responses based on user input.  
    - Utilized **Sentence Transformer models** and **cosine similarity** to match user queries with the most relevant legal provisions.  
    - Identified contradictions between overlapping laws and suggested alternative documents when conflicts were found.

    This solution streamlines legal compliance and enhances accessibility to complex regulatory frameworks.

    **Tech Stack**: Sentence Transformers, Python, MongoDB, Tkinter GUI, NLP
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
    Built a secure, network-based **cloud storage system** using Python and UDP (March 2024), enabling efficient file transfer and command execution across systems.

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
        "<h3><a href='https://github.com/sUhAs1011/My_Portfolio' target='_blank' style='text-decoration: none; color: white;'>📁 Personal Portfolio Website</a></h3>",
        unsafe_allow_html=True
    )
    st.write("""
    Designed and developed an interactive personal portfolio website using **Streamlit**, showcasing my projects, skills, and educational background.

    Features include:
    - Animated hero section with a circular profile picture and gradient headers  
    - Skill badges, project showcases with GitHub integration  
    - A vertical educational timeline  
    - Downloadable resume and aesthetic contact buttons  

    The portfolio is fully responsive and easy to maintain, serving as a central hub for professional representation.

    **Tech Stack**: Streamlit, Python, HTML/CSS, PIL
    """)

with col_right:
    st.image("portfolio.jpg", caption="Streamlit Portfolio", use_container_width=True)


# --- Custom Footer with Styling ---
st.markdown("""
    <div style='text-align: center; padding-top: 20px; font-size: 40px; font-weight: 500; color: #ffffff;'>
        Made by Suhas Venkata
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

# --- RESUME DOWNLOAD ---
with open("new_resume.pdf", "rb") as file:
    resume_data = file.read()
    b64_resume = base64.b64encode(resume_data).decode()

st.markdown("""
<div style='text-align: center;'>
    <a href="data:application/pdf;base64,{}" download="Suhas_Resume.pdf" class="contact-button">📄 Resume</a>
</div>
""".format(b64_resume), unsafe_allow_html=True)

# --- Centered Contact Buttons ---
st.markdown("""
<div style='text-align: center; margin-top: 20px;'>
    <a href="mailto:suhas.karamalaputti@gmail.com" class="contact-button">📧 Email</a>
    <a href="https://www.linkedin.com/in/suhas-venkata-b78750348/" target="_blank" class="contact-button">🔗 LinkedIn</a>
    <a href="https://github.com/sUhAs1011" target="_blank" class="contact-button">💻 GitHub</a>
</div>
""", unsafe_allow_html=True)


