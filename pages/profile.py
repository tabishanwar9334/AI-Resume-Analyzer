import streamlit as st
import pymongo
from PIL import Image

# --------------------------------
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -------------------------------------------------------------------


conn=pymongo.MongoClient("mongodb+srv://tabish:Tabish2004@cluster0.fm0euup.mongodb.net/?appName=Cluster0")
try:
    conn.admin.command("ping")
    st.success("✅ MongoDB Connected")
except Exception as e:
    st.error(f"❌ MongoDB Error: {e}")
mydb=conn["ojt2"]
my=mydb["student"]
@st.dialog("CHANGE PASSWORD")
def cp():
       t1=st.text_input("Enter The Old Password")
       t2=st.text_input("Enter The New Password")
       if st.button("Change Password"):
              res=my.update_one({"password":t1},{'$set':{"password":t2}})
              st.success("Password Changed Successfully ✅")


       
c1,c2,c3,c6=st.columns(4)
c4,c5=st.columns(2)
c4.header("📊 CV Analysis..")
if c1.button("🔒 Change Password",use_container_width=True):
       cp()
if c2.button("👤 See Profile",use_container_width=True):
       str1=st.session_state["username"]
       str2=st.session_state["password"]
       res=my.find({"username":str1,"password":str2})
       st.success("USER PROFILE")
       for data in res:
              st.text_input("Username",data["username"])
              st.text_input("Password",data["password"])
              st.text_input("Address",data["address"])
              st.text_input("Course",data["course"])
              st.text_input("DOB",data["dob"])
              st.text_input("Mobile No",data["mobileno"])
                     
if c3.button("📊 CV Analysis",use_container_width=True):
       st.switch_page("pages/cv.py")
if c6.button("Logout",use_container_width=True):
       del st.session_state["username"]
       del st.session_state["password"]
       st.switch_page("main.py")

