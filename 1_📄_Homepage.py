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

# ---- Navigation with section ----

pg = st.navigation(
  {
    "Home": [home_page],
    "Projects": [strucsure_page]
  }
)

# ----- Run Navigation --------
pg.run()
