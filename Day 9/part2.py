with open ("input.txt") as f:
    numbers = f.readlines()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].replace("\n", ""))
    
    index = 0
    for i in range(25, len(numbers)):
        found = False
        for j in range(25):
            if found:
                break
            for k in range(j+1, 25):
                if found:
                    break
                if (numbers[i] == numbers[i-25+j] + numbers[i-25+k]):
                    found = True
        if not found:
            index = i

    found = False
    start = 0
    end = 0
    for i in range(len(numbers)):
        sum = 0
        start = i
        if found:
            break
        for j in range(i, len(numbers)):
            if sum + numbers[j] < numbers[index]:
                sum += numbers[j]
            elif sum + numbers[j] == numbers[index]:
                end = j
                found = True
                break
        
    interval = numbers[start:end+1]
    interval.sort()
    print(interval[0]+interval[-1])