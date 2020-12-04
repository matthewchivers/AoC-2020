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
        num_x = nums[x]
        for y in range(x, len(nums)):
            num_y = nums[y]
            for z in range(y, len(nums)):
                num_z = nums[z]
                if(num_x + num_y + num_z == 2020):
                    print(str(num_x) + " + " + str(num_y) + " + " + str(num_z) + " = " + str(num_x + num_y + num_z))
                    print(str(num_x) + " * " + str(num_y) + " * " + str(num_z) + " = " + str(num_x * num_y * num_z))
