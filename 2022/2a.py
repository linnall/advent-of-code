def solution():
    # rock, paper, scissor 
    moves = {'A': 1, 'B': 2, 'C': 3}
    mymoves = {'X': 1, 'Y': 2, 'Z': 3}
    points = 0
    with open('2.in', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            m1, m2 = line.split()
            points += mymoves[m2]
            # tie
            if moves[m1] == mymoves[m2]:
                points += 3
            # I won
            elif mymoves[m2] - moves[m1] == 1 or (moves[m1] == 3 and mymoves[m2] == 1):
                points += 6
    print(points)

solution()