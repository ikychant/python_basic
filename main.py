print("Hello Math World")

# Calculate the area of a rectangle (rectangle)
b = 10
h = 10
rectangle = b * h
print(rectangle)

# Conditional Statement
if rectangle < 100:
    print("Small")
elif rectangle == 100:
    print("Perfect")
else:
    print("Large")

# Loop
print("with for")
for i in range(0, 3):
    print(i + 1, rectangle)

# Function Based
def function_area_of_rectangle(rectangle, b, h):
    print(rectangle)
    return b * h

print(function_area_of_rectangle("Calculate with Function Based", 10, 4))

# Class Based
class Rectangle():
    def __init__(self, rectangle, b, h):
        self.rectangle = rectangle
        self.b = b
        self.h = h
    def calculate_area(self):
        return (self.b * self.h)

rectangle_class = Rectangle("Calculate with Class Based", 50, 3)
print(rectangle_class.rectangle)
print(rectangle_class.calculate_area())