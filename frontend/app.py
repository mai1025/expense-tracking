import streamlit as st
from app_update_ui import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab

# FastAPI backendURL
BACKEND_URL = "http://127.0.0.1:8000"

st.title("Expense Tracking System")

categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

tab1, tab2, tab3 = st.tabs(["Add / Update", "Analytics By Category", "Analytics By Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()





