import streamlit as st
from datetime import datetime
import requests

# FastAPI backendURL
BACKEND_URL = "http://127.0.0.1:8000"

def add_update_tab():
    selected_date = st.date_input("Select Date", datetime(2024,8,1))

    # Make the GET request to FastAPI
    response = requests.get(f"{BACKEND_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
        # st.write(existing_expenses)
    else:
        st.error("Failed to connect to backend server")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    # Initialize the form container using a 'with' block
    with st.form(key=f"expenses_form{selected_date}") as form:
        h_col1, h_col2, h_col3 = st.columns(3)
        h_col1.markdown("Amount")
        h_col2.markdown("Category")
        h_col3.markdown("Note")

        updated_expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = float(existing_expenses[i]["amount"])
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Rent"
                notes = ""


            col1, col2, col3 = st.columns(3)
            with col1:
                updated_amount = st.number_input(label="Amount", min_value=0.0, value=amount, step=1.0, key=f"amount{selected_date}{i}")
            with col2:
                updated_category = st.selectbox(label="Category", options=categories, index=categories.index(category), key=f"category{selected_date}{i}")
            with col3:
                updated_note = st.text_input(label="Note", value=notes, key=f"notes{selected_date}{i}")

            if updated_amount != 0.0:
                updated_expenses.append(
                    {
                        'amount': updated_amount,
                        'category': updated_category,
                        'notes': updated_note
                    })

        # EVERY form MUST have exactly one submit button
        if st.form_submit_button(label="Submit"):
            # st.write(updated_expenses)
            response = requests.post(f"{BACKEND_URL}/expenses/{selected_date}", json=updated_expenses)
            if response.status_code == 200:
                st.success("Successfully updated!")
            else:
                st.error("Failed to update")







