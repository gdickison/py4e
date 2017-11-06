numbers = [800, 8, 85, -5, 9, 3, 909, 4, -10, 1002, 1, 0, 15]

def findLarge(numbers):
    biggest = numbers[0] #biggest can also be set to None
    for number in numbers:
        if number >= biggest:
            biggest = number
    return biggest

def findSmall(numbers):
    smallest = numbers[0] #smallest can also be set to None
    for number in numbers:
        if number <= smallest:
            smallest = number
    return smallest

def findHighLow(numbers):
    high = numbers[0] #high can also be set to None
    low = numbers[0] #low can also be set to None
    for number in numbers:
        if number >= high:
            high = number
        elif number <=low:
            low = number
    print("The highest number is ", high, "\nThe lowest number is ", low)

print(findLarge(numbers))
print(findSmall(numbers))
findHighLow(numbers)
