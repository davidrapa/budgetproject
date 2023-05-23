from __future__ import absolute_import

from flask import render_template
from models import Income, Expense

@app.route("/")
def index():
    incomes = Income.query.all()
    expenses = Expense.query.all()
    return render_template("index.html", incomes=incomes, expenses=expenses)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/add_income")
def add_income():
    return render_template("add_income.html")

@app.route("/add_expense")
def add_expense():
    return render_template("add_expense.html")

@app.route("/view_reports")
def view_reports():
    reports = []
    for income in Income.query.all():
        reports.append({
            "date": income.date,
            "income": income.amount,
            "expenses": sum([expense.amount for expense in Expense.query.filter_by(date=income.date)]),
            "balance": income.amount - sum([expense.amount for expense in Expense.query.filter_by(date=income.date)])
        })
    return render_template("view_reports.html", reports=reports)