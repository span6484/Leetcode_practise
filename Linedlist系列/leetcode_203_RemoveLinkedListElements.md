# LinkedList 系列 -----删除指定值
## Question link  https://leetcode.com/problems/remove-linked-list-elements/ ##
## [leetcode_203_RemoveLinkedListElements](./leetcode_203_RemoveLinkedListElements.py): ##

思路：
考虑多种情况：
* []          val: 1 
* [1]          val: 1 
* [1,1,1,1]          val: 1 
* [1,2]          val: 1
* [1,2,3,2]          val: 2 