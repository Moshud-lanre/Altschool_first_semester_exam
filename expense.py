from uuid import uuid4
from datetime import datetime

class Expense:
    
    def __init__(self, title:str, amount:float) -> None:
        self.id = str(uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
        

    def update (self, new_title:str=None, new_amount:float=None):
        
        if new_amount != None :
            self.amount = new_amount
        if new_title != None:
            self.title = new_title
        
        self.updated_at = datetime.utcnow()

    def to_dict(self) :
        
        expense = {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }
        
        return expense







class ExpenseDatebase:

    def __init__(self) -> None:
        self.database = []

    def add_expense(self, expense):
        self.database.append(expense)
        return len(self.database)
    
    def remove_expense(self, id):
        self.database = [expense for expense in self.database if expense.id != id ]
        return len(self.database)

    def get_expense_by_id(self, id):
          expense = [x.to_dict() for x in self.database if x.id == id]
          return expense
    
    def get_expense_by_title(self, tilte):
        expense = [x.to_dict() for x in self.database if x.title == tilte]
        return expense
    
    def to_dict(self):
        expenses = [expense.to_dict() for expense in self.database]
        return expenses



