import streamlit as st
import pickle
import numpy as np

def load_model():
  with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)
  return data

data = load_model()
regressor = data['model']

def show_predict_page():
  st.title(" 🏛️StrucSure: Concrete's Compressive Strength Intelligent Predictor")
  st.info("""#### Please input information """)

# Variables for prediction

cement = st.number_input("Cement (g)", placeholder = "Type a number")
slag = st.number_input("Slag (g)", placeholder = "Type a number") 
flyash = st.number_input("Flyash (g)", placeholder = "Type a number")
water = st.number_input("Water (g)", placeholder = "Type a number")
superplasticizer = st.number_input("Superplasticizer (g)", placeholder = "Type a number")
courseAggregate = st.number_input("Course Aggregate (g)", placeholder = "Type a number")
fineAggregate = st.number_input("Fine Aggregate (g)", placeholder = "Type a number")
waterToCement = st.number_input("Water to Cement Ratio (g)", placeholder = "Type a number")

predict = st.button("Predict Strength")

  
  



