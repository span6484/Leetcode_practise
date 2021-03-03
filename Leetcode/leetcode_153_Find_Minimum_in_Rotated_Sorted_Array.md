# binarysearch 找最小值 思路  
* Question link  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
* [leetcode_153_searchMin.py](./leetcode_153_searchMin.py):

举例 数组[3,4,5,1,2] 
* 先判断向哪边切割， 找出最初的mid，并将这个mid根据情况设置成start，还是end
* 如果是有序数组，nums[0] 就是最小的
* 如果是乱序数组， 找到乱序数组中最小数所在的有序数组 比如 [3,4,5,1,2]中找到 [1，2]数组并且返回第一个数字即1对应的序列  