# Student - Entity
#
# name, roll_number, marks
# attributes
#
# display_details
# calculate_total
# calculate_percentage
# calculate_grade
# check_result
# update_marks


class Student:

    def __init__(self):
        name = input("Enter Student Name: ")
        roll_number = input("Enter Roll Number: ")

        self.name = name
        self.roll_number = roll_number

        self.maths = 0
        self.science = 0
        self.english = 0

        print("\nHello", self.name)
        print("Student record has been created successfully.")

    def enter_marks(self):

        print("\n========= Enter Marks =========")

        self.maths = int(input("Enter Maths Marks: "))
        self.science = int(input("Enter Science Marks: "))
        self.english = int(input("Enter English Marks: "))

        if self.maths < 0 or self.maths > 100:
            print("Error: Maths marks should be between 0 and 100.")
            return

        if self.science < 0 or self.science > 100:
            print("Error: Science marks should be between 0 and 100.")
            return

        if self.english < 0 or self.english > 100:
            print("Error: English marks should be between 0 and 100.")
            return

        print("Marks entered successfully.")

    def display_details(self):

        print("\n========= Student Details =========")

        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)

        print("Maths:", self.maths)
        print("Science:", self.science)
        print("English:", self.english)

    def calculate_total(self):

        total = self.maths + self.science + self.english

        print("Total Marks:", total)

        return total

    def calculate_percentage(self):

        total = self.maths + self.science + self.english

        percentage = total / 3

        print("Percentage:", percentage)

        return percentage

    def calculate_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            grade = "A+"

        elif percentage >= 80:
            grade = "A"

        elif percentage >= 70:
            grade = "B"

        elif percentage >= 60:
            grade = "C"

        elif percentage >= 50:
            grade = "D"

        else:
            grade = "F"

        print("Grade:", grade)

        return grade

    def check_result(self):

        if self.maths < 40:
            print("Result: FAIL")
            print("Reason: Failed in Maths")
            return

        if self.science < 40:
            print("Result: FAIL")
            print("Reason: Failed in Science")
            return

        if self.english < 40:
            print("Result: FAIL")
            print("Reason: Failed in English")
            return

        print("Result: PASS")


# Creating Student Object

student1 = Student()

student1.enter_marks()

student1.display_details()

student1.calculate_total()

student1.calculate_percentage()

student1.calculate_grade()

student1.check_result()