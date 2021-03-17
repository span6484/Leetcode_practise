# Lab1

1. * for 第三个参数
   * **f** String formatter

```python
for celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = celsius // 5 * 9 + 32
    print(f'{celsius:7d}\t{fahrenheit:10d}')
```

```python
print(f"{name} is and {type} company")
```

We can also call a function inside

```python
def greet(name):
    return "Hello, " + name
## calling the function using f-string
name = "Datacamp"
print(f"{greet(name)}")
```



**关键词**：steps of 10.



2.    **关键词**：random， seek, randint(from, to)

   

   

   * Generate integer random

     ```python
     from random import Random
     a = Random()
     a.randint(from, to)
     ```

   * Question: what is '***Input a seed for the random number generator: 0'***used for

     Answer:

     * **seed()** 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
     * 我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。

     

```
import random

random.seed ( [x] )
```

```
output:
In [7]: random.seed(10)

In [8]: print(random.random())
0.5714025946899135

In [9]: random.seed(10)

In [10]: print(random.random())
0.5714025946899135

```





3. 关键词： sys, try, randrange, loop

   ```python
   from random import seed, randint, randrange
   import sys
   
   arg_for_seed = input('Input a seed for the random number generator: ')
   try:
       arg_for_seed = int(arg_for_seed)
   
       # 抛出整数异常
   except ValueError:		
       print('Input is not an integer, giving up.')
       sys.exit
   
   num = input('How many elements do you want to generate? ')
   ```

   ```python
   #快速随机生成-50到50的数并存在list里
   L = [randint(-50,50) for _ in range(element_num)]
   ```

   

```python
#能够快速锁定对应的区间的数量
intervals = [0]*4
for i in range(num):
    intervals[L[i] // 5] += 1

```

```python
#通过i index来锁定intervals中对应的数量，用i*5来实现区域的划分
for i in range(4):
    if intervals[i] == 0:
        print(f"There is no element between {i*5} and {i*5+4}.")
    if intervals[i] == 1:
        print(f"There is 1 element betwween {i*5} and {i*5+4}.")
    else:

        print(f"There are {intervals[i]} elements between {i*5} and {i*5+4}")   

```



4. 关键词： **standard deviation**, medium, **Square root**, function

   * calculation standard deviation

     * find mean

     * substract the mean and square the result

     * Add them and divde by N-1

     * ### Take the square root of that:

       Ex: find 9,2,5,4,12,7 standard deviation

       solution: the mean is (9+2+5+4+12+7) / 6 = 39/6 = 6.5

       ​				(9 - 6.5)^2 = (2.5)^2 = 6.25

       ​				(2 - 6.5)^2 = (-4.5)^2 = 20.25

       ​				(5 - 6.5)^2 = (-1.5)^2 = 2.25

       ​				(4 - 6.5)^2 = (-2.5)^2 = 6.25

       ​				(12 - 6.5)^2 = (5.5)^2 = 30.25

       ​				(7 - 6.5)^2 = (0.5)^2 = 0.25

       Sum = 6.25 + 20.25 + 2.25 + 6.25 + 30.25 + 0.25 = **65.5**

       Divide by **N**: (1/6) × 65.5 = **10.92**

        √(10.92) = **3.305...**

       So the standard deviation is 3.305		

   * Square root √￣

     √2￣ : 2**0.5

   * 保留2位数

     ```python
     print(f"standard deviation is {st_vaule:.2f}")
     ```

     

   - medium

     - 计算medium时， 需要将list 先sort， 返回中间数， 如果为复数， 返回 中间两数 相加 除以2的值

       ```
       # L is [2,3,1,4]
       # element_num is 
       L.sort()
       if element_num % 2:
           medium_val = L[element_num // 2]
       else:
           medium_val = (L[(element_num-1)//2] + L[element_num//2]) / 2
       ```

   - function

     ```python
     import statistics
     
     print(f'The mean is {mean(L):.2f}.')
     print(f'The median is {median(L):.2f}.')
     print(f'The standard deviation is {pstdev(L):.2f}.')
         
     ```

     