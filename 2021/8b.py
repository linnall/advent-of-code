def solution():
    total = 0
    with open('8.in', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            numbers, output = list(map(lambda l: l.split(), line.split(' | ')))
            mappings = {}
            fiveSegments = []
            sixSegments = []
            one = ''
            four = ''
            seven = ''

            # identify 1, 4, 7, 8
            for number in numbers:
                segStr = ''.join(sorted(number))
                if len(number) == 2:
                    mappings[segStr] = 1
                    one = segStr
                elif len(number) == 3:
                    mappings[segStr] = 7
                    seven = segStr
                elif len(number) == 4:
                    mappings[segStr] = 4
                    four = segStr
                elif len(number) == 5:
                    fiveSegments.append(number)
                elif len(number) == 6:
                    sixSegments.append(number)
                else:
                    mappings[''.join(sorted(number))] = 8
            # differentiate the 5 segment numbers
            for number in fiveSegments:
                sortedStr = ''.join(sorted(number))
                s = set(list(number))
                sharedSegmentsFour = 0
                sharedSegmentsOne = 0
                for ch in four:
                    if ch in number:
                        sharedSegmentsFour += 1
                for ch in one:
                    if ch in number:
                        sharedSegmentsOne += 1
                if sharedSegmentsOne == 2:
                    mappings[sortedStr] = 3
                elif sharedSegmentsFour == 3:
                    mappings[sortedStr] = 5
                else:
                    mappings[sortedStr] = 2
            # differentiate the 6 segment numbers
            for number in sixSegments:
                sortedStr = ''.join(sorted(number))
                sharedSegmentsFour = 0
                sharedSegmentsSeven = 0
                for ch in four:
                    if ch in number:
                        sharedSegmentsFour += 1
                for ch in seven:
                    if ch in number:
                        sharedSegmentsSeven += 1
                if sharedSegmentsFour == 4 and sharedSegmentsSeven == 3:
                    mappings[sortedStr] = 9
                elif sharedSegmentsSeven == 3:
                    mappings[sortedStr] = 0
                else:
                    mappings[sortedStr] = 6

            outputStr = []
            for number in output:
                outputStr.append(str(mappings[''.join(sorted(number))]))
            total += int(''.join(outputStr))
    return total

print(solution())