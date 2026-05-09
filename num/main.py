import time

num = input ("Enter a number: ")

if num == "42":
    print ("This is my favorite number! And the answer to the Ultimate Question of Life, The Universe, and Everything.")
elif num == "67":
    print ("This is a bannd trend.")
    time.sleep(3)
    exit
elif num >= "1000000":
    print ("This is a BIG number")
elif num <= "0":
    print ("This is negative number")
else:
    print ("This is YOUR favorite number")