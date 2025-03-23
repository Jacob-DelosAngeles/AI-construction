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

    /* Sidebar Main Container */
    [data-testid="stSidebar"] {
        background-color: #1E1E1E; /* Dark background */
        padding: 15px;
    }

    /* Sidebar Card Container */
    .sidebar-card {
        background: white;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    /* Sidebar Title */
    .sidebar-title {
        font-size: 18px;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Button Styling */
    .sidebar-btn {
        background: #17A2B8; /* Teal Color */
        color: white;
        padding: 10px;
        text-align: center;
        border-radius: 6px;
        font-size: 16px;
        font-weight: bold;
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: 0.3s;
    }

    .sidebar-btn:hover {
        background: #138496;
    }

    .active-btn {
        background: #28A745; /* Green for Active */
    }

    /* About Section */
    .sidebar-about {
        background: #DCE3F5;
        padding: 10px;
        border-radius: 8px;
        margin-top: 20px;
        text-align: center;
    }

    /* Footer */
    .sidebar-footer {
        font-size: 14px;
        text-align: center;
        margin-top: 10px;
    }
  </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Card UI
st.sidebar.markdown(
    """
    <div class="sidebar-card">
        <div class="sidebar-title">📜 Main Menu</div>

        <a href="#" class="sidebar-btn active-btn">🌍 Explore</a>
        <a href="#" class="sidebar-btn">✅ Predict</a>
    </div>

    <div class="sidebar-about">
        🌍 <a href="https://eo-cdt.org" target="_blank">https://eo-cdt.org</a>
    </div>

    <div class="sidebar-footer">© 2022 SatSchool</div>
    """,
    unsafe_allow_html=True
)

    
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
  #st.title("🏛️StrucSure")
  st.markdown("<h1 style='text-align: center;'>Strucsure</h1>", unsafe_allow_html=True)
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
    
   
  
  



