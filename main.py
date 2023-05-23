import math
import json
import sys

ERROR_CODE = -1

E = 10 ** -4


def find_exterm(r: list, f):
    x = (r[0] + r[1]) / 2
    is_max = f(x) > f(r[0]) and f(x) > f(r[1])
    step = 0
    while r[1] - r[0] > E:
        x = (r[0] + r[1]) / 2
        x1 = x - E * 0.1
        x2 = x + E * 0.1
        if is_max and f(x1) < f(x2) \
                or not is_max and f(x1) > f(x2):
            r[0] = x
        else:
            r[1] = x
        step += 1
        if is_max:
            yield "max", step, x, f(x), math.fabs(r[0] - r[1])
        else:
            yield "min", step, x, f(x), math.fabs(r[0] - r[1])


def findall_extremes(ranges: list, func):
    return list(
        map(
            lambda r: find_exterm(r, func),
            ranges
        )
    )


if __name__ == '__main__':
    functions: dict
    try:
        with open("input.json", "r") as json_file:
            functions = json.load(json_file)
    except FileNotFoundError as fnf:
        print(f"Файл input.json не найден.\n{fnf}")
        sys.exit(ERROR_CODE)

    print(f"Поиск экстремумов методом дихотомии с точностью {E}:")
    for func in functions:
        print(f"\n{func}: " + functions[func]["str_f"])
        ind = 0
        for extr in findall_extremes(functions[func]["ranges"], eval(functions[func]["func"])):
            fin_val: list
            for step in extr:
                print(f"    {step[1]}: ({step[2]}, {step[3]}) E = {step[4]}")
                fin_val = step
            print(f"  {fin_val[0]}: ({fin_val[2]}, {fin_val[3]}) E = {fin_val[4]}")

