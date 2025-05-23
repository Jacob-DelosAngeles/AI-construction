import streamlit as st
import pickle
import keras
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler



# Loading the Model - Linear Regression
def load_model():
  with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)
  return data

data = load_model()
regressor = data['model']

# Loading the Model - Neural Network
def load_nn_model(filename='model.pkl'):
  with open(filename, 'rb') as file:
    model = pickle.load(file)
  return model

model = load_nn_model('500_250_100_50_1_ComplexNN.pk')

# Checking if the Input values are within the range

minimum = [102, 0, 0, 121.8, 0, 801, 594, 1, 0.2669]
maximum = [540, 359.4, 195, 247, 32.2, 1145, 992.6, 365, 1.8824]








# Showing the Page
def show_predict_page():
  
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

  

# Adding Contents
  st.markdown("<h1 style='text-align: center;'>StrucSure</h1>", unsafe_allow_html=True)
  st.write("<div style='text-align:center;'>Concrete's Compressive Strength Intelligent Predictor</div>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center;'>Please input information</h3>", unsafe_allow_html=True)
  #st.subheader("Please Input Information", divider = "red
  st.markdown("<div style='border-top: 3px solid black; margin-top: 10px; margin-bottom: 10px;'></div>", unsafe_allow_html=True)

  
  

# Variables for prediction

  st.subheader('Primary Materials')
  cement = st.number_input("Cement (g)", min_value = 102.0, max_value = 540.0, step = 1.0, help="Enter a value between 102 and 540 grams")
  courseAggregate = st.number_input("Course Aggregate (g)", min_value = 801.0, max_value = 1145.0, step = 1.0,  help="Enter a value between 801 and 1145 grams")
  fineAggregate = st.number_input("Fine Aggregate (g)", min_value = 594.0, max_value = 992.6, step = 1.0, help="Enter a value between 594 and 992.6 grams")
  water = st.number_input("Water (g)", min_value = 121.8, max_value = 247.0, step = 1.0, help="Enter a value between 121.8 and 247 grams")

  st.subheader('Admixtures')
  superplasticizer = st.number_input("Superplasticizer (g)", min_value = 0.0, max_value = 32.2, step = 1.0, help="Enter a value between 0 and 32.2 grams")
  slag = st.number_input("Slag (g)", min_value = 0.0, max_value = 359.4, step = 1.0, help="Enter a value between 0 and 359.4 grams") 
  flyash = st.number_input("Flyash (g)", min_value = 0.0, max_value = 195.0, step = 1.0, help="Enter a value between 0 and 195 grams")

  st.subheader('Additional Info')
  age = st.number_input("Age (days)", min_value = 1.0, max_value = 365.0, step = 1.0, help="Enter a value between 1 and 365 days")
  waterToCement = water / cement
  
  
  predict = st.button("Predict Strength")

  
  # If Predict button is clicked
  if predict:

    X = np.array([[cement, slag, flyash, water, superplasticizer, courseAggregate, fineAggregate, age, waterToCement]])
    
    # Normalization of Data
    X_norm = (X - data['mu'])/data['sigma']
  
    strength = model.predict(X_norm)    # model- neural network, regressor - linear regression
    st.subheader(f"Estimated Strength: {(strength[0][0]):.2f} csMPa")  
    
show_predict_page()
    
   
  
  



