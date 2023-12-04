def solution():
    with open('4.in', 'r') as file:
        cards = file.read().split('\n')
        total = 0
        for card in cards:
            _, numbers = card.split(': ')
            winning, given = numbers.split(' | ')
            seen = set(winning.split())
            score = 0.5
            for num in given.split():
                if num in seen:
                    score *= 2
            if score > 0.5:
                total += score
    return total

print(solution())