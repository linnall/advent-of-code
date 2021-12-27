def solution():
    horizontal = 0
    depth = 0
    with open('2.in', 'r') as file:
        for line in file:
            command = line.split()
            num = command[1]
            if command[0] == 'forward':
                horizontal += int(num)
            elif command[0] == 'up':
                depth -= int(num)
            else:
                # down
                depth += int(num)
    print(depth * horizontal)


solution()
