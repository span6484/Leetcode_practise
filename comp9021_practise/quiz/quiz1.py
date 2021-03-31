#############################################
#method1       ##############################
#############################################
# from random import randrange, seed
# import sys
# try:
#     seed_arg, end_val = input("Enter two integers: ").split()
# except ValueError:
#     print("Please enter both value equal or more than 0")
#     sys.exit()

# seed_arg = int(seed_arg) + 1
# end_val = int(end_val) + 1

# seed(seed_arg)
# map = dict()
# no_key = []
# time = 0
# array = list()
# array.append("None")
# for i in range(1, end_val):
#     value = randrange(-end_val // 2, end_val)
#     if value > 0:
#         map[i] = value
#         time += 1
#         array.append(value)
#     else:
#         no_key.append(i)
#         array.append("None")

# print(f"The generated mapping is: \n{map}")
# print(f"The mappings's so-called 'keys' make up a set whose number of elements is \n{time}")
# print(f"The list of integers between 1 and 16 that are not keys of the mapping is:\n{no_key}")
# print(f"Represented as a list, the mapping is:\n{array}")

# del_index = list()
# for i in map:
#     for j in map:
#         if map[i] == map[j] and i != j:
#             if i not in del_index:
#                 del_index.append(i)
#             if j not in del_index:
#                 del_index.append(j)
# for i in del_index:
#     del map[i]
# print(f"The one-to-one part of the mapping is: {map}")


#############################################
#method2       ##############################
#############################################
import sys
from random import seed, randrange


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE

def return_nonkeys(upper_bound,mapping):
    for i in range(1, upper_bound):
        if i not in mapping.keys():
            nonkeys.append(i)
        
    return nonkeys

def return_none(upper_bound,mapping):
    # mapping_as_a_list.append(None)
    for i in range(upper_bound):
        if i not in mapping.keys():
            mapping_as_a_list.append(None)
        else:
            mapping_as_a_list.append(mapping[i])
    return mapping_as_a_list

def return_one_to_one(mapping):
    temp = []
    mapping_list = list(mapping.items())
    value_list = list(mapping.values())
    for i in range(len((value_list))):
        if(value_list.count(value_list[i]) != 1):
            temp.append(i)

    for index in sorted(temp,reverse = True):
        del mapping_list[index]
    return dict(mapping_list)


nonkeys = return_nonkeys(upper_bound, mapping)
mapping_as_a_list = return_none(upper_bound,mapping)
one_to_one_part_of_mapping = return_one_to_one(mapping)
print()
print('EDIT THIS PRINT STATEMENT')
print('The mappings\'s so-called "keys" make up a set whose number of elements is ' + str(len(list(mapping.items())))+".")
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                      for key in sorted(one_to_one_part_of_mapping)
                             }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)
