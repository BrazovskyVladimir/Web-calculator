from math import *


def calculate(string):
    try:
        return str(eval(string))
    except (SyntaxError, NameError, TypeError):
        return 'Er    ror in expression: "' + string + '"<br>Fix error and try again'
    except ValueError:
        return 'Error. Cannot calculate result of expression: "' + string + '"<br>Fix and try again.'
