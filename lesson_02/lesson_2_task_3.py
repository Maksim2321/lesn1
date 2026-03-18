import math

def square(side):
    area = side * side
    return math.ceil(area) if side != int(side) else area