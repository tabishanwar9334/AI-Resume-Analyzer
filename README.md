# AI Resume Analyzer

## 1. Project Title

**AI Resume Analyzer Using Machine Learning**

---

## 2. About Project

AI Resume Analyzer is a web-based application developed using Python, Streamlit, Machine Learning, and MongoDB. The system helps recruiters and organizations evaluate resumes by comparing them with job descriptions and generating a similarity score. This reduces manual effort and improves the efficiency of the recruitment process.

---

## 3. Purpose / Advantages / Applications

### Purpose

* Automate the resume screening process.
* Compare candidate resumes with job requirements.
* Provide a compatibility score for better hiring decisions.

### Advantages

* Saves time during recruitment.
* Reduces manual resume screening.
* Provides quick and accurate results.
* Easy to use and accessible through a web interface.

### Applications

* HR Management Systems
* Recruitment Agencies
* Corporate Hiring Processes
* Educational Placement Cells

---

## 4. Front-End Technologies

### Python Streamlit

Streamlit is used to create the user interface of the application. It provides interactive forms, file upload functionality, dashboards, and data visualization features.

---

## 5. Back-End Technology

### MongoDB

MongoDB is used to store user information such as registration details, login credentials, profile information, and uploaded data.

---

## 6. E-R Diagram

```text
 ┌─────────────┐
 │    USER     │
 ├─────────────┤
 │ Username    │
 │ Password    │
 │ Mobile      │
 │ DOB         │
 │ Gender      │
 │ Course      │
 │ Photo       │
 └──────┬──────┘
        │
        │ Uploads
        │
 ┌──────▼──────┐
 │   RESUME    │
 ├─────────────┤
 │ CV PDF      │
 │ Resume Text │
 └──────┬──────┘
        │ Compared With
        │
 ┌──────▼──────────┐
 │ JOB DESCRIPTION │
 ├─────────────────┤
 │ JD PDF          │
 │ JD Text         │
 └──────┬──────────┘
        │
        │ Generates
        │
 ┌──────▼──────┐
 │ MATCH SCORE │
 ├─────────────┤
 │ Similarity% │
 └─────────────┘
```



---

## 7. DFD (Data Flow Diagram)

```text
User
  |
  v
Upload Resume & JD
  |
  v
Text Extraction
  |
  v
Machine Learning Analysis
  |
  v
Similarity Score
  |
  v
Result Display
```



---

## 8. Running Project Screenshots

Add screenshots here:

### Home Page

![Home Page](screenshots/home.png)

### Sign Up Page

![Sign Up](screenshots/signup.png)

### Sign In Page

![Sign In](screenshots/signin.png)

### Resume Analysis Page

![Resume Analysis](screenshots/cv.png)

### Profile Page

![Profile](screenshots/profile.png)

---

## 9. Source Code

The complete source code is available in this repository.

### Main Files

* main.py
* SignUp.py
* SignIn.py
* cv.py
* profile.py
* style.css

---

## 10. Project URL

### GitHub Repository

https://github.com/YOUR_USERNAME/AI-Resume-Analyzer

### Live Demo (Optional)

https://your-project-url.com

---

## Technologies Used

* Python
* Streamlit
* MongoDB
* Scikit-Learn
* PyPDF
* HTML/CSS

---

## Author

**Tabish Anwar**
B.Sc IT Student | Python Developer | AI Enthusiast
