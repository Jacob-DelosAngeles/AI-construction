import streamlit as st

# ----- PAGE SETUP -------
home_page = st.Page(
  page = "pages/overview_page.py",
  title="Homepage",
  icon = "📄",
  default=True,
)

strucsure_page = st.Page(
  page = "pages/StrucSure.py",
  title = "StrucSure",
  icon="🏦",

)

algorithms_page = st.Page(
  page = "pages/algorithms.py",
  title = "Machine Learning Algorithms",
  icon = "💻"
)

# ---- Navigation with section ----

pg = st.navigation(
  {
    "Home": [home_page],
    "Projects": [strucsure_page, algorithms_page]
  }
)

# ---- Logo on all Pages ----
st.logo("images/LOGO.png")
st.sidebar.test("Forward Progress. Proper Direction")


# ----- Run Navigation --------
pg.run()
