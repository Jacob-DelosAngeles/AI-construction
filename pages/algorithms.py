import streamlit as st
# Adding Background
page_bg_img = """
<style>
  [data-testid="stAppViewContainer"] {
    background-image: url("https://jacob-delosangeles.github.io/AI-construction/images/backgroundConcrete.jpg");
    background-size: cover;
  }
  [data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
  }

  [data-testid="stSidebar"]{
  background-image: url("https://jacob-delosangeles.github.io/AI-construction/images/SideBar_bg.png");
  background-position: center;
  }

  [data-testid="stSidebar"] * {
      color: white !important;  /* Ensures all text is white */
  }

  /* Button Styling */
  .stButton>button {
      background-color: #00ADB5; /* Teal button color */
      color: white;
      border-radius: 8px;
      padding: 8px;
      border: none;
  }
  
  .stButton>button:hover {
      background-color: #008B8B; /* Darker teal on hover */
      color: white;
  }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Under Development")
