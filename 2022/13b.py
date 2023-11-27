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


def merge(lists):
    if len(lists) == 1:
        return lists
    else:
        m = (len(lists) - 1) // 2
        l1 = merge(lists[0 : m + 1])
        l2 = merge(lists[m + 1 : len(lists)])
        mergedLists = []
        p1, p2 = 0, 0
        while p1 < len(l1) and p2 < len(l2):
            if compare(l1[p1], l2[p2]) == 1:
                mergedLists.append(l1[p1])
                p1 += 1
            else:
                mergedLists.append(l2[p2])
                p2 += 1
        if p1 < len(l1):
            mergedLists.extend(l1[p1 : len(l1)])
        if p2 < len(l2):
            mergedLists.extend(l2[p2 : len(l2)])
        return mergedLists


def solution():
    all_lists = []
    with open("13.in", "r") as file:
        pairs = file.read().split("\n\n")
        for pair in pairs:
            lists = pair.split("\n")
            all_lists.extend(list(map(eval, lists)))
    all_lists.extend([[[2]], [[6]]])
    sortedList = merge(all_lists)
    return (sortedList.index([[2]]) + 1) * (sortedList.index([[6]]) + 1)


print(solution())
