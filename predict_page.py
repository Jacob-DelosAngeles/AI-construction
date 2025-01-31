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
  st.title("🏛️StrucSure\nConcrete's Compressive Strength Intelligent Predictor")
  st.info("""#### Please input information """)

# Variables for prediction

  cement = st.number_input("Cement (g)", placeholder = "Type a number")
  slag = st.number_input("Slag (g)", placeholder = "Type a number") 
  flyash = st.number_input("Flyash (g)", placeholder = "Type a number")
  water = st.number_input("Water (g)", placeholder = "Type a number")
  superplasticizer = st.number_input("Superplasticizer (g)", placeholder = "Type a number")
  courseAggregate = st.number_input("Course Aggregate (g)", placeholder = "Type a number")
  fineAggregate = st.number_input("Fine Aggregate (g)", placeholder = "Type a number")
  age = st.number_input("Age (days)" = "Type a number")
  waterToCement = st.number_input("Water to Cement Ratio (g)", placeholder = "Type a number")
  
  predict = st.button("Predict Strength")

  if predict:
    X = np.array([[cement, slag, flyash, water, superplasticizer, courseAggregate, fineAggregate, waterToCement]])

    # TO DO: normalize the values first
    # Get the mean and standard deviation values
    # Confirm if standard deviation nga ba gamit sa normalization
    # (X - mu)/sigma formula to normalize 

    # show mu and sigma
    st.write(f"mu: {data['mu']}")
    st.write(f"sigma: {data['sigma']}")
    
    
    strength = regressor.predict(X)
    st.subheader(f"Estimated Strength: {strength:.2f} csMPa")
    

  
  



