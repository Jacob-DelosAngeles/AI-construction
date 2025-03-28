import streamlit as st



def show_overview_page():

  # Adding Background
  page_bg_img = """
  <style>
    [data-testid="stAppViewContainer"] {
      background-image: url("https://jacob-delosangeles.github.io/AI-construction/images/MainBar_bg.png");
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
        
  </style>
  """
   
  st.markdown(page_bg_img, unsafe_allow_html=True)

  st.markdown(
    """
    <style>
    .stImage img {
        max-height: 300 px;  /* Adjust the height */
        width: auto; 
        display: block;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
  
  # Add contents
  st.markdown("<h1 style='text-align: center;'>VelocityAI Inc.</h1>", unsafe_allow_html=True)
  #st.image("https://jacob-delosangeles.github.io/AI-construction/images/LOGO.png")
  st.markdown("<h3 style='text-align: center;'>Building Strength with Data-Driven Intelligence</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: justify;'>At VelocityAI, we are redefining how the construction industry ensures concrete strength. Our AI-powered tool, StrucSure, estimates the compressive strength of concrete with high accuracy, helping engineers and construction firms save time, reduce material waste, and improve quality control. Before conducting concrete mixes, you can get instant predictions using our machine learning model. Helping you make faster, smarter, and cost-efficient decisions in your projects.</h4>", unsafe_allow_html=True)
