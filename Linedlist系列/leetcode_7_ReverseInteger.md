# Reverse Integer
* Question link  https://leetcode.com/problems/reverse-integer/
* [leetcode_706_DesignHashMap](./leetcode_7_ReverseInteger.py):
![leetcode_7](https://user-images.githubusercontent.com/37071362/98667157-29ecf000-23a2-11eb-8186-d7311418306c.PNG)


## 解题思路：

1. 转成str， 计算长度
2. 设置负数信号， 如果是负数， 取绝对值

3. 设置array，方便取出每一个存入, 比如 123 存入 [1,2,3]

4. 规律： 

根据长度， 判断为10**（len-1）次方 比如

```  
123 // 10**2 = 1    存入array

剩下的值为：

123-1*10**2 = 23

再重复

23 // 10**1 = 2  存入
。。。
。。。
```

5. 如果是负数， 返回值记得*-1
