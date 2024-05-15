import time, os 
import random
import math

os.system('cls')
def title():
    print("                     Sebastiaan's")
    print(" ,-----.      ,--.           ,--.        ,--.                  ")
    print("'  .--./,--,--|  |,---,--.,--|  |,--,--,-'  '-.,---.,--.--.         ") 
    print("|  |   ' ,-.  |  | .--|  ||  |  ' ,-.  '-.  .-| .-. |  .--'    ")
    print("'  '--'\ '-'  |  \ `--'  ''  |  \ '-'  | |  | ' '-' |  |       ")
    print("`-----'`--`--`--'`---'`----'`--'`--`--' `--'  `---'`--'       ")
    print("===========================================================")
    time.sleep(1)
    print(" '1' to find volume of cube")
    time.sleep(1)
    print(" '2' to find volue of cone")
    time.sleep(1)
    print(" '3' to find volume of sphere")
    time.sleep(1)
    print(" '4' to find surface area of cube")
    time.sleep(1)
    print(" '5' to find surface area of cone")
    time.sleep(1)
    print(" '6' to find surface area of sphere")
    time.sleep(1)
   
def volCube(num):
    print("volume of cube = ",pow(num,3))
    input("press 'enter' to return")

def volCone(radius, height):
    print("volume of cone = ", 3.14*radius**2*(height / 3))
    input("press 'enter' to return")

def volSphere(radius):
    print("volume of sphere = ", (4/3*3.14*radius**3))
    input("press 'enter' to return")

def saCube(side):
    print("surace area of cube = ", (side**2)*6)
    input("press 'enter' to return")

def saCone(radius, height):
    print("surface area of cone = ", 3.14*radius*(radius+(height*2+radius*2)**0.5))
    input("press 'enter' to return")
  
def saSphere(radius):
    print("surface area of sphere = ", 4*3.14*radius**2)
    input("press 'enter' to return")