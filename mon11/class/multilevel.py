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
class Result(Test):
    def displayresult(self):
        self.displaydata()
        self.displaymarks()
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail") 
roll_no = int(input("Enter Roll No: "))
name = input("Enter Name: ")
course = input("Enter Course: ")
marks = int(input("Enter Marks: "))
stud1 = Result()
stud1.getdata(name, roll_no, course)
stud1.getmarks(marks)
stud1.displayresult()
                                           