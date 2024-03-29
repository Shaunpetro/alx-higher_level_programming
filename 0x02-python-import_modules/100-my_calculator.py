#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        ops = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in ops:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f"{a} {sys.argv[2]} {b} = {ops[sys.argv[2]](a, b)}")

        if __name__ == "__main__":
            main()
