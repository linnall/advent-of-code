from collections import defaultdict
from string import ascii_lowercase
from string import ascii_uppercase

def solution():
    lower = {v:k for k,v in enumerate(ascii_lowercase)}
    upper = {v:k+26 for k,v in enumerate(ascii_uppercase)}
    total = 0
    with open('3.in', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            d1 = defaultdict(int)
            # loop through each line
            for i, char in enumerate(line):
                if i < len(line) // 2:
                    d1[char] += 1
                else:
                    if d1[char] > 0:
                        # upper case
                        if ord(char) < 91:
                            total += upper[char] + 1
                        # lower case
                        else:
                            total += lower[char] + 1
                        break
        print(total)

solution()