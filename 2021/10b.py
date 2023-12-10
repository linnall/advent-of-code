POINTS = {"{": 3, "(": 1, "[": 2, "<": 4}
RIGHT = {"}": "{", ")": "(", "]": "[", ">": "<"}


def solution():
    scores = []
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
                            leftStack = []
                            break
            if leftStack:
                score = 0
                while leftStack:
                    bracket = leftStack.pop()
                    score *= 5
                    score += POINTS[bracket]
                scores.append(score)
    return sorted(scores)[len(scores) // 2]

print(solution())
