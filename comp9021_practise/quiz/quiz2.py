# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3

import sys
from random import seed, randrange
from pprint import pprint
from collections import deque

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}
original_mapping = mapping

# INSERT YOUR CODE HERE
def return_circle(mapping):
    for i in mapping:
        if i == mapping[i]:
            cycles.append([i])
        else:
            #control the first time
            time = 0
            initial_key = i
            circle_key = i
            circle_value =mapping[circle_key]
            array = [initial_key]
            
            while circle_key != initial_key or time == 0:
                time += 1
                # circle_value = mapping[circle_key]
                if circle_value not in array and circle_value in mapping.keys():
                    circle_key = circle_value
                    circle_value = mapping[circle_key]
                    array.append(circle_key)
                else:
                    if circle_value == initial_key:
                        circle_key = circle_value
                        array = sorted(array)
                        if array not in cycles:
                            cycles.append(array)
                    
                    else:
                        array = []
                        break
    return cycles


def return_reversed(original_mapping):
    value = list(mapping.values())
    value_len = len(value)
    count_arr = []
    for i in range(value_len):
        count_index = value.count(value[i])
        if count_index not in count_arr:
            count_arr.append(count_index)
    count_arr = sorted(count_arr)

    for reverse_index in count_arr:
        temp = {}
        for i in range(value_len):
            if value.count(value[i]) == reverse_index:
                if value[i] in temp.keys():
                    temp[value[i]].append(keys[i])
                else:
                    temp[value[i]]=[keys[i]]
        reversed_dict_per_length[reverse_index] = temp
    return reversed_dict_per_length

cycles = return_circle(mapping)
reversed_dict_per_length = return_reversed(mapping)
print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)

