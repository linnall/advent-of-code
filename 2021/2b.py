def solution():
    horizontal = 0
    depth = 0
    aim = 0
    with open('2.in', 'r') as file:
        for line in file:
            command = line.split()
            num = command[1]
            if command[0] == 'forward':
                horizontal += int(num)
                depth += int(num) * aim
            elif command[0] == 'up':
                aim -= int(num)
            else:
                # down
                aim += int(num)
    print(depth * horizontal)


solution()
