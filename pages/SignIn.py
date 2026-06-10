import streamlit as st
import pymongo

# --------------------------------
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -------------------------------------------------------------------

# ----------------------------

st.markdown("""
<div class="hero-box">
    <h1>🔐 Welcome Back</h1>
    <h3>Sign In To Continue</h3>
</div>
""", unsafe_allow_html=True)

# ---------------------------------

conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.1")
# conn=pymongo.MongoClient("mongodb+srv://kunalg15_db_user:UchdhJoflEo7GMli@citcapp.mong26u.mongodb.net/?appName=CitcApp")
mydb=conn["ojt2"]
my=mydb["student"]

# st.header("📊 CV Analysis using AI and ML")
st.subheader("👤 SignIn")
st.logo("cv.png",size="large")
with st.form("SignIn"):

       # ---------------------------
       st.markdown("""
       <div class="about-card">
       <h2>Login Account</h2>
       </div>
       """, unsafe_allow_html=True)

       t1 = st.text_input("👤 Username",placeholder="Enter username")

       t2 = st.text_input("🔑 Password",type="password",placeholder="Enter password")

       # ------------------------------

       # t1=st.text_input("👤User name")
       # t2=st.text_input("🔒 Password",type="password")

       if st.form_submit_button("SignIn"):
              if not t1 or not t2:
                     st.error("Fill The Fields!!!")
              else:
                     res=my.find({"username":t1,"password":t2})
                     v=0
                     for data in res:
                            v=v+1
                            st.session_state["username"]=data['username']
                            st.session_state["password"]=data['password']
                            st.session_state["img"]=data['photo']
                            
                            st.switch_page("pages/profile.py")
                     if v==0:
                            st.error("Invalid Login Details")
                     
                     
                     
