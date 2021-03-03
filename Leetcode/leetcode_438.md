# Find All Anagrams in a string           

[Question link](https://leetcode.com/problems/design-hashmap/)

[leetcode_438_Find_All_Anagrams_In_A_String ](./leetcode_438_Find_All_Anagrams_In_A_String.py)

[时间复杂度](https://www.bigocheatsheet.com/)

需要用hashMap 不然会超时， 这道题目时间复杂度要求为O(n), 不可以使用嵌套循环， 不可以使用sort<br />


# 解题思路过程
## 第一次思路       
排序：
取出数组对应的长度，将对应数组排序与target对比，一个个往后 <br />
Error， runtime too long）


## 第二次思路
使用dict， 将字母为key，字母出现频率为value， 进行对比
发现字典内顺序不同也可以，不需要一个key一个key进行对比
```python
arr1 = dict()
arr2 = dict()
# {'a': 2, 'b': 4}
arr1['a'] = 2
arr1['b'] = 4 
# {'b': 4, 'a': 2}
arr2['b'] = 4
arr2['a'] = 2
arr1 == arr2 #True
```
Error:  Run time Too long
调用了创建dict的function，for再次嵌套导致复杂度提高

问题： 如何创建字典并且依次前进只有for，不嵌套