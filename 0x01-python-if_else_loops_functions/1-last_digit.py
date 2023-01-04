#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "is"
rem = math.fmod(number, 10)
if rem > 5:
    print(f"{str1} {number} {str2} {rem:.0f} and is greater than 5")
elif rem == 0:
    print(f"{str1} {number} {str2} {rem:.0f} and is 0")
elif rem < 6 and not 0:
    print(f"{str1} {number} {str2} {rem:.0f} and is less than 6 and not 0")
