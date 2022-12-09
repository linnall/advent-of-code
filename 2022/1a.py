def solution():
    maxCals = 0
    with open('1.in', 'r') as file:
        elfCals = file.read().split('\n\n')
        for elfCal in elfCals:
            elfCal = [int(e) for e in elfCal.split('\n')]
            maxCals = max(maxCals, sum(elfCal))
    return maxCals


print(solution())
