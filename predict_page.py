import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


# Loading the Model
def load_model():
  with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)
  return data

data = load_model()
regressor = data['model']




# Checking if the Input values are within the range

minimum = [102, 0, 0, 121.8, 0, 801, 594, 1, 0.2669]
maximum = [540, 359.4, 195, 247, 32.2, 1145, 992.6, 365, 1.8824]
def is_within_range(X_numpy_features, minimum, maximum):
    """"
    X_numpy_features: 2D array of integers from the user
    minimum: List of minimum Values
    maximum: List of Maximum Values
    """

    # Truth List
    features = ['cement', 'slag', 'flyash', 'water', 'superplasticizer', 'course aggregate', 'fine aggregate', 'age', 'water to cement ratio']
    errors = []
    changeFeatures = []
    
    for i in range(len(X_numpy_features[0])):
        if minimum[i] <= X_numpy_features[0][i] <= maximum[i]:
            errors.append(True)
        else:
            errors.append(False)
    
    for e in range(len(errors)):
        if errors[e] == True:
            continue
        else:
            changeFeatures.append(features[e])

    return changeFeatures







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
    
  </style>
  """
  st.markdown(page_bg_img, unsafe_allow_html=True)

  # Pending sidebar background
  """
  [data-testid="stSidebar"]{
    background-image: url("https://jacob-delosangeles.github.io/AI-construction/images/backgroundSidebar_1.jpg");
    background-position: center;
    }
  """

# Adding Contents
  st.title("🏛️StrucSure\nConcrete's Compressive Strength Intelligent Predictor")
  st.subheader("Please Input Information", divider = "grey")
  

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

    # Check if each data is within the range of minimum and maximum values

    data_values = is_within_range(X, minimum, maximum)

    if not data_values:
      # Normalization of Data
      X_norm = (X - data['mu'])/data['sigma']
  
      strength = regressor.predict(X_norm)
      st.subheader(f"Estimated Strength: {strength[0]:.2f} csMPa")

    else:
      for i in range(len(data_values)):
        st.subheader(f"Please check value of {data_values[i]}")
    
   
  
  



