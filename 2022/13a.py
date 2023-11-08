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


def compare(list1, list2):
    while list1 and list2:
        l1 = list1.popleft()
        l2 = list2.popleft()
        if type(l1) is int and type(l2) is int:
            if l1 < l2:
                return 1
            elif l1 > l2:
                return -1
            else:
                return 0
        elif type(l1) is list and type(l2) is list:
            ret = compare(deque(l1), deque(l2))
            if ret == 1:
                return 1
        else:
            if type(l1) is int:
                l1 = [l1]
            else:
                l2 = [l2]
            list1.appendleft(l1)
            list2.appendleft(l2)
    if list2:
        return 1
    elif list1:
        return -1
    return 0  # if the lists are the same


def solution():
    with open("13.in", "r") as file:
        pairs = file.read().split("\n\n")
        inOrder = 0
        for i, pair in enumerate(pairs):
            lists = pair.split("\n")
            list1String = deque(list(lists[0]))
            # remove first lbracket
            list1String.popleft()
            list1 = buildList(list1String)
            list2String = deque(list(lists[1]))
            # remove first lbracket
            list2String.popleft()
            list2 = buildList(list2String)
            # compare
            if compare(deque(list1), deque(list2)) == 1:
                inOrder += i + 1
        return inOrder


print(solution())
