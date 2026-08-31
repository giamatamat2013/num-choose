import time
import math
from pathlib import Path
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

data_dir = Path.home() / "AppData" / "Roaming" / "giamatamat2013"
data_dir.mkdir(parents=True, exist_ok=True)
banned_file_path = data_dir / "banned" #אומר איפה הקובץ שאם קיים זה אומר שאני ban

num = None
if banned_file_path.exists(): #אם קובץ הבאן קיים
    while num != "42": #כל עוד המספר הוא לא 42 לא ממשיך
        print("You are banned from using this program.") #כתוב שאני באן
        num = input("") #נותן הזדמנות לכתוב מספר
        if num == "42": #אם מספר = 42 (אם לא, מתחיל מחדל את הלולאה ושואל למספר שוב)
            print("You are unbanned.") #אתה לא בבאן, כיתוב
            banned_file_path.unlink(missing_ok=True) #מחיקת הקובץ שאומר שאני באן

num_history = []

while True:
    num = input ("Enter a number: ")
    num_history.append(num)

    print(f"Your num is: {num}")
    if num == "42":
        print ("This is Itamar's favorite number! And the answer to the Ultimate Question of Life, The Universe, and Everything.")
    elif num == str(66+1) or num == str(40+1): # שיניתי פה שבמקום שיכתוב את המספרים  המקוללים יכותב רק40+1 ו66+1 כדי לא לקלל את הקוד
        print ("This is a banned trend.")
        banned_file_path.touch(exist_ok=True) # יוצר קובץ שלמעלה אם מזהה שקיים נותן באן
        time.sleep(1)
        exit()
    elif num == "":
        print ("You didn't enter anything, try again.")
    elif num < "0":
        print ("This is negative number.")
    elif num == "23":
        print ("This is amit's favorite number!")
    elif num == "0" or num == "∞":
        print ("This is Eitan's favorite number! And any other number.")
    elif num == "4":
        print ("this is the first square number.")
    elif num == "2013":
        print ("What a creativity, did you copy from the title?")
    elif num == "6":
        print ("This is the most skipped number!")
    elif num == "12":
        print ("This is the basis of the counting of Tatarism.")
    elif num == "520":
        print("This is a bad game!")
    elif num == "2048":
        print ("This is a good game!")
    elif num == "7":
        print ("This is the most popular number in the world!")
    elif num == "365":
        print ("This is the number of days in a year!")
    elif num == "10":
        print ("This is Carmel's favorite number!")
    elif num == "2019":
        print ("This is Omer's birthday year!")
    elif num == "3":
        print ("This is the closest full number to pi.")
    elif num == str(round(math.pi, 2)): 
        print ("This is two numbers after the dot of pi.")
    elif num =="8":
        print ("It's a rotated infinity symbol.")
    elif num == "123" or num == "1234" or num == "12345" or num == "123456" or num == "1234567" or num == "12345678" or num == "123456789" or num == "1234567890":
        print ("You really suck at choosing passwords!")
    elif num == "404":
        print ("Page not found")
        time.sleep(5)
    elif num == "040":
        print("Page yes found")
    elif num == "69" or num == "96":
        print ("This number stays the same even if you rotate it 180 degrees.")
    elif num == "1":
        print ("This is the first natural number.")
    elif num == "2":
        print ("This is the only even prime number.")
    elif num == "num history":
        num_history.remove("num history")
        for x in num_history:
            print (x)
    elif num >= "999999999999":
        print ("This number is too large for me to understand, try a smaller one.")
    elif num == "999999999998":
        print ("Are you kidding me?")
    elif num == "37" or num == "39":
        print("37 ≠ 39")
    elif not str(num).isnumeric():
        print ("This is not a number, try again.")
    else:
        print ("This is YOUR favorite number!")
