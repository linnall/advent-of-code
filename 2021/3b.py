from typing import List

# takes list of binary numbers and bit position and returns the dominant bit value of that position


def solution_help(list: List[str], posInt: int):
    sum = 0
    fileLines = len(list)
    for line in list:
        sum += int(line[posInt])
    if sum * 2 < fileLines:
        return 0
    else:
        return 1


def findC02Value(c02Nums: List[str], bitsNum: int):
    for i in range(bitsNum):
        if len(c02Nums) == 1:
            break
        else:
            inferiorBit = abs(solution_help(c02Nums, i) - 1)
            if inferiorBit == 1:
                newC02Nums = []
                for num in c02Nums:
                    if num[i] == '1':
                        newC02Nums.append(num)
                c02Nums = newC02Nums
            else:
                newC02Nums = []
                for num in c02Nums:
                    if num[i] == '0':
                        newC02Nums.append(num)
                c02Nums = newC02Nums
    print(c02Nums[0])
    return int(c02Nums[0], 2)


def findOxygenValue(oxygenNums: List[str], bitsNum: int):
    for i in range(bitsNum):
        if len(oxygenNums) == 1:
            break
        else:
            superiorBit = solution_help(oxygenNums, i)
            if superiorBit == 1:
                newOxyNums = []
                for num in oxygenNums:
                    if num[i] == '1':
                        newOxyNums.append(num)
                oxygenNums = newOxyNums
            else:
                newOxyNums = []
                for num in oxygenNums:
                    if num[i] == '0':
                        newOxyNums.append(num)
                oxygenNums = newOxyNums
    print(oxygenNums[0])
    return int(oxygenNums[0], 2)


def solution():
    bitsNum = 0
    oxygenNums = []
    c02Nums = []
    with open('3.in', 'r') as file:
        for line in file:
            bitsNum = len(line)
            c02Nums.append(line)
            oxygenNums.append(line)
    print(bitsNum)
    o = findOxygenValue(oxygenNums, bitsNum)
    c = findC02Value(c02Nums, bitsNum)
    print(o*c)


solution()
