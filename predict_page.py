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
  st.title("Concrete's Compressive Strength Intelligent Predictor")

  st.write("""### Please input information """)
  
  st.sidebar.selectbox("Explore or Predict", ("Predict, Explore"))



