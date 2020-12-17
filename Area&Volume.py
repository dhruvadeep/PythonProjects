import math

# Finding areas 
print("1. Square")
print("2. Retrangle")
print("3. Circle")
print("4. Cube")
print("5. Cuboid")

work = 0 # for looping
while work==0:
    choice = int(input("Enter your choice: "))
    if choice in [1, 2, 3, 4, 5]:
        work = 1
    else:
        print("Error occured..")

def area(choice): 
    if choice in [1, 4]:
        side = float(input("Enter side lenght(cm): "))
        if choice == 1:
            print("Area of square: ", side*side)
        else:
            print("Volume of cube: ", *side*side*side)
    elif choice in [2, 5]:
        lenght = float(input("Enter side lenght(cm): "))
        breath = float(input("Enter side breath(cm): "))
        if choice == 2:
            print("Area of Retrangle: ", lenght*breath)
        else:
            height = float(input("Enter height lenght(cm): "))
            print("Volume of Cuboid: ", lenght*breath*height)
    elif choice == 3:
        radius = float(input("Enter radius(cm): "))
        print("Area of circle: ", 3.14*radius*radius)

area(choice)
        
