# single inheritance
class Student:
    def getdata(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course
    def displaydata(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Course:", self.course)
class   Test(Student):
    def getmarks(self, marks):
        self.marks = marks
    def displaymarks(self):
        print("Marks:", self.marks)    
name=input("Are you sure to enter the matrix")
        
stud1=Test()
stud1.getdata("Alice", 101, "Mathematics")
stud1.getmarks(95)
stud1.displaydata()
stud1.displaymarks()        
        