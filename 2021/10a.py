POINTS = {"}": 1197, ")": 3, "]": 57, ">": 25137}
RIGHT = {"}": "{", ")": "(", "]": "[", ">": "<"}


def solution():
    totalRisk = 0
    matrix = []
    errorTotal = 0
    with open('10.in', 'r') as file:
        for line in file:
            leftStack = []
            for char in line:
                if char == "\n":
                    continue
                else:
                    # left brackets
                    if char == "[" or char == "{" or char == "<" or char == "(":
                        leftStack.append(char)
                    else:
                        # check for right braces
                        leftBrace = leftStack.pop()
                        if leftBrace != RIGHT[char]:
                            errorTotal += POINTS[char]
                            break
    print(errorTotal)


solution()
