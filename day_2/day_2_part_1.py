#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Day 2 - Part 1 
Advent of Code
"""

if __name__ == '__main__':
    f = open("input.txt", "r")
    count = 0
    for line in f:
        # We only need to analyse each line individually and then ++ count
        # if (isCorrect)
        #   count++
