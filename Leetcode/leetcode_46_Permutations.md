# 46. Permutations
* Question link  https://leetcode.com/problems/permutations/
* [leetcode_46_Permutations](./leetcode_46_Permutations.py)

## 解题思路：

1. 创建两个list， 一个是result，一个是临时存储

2. 方法，使用递归， 通过递归来进一步获取数值，注意递归后每个会进行pop， 一次来达到清空目标数值要求，比如， 123 中要通过pop，来清除掉添加的2，3， 只剩1， 从而可以继续132


4. 关键词： 全排列， 回溯，递归， permutation

5. 笔记参考 Notability Python Permutations