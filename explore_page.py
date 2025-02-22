import streamlit as st

def show_explore_page():

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
    background-image: url("https://jacob-delosangeles.github.io/AI-construction/images/backgroundSidebar_1.jpg");
    background-position: center;
    }
    
  </style>
  """
  st.markdown(page_bg_img, unsafe_allow_html=True)

  # Add contents
  st.title("🤖 StrucSure 🏗️")

  st.info("""### Building Strength with Data-Driven Intelligence """)
