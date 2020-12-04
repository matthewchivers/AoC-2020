#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Day 1 - Part 2
Advent of Code
"""

if __name__ == '__main__':
    f = open("input.txt", "r")
    nums = []
    for line in f:
        nums.append(int(line.strip()))

    for x in range(len(nums)):
        for y in range(x, len(nums)):
            for z in range(y, len(nums)):
                if(num[x] + num[y] + num[z] == 2020):
                    print(str(num[x]) + " + " + str(num[y]) + " + " + str(num[z]) + " = " + str(num[x] + num[y] + num[z]))
                    print(str(num[x]) + " * " + str(num[y]) + " * " + str(num[z]) + " = " + str(num[x] * num[y] * num[z]))

