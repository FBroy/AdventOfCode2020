with open("input.txt") as f:
    lines = f.readlines()
    amount = []
    letters = []
    codes = []
    index = 0
    for line in lines:
        items = line.split(" ")
        amount.append(items[0].split("-"))
        letters.append(items[1].replace(":", ""))
        codes.append(items[2].replace("\n", ""))
        index += 1

    correct = 0

    for i in range(len(codes)):
        if int(amount[i][0]) <= codes[i].count(letters[i]) <= int(amount[i][1]):
            correct += 1

    print(correct)
