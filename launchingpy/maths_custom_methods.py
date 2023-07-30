import math

def pythagoras_method(a,hyp):
    if isinstance(a,list):
        """for instance in a:
            b = math.sqrt(hip**2-a**2)
            b.append(b)
            return b"""
        return {'b': [math.sqrt(hyp**2-x**2) for x in a]}
