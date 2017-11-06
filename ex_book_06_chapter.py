# Exercise 1 - Write a while loop that starts at the last character of a string and works it's way backwards to the first character, printing each letter on a separate line.

string = input("Enter some text:")
index = len(string)
while index > 0 :
    print(string[index-1])
    index = index - 1

# Exercise 3

def findLetter(word, letter) :
    count = 0
    for item in word :
        if item == letter :
            count = count + 1
    print(letter, "appears in", word, count, "times.")

word = input("Enter a word:")
letter = input("Enter a letter:")
findLetter(word, letter)

# Exercise 4 - write an invocation that counts the number of times a letter occurs in a string

def findLtrInWord(word, letter) :
    print(word.count(letter))

findLtrInWord(word, letter)
