def equilateral(sides):
    if all(sides):
        return sides.count(sides[0]) == len(sides)
    return False


def isosceles(sides):
    if len(set(sides)) == 1 and all(sides):
        return True
    if [el for el in sides if sides.count(sides[sides.index(el)]) > 1] and (
            min(sides) * 2) >= max(sides):
        return True
    return False


def scalene(sides):
    if len(set(sides)) != 3 or not all(sides):
        return False
    if (max(sides) * 2) <= sum(sides):
        return True
    return False
