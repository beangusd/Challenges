import time

done = False

while done == False:
    x = input("Are you done yet ")
    if x == "done":
        print("Yay")
        done = True
        break
    else:
        print("Okay...")
        done = True
        break