import heapq


def solution():
    heap = []
    heapq.heapify(heap)
    with open('1.in', 'r') as file:
        elfCals = file.read().split('\n\n')
        for elfCal in elfCals:
            elfCal = [int(e) for e in elfCal.split('\n')]
            tempTotal = sum(elfCal)
            if len(heap) < 3:
                heapq.heappush(heap, tempTotal)
            else:
                # check if we have a new value in top 3
                if heap[0] < tempTotal:
                    heapq.heappop(heap)
                    heapq.heappush(heap, tempTotal)
    return sum(heap[0:3])


print(solution())
