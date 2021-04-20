# 7. Reverse Integer
**Easy**         30min



Given a signed 32-bit integer `x`, return `x` *with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.



**Example 1:**

```
Input: x = 123
Output: 321
```

**Example 2:**

```
Input: x = -123
Output: -321
```

**Example 3:**

```
Input: x = 120
Output: 21
```

**Example 4:**

```
Input: x = 0
Output: 0
```

### 解题思路：

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

6. 第二次做的时候我加入了array[-1: -(len(temp+1))]的想法， 将array直接从尾部开始便利，更方便的判断首字母是否为0的情况

```python
        for i in range(-1,-(len(temp)+1), -1):
            if temp[i] == 0 and no_head:
                continue
            else:
                no_head = False
                # array.append(temp[i])
                val += int(temp[i])*10**index
                index -= 1
```



### 遇到bug

```python
    def reverse(self, x: int) -> int:
        temp = x +''
```

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```



```shell
Input:
1563847412
Output:
2147483651
Expected:
0
```





### Solution (1nd)

```python
class Solution:
    def reverse(self, x: int) -> int:
        
        if(x>2**31-1 or x<-2**31):
            return 0
        
        if(x<0):
            sign = True
            x = -1 * x
        else:
            sign = False
            
        arr = []    
        a = str(x)
        strlen = len(a)
        
        index = strlen - 1
        
        while index != -1:
            arr.append(x//10**index)
            x = x - x//10**index * 10**index
            index -= 1
            
        new_value = 0
        for i in range(0, strlen):
            new_value += arr[i] * 10**i
        
        if (sign == True):
            new_value = -1*new_value
        
        if(new_value>2**31-1 or new_value<-2**31):
            return 0
        return new_value
        
```



### Solution (2nd)

```python
  class Solution:  
    def reverse(self, x: int) -> int:
          if x < -2**31 or x > 2**31 - 1:
              return 0
          temp = str(x)
          if len(temp) == 1:
              return x
          # array = []
          if temp[0] == '-':
              sign = -1
              temp = temp[1:]
          else:
              sign = 1
          val = 0
          index = len(temp)-1
          no_head = True
          for i in range(-1,-(len(temp)+1), -1):
              if temp[i] == 0 and no_head:
                  continue
              else:
                  no_head = False
                  # array.append(temp[i])
                  val += int(temp[i])*10**index
                  index -= 1
          val *= sign
          if val < -2**31 or val > 2**31 - 1:
              return 0
          return val
```

