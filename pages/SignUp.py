
import streamlit as st
import pymongo
import random
from datetime import date

# --------------------------------
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -------------------------------------------------------------------

conn=pymongo.MongoClient("mongodb+srv://tabish:<Tabish2004>@cluster0.fm0euup.mongodb.net/?appName=Cluster0")
try:
    conn.admin.command("ping")
    st.success("✅ MongoDB Connected")
except Exception as e:
    st.error(f"❌ MongoDB Error: {e}")

mydb=conn["ojt2"]
my=mydb["student"]

# st.header("C V Analysis using AI and Machine Learning")
# st.subheader("📝 SignUp")

# ---------------------------------------

st.markdown("""
<div class="hero-box">
    <h1>🚀 Create Your Account</h1>
    <h3>Join AI Resume Analyzer</h3>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------
st.logo("cv.png",size="large")

# st.markdown("---")

c1,c2,c3=st.columns(3)
with st.form("SignUp Form"):
       left,right = st.columns(2)

       with left:
              username=st.text_input("👨‍💼 Username")
              password=st.text_input("🔑 Password",type="password")
              address=st.text_area("🏠 Address")
              mobile=st.text_input("📞 Mobile Number")
              gender=st.radio("Gender",['M','F'])
              age=st.slider("Age",16,28)

       with right:
              course=st.selectbox("Select Your Course",["B.SC CA","B.SC IT","B.SC CS"])
             
              dob = st.date_input("📅 Date of Birth",min_value=date(1950, 1, 1),max_value=date.today())
              live_photo=st.camera_input("Upload Your Live Picture")
              count=random.randrange(1,10)
              str1="img"
              str1=str1+str(count)
              str1=str1+".png"
              count=count+1
              if live_photo:
                     with open(str1,"wb") as f:
                            f.write(live_photo.getvalue())

       
       
       
      

       submit = st.form_submit_button("🚀 Create Account")

       if submit:
              my.insert_one({"username":username,"password":password,"address":address,"course":course,"dob":str(dob),"mobileno":mobile,"gender":gender,"age":age,"photo":str1})
              # st.success("SIGN UP SYCCESSFULLY ✅")
              st.balloons()
              st.success("🎉 Account Created Successfully!")






