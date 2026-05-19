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

def num_choose():
    
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
    elif num == 7:
        print ("This is the most popular number in the world!")
    elif num == 365:
        print ("This is the number of days in a year!")
    elif num == 10:
        print ("This is Carmel favorite number!")
    elif num == 2019:
        print ("this is Omer birthday year")
    elif num == 3:
        print ("this is the closest full number to pi")
    elif num ==8:
        print ("It's a rotated infinity symbol.")
    elif num ==123:
        print (" you really suck at choosing passwords ")
    elif num == 404:
        print ("page not found")
        time.sleep(5)
    elif num == 69 or num == 96:
        print ("This number stays the same even if you rotate it 180 degrees.")
    elif num == 1:
        print ("This is the first natural number")
    else:
        print ("This is YOUR favorite number")


while True:
    num_choose()