# Calculate the Area of a Room 

from cmath import pi


width = float(input("Please Enter Width: "))
length = float(input("Please Enter Length: "))

area_sq = width*length

print("The square footage =  " , area_sq) 

# Calculate the Circumference of a Room 

radius = float(input("Please Enter Radius: "))

area_c = pi*radius**2

print("The Area of a circle is ", area_c)