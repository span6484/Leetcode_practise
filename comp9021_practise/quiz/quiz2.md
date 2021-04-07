# quiz2

## quesiton

```python
$ python3 quiz_2.py
Enter two integers: 0 4
The generated mapping is:
   {2: 3, 4: 1}
The keys are, from smallest to largest:
   [2, 4]
Properly ordered, the cycles given by the mapping are:
   []
The (triply ordered) reversed dictionary per lengths is:
{1: {1: [4], 3: [2]}}
```

```
$ python3 quiz_2.py
Enter two integers: 0 6
The generated mapping is:
   {1: 1, 3: 3, 5: 6, 6: 6}
The keys are, from smallest to largest:
   [1, 3, 5, 6]
Properly ordered, the cycles given by the mapping are:
   [[1], [3], [6]]
The (triply ordered) reversed dictionary per lengths is:
{1: {1: [1], 3: [3]}, 2: {6: [5, 6]}}
$ python3 quiz_2.py
```

```
Enter two integers: 0 11
The generated mapping is:
   {2: 7, 3: 11, 4: 10, 5: 10, 7: 2, 9: 5, 10: 10, 11: 5}
The keys are, from smallest to largest:
   [2, 3, 4, 5, 7, 9, 10, 11]
Properly ordered, the cycles given by the mapping are:
   [[2, 7], [10]]
The (triply ordered) reversed dictionary per lengths is:
{1: {2: [7], 7: [2], 11: [3]}, 2: {5: [9, 11]}, 3: {10: [4, 5, 10]}}
```



## Solution1:

1）找出circle， 最终的值能与键对应上，2:7， 7: 8， 8:2

思路： 设置array 用来临时储存符合条件的circle，设置 inital_key, 和circle key， 一个个往后面找， 当circle_key 等于initial_key， 则将array存入circle， 如果circle_value不存在或者等于array中的其他已经存在的其他数，则不是circle

```python
#{2:7， 7: 8， 8:2}
def return_circle(mapping):
    for i in mapping:
        if i == mapping[i]:
            cycles.append([i])
        else:
            #control the first time
            #initial_key = 2 , circle_key = 2, circle_value = 7
            #now the inital_key and circle_key are same, so, need to set the time to avoid 							the first time situation
            
            time = 0
            initial_key = i
            circle_key = i
            circle_value =mapping[circle_key]
            array = [initial_key]
            
            while circle_key != initial_key or time == 0:
                time += 1
                # circle_value = mapping[circle_key]
                if circle_value not in array and circle_value in mapping.keys():
                    circle_key = circle_value
                    circle_value = mapping[circle_key]
                    array.append(circle_key)
                else:
                    if circle_value == initial_key:
                        circle_key = circle_value
                        array = sorted(array)
                        if array not in cycles:
                            cycles.append(array)
                    
                    else:
                        array = []
                        break
    return cycles
```

2）将字典中的key 和 value，reverse，一个字典里面存字典， 外面的是重复值存在的个数，里面的则是key， key遇到重复的则存入arry，比如{7：2, 8 : 2}  ===> {2: 7, 2: 8} ===> {2:[7,8]}

​	思路：

1. 题目前面已经有了keys 数组， 将字典中 values 也取出作为数组 	keys： [7,8] values: [2,2] 

2. 双循环， 先通过 count 找到有多少个不同个数的值， 比如 {2:7, 2:8}中有2个重复的。将这些存入count_array
3. 外循环为count_array， 针对不同类别进行划分， 存储
4. 内循环为mapping元素个数, , 当values[i]的数量等于外循环reverse_index，则添加， 但需要 加个附加条件， 即这个值是否已经存在，如果已经存在， 那么就接在现有的数组里面接着存

```python
def return_reversed(original_mapping):
    value = list(mapping.values())
    value_len = len(value)
    count_arr = []
    for i in range(value_len):
        count_index = value.count(value[i])
        if count_index not in count_arr:
            count_arr.append(count_index)
    count_arr = sorted(count_arr)

    for reverse_index in count_arr:
        temp = {}
        for i in range(value_len):
            if value.count(value[i]) == reverse_index:
                if value[i] in temp.keys():
                    temp[value[i]].append(keys[i])
                else:
                    temp[value[i]]=[keys[i]]
        reversed_dict_per_length[reverse_index] = temp
    return reversed_dict_per_length	
```



## 本题遇见过的bug

1. ​	'int' object is not iterable

   iterable 可遍历的

   ```python
     value_len = len(keys)  
     for i in value_len:
           count_index = value.count(value[i])
           if count_index == 1:
               reversed_dict_per_length[count_index][value[i]]=keys[i] 
   ```

   

   ```
     File "quiz2.py", line 75, in <module>
       reversed_dict_per_length = return_reversed(mapping)
     File "quiz2.py", line 68, in return_reversed
       for i in value_len:
   TypeError: 'int' object is not iterable
   ```

   

   原因：

   value 前面要加range 在for中

   ```
     for i in range(value_len):
   ```

   

2. list 是有序的

   [1,2,3] != [3,2,1]

3. list 方法

   a = [1,2,2]

   a.count(2). == 2        //True