
#This program calculates the area of a triangle.

def getData() -> (float, float):
    '''ask for user input the length and height of the triangle'''
    length = float(input("Enter the length of the triangle: "))
    height = float(input("Enter the perpendicular height of the triangle: "))
    return length, height


def trigArea(length:float, height:float) -> (float):
    '''Calculate the triangle area'''
    area = length * height / 2
    return area


def displayData(length:float, height:float, area:float) -> None:
    '''output the data'''
    print("The length of the triangle is ", length)
    print("The height of the triangle is ", height)
    print("The area of the triangle is ", area)


def main():
    length, height = getData()
    area = trigArea(length, height)
    displayData(length, height, area)

if __name__=="__main__":
    main()

# case 1
# Enter the length of the triangle: 10
# Enter the perpendicular height of the triangle: 10
# The length of the triangle is  10.0
# The height of the triangle is  10.0
# The area of the triangle is  50.0

# case 2
# Enter the length of the triangle: 1
# Enter the perpendicular height of the triangle: 1
# The length of the triangle is  1.0
# The height of the triangle is  1.0
# The area of the triangle is  0.5

# case 3
# Enter the length of the triangle: 7.5
# Enter the perpendicular height of the triangle: 8.7
# The length of the triangle is  7.5
# The height of the triangle is  8.7
# The area of the triangle is  32.625

# case 4
# Enter the length of the triangle: -10
# Enter the perpendicular height of the triangle: -10
# The length of the triangle is  -10.0
# The height of the triangle is  -10.0
# The area of the triangle is  50.0

# case 5
# Enter the length of the triangle: 2.25
# Enter the perpendicular height of the triangle: 1.75
# The length of the triangle is  2.25
# The height of the triangle is  1.75
# The area of the triangle is  1.96875