import streamlit as st
from datetime import datetime
import requests
import pandas as pd

BACKEND_URL = "http://127.0.0.1:8000"

def analytics_category_tab():
    col1, col2 = st.columns(2)
    with col1: start_date = st.date_input("Start Date", datetime(2024,8,1))
    with col2: end_date = st.date_input("End Date", datetime(2024,8,2))

    if st.button("Get Analytics"):
        dates = {
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{BACKEND_URL}/expenses/analytic_by_category", json=dates)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame.from_dict(data, orient='index')
            sorted_df = df.sort_values(by="percentage", ascending=False)
            st.write(sorted_df)

            st.bar_chart(sorted_df[["percentage"]])
        else:
            st.error(f"Error: {response.status_code}:{response.text}")




