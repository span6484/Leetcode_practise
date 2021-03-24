import math
import sys
# print(math.factorial(345))

state = True
while state:
    val = input("Input a nonnegative interger: ")

    try:
        a = int(val)
        val = int(val)

    except ValueError:
        print("Incorrect input, giving up.")
        continue

    if val <= 0:
        print("Incorrect input, giving up")
    else:
        state = False

val = math.factorial(val)

val1 = val
num1 = 0
while(val1%10 == 0):
    num1 += 1
    val1//= 10
print(f"Computing the number of trailing 0s in 15! by dividing by 10 for long enough: {num1}")
        

strNum = str(val)
i = -1
num2 = 0
while(strNum[i] == '0'):
    num2 += 1
    i -= 1
print(f"Computing the number of trailing 0s in 15! by dividing by 10 for long enough: {num2}")



power_of_five = 5
num3 = 0
while a >= power_of_five:
    num3 += a // power_of_five
    power_of_five *= 5
    
    
print(f"Computing the number of trailing 0s in 15! by dividing by 10 for long enough: {num3}")