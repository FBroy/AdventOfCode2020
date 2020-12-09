from copy import deepcopy


def check():
    index = 0
    accumulator = 0
    while True:
        if index >= len(tmp):
            print(accumulator)
            exit()
        if (tmp[index][1]):
            return

        if "nop" in tmp[index][0]:
            tmp[index][1] = True
            index += 1
            
        elif "acc" in tmp[index][0]:
            accumulator += int(tmp[index][0][1])
            tmp[index][1] = True
            index += 1
        else:
            tmp[index][1] = True
            index += int(tmp[index][0][1])


with open("input.txt") as f:
    lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = [lines[i].replace("\n", "").split(" "), False]

    for i in range(len(lines)):
        tmp = deepcopy(lines)
        if tmp[i][0][0] == "jmp":
            tmp[i][0][0] = "nop"
        elif tmp[i][0][0] == "nop":
            tmp[i][0][0] = "jmp"
        else:
            continue
        check()