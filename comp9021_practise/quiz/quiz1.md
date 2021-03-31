# Quiz1

### 题目

**QUIZ 1**

COMP9021 PRINCIPLES OF PROGRAMMING

```
$ python3 quiz_1.py
Enter two integers: 0 4
The generated mapping is:
   {3: 1}
```



```
The mappings's so-called "keys" make up a set whose number of elements is 1.
The list of integers between 1 and 4 that are not keys of the mapping is:
   [1, 2, 4]
Represented as a list, the mapping is:
   [None, None, None, 1, None]
The one-to-one part of the mapping is:
   {3: 1}
$ python3 quiz_1.py
Enter two integers: 0 8
The generated mapping is:
   {2: 4, 3: 8, 4: 7, 5: 7}
The mappings's so-called "keys" make up a set whose number of elements is 4.
The list of integers between 1 and 8 that are not keys of the mapping is:
   [1, 6, 7, 8]
Represented as a list, the mapping is:
   [None, None, 4, 8, 7, 7, None, None, None]
The one-to-one part of the mapping is:
   {2: 4, 3: 8}
```

1. seed

   用来固定住random， 需要从 random包导入， 可以理解成一个固定公式锁定输入值

   ex：seed（12）

2. 本题给定位为前提条件：

   - enter的两个数都要+1， 并且randrange(n+1 // 2, N)， (n+1)//2

   - enter的第一个数为seed（）中的固定值
   - enter的第二个数为randrange的end value

### 第一遍做

```python
# 没有看学校给定条件
from random import randrange, seed

try:
    seed_arg, end_val = input("Enter two integers: ").split()
except ValueError:
    print("Please enter both value equal or more than 0")


seed_arg = int(seed_arg) + 1
end_val = int(end_val) + 1

seed(seed_arg)
map = dict()
no_key = []
time = 0
array = list()
array.append("None")
for i in range(1, end_val):
    value = randrange(-end_val // 2, end_val)
    if value > 0:
        map[i] = value
        time += 1
        array.append(value)
    else:
        no_key.append(i)
        array.append("None")

print(f"The generated mapping is: \n{map}")
print(f"The mappings's so-called 'keys' make up a set whose number of elements is \n{time}")
print(f"The list of integers between 1 and 16 that are not keys of the mapping is:\n{no_key}")
print(f"Represented as a list, the mapping is:\n{array}")

del_index = list()
for i in map:
    for j in map:
        if map[i] == map[j] and i != j:
            if i not in del_index:
                del_index.append(i)
            if j not in del_index:
                del_index.append(j)
for i in del_index:
    del map[i]
print(f"The one-to-one part of the mapping is: {map}")
```



- 找one-to-one时出现了卡顿， 如何将所有重复的对应的dic删除

  solve： 通过设置一个array来存入待删除的index， 如果存在， 不反复存入



答案：

```python
def return_nonkeys(upper_bound,mapping):
    for i in range(1,upper_bound):
        if i not in list(mapping.keys()):
            nonkeys.append(i)

    return nonkeys

def return_none(upper_bound,mapping):
    length = upper_bound
    for i in range(length):
        mapping_as_a_list.append(mapping.get(i))

    return mapping_as_a_list

def return_one_to_one(mapping):
    temp = []
    mapping_list = list(mapping.items())
    values_list = list(mapping.values())
    for i in range(0,len(values_list)):
        if (values_list.count(values_list[i])) != 1:
            temp.append(i)
    for index in sorted(temp, reverse = True):
        del mapping_list[index]

    return dict(mapping_list)
```



- List 有count 方法 能得到有多少个值

  ```
  a = [1,2,1,1]
  a.count(1)
  ```

  

- return_one_to_ 一样的写法， 不过这是个更省内存

  ```
      for index in sorted(temp, reverse = True):
          del mapping_list[index]
  ```

  