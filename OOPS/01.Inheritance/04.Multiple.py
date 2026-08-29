
# ============================================================
# 3. MULTIPLE INHERITANCE
# Multiple Parent Classes → One Child Class
# ============================================================

class Father:

    def __init__(self, father_name):
        self.father_name = father_name

    def driving(self):
        print(self.father_name, "knows driving")


class Mother:

    def __init__(self, mother_name):
        self.mother_name = mother_name

    def cooking(self):
        print(self.mother_name, "knows cooking")


class Child(Father, Mother):

    def __init__(self, child_name, father_name, mother_name):
        self.child_name = child_name
        self.father_name = father_name
        self.mother_name = mother_name

    def playing(self):
        print(self.child_name, "is playing")


child = Child(
    "Rahul",
    "Raj",
    "Priya"
)

print("\nChild Name:", child.child_name)
print("Father Name:", child.father_name)
print("Mother Name:", child.mother_name)

child.driving()
child.cooking()
child.playing()

