def getRadius(r):
    return 3.14 * r * r


def getCircum(r):
    return 3.14 * 2 * r


r = int(input('Please input the radius of the circle'))
print(f"The area of the circle is {getRadius(r)} and the circum is {getCircum(r)}")
