from random import seed, randint
import sys
import statistics

random_seed = input("Input a seed for the random number generator: ")
try:
    random_seed = int(random_seed)

except ValueError:
    print("Please enter the integer value")
    sys.exit
element_num = input("How many elements do you want to generate? ")
try:
    element_num = int(element_num)

except ValueError:
    print("Please enter the integer value")
    sys.exit
seed(random_seed)


L = [randint(-50,50) for _ in range(element_num)]
print(f"list is {L}")

#mean
print("method1:")
print(f"mean is {statistics.mean(L)}")
# median
print(f"median is {statistics.median(L)}")
#standard deviation
print(f"standard deviation is {statistics.pstdev(L)}")
print("")
print("method2:")

# mean
num = 0
for i in L:
    num += i
mean_val = num / len(L)

# medium
index = len(L) // 2
L.sort()
if element_num % 2:
    medium_val = L[element_num // 2]
else:
    medium_val = (L[(element_num-1)//2] + L[element_num//2]) / 2

# standard deviation

sum_dv = 0
for i in L:
    sum_dv += (i-mean_val)**2

print(f"sum_dc is {sum_dv}")
sum_dv = sum_dv/(len(L))
st_vaule = sum_dv**0.5
print(L)
print(f"mean is {mean_val}")
# median
print(f"median is {medium_val}")
#standard deviation
print(f"standard deviation is {st_vaule:.2f}")