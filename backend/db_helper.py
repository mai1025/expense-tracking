import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
from logging_setup import get_logger

logger = get_logger(__name__)

# SQL Workflow: 1.Connect => 2.Get Cursor => 3.Execute commands => 4.Commit/Close
@contextmanager
def get_db_cursor():
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='expense_manager'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            yield cursor

        if connection.unread_result is False:
            connection.commit()

    except Error as e:
        print(f"Database error: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# fetch expense for date
def fetch_expenses_for_date(date):
    logger.info(f"Fetch expense for {date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * from expenses WHERE expense_date = %s", (date,))
        expenses = cursor.fetchall()
        return expenses


# delete expense for date
def delete_expense_for_date(date):
    logger.info(f"Delete expense for {date}")
    with get_db_cursor() as cursor:
        cursor.execute("DELETE from expenses WHERE expense_date = %s", (date,))


# insert expense
def insert_expense(date, amount, category, notes):
    logger.info(f"Insert expense for {date} {amount} {category} {notes}")
    with get_db_cursor() as cursor:
        cursor.execute('''INSERT INTO expenses 
                            (expense_date, amount, category, notes)
                            VALUES(%s, %s, %s, %s)''', (date, amount, category, notes))


# fetch sum of expenses by each category
def fetch_expense_summary(start_date, end_date):
    logger.info(f"Fetch expense summary for {start_date} {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT category, SUM(amount) as total
                            FROM expenses WHERE expense_date BETWEEN %s AND %s 
                            GROUP BY category''',
                            (start_date, end_date)
                       )
        expenses = cursor.fetchall()
        return expenses

# fetch sum of expenses by each month
def fetch_expense_summary_by_months():
    logger.info("Fetch expense summary by month")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT DATE_FORMAT(expense_date, '%M') as Month_Name, SUM(amount) as Total
                            FROM expenses
                            GROUP BY DATE_FORMAT(expense_date, '%M'), MONTH(expense_date)
                            ORDER BY MONTH(expense_date)''')
        expenses = cursor.fetchall()
        return expenses

if __name__ == "__main__":
    # expenses = fetch_expenses_for_date("2024-08-01")
    # print(expenses)
    # insert_expense("2025-10-25", 100, "EnteRrtainment", "Birthday party")
    # delete_expense_for_date("2025-10-25")
    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for row in summary:
        print(row)