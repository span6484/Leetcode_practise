# Find All Anagrams in a string           
* Question link  https://leetcode.com/problems/design-hashmap/
* [leetcode_438_Find_All_Anagrams_In_A_String](./leetcode_438_Find_All_Anagrams_In_A_String.py):

* 设置一个dummy，可以检测Head，Hash Map使用案例与dictionary一样

## Exampe：    d[key, value]
d = dict()

d['steven'] = 10

d['Andy'] = 20

d.items()

d['steven']

hash("steven") % 20    ----->得到所在的index
### hash-function 算出hash value， 然后去数组上取值, 会比遍历找值更快， 一个人一个房间， O（1）