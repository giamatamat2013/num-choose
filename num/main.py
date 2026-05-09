import time

num = input ("Enter a number: ")

if num == "42":
    print ("This is my favorite number! And the answer to the Ultimate Question of Life, The Universe, and Everything.")
elif num == "67":
    print ("This is a bannd trend.")
    time.sleep(1)
    exit
elif num <= "0":
    print ("This is negative number")
elif num == "23":
    print ("This is amit favorite number")
else:
    print ("This is YOUR favorite number")