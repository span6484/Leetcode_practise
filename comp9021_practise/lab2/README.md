# Lab2 



### calculate factorial of n: n!

n! = 1 * 2 * 3 * ... * n

```python
import math
n = 3
print(math.factorial(n)) 
```

```
output: 6
```



Power of 5: 5 的次方

```python
def third_computation(x):
    nb_of_trailing_0s = 0
    power_of_five = 5
    while x >= power_of_five:
        nb_of_trailing_0s += x // power_of_five
        power_of_five *= 5
    return nb_of_trailing_0s
```



```python
try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
```





### Q2

```python
for i in range(2, N + 1):
    # 1 divides i, so counts for one divisor.
    # It is enough to look at 2, ..., i // 2 as other potential divisors.
    if 1 + sum(j for j in range(2, i//2+1) if i % j == 0) == i:
        print(i, 'is a perfect number.')

```

注意写法，j for j in range(2, i//2+1)





### Q3

问题解释：

这道题目给了一个固定的乘法形式， 寻找每列相加都一样的数字

比如 411*13

​	 4 				1  				   1

x.    				 1  					3

---

1 2				3						3

4	1		     1 

----

5	3			4							3



Sum1 :   1+3+3+3= 10

Sum2 :   1+1+3+1+4 = 10

Sum3:   4+ 2 + 1 + 3 = 10

Sum4 : 1 + 4 + 5 = 10



老师的思路是：

嵌套循环来遍历所有符合条件的数

```python
for i in range(100, 1000):
	for j in range (10, 100):
```



设置 第一行 product0， 第二行product 1 值 ,

 ```python
product0 = i * (j % 10) 
product1 = i * (j // 10)
 ```

23 = 23//10 + 23%10



因为题目说了 形式固定， 所以通过continue 来排除不符合的条件，

```
if product0 < 1000：
	continue
if product1 >= 1000:
	continue
```

 总数sum 就等于 total = product0 + 10 * product、

第一列相加： 不包含product1

```
the_sum = i % 10 + y % 10 + product0 % 10 + total % 10
```

第二列相加：

```
i//10%10 + j // 10 + product0 // 10 % 10 + product1 % 10 + total // 10% 10
```



第三列相加： 不含j

```
j //100 + product0 // 100 + product1 // 10 % 10 + total// 100 % 10
```



最后一行：

```
product0 // 1000 + product1 // 100 + total// 1000
```





### Q4

 Bayes-Price theorem 条件概率

> describes the [probability](https://en.wikipedia.org/wiki/Probability) of an [event](https://en.wikipedia.org/wiki/Event_(probability_theory)), based on prior knowledge of conditions that might be related to the event.



![image-20210323101048956](/Users/shaoqiupan/Library/Application Support/typora-user-images/image-20210323101048956.png)



概率： 

大量同类事件， 可重复发生N次

事件A, 发生 M 次

p(A) = M/N

Ex:  10000个 男性，  男性里有300 个色盲， P(A) = 300 / 10000



贝叶斯公式：

酒鬼在A B C 三个酒吧 喝酒概率是30%平均， 在家是10%

警察查2个酒吧

A1: 酒吧喝酒 			 A2: 家

B1: 被抓			B2:  未抓

P(B1|A1) :   条件概率， 这里是指在酒吧喝酒的情况下被抓的概率 => 2/3      

P(B2|A2): 在家情况喝酒被抓概率， => 1。因为在家，不可能被抓



P(A1 | B2) =  p (A1) P(B2|A2)    / p (A1) p (B2|A1) + P(A2)P(B2| A2) :

解释： P(A1 | B2):  酒吧喝酒没有被抓

​		p (A1) P(B2|A2) 		: 喝酒 并且在喝酒情况下没有被抓的概率

 p (A1) p (B2|A1) + P(A2)P(B2| A2) ：  喝酒 并且在喝酒情况下没有被抓的概率 + 在家里并且在家喝酒没被抓概率

分子： 喝酒没被抓  分母 没被抓  



= （0.9 * （1/3）） / [(0.9 * （1/3）） + 0.1*1]



