from math import *


def calculate(string):
    try:
        return str(eval(string))
    except (SyntaxError, NameError, TypeError):
        return 'Error in expression: "' + string + '"<br>Fix error and try again'
