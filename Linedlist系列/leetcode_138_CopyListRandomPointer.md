# LinkedList 系列 -----删除指定值
## Question link  https://leetcode.com/problems/copy-list-with-random-pointer ##
## [leetcode_138_CopyListRandomPointer](./leetcode_138_CopyListRandomPointer.py): ##


## Hints:

1. 先把while 创造复制一遍Node, 只copy val, 其他两个为NULL. Node
即(cur.val, None, None)。

2. 搞清楚next， 跟 random 指向哪里

3. 重要思路 字典 dic，参考 https://www.youtube.com/watch?v=oXABtaRa37U&t=213s

    原Node为key， copy的node为value

4. random的对象是一个节点， 数组里面标志的的如[13,0]

5. 为什么要用dic[cur.random]

```python
    dic[cur].random = dic[cur.random]
```

cur.random 的值确实是我们要复制的节点， 但如果直接用等于则相当于新的random的节点指向旧的random的节点， cur.random的值等于 dic[cur.random]的值， 但从字典的思想里，cur.random是key，即旧的节点， dic[cur.random]是在value里， 新的节点

 
