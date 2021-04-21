# Fibonacci

Recall that the Fibonacci numbers can be calculated using a recursive algorithm. However, the language runtimes of many programming languages, such as Java, have limitations which effectively limit the depth to which recursive method calls can go, at which point a `java.lang.StackOverflowError` would be thrown. Instead of writing recursive code, which is then executed by the language runtime using an internal stack, the programmer can write the function iteratively, accessing an explicit stack within their code.

The Fibonacci number sequence is defined by:

![image](https://user-images.githubusercontent.com/37071362/115527423-9eb64580-a2c3-11eb-9e35-c5f824060ea4.png)



Implement the `getSequence` method in either the Python or Java scaffold provided, without using recursion.

It should return the stack containing the Fibonacci numbers from f(0)*f*(0) up to and including f(n)*f*(*n*), with f(n)*f*(*n*) as the top element.

For example:

`getSequence(3)` should return the stack containing (0, 1, 1, 2) (in that order; bottom to top), and

`getSequence(5)` should return a stack containing (0, 1, 1, 2, 3, 5).



### Output sample:

```python
enter 5
0
1
deque([0, 1, 1])
1
1
deque([0, 1, 1, 2])
1
2
deque([0, 1, 1, 2, 3])
2
3
deque([0, 1, 1, 2, 3, 5])
```







### 解题思路

我们不被允许使用递归， 让复杂度为O(n) ，借助deque思想来做， 因为f(n) = f(n-1) + f(n-2), 我们可以在deque中append0， 1， 再通过index依次向后相加



## Solution



```python
# The stack implementation in python you should use in this exercise
# is collections.deque. There are a few differences between the Stack ADT
# in lectures and the python implementation using collections.deque:
# Stack ADT       Equivalent using a collections.deque as a stack in python:
# push(element)   append(element)
# pop()           pop()
# peek()          look at element at index -1
# size()          len(deque)
# isEmpty()       There are a few ways of checking this, however no specific function.
#                 e.g. checking if the length of the deque [ len(deque) ] is 0
from collections import deque

def get_sequence(n):
    """Gets the fibonacci sequence from f(0) up to and including f(n).
    If n is negative, it returns an empty stack.

    Args:
        n: The maximum fibonacci number to compute.

    Returns:
        A Stack [implemented using a deque] containing the fibonacci numbers
        from f(0) up to and including f(n).
        For example for n = 3, it returns deque([0, 1, 1, 2])
    """
    # TODO: Implement this.
    stack = deque()
    index1 = 0
    index2 = 1
    for i in range(n+1):
        if i < 2:
            stack.append(i)
            continue
        sum = stack[index1] + stack[index2]
        stack.append(sum)
        index1 += 1
        index2 += 1
    return stack

```

