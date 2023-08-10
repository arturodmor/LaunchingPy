import math

def pythagoras_method(a,hyp):
    if isinstance(a,list):
        return [math.sqrt(hyp**2-x**2) for x in a]
