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
  st.info("""#### Please input information """)
  

# Variables for prediction

  st.subheader('Primary Materials')
  cement = st.number_input("Cement (g)", min_value = 102, max_value = 540, step = 1, help="Enter a value between 100 and 600 grams")
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
    
   
  
  



