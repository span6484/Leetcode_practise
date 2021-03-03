# -*- coding:utf8 -*-
# p46
# 问题：
# 异序词检测：
# Given two strings s and t, write a function to determine if t is an anagram of s.
 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# 四种方法，我们将测试最快的方法

# 目标速度： O(n)
# 思路：计数法, 字典

from timeit import Timer

#Solution 1   
# def anagramSolution(s1,s2):
    
#     isAnagram = True
    
#     c1 = [0] * 26
#     c2 = [0] * 26
    
#     # In [2]: ord('a')
#     # Out[2]: 97
#     for i in range(len(s1)):
#         index = ord(s1[i]) - ord('a')
#         c1[index] += 1

#     for i in range(len(s2)):
#         index = ord(s2[i]) - ord('a')
#         c2[index] += 1


#     if c1 == c2:
#         isAnagram = True
    
#     else:
#         isAnagram = False
    
#     return isAnagram



# Solution 2: dictionary
def anagramSolution(s1,s2):
    isAnagram = True
    group1 = {}
    group2 = {}
    for i in range(ord('a'), ord('z')+1):
        group1[chr(i)] = 0
        group2[chr(i)] = 0
    
    for i in s1:
        group1[i] += 1

    for i in s2:
        group2[i] += 1
    
    if group1 == group2:
        isAnagram = True
    else:
        isAnagram = False
    return isAnagram


a = "ethe"
b = "the"

c = anagramSolution(a,b)
if c:
    print("they are same")

else:
    print("they are not same")

# t1 = Timer("anagramSolution('ther','sdaf')", "from __main__ import anagramSolution")

# print("Total time is %f"%t1.timeit(number = 100))