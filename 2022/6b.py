def solution():
    seen = {}
    begin = 0
    with open("6.in", "r") as file:
        stream = file.read()
        for i in range(len(stream)):
            char = stream[i]
            if char in seen:
                newBegin = seen[char] + 1
                for j in range(begin, newBegin):
                    del seen[stream[j]]
                seen[char] = i
                begin = newBegin
            else:
                seen[char] = i
            if len(seen.values()) == 14:
                return i + 1


print(solution())
