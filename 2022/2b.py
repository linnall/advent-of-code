def solution():
    points = 0
    # rock, paper, scissor
    # pointsVal = {'X': 1, 'Y': 2, 'Z': 3}
    toWin = {'A': 2, 'B': 3, 'C': 1}
    toTie = {'A': 1, 'B': 2, 'C': 3}
    toLose = {'A': 3, 'B': 1, 'C': 2}

    with open('2.in', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            m1, m2 = line.split()
            # lose
            if m2 == 'X':
                points += toLose[m1]
            elif m2 == 'Y':
                points += 3 + toTie[m1]
            else:
                points += 6 + toWin[m1]
        print(points)

solution()
