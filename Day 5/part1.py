with open("input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    
    ids = []
    for line in lines:

        rows = []
        for i in range(128):
            rows.append(i)
        columns = []
        for i in range(8):
            columns.append(i)

        for letter in line:
            if letter == "F":
                rows = rows[:len(rows)//2]
            elif letter == "B":
                rows = rows[len(rows)//2:]
            elif letter == "L":
                columns = columns[:len(columns)//2]
            else:
                columns = columns[len(columns)//2:]
        ids.append(rows[0]*8+columns[0])

print(max(ids))
