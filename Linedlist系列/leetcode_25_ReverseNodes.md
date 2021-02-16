# 25. Reverse Nodes in k-Group
* Question link  https://leetcode.com/problems/reverse-nodes-in-k-group/
* [leetcode_25_ReverseNode](./leetcode_25_ReverseNodes.py)

## 解题思路：

1. 先分析，k代表着每一组变化的长度

2. 题目需求，将list分组进行反转，先写出reverse方法，将list分成几组，不着急连起来，当每段都分开排好序后，再连起来节点，注意判断最后分情况讨论，最后一个指针是指向不需要排序的数组，还是指向None. 全程应该注意指针位置和指向位置

3. 特殊要求 Memory复杂度为O(1)

4. 当前方法复杂度为 O(n^2)