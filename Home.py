import streamlit as st

st.set_page_config(layout="centered")

col1, col2, col3=  st.columns([1,2,1])
with col2:
    st.image("img/color.jpeg")

col1, col2, col3=  st.columns([1,2,1])
with col2:
    st.header("Protowerx AI Advisors")




#col1, col2, col3 =  st.columns([1, 1, 1]) # column widths for a balanced

#with col1:
st.header("Who We Are")
st.write("Introducing ProtoWerx AI Advisors – your trusted partner in navigating the complexities of AI integration for small businesses.") 

#with col2:
st.header("Why Protowerx?")
st.write("In a landscape inundated with buzzwords and flashy promises, Protowerx stands out as a beacon of clarity and expertise. We understand the challenges faced by small to medium-sized businesses when it comes to leveraging AI technologies effectively.")

#with col3:
st.header("Services")
st.write("With a team of seasoned AI solution advisors boasting extensive experience in development, integration, and testing across diverse industries, Protowerx is uniquely positioned to guide you through your AI journey. We offer tailored consultation, comprehensive reports, expertly crafted architectures, and prototype AI systems, all designed to cut through the noise of AI marketing hype and deliver tangible solutions tailored to your business needs.")
             

             
             
             #Our target market? Businesses eager to harness the power of AI but lacking the in-house resources to do so. While the competition may be fierce, ProtoWerx sets itself apart by offering personalized, hands-on service directly to our clients, ensuring every solution is meticulously crafted to drive tangible results.
             
             
             
             #Whether you're looking to optimize workflows, enhance customer experiences, or unlock new opportunities, ProtoWerx is here to help you realize your AI ambitions. Let's embark on this journey together towards a smarter, more prosperous future.")
