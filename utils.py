"""
utils.py

This file contains helper functions used in the project.
"""


# Creating Utility class
class Utility:

    # Constructor
    def __init__(self):

        # Default budget value
        self.monthly_budget = 0

    # Function to set monthly budget
    def set_budget(self):

        # Repeat until correct amount is entered
        while True:

            try:

                # Taking budget from user
                budget = float(input("Enter Monthly Budget : ₹"))

                # Budget should be greater than zero
                if budget <= 0:

                    print("Budget should be greater than zero.")
                    continue

                # Save budget
                self.monthly_budget = budget

                print("Budget Saved Successfully.")

                break

            except ValueError:

                print("Please enter a valid amount.")

    # Function to display current budget
    def show_budget(self):

        print(f"\nMonthly Budget : ₹{self.monthly_budget}")

    # Function to check budget status
    def check_budget(self, total_expense):

        # Display budget first
        print(f"\nBudget : ₹{self.monthly_budget}")

        print(f"Total Expense : ₹{total_expense}")

        # Compare budget and expense
        if total_expense > self.monthly_budget:

            print("Warning! Budget Limit Exceeded.")

        elif total_expense == self.monthly_budget:

            print("You have used your complete budget.")

        else:

            remaining = self.monthly_budget - total_expense

            print(f"Remaining Budget : ₹{remaining}")

    # Function to validate expense id
    def check_expense_id(self, expense_id):

        # Expense ID should be positive
        if expense_id <= 0:

            return False

        return True

    # Function to validate category
    def check_category(self, category):

        # Category should not be empty
        if category.strip() == "":

            return False

        return True

    # Function to validate description
    def check_description(self, description):

        # Description should not be empty
        if description.strip() == "":

            return False

        return True

    # Function to validate recurring expense
    def check_recurring(self, choice):

        # Convert input into lowercase
        choice = choice.lower()

        # Check user choice
        if choice == "yes":

            return True

        elif choice == "no":

            return False

        else:

            print("Please enter Yes or No.")

            return None