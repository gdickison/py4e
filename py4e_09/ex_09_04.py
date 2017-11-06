# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter a file name:")
txtFile = open(fname)
emails = dict()
for line in txtFile :
    if not line.startswith("From ") :
        continue
    line = line.split()
    email = line[1]
    emails[email] = emails.get(email,0) + 1

bigEmail = None
bigCount = None
for address, count in emails.items() :
    if bigEmail is None or count > bigCount :
        bigEmail = address
        bigCount = count

print(bigEmail, bigCount)
