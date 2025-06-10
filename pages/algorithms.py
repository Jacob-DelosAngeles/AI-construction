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

def show_machine_learning():

  st.markdown('<h1>Machine Learning Process</h1>', unsafe_allow_html=True)

  st.markdown("""
  <p>This section outlines the steps taken to develop the AI model used in <strong>StrucSure</strong>, from data collection to model deployment.</p>

  <h3><u>Steps Followed:</u></h3>
  <ol>
    <li><strong>Data Collection</strong><br>We sourced a concrete compressive strength dataset from <a href="https://www.kaggle.com/datasets">Kaggle</a>.</li>
    <li><strong>Feature Engineering</strong><br>We cleaned the data, handled missing values, normalized features, and split the dataset into training and testing sets.</li>
    <li><strong>Model Development</strong><br>An Artificial Neural Network (ANN) model was implemented using TensorFlow/Keras to predict compressive strength.</li>
    <li><strong>Training & Evaluation</strong><br>The model was trained, evaluated using metrics like MAE and RMSE, and tuned for optimal performance.</li>
  </ol>
  """, unsafe_allow_html=True)


show_machine_learning()
