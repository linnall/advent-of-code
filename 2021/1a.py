def solution():
    ret = 0
    with open('1.in', 'r') as file:
        count = 0
        prevDepth = 0
        for line in file:
            if count:
                if int(line) - int(prevDepth) > 0:
                    ret += 1
            prevDepth = line
            count += 1
    file.close()
    print(ret)

solution()