# 78. SubSets
* Question link https://leetcode.com/problems/subsets/
* [leetcode_78_subSets](./leetcode_78_subSets.py) <br>

## 解题思路：

1. 参照回溯模版
2. 通过num变化来进行一个个添加，

```
input： 【1，2，3】
output: 

[[],[1], [1,2], [1,2,3], [2], [2,3], [3]]

```

可以发现index不走回头路， 将一边遍历到底再折返


