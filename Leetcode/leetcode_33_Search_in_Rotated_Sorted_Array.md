# BinarySearch 找指定值思路：
## Question link  https://leetcode.com/problems/search-in-rotated-sorted-array/ ##
## [leetcode_33_Search_in_Rotated_Sorted_Array.py](./leetcode_33_Search_in_Rotated_Sorted_Array.py): ##

* 需要找出所有-1的情况并报出

* 分情况讨论有序和无序：
    + 有序的情况有两种： [1,2,3,4,5]
        1. target在mid位置之前
        2. target在mid位置之后
    + 无序的情况：    [3,4,5,1,2] target = 1
        1. 先比较target与end，分情况讨论
        2. 当target小于位置时， 比较mid与end大小，再次分情况讨论， 判断mid与target大小， 从而得到mid，target，end具体位置
        3. 进一步考虑向哪个方向进行二分搜索

        比如，mid是 5， target是 1， end是 2， 根据比较得出应该 search（mid+1， end， 因为 target 在mid与end之间

* 重点是要清楚target 与 mid 与 end 三者关系
        