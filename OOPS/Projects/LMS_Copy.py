class Book:
    def __init__(self):
        Title = input("Please Enter Book's Title:")
        Author = input("Please Enter Book's Author:")
        ID = input("Please Enter Book's ID:")
        IssueStatus = False

        self.title = Title
        self.author = Author
        self.id = ID
        self.Is = IssueStatus

        print("===================================")
        print("Book Successfully Entered in System")
        print("===================================")
        print()

    def ShowDetails(self):
        print("===================================")
        print("           Book Details            ")
        print("-----------------------------------")
        print()
        print(f'Book Title: {self.title}')
        print(f'Book Author: {self.author}')
        print(f'Book ID: {self.id}')
        print(f'Book Issue Status: {self.Is}')
        print()
        print("-----------------------------------")
        print()

    def ShowStatus(self):
        converter = ""
        if self.Is == False:
            converter = "Available"
        else:
            converter = "Checked Out"
        print("===================================")
        print("            Book Status            ")
        print("===================================")
        print()
        print(f'Book Issue Status:{converter}')
        print()
        print("-----------------------------------")
        print()

    def IssueBook(self):
        if not self.Is:
            self.Is = True
            print("Book Successfully Issued:")
            print(f'    Book Issued:{self.title}')
            print(f'    Book Author:{self.author}')
            print(f'    Book ID:{self.id}')
            print()
        else:
            print("Book is already issued. Please come again another time.")
            print()
    
    def returnBook(self):
        if self.Is:
            self.Is = False
            print("Book Successfully Returned:")
            print(f'    Book Issued:{self.title}')
            print(f'    Book Author:{self.author}')
            print(f'    Book ID:{self.id}')
            print()
        else:
            print("This Book has not been issued. Unable to return non-issued book.")
            print()

Book1 = Book()

Book1.ShowDetails()

Book1.ShowStatus()

Book1.IssueBook()

Book1.ShowStatus()

Book1.IssueBook()

Book1.returnBook()

Book1.ShowStatus()