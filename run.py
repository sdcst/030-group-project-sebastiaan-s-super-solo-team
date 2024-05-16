import time, os, random, math
import definitions
##perma-loop
z=0
while z !=1:
    os.system('cls')
    definitions.title()
    try:
        choice = int(input("enter an option: "))
        while choice == 0 or choice > 6 or choice < 0:
            print("\n\n\n           invalid choice...")
            time.sleep(3)
            choice = int(input("enter an option: "))
        if choice == 1:
            x = float(input("input a side-length: "))
            definitions.volCube(x)
        if choice == 2:
            x = float(input("input a radius: "))
            y = float(input("input a height: "))
            definitions.volCone(x, y)
        if choice == 3:
            x = float(input("input a radius: "))
            definitions.volSphere(x)
        if choice == 4:
            x = float(input("input a side length: "))
            definitions.saCube(x)
        if choice == 5:
            x = float(input("input a radius: "))
            y = float(input("input a height: "))
            definitions.saCone(x, y)
        if choice == 6:
            x = float(input("input a radius: "))
            definitions.saSphere(x)
    except:
        print("\n\n\n           invalid choice...")
        time.sleep(3)
        exit