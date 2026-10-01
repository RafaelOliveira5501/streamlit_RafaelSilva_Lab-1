import streamlit as st
import info

st.title("Web Development Lab 1")

st.header("CS 1301")
st.subheader("Web Development - Section FAD")  
st.subheader("Rafael Oliveira e Silva")

st.write("""
Welcome to our Streamlit Web Development Lab 1 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Portfolio**: My personal portfolio, including my education, experience, projects, skills, and activities.
2. **Quiz Page**: An interactive quiz that matches you with a future tech career: AI Engineer, Robotics Engineer, or Space Systems Engineer.
""")

def links_section():
    st.sidebar.header("Links")

    st.sidebar.text("Check out my GitHub")

    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="GitHub" width="75" height="75"></a>'

    st.sidebar.markdown(github_link, unsafe_allow_html=True)

    st.sidebar.text("Connect with me on LinkedIn")

    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'

    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)



    st.sidebar.text("Send me an email")

    email_link = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'

    st.sidebar.markdown(email_link, unsafe_allow_html=True)

links_section()
