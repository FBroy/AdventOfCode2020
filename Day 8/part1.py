with open("input.txt") as f:
    lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = [lines[i].replace("\n", "").split(" "), False]
    
    index = 0
    accumulator = 0
    while True:
        if (lines[index][1]):
            break
        
        if "nop" in lines[index][0]:
            lines[index][1] = True
            index += 1
            
        elif "acc" in lines[index][0]:
            accumulator += int(lines[index][0][1])
            lines[index][1] = True
            index += 1
        else:
            lines[index][1] = True
            index += int(lines[index][0][1])

    print(accumulator)