class Student:
    def __init__(self):
        Name = input("Student Name: ")
        R_Num = input("Student Roll Number: ")

        self.name = Name
        self.rNum = R_Num

        self.MathsMarks = 0
        self.ScienceMarks = 0
        self.EnglishMarks = 0

        print(f"Student Record for {self.name} has been successfully created.")

    def MarksInit(self):
        print("Enter Marks for All Subjects Below:")
        self.MathsMarks = int(input("Enter Maths Marks"))
        if self.MathsMarks>100 or self.MathsMarks<0:
            print("Marks must be between 0 & 100")
            return
        self.ScienceMarks = int(input("Enter Science Marks"))
        if self.ScienceMarks>100 or self.ScienceMarks<0:
            print("Marks must be between 0 & 100")
            return
        self.EnglishMarks = int(input("Enter English Marks"))
        if self.EnglishMarks>100 or self.EnglishMarks<0:
            print("Marks must be between 0 & 100")
            return
        print("Marks are now initialized")

    def ShowDetails(self):
        print("------------------------------")
        print("       Student Details        ")
        print("------------------------------")
        print(f'Name: {self.name}')
        print(f'Roll Number: {self.rNum}')
        print(f'Maths Marks: {self.MathsMarks}')
        print(f'Name: {self.ScienceMarks}')
        print(f'Name: {self.EnglishMarks}')
        print()

    def CalcTot(self):
        total = self.EnglishMarks + self.ScienceMarks + self.MathsMarks
        print("     Student Marks Total     ")
        print("-----------------------------")
        print(f'Total................{total}')
        print()

    def CalcPercent(self):
        percentage = (self.EnglishMarks + self.MathsMarks + self.ScienceMarks) / 3
        print("     Student Marks Percentage     ")
        print("----------------------------------")
        print(f'Percentage.......... {percentage}')
        print()
        return percentage

    def GradePercent(self):
        percentage = self.CalcPercent()
        print("     Student Marks - Letter Grade     ")
        print("--------------------------------------")
        if percentage >= 90:
            Grade = "A+"
        elif percentage >= 80:
            Grade = "A"
        elif percentage >= 70:
            Grade = "B"
        elif percentage >= 60:
            Grade = "C"
        elif percentage >= 50:
            Grade = "D"
        else:
            Grade = "F"
        print(f"Percent: {Grade}")
        return Grade

    def PassFail(self):
        if self.EnglishMarks < 40:
            print("Result: Fail")
            print("Reason: Failed in English.")
        elif self.MathsMarks < 40:
            print("Result: Fail")
            print("Reason: Failed in Maths.")
        elif self.ScienceMarks < 40:
            print("Result: Fail")
            print("Reason: Failed in Science.")
        else:
            print("Result: PASS")

StudentA = Student()
StudentA.MarksInit()
StudentA.ShowDetails()
StudentA.CalcTot()
StudentA.CalcPercent()
StudentA.GradePercent()
StudentA.PassFail()