
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Suhas_Portfolio", page_icon="📁", layout="wide")

# --- LOAD IMAGE ---
# Assuming 'profile.jpg' is in the same directory as your script
# Function to safely load and convert images to base64 for inline HTML
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
    width: 280px;
    height: 280px;
    object-fit: cover;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
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
    font-size: 17px;
    transition: color 0.3s, background-color 0.3s;
    margin-left: 20px; /* Space between links */
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
    <a href="#skills">🛠️ Skills</a>
    <a href="#experience">💼 Experience</a>
    <a href="#journey">🚶‍♂️ My Journey</a>
    <a href="#achievements">🏆 Achievements</a>
    <a href="#projects">🚀 Projects</a>
</div>
""", unsafe_allow_html=True)
# Removed excessive <br> tags. The content-section padding-top should handle spacing.
# If more space is still needed, adjust the padding-top in .content-section CSS or add fewer <br> tags.
# st.markdown("<br>", unsafe_allow_html=True) # You can add one or two if needed

# --- HERO SECTION ---
st.markdown("<div id='home' class='content-section'>", unsafe_allow_html=True)
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
    st.markdown("<div class='gradient-text'>Suhas Venkata <span>👋</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>CSE Student at PES University</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='intro'>
        I'm Suhas Venkata, a Computer Science junior at PES University (Electronic City) with a strong interest in machine learning and deep learning. I'm passionate about learning, taking on new challenges, and sharpening my technical skills to make a meaningful impact.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if img_b64: # Only render if image was loaded successfully
        st.markdown(f"<img src='data:image/png;base64,{img_b64}' class='profile-pic'/>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True) # End of Home section

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
st.markdown("---")
st.markdown("## 🛠️ Skills")

# --- Programming Languages Sub-section ---
st.markdown("#### 💻 Programming Languages")
prog_langs = ["Python", "Java", "C++", "C", "Rust"]
prog_cols = st.columns(3)
for i, lang in enumerate(prog_langs):
    with prog_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <div class='skill-text'>{lang}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Web Development Sub-section ---
st.markdown("#### 🌐 Web Development")
web_devs = ["HTML", "CSS", "JavaScript", "Streamlit"]
web_cols = st.columns(3)
for i, tech in enumerate(web_devs):
    with web_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <div class='skill-text'>{tech}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Databases Sub-section ---
st.markdown("#### 🗄️ Databases")
dbs = ["MySQL", "MongoDB", "ChromaDB"]
db_cols = st.columns(3)
for i, db in enumerate(dbs):
    with db_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <div class='skill-text'>{db}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- AI/ML Sub-section ---
st.markdown("#### 🤖 AI / ML")
ml_libs = ["Scikit-learn", "Pandas", "Numpy", "NLTK", "Spacy", "Pytorch"]
ml_cols = st.columns(3)
for i, lib in enumerate(ml_libs):
    with ml_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <div class='skill-text'>{lib}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Tools Sub-section ---
st.markdown("#### 🧰 Tools")
tools = ["Git", "Docker", "Kubernetes", "VSCode", "Jupyter", "Colab"]
tool_cols = st.columns(3)
for i, tool in enumerate(tools):
    with tool_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <div class='skill-text'>{tool}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Operating Systems Sub-section ---
st.markdown("#### 🖥️ Operating Systems")
oses = ["Windows", "Ubuntu", "Linux"]
os_cols = st.columns(3)
for i, os in enumerate(oses):
    with os_cols[i % 3]:
        st.markdown(
            f"""
            <div class='skill-box'>
                <div class='skill-text'>{os}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- EXPERIENCE SECTION ---
st.markdown("<div id='experience' class='content-section'>", unsafe_allow_html=True)
st.markdown("---")
st.header("💼 Experience")

st.subheader("C3I(Centre of Cognitive Computing and Computational Intelligence) June 2025 – August 2025 ")
st.write("""
- Built a career advisory platform leveraging NLP, vector search, and data analytics to identify gaps between user resume skills and target job
requirements.
- Recommended personalized online courses (primarily from Coursera) to help users bridge skill gaps and upskill effectively based on job
description analysis.
""")
st.markdown("</div>", unsafe_allow_html=True) # End of Experience section


