# to find area of square, rectangle and triangle using lambda functions
side=int(input("Enter the side of the square: "))   
area_square=lambda a:a*a
print(f"The area of the square is {area_square(side)}")

length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))
area_rectangle=lambda l,b:l*b
print(f"The area of the rectangle is {area_rectangle(length,breadth)}")

base=int(input("Enter the base of the triangle: "))
height=int(input("Enter the height of the triangle: "))
area_triangle=lambda b,h:0.5*b*h
print(f"The area of the triangle is {area_triangle(base,height)}")
