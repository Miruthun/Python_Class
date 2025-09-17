# Name -- input --> "Arvinder" ,12345 , -12876niaufalufuuh 

# Calculator -- Division --> 5 // 3 , -6 // 3 , 56 // 0 


# try -- Try this code block -- I will write my code that i want to execute inside try block.

# except -- It will run if try throws an error 

# finally -- This is something which will execute in both scenarios means whether there is an error or not.

# if True:
#     print(x)
# else:
#     print("We are here in Else")

# try:
#     print("print")
# except:
#     print("Not able to print")

# finally: 
#     print("I tried")

# Why do we need finally ?
#  Finally is used to perform Graceful exit tasks :

def Division(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero") 
    except TypeError:
        print("Only numbers can be divided")
    else:
        print("Result :" ,result)

    finally:
        print("Code Completed.")


# Division(30,6)
# Division(24,-5)
# Division("Hello",4)
Division(10,0)