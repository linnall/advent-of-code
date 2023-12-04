from collections import defaultdict
def solution():
    with open('4.in', 'r') as file:
        copies = defaultdict(int)
        cards = file.read().split('\n')
        for i, card in enumerate(cards):
            _, numbers = card.split(': ')
            winning, given = numbers.split(' | ')
            seen = set(winning.split())
            matching_nums = 0
            for num in given.split():
                if num in seen:
                    matching_nums += 1
            copies[i] += 1
            for _ in range(copies[i]):
                for val in range(1, matching_nums + 1):
                    copies[i + val] += 1
    return sum(copies.values())

print(solution())