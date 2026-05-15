import time
logo = r"""
        _                       _                         _    
  __ _(_) __ _ _ __ ___   __ _| |_ __ _ _ __ ___   __ _| |_ 
 / _` | |/ _` | '_ ` _ \ / _` | __/ _` | '_ ` _ \ / _` | __| 
| (_| | | (_| | | | | | | (_| | || (_| | | | | | | (_| | |_  
 \__, |_|\__,_|_| |_| |_|\__,_|\__\__,_|_| |_| |_|\__,_|\__| 
 |___/                        
   ____   ___  _ _____ 
 |___ \ / _ \/ ||___ / 
   __) | | | | |  |_ \ 
  / __/| |_| | | ___) |
 |_____|\___/|_||____/                                
"""
print(logo)
num = int(input ("Enter a number: "))

if num == 42:
    print ("This is Itamar's favorite number! And the answer to the Ultimate Question of Life, The Universe, and Everything.")
elif num == 67:
    print ("This is a bannd trend.")
    time.sleep(1)
    exit
elif num < 0:
    print ("This is negative number")
elif num == 23:
    print ("This is amit's favorite number")
elif num == 0:
    print ("This is Eitan's favorite number")
elif num == 2013:
    print ("What a creativity, did you copy from the title?")
elif num == 6:
    print ("This is the most skipped number!")
elif num == 12:
    print ("This is the basis of the counting of Tatarism.")
else:
    print ("This is YOUR favorite number")