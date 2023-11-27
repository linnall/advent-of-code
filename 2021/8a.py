def solution():
    count = 0
    with open('8.in', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            _, output = list(map(lambda l: l.split(), line.split('|')))
            for seq in output:
                seqLen = len(seq)
                if seqLen == 2 or seqLen == 4 or seqLen == 3 or seqLen == 7:
                    count += 1
    return count

print(solution())