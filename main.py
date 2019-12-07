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
for i in range(0, 10):
    print(i + 1, rectangle)

# Function Based
def function_area_of_rectangle(rectangle, b, h):
    print(rectangle)
    return b * h

print(function_area_of_rectangle("r", 10, 4))