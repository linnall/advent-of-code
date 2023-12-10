def solution():
    total = 0
    with open('1.in', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            digits = []
            for i, ch in enumerate(line):
                if ch.isdigit():
                    digits.append(int(ch))
                for j, val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                    if line[i:].startswith(val):
                        digits.append(j + 1)               
            total += digits[0] * 10 + digits[-1]
    return total

print(solution())