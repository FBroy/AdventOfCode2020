with open("input.txt") as f:
    lines = f.readlines()
    results = []
    
    paths = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")

    for path in paths:
        trees = 0
        index = 0
        row = 0
        while (row < len(lines)):
            if lines[row][index%len(lines[i])] == "#":
                trees += 1
            index += path[0]
            row += path[1]
        
        results.append(trees)

print(results)
product = 1
for i in results:
    product *= i

print(product)