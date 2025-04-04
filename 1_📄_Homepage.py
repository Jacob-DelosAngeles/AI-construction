import streamlit as st

# ----- PAGE SETUP -------
home_page = st.Page(
  page = "page/overview_page.py",
  title="Homepage",
  icon = "📄",
  default=True,
)

strucsure_page = st.Page(
  page = "page/StrucSure.py",
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
