def equilateral(sides):
    return len(set(sides)) == 1 and isTriangle(sides)


def isosceles(sides):
    return len(set(sides)) <= 2 and isTriangle(sides)


def scalene(sides):
    return len(set(sides)) == 3 and isTriangle(sides)


def isTriangle(sides):
    
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)

    return a> 0 and a+b >=c