from collections import deque


def buildList(queue):
    lst = []
    while queue:
        ch = queue.popleft()
        if ch == "[":
            lst.append(buildList(queue))
        elif ch == "]":
            return lst
        elif ch == ",":
            continue
        else:
            lst.append(int(ch))


def compare(l1, l2):
    if type(l1) is int and type(l2) is int:
        if l1 < l2:
            return 1
        elif l1 > l2:
            return -1
        else:
            return 0
    elif type(l1) is list and type(l2) is list:
        i = 0
        while i < len(l1) and i < len(l2):
            ret = compare(l1[i], l2[i])
            if ret == 1:
                return 1
            elif ret == -1:
                return -1
            i += 1
        if i == len(l1) and i == len(l2):
            return 0
        elif i == len(l2):
            return -1
        else:
            return 1
    elif type(l1) is int:
        return compare([l1], l2)
    else:
        return compare(l1, [l2])


def solution():
    with open("13.in", "r") as file:
        pairs = file.read().split("\n\n")
        inOrder = 0
        for i, pair in enumerate(pairs):
            lists = pair.split("\n")
            # list1String = deque(list(lists[0]))
            # # remove first lbracket
            # list1String.popleft()
            # list1 = buildList(list1String)
            # list2String = deque(list(lists[1]))
            # # remove first lbracket
            # list2String.popleft()
            # list2 = buildList(list2String)
            # compare
            list1 = eval(lists[0])
            list2 = eval(lists[1])
            print(list1)
            print(list2)
            if compare(list1, list2) == 1:
                print(i + 1)
                inOrder += i + 1
        return inOrder


print(solution())
