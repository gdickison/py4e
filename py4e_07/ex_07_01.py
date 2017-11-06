xFile = open("ex_02_03.py")

count = 0
for cheese in xFile :
    cheese = cheese.rstrip()
    print(count, cheese)
    count = count +1

for line in xFile :
    count = count + 1
print(count)
