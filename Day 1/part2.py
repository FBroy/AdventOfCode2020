with open("input.txt") as f:
    numbers = [int(x) for x in f.readlines()]

numbers.sort()

for i in range(len(numbers)):
    left = 0
    right = len(numbers)-1
    while True:
        if left >= right:
            break
        sum = numbers[left] + numbers[right] + numbers[i]
        if sum == 2020:
            print(numbers[left] * numbers[right] * numbers[i])
            exit()
        elif sum < 2020:
            left += 1
        else:
            right -= 1