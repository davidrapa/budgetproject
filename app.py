from __future__ import absolute_import

import budgetproject

from budgetproject.models import Income, Expense
from budgetproject.views import income_view, expense_view, reports_view

app = Flask(__name__)

app.register_blueprint(income_view)
app.register_blueprint(expense_view)
app.register_blueprint(reports_view)

if __name__ == "__main__":
    app.run(debug=True)