import streamlit as st

# --------------------------------
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -------------------------------------------------------------------


st.header("C V Analysis using AI and Machine Learning")
st.logo("cv.png",size="large")
st.header("📫 Get In Touch With Me!")
with st.form("contact_form"):
        name = st.text_input("Full Name", placeholder="Your Name")
        email = st.text_input("Email Address", placeholder="Your Email")
        message = st.text_area("Your Message", placeholder="How can I help you?")
        submit_button = st.form_submit_button("Send Message")
        if submit_button:
            if not name or not email or not message:
                st.error("Please fill in all fields.")
            else:
                st.success(f"Thanks for reaching out, {name}!")
              

