#!/usr/bin/python3


import sys

#
#     https://adventofcode.com/2022/day/13
# 


def task1(input):
    
    return 1


# def task2(input):
    
   


def main():

    problem_name = sys.argv[1]
    with open(f"{problem_name}") as f:
        input = [line.rstrip() for line in f]

    print(f"Task1: {task1(input)}")
    # print(f"Task2: {task2(input)}")

    return 0

if __name__ == "__main__":
    main()