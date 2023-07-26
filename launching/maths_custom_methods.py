import math

def pythagoras_method(a,hip):
    if isinstance(a,list):
        for instance in a:
            b = math.sqrt(hip**2-a**2)
            return b