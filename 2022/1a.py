def solution():
    elfCals = []
    with open('1.in', 'r') as file:
        elfCals = file.read().split('\n\n')
        elfCals = map(lambda s: sum([int(e) for e in s.split('\n')]), elfCals)
        elfCals = list(elfCals)
    return max(elfCals)


print(solution())
