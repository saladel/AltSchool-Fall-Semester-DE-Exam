import uuid
from datetime import datetime

"""
Expense Class:
Represents an individual financial expense.

Attributes:
1. id: A unique identifier generated as a UUID string.
2. title: A string representing the title of the expense.
3. amount: A float representing the amount of the expense.
4. created_at: A timestamp indicating when the expense was created (UTC).
5. updated_at: A timestamp indicating the last time the expense was updated (UTC).

Methods:
1. __init__: Initializes the attributes.
2. update: Allows updating the title and/or amount, updating the updated_at timestamp.
3. to_dict: Returns a dictionary representation of the expense.

ExpenseDB class
Manages a collection of Expense objects.
Attributes:
1. expenses: A list storing Expense instances.

Methods:
1. __init__: Initializes the list.
2. add_expense: Adds an expense.
3. remove_expense: Removes an expense.
4. get_expense_by_id: Retrieves an expense by ID.
5. get_expense_by_title: Retrieves expenses by title.
6. to_dict: Returns a list of dictionaries representing expenses.

"""
# Expense class
class Expense:
    # 1. an __init__ method to initialize the attributes.
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    # 2. an update method that allows updating the title and/or amount of the expense.
    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    # 3. to_dict method that returns a dictionary representation of an instance to the Expense class.
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(" "),
            "updated_at": self.updated_at.isoformat(" ")
        }

# Expense Database class
class ExpenseDataBase:
    # an __init__ method to initialize the expenses list.
    def __init__(self):
        self.expenses = []

    # Adds an expense to the database.
    def add_expense(self, expense):
        self.expenses.append(expense)

    # Removes an expense from the database.
    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, expense_title):
        # returns a list of expenses
        return [expense for expense in self.expenses if expense.title == expense_title]
    
    # returns a list of dictionaries representing each expense in the database.
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]



# Example usage:

# create new expense database object
expense_db = ExpenseDataBase()

# create new expense object
expense1 = Expense("Internet Sub", 12800)
expense2 = Expense("Transport", 25000)

# add expenses to expense_db
expense_db.add_expense(expense1)
expense_db.add_expense(expense2)

print("These are your expenses:", expense_db.to_dict())


expense_db.remove_expense(expense1.id)
print("This is your updated expenses:", expense_db.to_dict())