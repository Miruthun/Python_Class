import BookingRecord as BR
import BookingConfirmation as BC
import View as V
import Search as S
import Cancel as C
import Export as E
import Revenue as R
import ValidationChecks as VC

# My Main Menu Function
def Menu():
    while True:
        menu = {
            '1': "Book Cart",
            '2': "View Bookings",
            '3': "Search Bookings",
            '4': "Cancel Bookings",
            '5': "Export Bookings",
            '6': "Revenue Report",
            '7': "Exit"
        }
        for key, value in menu.items():
            print(f'{key}: {value}')
        menu_select = VC.name_check("Please choose a number to continue: ", menu)
        if menu_select == "1":
            start = BR.Bookings_Record()
            BC.BookCnf(start)
        elif menu_select == "2":
            V.View_Books()
        elif menu_select == "3":
            S.Search()
        elif menu_select == "4":
            C.cancelBook()
        elif menu_select == "5":
            E.export()
        elif menu_select == "6":
            R.rev()
        elif menu_select == "7":
            print("Thank you for choosing us!")
            break
        
if __name__ == "__main__":
    Menu()