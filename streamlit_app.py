import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page



# Initialize session state
if "page" not in st.session_state:
  st.session_state.page = "Explore"  # Default page

# Sidebar buttons
st.sidebar.title("🔹 StrucSure")
if st.sidebar.button("🌍 Explore  "):
  st.session_state.page = "Explore"

if st.sidebar.button("✅ Predict  "):
  st.session_state.page = "Predict"

# Display the selected page
if st.session_state.page == "Explore":
  show_explore_page()
elif st.session_state.page == "Predict":
  show_predict_page()
