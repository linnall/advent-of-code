def solution():
    total = 0
    with open('2.in', 'r') as file:
        games = file.read().split('\n')
        for i, game in enumerate(games):
            max_cubes = {"red": 0, "green": 0, "blue": 0}
            rounds = game.split(': ')[1].split('; ')
            for round in rounds:
                cubes = round.split(', ')
                for pair in cubes:
                    num, colour = pair.split()
                    n = int(num)
                    for c in ["red", "green", "blue"]:
                        if colour == c and n > max_cubes[colour]:
                            max_cubes[colour] = n
            total += max_cubes["red"] * max_cubes["blue"] * max_cubes["green"]
    return total 

print(solution())