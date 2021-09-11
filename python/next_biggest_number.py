#!/usr/bin/python3
import sys
from itertools import permutations

def main():
    next_biggest_number(sys.argv[1])

def next_biggest_number(num):
    next_highest = sys.maxsize
    for s in sorted(permutations(str(num))):
        test_num = int(''.join(s))
        if test_num <= num:
            continue
        elif test_num > num and test_num < next_highest:
            next_highest = test_num
            ## Since the list is sorted no higher number can be the result
            break
    if next_highest == sys.maxsize:
        return -1
    else:
        return next_highest

if __name__ == "__main__":
    main()



