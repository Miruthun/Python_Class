# ============================================================
# 5. HYBRID INHERITANCE
# Combination of Two or More Types of Inheritance
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Employee(Person):

    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def work(self):
        print(self.name, "is working")


class Manager(Person):

    def manage(self):
        print(self.name, "is managing the team")


class Developer(Employee):

    def code(self):
        print(self.name, "is writing code")


class TechLead(Developer, Manager):

    def lead(self):
        print(self.name, "is leading the development team")


tech_lead = TechLead("Arvinder", 101)

print("\nName:", tech_lead.name)
print("Employee ID:", tech_lead.employee_id)

tech_lead.introduce()    # From Person
tech_lead.work()         # From Employee
tech_lead.code()         # From Developer
tech_lead.manage()       # From Manager
tech_lead.lead()         # From TechLead