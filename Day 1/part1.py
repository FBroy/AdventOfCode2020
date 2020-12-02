with open("input.txt") as f:
    numbers = [int(x) for x in f.readlines()]

numbers.sort()

left = 0
right = len(numbers)-1

while True:
    if left >= right:
        break
    sum = numbers[left] + numbers[right]
    if sum == 2020:
        print(numbers[left] * numbers[right])
        break
    elif sum < 2020:
        left += 1
    else:
        right -= 1