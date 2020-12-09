with open ("input.txt") as f:
    numbers = f.readlines()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].replace("\n", ""))
    
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
            print(numbers[i])
            exit()