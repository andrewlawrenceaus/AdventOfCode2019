import os
import math

total_fuel = 0


def file_path():
    script_dir = os.path.dirname(__file__)
    rel_path = "resources\\day_one.txt"
    return os.path.join(script_dir, rel_path)


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def calc_fuel(mass):
    return round_down(mass / 3) - 2


with open(file_path()) as fp:
    line = fp.readline()
    while line:
        total_fuel += calc_fuel(int(line))
        line = fp.readline()
    print(total_fuel)
