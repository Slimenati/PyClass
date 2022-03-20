#calculates the area and length of a rectangle with given dimensions
length = int(input("Enter the length of the rectangle:"))
width = int(input("Enter the width of the rectangle:"))
area = length * width
perimeter = (length * 2) + (width * 2)
print (f"The area of a rectangle of length {length} and width {width} is {area}, and its perimeter is {perimeter}.")
