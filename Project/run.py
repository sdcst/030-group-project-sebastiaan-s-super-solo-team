import time, os, random, math, definitions
os.system('cls')
definitions.title()
choice = input()

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