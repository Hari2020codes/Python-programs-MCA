class student:
    def __init__(self, roll,name, course):
        self.name = name
        self.course = course
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}\n, roll: {self.roll}, course: {self.course}")
stud1=student(101, "Alice", "MCA")
stud1.display()
stud2=student(102, "Bob", "MCA")
stud2.display()        