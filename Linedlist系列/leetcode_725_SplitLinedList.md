# HashMap   
* Question link  https://leetcode.com/problems/split-linked-list-in-parts/
* [leetcode_706_DesignHashMap](./leetcode_725_SplitLinedList.py):

## 解题思路：

1. 用字典进行存储， 将数值以key value 形式一一存入
2. 根据返回值可以判断，需返回一个二维数组，每个里面的数组是list形式，Tips： 每个存入array的list应该是独立的，即 .next = None

3. 如果root为，k=3，返回值为[[], [], []]

4. 分两种情况讨论
    + root的len < k
        + 规律: 一一打印， 其他none的数量为（k-len）
    ```
    root = [1,2,3]
    k = 5
    expect value: [[1],[2],[3],[],[]]
    ```
    + root的len >= k， 这也要分两种：
    ```
    root = [1,2,3,4,5]
    k = 3
    expect value: [[1,2],[3,4],[5]]
    ```
      + 规律: 
        + len % k 是 较多的数组的数量，比如 [1,2], [3,4] 一共2个
        + math.ceil(len/k) 是指有多少个较多的数组， 比如 [1,2]中 有2个元素
        + int(len/k) 是指有多少个较多的数组， 比如 [5]中 有1个元素
        
      + 当len % k != 0 时：
        + 使用双循环，外循环负责计算要append多少个较多的数组， 内循环负责往下走， 比如刚开始array为空，走到   <strong> 2</strong>时存起来为一个数组， 记住，数值2对应的Node.next = None， 这样子才能断开， 并且开启新的节点。 <br><br>
        这里使用point来帮助添加，因为head在一个一个往前走，需要point来指向每个array对应的head作为数组的起点

        + 剩余部分：
        采取相同的方法打印出剩下的节点，同样用point， 这里head因为没有重置，所以可以继续走一直走完整个节点

    + 最终直接返回数组即可
    
    
