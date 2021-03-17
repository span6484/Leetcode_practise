from random import Random, seed,randint

arg_seed = input("Input a seed for the random number generator: ")
seed(arg_seed)
nums = input("How many elements do you want to generate: ")

nums1 = int(nums)
array = []
for i in range(nums1):
    array.append(randint(0,100))
print(array)


def find_max(array):
    index = None
    for i in array:
        if index == None:
            index = i
        else:
            if i > index:
                index = i

    return index
                
def find_min(array):
    index = None
    for i in array:
        if index == None:
            index = i
        else:
            if i < index:
                index = i

    return index
                
print(f"The maximum difference between largest and smallest values in this list is: {find_max(array)-find_min(array)}")