import streamlit as st

st.set_page_config(layout="centered")

col1, col2, col3=  st.columns([1,2,1])
with col2:
    st.image("img/color.jpeg")

col1, col2, col3=  st.columns([1,2,1])
with col2:
    st.header("Protowerx AI Advisors")


col1, col2, col3=  st.columns([1,2,1])
with col2:
    st.header("Advisory Team")

col1, col2, col3=  st.columns([1,1,1])
with col1:
    st.image("img/lane_headshot.jpg")
    st.subheader("Lane Boyer")
    st.link("https://www.linkedin.com/in/lane-boyer-485836a/")
    st.write("As an AI/ML solutions data scientist/engineering manager, I leverage my experience and passion for field-testing new technology to design, architect, and build operational AI solutions / systems for real-world customer requirements. I have executed AI/ML development and engineering efforts across the energy and defense industries both domestically and abroad. I have led teams, projects, and people from AI concept to experimentation to deployment. I hold an M.S. in Artificial Intelligence from Northwester University and M.S and B.S. degrees in Geology from the University of Arkansas.")

    st.write("I enjoy competing in endurance running events and have run 14 marathons in the last 8 years with a PR of 2:27. I excel at working with a team to solve difficult problems and especially enjoy employing new technologies to do so.")

with col2:
    st.image("img/derek.jpeg")
    st.subheader("Derek Hanson, PhD")
    st.link("https://www.linkedin.com/in/hansondj/")
    st.write("As a Senior Data Scientist at SparkCognition Government Systems (SGS), I develop and deploy cutting-edge AI and ML solutions for various government and defense clients. I have over 8 years of experience in using data science, analytics, and experimentation to improve technology products and services.")

    st.write("I am passionate about leveraging AI and ML to solve complex and impactful problems, and to deliver value and innovation to the government and defense sector. I am always eager to learn new tools and techniques, and to collaborate with diverse and talented teams. I strive to create ethical, scalable, and robust AI and ML solutions that can enhance the security, efficiency, and performance of our clients.")

with col3:
    st.image("img/bill.jpeg")
    st.subheader("Bill Spiesman, PhD")
    st.link("https://www.linkedin.com/in/spiesman/")
