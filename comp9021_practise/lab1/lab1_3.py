from random import seed, randint, randrange
import sys
# val = input("Input a seed for the random number generator: ")
# seed_num = int(val)
# seed(seed_num)
# num = input("How many elements do you want to generate? ")
# ele_num = int(num)
# array = []
# for i in range(ele_num):
#     array.append(randint(0,20))
# print(f"The list is: {array}")


# index5 = 0
# index10 = 0
# index15 = 0
# index20 = 0

# for i in array:
#     if i >=0 and i < 5:
#         index5 += 1
#     if  i >=5 and i < 10:
#         index10 += 1
#     if i >=10 and i < 15:
#         index15 += 1

#     if i>=15 and i < 20:
#         index20 += 1

# if index5 == 0:
#     print("There is no element between 0 and 4.")
# elif index5 == 1:
#     print(f"There is {index5} element between 0 and 4.")
# else:
#     print(f"There are {index5} elements between 0 and 4.")


# if index10 == 0:
#     print("There is no element between 5 and 9.")
# elif index10 == 1:
#     print(f"There is {index10} element between 5 and 9.")
# else:
#     print(f"There are {index10} elements between 5 and 9.")



# if index15 == 0:
#     print("There is no element between 10 and 14")
# elif index15 == 1:
#     print(f"There is {index15} element between 10 and 14.")
# else:
#     print(f"There are {index15} elements between 10 and 14")


# if index20 == 0:
#     print("There is no element between 15 and 19")
# elif index20 == 1:
#     print(f"There is {index20} element between 15 and 19.")
# else:
#     print(f"There are {index20} elements between 15 and 19")

arg_for_seed = input('Input a seed for the random number generator: ')
try:
    arg_for_seed = int(arg_for_seed)

except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit

num = input('How many elements do you want to generate? ')

try:
    num = int(num)

except ValueError:
    print('Input is not an integer, giving up')
    sys.exit()
if num <=0:
    print('Input should be strictly positive, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(20) for _ in range(num)]
print(L)

intervals = [0]*4
for i in range(num):
    intervals[L[i] // 5] += 1

for i in range(4):
    if intervals[i] == 0:
        print(f"There is no element between {i*5} and {i*5+4}.")
    if intervals[i] == 1:
        print(f"There is 1 element betwween {i*5} and {i*5+4}.")
    else:

        print(f"There are {intervals[i]} elements between {i*5} and {i*5+4}")   


