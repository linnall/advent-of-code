class Monkey:
    def __init__(self):
        self.items = []
        self.worryLevel = 0
        self.operationTerms = []
        self.divisor = 1
        self.monkeyTrue = -1
        self.monkeyFalse = -1

    def __str__(self):
        return f"{self.items}\n{self.operationTerms}\n{self.divisor}\n{self.monkeyTrue}\n{self.monkeyFalse}"


def solution():
    monkies = []
    with open("11.in", "r") as file:
        lines = file.read().split("\n\n")
        for monkey in lines:
            mlines = monkey.split("\n")
            m = Monkey()
            m.items = list(map(int, mlines[1].split(": ")[1].split(", ")))
            m.operationTerms = mlines[2].split()[3:]
            m.divisor = int(mlines[3].split()[-1])
            m.monkeyTrue = int(mlines[4].split()[-1])
            m.monkeyFalse = int(mlines[5].split()[-1])
            monkies.append(m)
        inspections = [0 for _ in range(len(monkies))]
        for i in range(20):
            print("ROUND", i)
            for j, activeMonkey in enumerate(monkies):
                print("MONKEY", j)
                if activeMonkey.items:
                    inspections[j] += len(activeMonkey.items)
                for item in activeMonkey.items:
                    term1, op, term2 = activeMonkey.operationTerms
                    newWorryLevel = 0
                    if term1 == "old":
                        newWorryLevel += item
                    else:
                        newWorryLevel += int(item)
                    if term2 == "old":
                        term2 = item
                    else:
                        term2 = int(term2)
                    if op == "+":
                        newWorryLevel += term2
                    else:  # product
                        newWorryLevel *= term2
                    newWorryLevel //= 3
                    if newWorryLevel % activeMonkey.divisor:
                        monkies[activeMonkey.monkeyFalse].items.append(newWorryLevel)
                    else:
                        monkies[activeMonkey.monkeyTrue].items.append(newWorryLevel)
                activeMonkey.items = []
        print(inspections)
        temp = []
        for i, num in enumerate(inspections):
            temp.append([num, i])
        temp.sort(reverse=True)
        return temp[0][0] * temp[1][0]


print(solution())