# --- MY JOURNEY SECTION ---
st.markdown("<div id='journey' class='content-section'>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h2 style='text-align:center;'>My Journey</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="timeline-container">

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>10th CBSE</h3>
      <p>DPS East</p>
      <p>📅 2006 – 2020</p>
      <p>90%</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content right">
      <h3>12th CBSE</h3>
      <p>Geetanjali Olympiad School</p>
      <p>📅 2020 – 2022</p>
      <p>86%</p>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-content left">
      <h3>B.Tech CSE</h3>
      <p>PES University</p>
      <p>📅 2022 – Present</p>
      <p>CGPA: 8.06</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)



# --- ACHIEVEMENTS SECTION ---
st.markdown("<div id='achievements' class='content-section'>", unsafe_allow_html=True)
st.markdown("---")
st.header("🏆 Achievements")

# Heal-O-Code Hackathon
st.subheader("🧠 Heal-O-Code Hackathon – March 2025")
st.write("""
Top 10 out of 50+ teams in **Heal-O-Code Hackathon**
Built a healthcare decision support tool using **Multi-Chain Blockchain** and **Ollama** for better drug recommendation.
""")

# MRD Scholarship
st.subheader("🎓 MRD Scholarship – March 2023")
st.write("""
Awarded the prestigious **MRD Scholarship** in Semester 1 by **PES University**, receiving a 20% tuition fee reimbursement in recognition of academic excellence.
""")

# Distinction Scholarship
st.subheader("🎖️ Distinction Scholarship ")
st.write("""
Received **Distinction Scholarship** of ₹ 2000 for achieving SGPA above **7.75** in **Semesters 2, 3, 4, 5 and 6** at **PES University**.
""")
st.markdown("</div>", unsafe_allow_html=True) # End of Achievements section

# --- PROJECTS SECTION ---
st.markdown("<div id='projects' class='content-section'>", unsafe_allow_html=True)
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
    Designed and developed a secure, scalable system to extract actionable insights from **Electronic Health Records (EHRs)** stored in **Inter Planetary File System (IPFS)**, with unique identifiers maintained on a **multi-chain blockchain** to ensure end-to-end data integrity and traceability.

    Key features include:
    - Analyzing patient histories
    - Predict adverse drug reactions
    - Recommend personalized treatment plans based on patient's history

    **Tech Stack**: Streamlit, Chart.js, IPFS, Multi-Chain Blockchain, ML
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

st.markdown("</div>", unsafe_allow_html=True) # End of Projects section

# --- Custom Footer with Styling ---
st.markdown("""
    <div style='text-align: center; padding-top: 20px; font-size: 40px; font-weight: 500; color: #ffffff;'>
        Made by Suhas Venkata
    </div>
""", unsafe_allow_html=True)


# --- RESUME DOWNLOAD ---
try:
    with open("new_resume.pdf", "rb") as file:
        resume_data = file.read()
        b64_resume = base64.b64encode(resume_data).decode()

    st.markdown(f"""
    <div style='text-align: center;'>
        <a href="data:application/pdf;base64,{b64_resume}" download="Suhas_Resume.pdf" class="contact-button">📄 Resume</a>
    </div>
    """, unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Resume file 'new_resume.pdf' not found. Download button will not appear.")

# --- Centered Contact Buttons ---
st.markdown("""
<div style='text-align: center; margin-top: 20px;'>
    <a href="mailto:suhas.karamalaputti@gmail.com" class="contact-button">📧 Email</a>
    <a href="https://www.linkedin.com/in/suhas-venkata-b78750348/" target="_blank" class="contact-button">🔗 LinkedIn</a>
    <a href="https://github.com/sUhAs1011" target="_blank" class="contact-button">💻 GitHub</a>
</div>
""", unsafe_allow_html=True)