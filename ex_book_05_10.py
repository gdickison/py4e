# Prompt the user to enter a number. Keep prompting until the user enters "done". If the user enters anything other than a number or "done" print "Invalid input." When the user enters "done" exit the program and print the maximum, minimum, total, count, and average of the numbers entered.

largest = None
smallest = None
count = 0
total = 0
average = 0
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    else :
        try :
            int(num)
        except :
            print("Invalid input")
            continue
    if count == 0 : #You can use an increment variable, or if largest [or smallest] is None :
        largest = int(num)
        smallest = int(num)
    elif int(num) > largest :
        largest = int(num)
    elif int(num) < smallest :
        smallest = int(num)
    count = count + 1
    total = total + int(num)
    average = total / count
print("Maximum is", largest)
print("Minimum is", smallest)
print("Count is", count)
print("Total is", total)
print("Average is", average)
