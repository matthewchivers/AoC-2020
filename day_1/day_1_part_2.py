#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Day 2 Problem from Advent of Code:

"""

if __name__ == '__main__':
    f = open("input.txt", "r")
    numbers = []
    for line in f:
        numbers.append(int(line.strip()))

    for x in range(len(numbers)):
        num_x = numbers[x]
        for y in range(x, len(numbers)):
            num_y = numbers[y]
            for z in range(y, len(numbers)):
                num_z = numbers[z]
                if(num_x + num_y + num_z == 2020):
                    print(str(num_x) + " + " + str(num_y) + " + " + str(num_z) + " = " + str(num_x + num_y + num_z))
                    print(str(num_x) + " * " + str(num_y) + " * " + str(num_z) + " = " + str(num_x * num_y * num_z))
