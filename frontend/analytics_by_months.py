import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://127.0.0.1:8000"

def analytics_months_tab():
    st.title("Expense Breakdown By Months")

    try:
        response = requests.get(f"{BACKEND_URL}/expenses/analytic_by_months")
        response.raise_for_status()

        expenses = response.json()

        st.write(expenses)

        # Convert the list of dicts directly to a DataFrame(a table with rows and columns)
        df = pd.DataFrame(expenses)

        # Set 'Month_Name' as the index
        # This moves the months out of the columns and turns them into row labels
        df_graph = df.set_index("Month_Name")
        # Graph the 'Total' column
        # Streamlit will automatically use the index ('Month_Name') for the X-axis
        st.bar_chart(df_graph["Total"])

        # Optional: write out the table to inspect
        st.write(df_graph)
        st.write(df)

    except requests.exceptions.HTTPError as err:
        st.write(f"HTTP error: {err}")
    except Exception as err:
        st.write(f"Other error: {err}")




