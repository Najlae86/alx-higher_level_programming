#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys
if len(sys.agrv) -1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
operator = {"+": add, "-": sub, "*": mul, "/": div}
if sys.argv[2] not in list(operator.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
a = sys.argv[1]
b = sys.argv[3]
print("{} {} {} = {}".format(a, sys.argv[2], b, operator[sys.agrv[2]](a, b)))
