# 704. Binary Search
* Question link  https://leetcode.com/problems/binary-search/
* [leetcode_706_DesignHashMap](./leetcode_704_BinarySearch.py)

## 解题思路：

1.  binary search 也叫折半查找， 一次搜索一半， k=log2n,（是以2为底，n的对数），所以时间复杂度可以表示O()=O(logn)

2. 循环条件，当 left + 1 < right , 则终止循环