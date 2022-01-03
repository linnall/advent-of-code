class BingoBoard:

    def __init__(self) -> None:
        self.board = []
        self.markedNums = 0

    def __repr__(self) -> str:
        ret = ''
        for line in self.board:
            for num in line:
                ret += num + ' '
            ret += '\n'
        return ret

    def check_value(self, val: str):
        found = 0
        for r, row in enumerate(self.board):
            for c, num in enumerate(row):
                if num == val:
                    row.pop(c)
                    row.insert(c, '-1')
                    found = 1
                    break
            if found:
                break
        if found:
            self.markedNums += 1

        # check if we have a winner
        winner = 0
        if self.markedNums >= 5 and found:
            # check row
            for i in range(5):
                if self.board[r][i] == '-1':
                    winner = 1
                else:
                    winner = 0
                    break
            if winner:
                return 1
            # check column
            for j in range(5):
                if self.board[j][c] == '-1':
                    winner = 1
                else:
                    winner = 0
                    break
        if winner:
            return 1
        else:
            return 0

    def calculate_winning_score(self):
        sum = 0
        for row in self.board:
            for num in row:
                if num != '-1':
                    sum += int(num)
        return sum


def getInput(numbers, boards):
    lineNum = 0
    with open('4.in', 'r') as file:
        curr_board = None
        for line in file:
            if lineNum == 0:
                numbers.extend(line.strip('\n').split(','))
            else:
                if line == '\n' and curr_board:
                    boards.append(curr_board)
                    curr_board = BingoBoard()
                elif line == '\n':
                    curr_board = BingoBoard()
                else:
                    curr_board.board.append(line.strip('\n').split())
            lineNum += 1
        boards.append(curr_board)


def solution():
    numbers = []
    boards = []
    getInput(numbers, boards)

    for num in numbers:
        boardNum = 0
        for board in boards:
            winnerBool = board.check_value(num)
            if winnerBool:
                # calculate score
                sum = board.calculate_winning_score()
                print(int(num) * sum)
                return 0
            boardNum += 1


solution()
