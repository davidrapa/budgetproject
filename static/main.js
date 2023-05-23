/* main.js */

$(function() {
  // Add event listener to the "Add Income" button.
  $("#add-income-button").on("click", function() {
    // Redirect to the income page.
    window.location.href = "/income";
  });

  // Add event listener to the "Income History" button.
  $("#income-history-button").on("click", function() {
    // Redirect to the income history page.
    window.location.href = "/income/history";
  });

  // Add event listener to the "Add Expense" button.
  $("#add-expense-button").on("click", function() {
    // Redirect to the expense page.
    window.location.href = "/expenses";
  });

  // Add event listener to the "Expense History" button.
  $("#expense-history-button").on("click", function() {
    // Redirect to the expense history page.
    window.location.href = "/expenses/history";
  });

  // Add event listener to the "Income Report" button.
  $("#income-report-button").on("click", function() {
    // Redirect to the income report page.
    window.location.href = "/reports/income";
  });

  // Add event listener to the "Expense Report" button.
  $("#expense-report-button").on("click", function() {
    // Redirect to the expense report page.
    window.location.href = "/reports/expenses";
  });

  // Add event listener to the "Budget Report" button.
  $("#budget-report-button").on("click", function() {
    // Redirect to the budget report page.
    window.location.href = "/reports/budget";
  });
});
