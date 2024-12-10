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
    