import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_model():
  with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)
  return data

data = load_model()
regressor = data['model']

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
    background-image: url("https://jacob-delosangeles.github.io/AI-construction/images/backgroundSidebar.jpg");
    background-position: center;
    }
    
  </style>
  """
  st.markdown(page_bg_img, unsafe_allow_html=True)

# Adding Contents
  st.title("🏛️StrucSure\nConcrete's Compressive Strength Intelligent Predictor")
  st.info("""#### Please input information """)
  

# Variables for prediction

  st.subheader('Primary Materials')
  cement = st.number_input("Cement (g)", placeholder = "Type a number")
  courseAggregate = st.number_input("Course Aggregate (g)", placeholder = "Type a number")
  fineAggregate = st.number_input("Fine Aggregate (g)", placeholder = "Type a number")
  water = st.number_input("Water (g)", placeholder = "Type a number")

  st.subheader('Admixtures')
  superplasticizer = st.number_input("Superplasticizer (g)", placeholder = "Type a number")
  slag = st.number_input("Slag (g)", placeholder = "Type a number") 
  flyash = st.number_input("Flyash (g)", placeholder = "Type a number")

  st.subheader('Additional Info')
  age = st.number_input("Age (days)", placeholder = "Type a number")
  waterToCement = st.number_input("Water to Cement Ratio (g)", placeholder = "Type a number")
  
  predict = st.button("Predict Strength")

  if predict:
    X = np.array([[cement, slag, flyash, water, superplasticizer, courseAggregate, fineAggregate, age, waterToCement]])

    # Normalization of Data
    X_norm = (X-data['mu'])/data['sigma']

    strength = regressor.predict(X_norm)
    st.subheader(f"Estimated Strength: {strength[0]:.2f} csMPa")
    
   
  
  



