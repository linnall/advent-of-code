#12 red cubes, 13 green cubes, and 14 blue cubes
dictionary = {"red": 12, "green": 13, "blue": 14}
def solution():
    total = 0
    with open('2.in', 'r') as file:
        games = file.read().split('\n')
        for i, game in enumerate(games):
            rounds = game.split(': ')[1].split('; ')
            invalid = False
            for round in rounds:
                cubes = round.split(', ')
                for pair in cubes:
                    num, colour = pair.split()
                    n = int(num)
                    for c, v in dictionary.items():
                        if colour == c and n > v:
                            invalid = True
                            break
                    if invalid:
                        break
                if invalid:
                    break
            if invalid:
                continue
            total += i + 1
    return total

print(solution())