# Expense Management System
This project is expense management system that consists of a Streamlit frontend application and FastAPI backend server.
The data is saved using mySQL. 
User can add, update, delete their expenses and show summary by category or month.

## Project Structure

- **frontend/**: Contains the Streamlit application code
- **backend/**: Contains the FastAPI backend server, mySQL database & logger to track activities
- **tests/**: Contains test cased for both frontend and backend
- **requirements.txt**: Lists of required Python package

## Setup Instructions

1. **Clone the repository:**
    ```bash
   git clone https://github.com/mai1025/expense-tracking.git
   cd expense-tracking
   ```

2. **Install dependencies:**
    ```commandline
   pip install -r requirements.txt
   ```
   
3. **Run the FastAPI server:**
    ```commandline
   uvicorn server.server:app --reload
   ```

4. **Run the Streamlit app:**
    ```commandline
   streamlit run frontend/app.py
   ```
   