from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        divide_number = first / second
        return divide_number
