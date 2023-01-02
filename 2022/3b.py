from collections import defaultdict
from string import ascii_lowercase
from string import ascii_uppercase

def solution():
    lower = {v:k for k,v in enumerate(ascii_lowercase)}
    upper = {v:k+26 for k,v in enumerate(ascii_uppercase)}
    total = 0
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    with open('3.in', 'r') as file:
        lines = file.read().split('\n')
        for i, line in enumerate(lines):
            if i % 3 == 0:
                d1 = defaultdict(int)
                d2 = defaultdict(int)
                for char in line:
                    d1[char] += 1
            elif i % 3 == 1:
               for char in line:
                    d2[char] += 1 
            # i % 3 == 2
            else:
                for char in line:
                    if d1[char] > 0 and d2[char] > 0:
                        # upper case
                        if ord(char) < 91:
                            total += upper[char] + 1
                        # lower case
                        else:
                            total += lower[char] + 1
                        break
            
        print(total)

solution()