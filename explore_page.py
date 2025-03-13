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
  </style>
  """
  st.markdown(page_bg_img, unsafe_allow_html=True)

  

  # Add contents
  st.title("🤖 VelocityAI 🏗️")

  st.info("""### Building Strength with Data-Driven Intelligence """)
  st.write("""#### At Velocity AI, we are redefining how the construction industry ensures concrete strength. Our AI-powered tool, StrucSure, predicts the compressive strength of concrete with high accuracy, helping engineers, developers, and construction firms save time, reduce material waste, and improve quality control. Instead of waiting for lab tests, you can get instant predictions using our machine learning model—helping you make faster, smarter, and cost-efficient decisions in your projects.""")
