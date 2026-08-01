# SMS - School Management System

# Principal - TakingCare - operations , Management 
# Teacher - TeachSubject , ViewStudentMarks , GradeStudent, TakeExams
# Student - canJOinAClass , CanJOinAGroup , CanViewMarks, CanViewTeacher

# Principal - ID , role , Name , Exp , Gender , City 
# Teacher - ID , name , class , subject, students 
# Student - ID , name , roll num , class , group , subject

# Non-teaching Staff - id, role , name , city , time 
# Room - id, how many benches are there , color , window , do we digital board , AC , 
# gates 

# schoolBus - 

# House - type  - 2bhk , 3bhk , 
# window per room , facing - east , south 
# floors - 

# room - 

# cart Booking System - 
# dept , cart , drivers , employee 

# class Student:
#     def __init__(self):
#         # create variables 
#         self.name = "Miruthun"
    
#     def PrintDetails(self):
#         print("My Name is :",self.name)

# student1 = Student()
# student1.PrintDetails()



# class Student:
#     def __init__(self,name):
#         # create variables 
#         self.name = name
    
#     def PrintDetails(self):
#         print("My Name is :",self.name)

# student1 = Student("Miruthun")
# student1.PrintDetails()



# class Student:
#     def __init__(self,name, age):
#         # create variables 
#         self.name = name
#         self.age = age
    
#     def PrintDetails(self):
#         print("My Name is :",self.name," and I am ",self.age, "years old")

# student1 = Student("Miruthun",24)
# student2 = Student("Arvinder",30)
# student2.PrintDetails()
# print(id(student2),id(student1))
# student1.PrintDetails()
# print(student1.age)



class SMS:
    def __init__(self, role,name,city):
        self.role = role
        self.name  = name 
        self.city = city
    
    def Introduction(self):
        print("My name is ",self.name,"I am from ",self.city," and I am a ",self.role,".")

    def UpdateCityDetails(self,newCityName):
        self.city = newCityName
    
    def UpdateRoleDetails(self,newRole):
        self.role = newRole
    

teacher = SMS("Teacher","Adam","Paris")
teacher.Introduction()
teacher.UpdateCityDetails("London")
teacher.Introduction()
teacher.UpdateRoleDetails("Head of Department")
teacher.Introduction()

principal = SMS("Principal","Smitha","UK")
principal.Introduction()







