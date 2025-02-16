import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


sidebar = st.sidebar #.selectbox("Explore or Predict", ("Predict", "Explore"))
explore = sidebar.button("Explore")
predict = sidebar.button("Predict")

if explore:
  show_explore_page()

if predict:
  show_predict_page()

else:
  show_explore_page()
  
# show_explore_page()
#if page == "Explore":
  #show_explore_page()
#else:
  #show_predict_page()
