largest = None
smallest = None
count = 0
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
print("Maximum is", largest)
print("Minimum is", smallest)
