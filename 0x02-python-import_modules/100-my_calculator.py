#!/usr/bin/python3
import calculator_1 as calc
from sys import argv as ar


def main():
    op = {"+": calc.add, "-": calc.sub, "*": calc.mul, "/": calc.div}
    if (len(ar) != 4):
        print(f"Usage: {ar[0]} <a> <operator> <b>")
        exit(1)
    if (ar[2] not in op):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{ar[1]} {ar[2]} {ar[3]} = {op[ar[2]](int(ar[1]), int(ar[3]))}")


if (__name__) == "__main__":
    main()
