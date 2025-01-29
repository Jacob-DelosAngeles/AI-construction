import streamlit as st
from predict_page import show_predict_page

# st.title('🏗️ Velocity AI')
# st.info('Forward Progress. Proper Direction')

st.sidebar.selectbox("Explore or Predict", ("Predict, Explore"))
show_predict_page()
