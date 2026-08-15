# LibraryBook - Entity
#
# title, author, book_id, is_issued
# attributes
#
# issue_book, return_book, display_details, check_status


class LibraryBook:

    def __init__(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        book_id = input("Enter Book ID: ")

        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_issued = False

        print("Book has been successfully added to the library.")

    def display_details(self):
        print("\n========= Book Details =========")
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Book ID:", self.book_id)

        if self.is_issued:
            print("Status: Issued")
        else:
            print("Status: Available")

    def check_status(self):
        if self.is_issued:
            print("Book Status: Currently Issued")
        else:
            print("Book Status: Available")

    def issue_book(self):

        if self.is_issued:
            print("Error: This book is already issued.")
            return

        self.is_issued = True

        print("Book issued successfully.")
        print("Book:", self.title)

    def return_book(self):

        if not self.is_issued:
            print("Error: This book was not issued.")
            return

        self.is_issued = False

        print("Book returned successfully.")
        print("Book:", self.title)


# Creating Object

book1 = LibraryBook()

book1.display_details()

book1.check_status()

book1.issue_book()

book1.check_status()

book1.issue_book()

book1.return_book()

book1.check_status()