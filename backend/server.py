from fastapi import FastAPI
import db_helper
from datetime import date
from pydantic import BaseModel
from typing import List

class Expense(BaseModel):
    amount: int
    category: str
    notes: str

class Dates(BaseModel):
    start_date: date
    end_date: date

app = FastAPI()

# MOVE STATIC ROUTES TO THE TOP
@app.post("/expenses/analytic_by_category")
def analyze_expenses(dates: Dates):
    start_date, end_date = dates.start_date, dates.end_date
    data = db_helper.fetch_expense_summary(start_date, end_date)
    ret = {}
    total = sum([row['total'] for row in data])
    for row in data:
        ret[row['category']] = {
            'total': row['total'],
            'percentage': int(row['total'] / total * 100) if total > 0 else 0
        }
    return ret

@app.get("/expenses/analytic_by_months")
def analyze_expenses_by_months():
    expenses = db_helper.fetch_expense_summary_by_months()
    return expenses

# DYNAMIC PATH WILD CARDS GO BELOW STATIC ROUTES
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses_for_date(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date, expenses : List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "successfully inserted"}

