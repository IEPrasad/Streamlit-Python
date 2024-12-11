import streamlit as st 

@st.experimental_dialog("Contact Me")
def show_contact_form():
  st.text_input("First Name")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment = "center")
with col1:
  st.image("./assets/profile-picture.png", width=230)

with col2:
  st.title("Sven Bosau", anchor=False)
  st.write(
    "Senior Data Analyst, assisting enterprises by supporting data-driven decision-making"
  )
  if st.button("💌 Contact Me"):
    show_contact_form()
    
# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
  """
  - 7 Years experince Extracting actionable insights from data
  - Strong's hands on experience and knowledge in Python And excel
  - Good understanding of statistical principles and their respective applications
  - Excellent team player and displaying a strong sense of initiative on tasks
  """
)

# --- SKILS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
  """
  - Programming: Python (Scikit-learn, Pandas), SQL, VBA
  - Data Visualization: PowerBi, MS Excel, Plotly
  - Modeling: Logistic regression, linear regression, decision trees
  - Databases: Postgres, MongoDB, MySQL
  """
  )