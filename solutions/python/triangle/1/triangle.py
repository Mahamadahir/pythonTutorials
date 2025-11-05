def equilateral(sides):
    a,b,c = sorted(sides)
    return (a == b == c) and isTriangle(sides)


def isosceles(sides):
    a,b,c = sorted(sides)
    return ((a == b) or (b == c) or (a == c)) and isTriangle(sides)


def scalene(sides):
    a,b,c = sorted(sides)
    return ((a != b) and (b != c) and (a != c)) and isTriangle(sides)


def isTriangle(sides):
    
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)

    return a> 0 and a+b >=c