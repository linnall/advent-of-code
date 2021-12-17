import functools


def solution():
    ret = 0
    with open('1.in', 'r') as file:
        count = 0
        threeSum = []
        for line in file:
            if count < 3:
                threeSum.append(int(line))
            else:
                print(threeSum)
                fsum = threeSum[1] + threeSum[2] + int(line)
                ssum = sum(threeSum)
                if fsum - ssum > 0:
                    ret += 1
                threeSum.pop(0)
                threeSum.append(int(line))
            count += 1
    file.close()
    print(ret)


solution()
