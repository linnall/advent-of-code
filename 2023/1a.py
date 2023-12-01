def solution():
    total = 0
    with open('1.in', 'r') as file:
        lines = file.read().split('\n')
        print(lines)
        for line in lines:
            first = None
            second = 0
            for ch in line:
                if ch.isdigit() and first is None:
                    first = int(ch)
                if ch.isdigit():
                    second = int(ch)
            total += first * 10 + second
    return total

print(solution())