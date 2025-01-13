from datetime import datetime

class Book:
    def __init__(self, title):
        self.title = title
        self.borrower = None
        self.due_date = None
    
    def borrow(self, name, date):
        self.borrower = name
        self.due_date = datetime.strptime(date, "%Y-%m-%d")  
        print(f"{self.title} kitobi {self.borrower} tomonidan qarzga olindi. Qaytarish muddati: {self.due_date.strftime('%Y-%m-%d')}.")

    def return_book(self):
        if self.borrower is None:
            print("Bu kitob qarzga olinmagan.")
        else:
            today = datetime.today()
            if today > self.due_date:
                print("Jazo qullaniladi!")
            else:
                print(f"{self.title} kitobi {self.borrower} tomonidan uz vaqtida qaytarildi.")
            self.borrower = None
            self.due_date = None

book1 = Book("Python Dasturlash")
book1.borrow("John", "2025-01-15") 
book1.return_book() 
