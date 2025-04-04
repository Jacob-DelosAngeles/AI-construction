import streamlit as st
from overview_page import show_overview_page
#from st_pages import Page, Section, show_pages, add_page_title, hide_pages

show_overview_page()

# # Initialize session state
# if "page" not in st.session_state:
#   st.session_state.page = "Overview"  # Default page

# # Sidebar buttons
# st.sidebar.title("🔹Main Menu")
# if st.sidebar.button("🌍 Overview  "):
#   st.session_state.page = "Overview"

# if st.sidebar.button("✅ Predict  "):
#   st.session_state.page = "Predict"

# # Display the selected page
# if st.session_state.page == "Overview":
#   show_overview_page()
# elif st.session_state.page == "Predict":
#   show_predict_page()
