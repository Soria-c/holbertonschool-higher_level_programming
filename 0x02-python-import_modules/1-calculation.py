#!/usr/bin/python3
if (__name__) == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    op = ("+", "-", "*", "/")
    opn = (calc.add, calc.sub, calc.mul, calc.div)
    for i in range(4):
        print(f"{a} {op[i]} {b} = {opn[i](a, b)}")
