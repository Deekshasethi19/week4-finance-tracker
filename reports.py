"""
reports.py

This file is used to generate different reports.
"""

# Importing required module
from collections import defaultdict


# Creating ReportGenerator class
class ReportGenerator:

    # Constructor
    def __init__(self, expense_list):

        # Store all expenses
        self.expense_list = expense_list

    # Function to calculate total expense
    def get_total_expense(self):

        # Variable to store total amount
        total = 0

        # Adding amount of every expense
        for expense in self.expense_list:

            total = total + expense.amount

        # Return total expense
        return total

    # Function to find highest expense
    def highest_expense(self):

        # Check whether list is empty
        if len(self.expense_list) == 0:

            print("No expense found.")
            return

        # Assume first expense is highest
        highest = self.expense_list[0]

        # Compare with every expense
        for expense in self.expense_list:

            if expense.amount > highest.amount:

                highest = expense

        return highest

    # Function to find lowest expense
    def lowest_expense(self):

        # Check whether list is empty
        if len(self.expense_list) == 0:

            print("No expense found.")
            return

        # Assume first expense is lowest
        lowest = self.expense_list[0]

        # Compare with every expense
        for expense in self.expense_list:

            if expense.amount < lowest.amount:

                lowest = expense

        return lowest

    # Function to calculate average expense
    def average_expense(self):

        # Check whether list is empty
        if len(self.expense_list) == 0:

            return 0

        # Calculate average
        average = self.get_total_expense() / len(self.expense_list)

        return average

    # Function to generate category wise report
    def category_report(self):

        # Dictionary to store category totals
        category_data = defaultdict(float)

        # Add amount according to category
        for expense in self.expense_list:

            category_data[expense.category] += expense.amount

        # Display report
        print("\n------ Category Wise Report ------\n")

        for category, amount in category_data.items():

            print(f"{category} : ₹{amount}")
        # Function to generate monthly report
    def monthly_report(self):

        # Dictionary to store month wise expenses
        monthly_data = defaultdict(float)

        # Loop through every expense
        for expense in self.expense_list:

            # Extract month from date
            month = expense.date[:7]

            # Add amount according to month
            monthly_data[month] += expense.amount

        # Check if there is any data
        if len(monthly_data) == 0:

            print("\nNo Expense Found.\n")
            return

        # Display monthly report
        print("\n------ Monthly Report ------\n")

        for month, amount in monthly_data.items():

            print(f"{month} : ₹{amount}")

    # Function to display monthly spending trend
    def monthly_trend(self):

        # Dictionary to store monthly expenses
        monthly_data = defaultdict(float)

        # Store amount month wise
        for expense in self.expense_list:

            month = expense.date[:7]

            monthly_data[month] += expense.amount

        # Check whether data is available
        if len(monthly_data) == 0:

            print("\nNo Expense Found.\n")
            return

        print("\n------ Monthly Spending Trend ------\n")

        # Display month wise amount
        for month, amount in monthly_data.items():

            print(f"{month} : ₹{amount}")

    # Function to display text based visualization
    def show_chart(self):

        # Dictionary to store category totals
        category_data = defaultdict(float)

        # Calculate category wise expense
        for expense in self.expense_list:

            category_data[expense.category] += expense.amount

        # Check whether list is empty
        if len(category_data) == 0:

            print("\nNo Expense Found.\n")
            return

        print("\n------ Expense Chart ------\n")

        # Display stars according to amount
        for category, amount in category_data.items():

            stars = "*" * max(1, int(amount / 100))

            print(f"{category:15} {stars} ₹{amount}")

    # Function to display expense statistics
    def expense_statistics(self):

        # Check whether list is empty
        if len(self.expense_list) == 0:

            print("\nNo Expense Found.\n")
            return

        print("\n========== Expense Statistics ==========\n")

        # Display total expense
        print("Total Expense :", self.get_total_expense())

        # Display average expense
        print("Average Expense :", round(self.average_expense(), 2))

        # Find highest expense
        highest = self.highest_expense()

        # Find lowest expense
        lowest = self.lowest_expense()

        # Display highest expense
        print("\nHighest Expense")

        print(highest)

        # Display lowest expense
        print("\nLowest Expense")

        print(lowest)    