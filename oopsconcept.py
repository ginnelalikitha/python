#oops cocept
"""class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance")

    def show(self):
        print("Balance:", self.balance)

atm = ATM(5000)
atm.deposit(1000)
atm.withdraw(2000)
atm.show()"""

#Library System
#Book (title, author)
#Library (add book, show books)
"""
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
class Library:
    def __init__(self,filename="books.txt"):
        self.filename=filename
        self.books=[]
        self.load_books()
    def add_book(self,title,author):
        book=Book(title,author)
        self.books.append(book)
        self.save_books(book)
    def save_books(self,book):
        with open(self.filename,"a") as file:
          file.write(f"{book.title},{book.author}\n")
    def load_books(self):
     try:
        with open(self.filename,"r") as file:
            for line in file:
                title,author=line.strip().split(",")
                self.books.append(Book(title,author))
     except FileNotFoundError:
      pass
    def view_books(self):
       if not self.books:
          print("no books found")
          return
       for book in self.books:
          print(f"{book.title}-{book.author}")
    def total_books(self):
       total = len(self.books)
       print(f"Total books:{total}")   

def main():
   system=Library()

   while True:
      print("\n ----LIBRARY SYSTEM-----")
      print("1.Add books")
      print("2.view books")
      print("3.view total")
      print("4.exit")
        
      choice=input("choose an option")
    
      if choice=="1":
         title=input("enter book name:")
         author=input("enter author:")
         system.add_book(title,author)
         print("Books added successfully")
      elif choice=="2":
         system.view_books()
      elif choice=="3":
         system.total_books()
      elif choice=="4":
         print("Goodbye!")
         break
      else:
         print("invalid choice.try again")
main() """



    