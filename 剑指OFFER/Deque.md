

## JAVA 栈，为什么要使用Deque，而不推荐使用Stack，Deque中ArrayDeque与LinkedList的区别，Deque方法详解

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020053121015811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0MDEzNjI5,size_16,color_FFFFFF,t_70)



### 为什么不推荐使用Stack？

因为Vector是当初JAVA曾经写得不太行的类，所以Stack也不太行。

Vector不行是因为效率不太行，很多方法都用了synchronized修饰，虽然线程安全，但是像ArrayDeque,[LinkedList](https://so.csdn.net/so/search?q=LinkedList&spm=1001.2101.3001.7020)这些线程不安全的，在需要安全的时候也可以用Collections.synchronizedCollection()转化成线程安全的，所以Vector就没什么用处了

再根据仿生学
Stack只能上进上出，有点像刺胞动物（腔肠动物），就是那种从哪里吃进去就哪里拉出来的那种生活在海洋里的比较低级的生物。
[Deque](https://so.csdn.net/so/search?q=Deque&spm=1001.2101.3001.7020)上进上出，上进下出，甚至下进上出，非常上流，只有你想不到，没有我Deque做不到的。

现在不会还有人不知道使用栈的时候选谁吧？



### ArrayDeque与LinkList区别：

###### ArrayDeque：

- 数组结构
- 插入元素不能为null
- 无法确定数据量时，后期扩容会影响效率

###### LinkList：

- 链表结构
- 插入元素能为null
- 无法确定数据量时，有更好表现





## Deque中常用方法:

以这2个为基础整出来的Deque除了结构不一样，方法都一样的。

###### 把Deque当栈用的时候：

|          |                                                         |
| -------- | ------------------------------------------------------- |
| 入栈     | push(E e)                                               |
| 出栈     | poll() / pop() 后者在栈空的时候会抛出异常，前者返回null |
| 查看栈顶 | peek() 为空时返回null                                   |

###### 把Deque当队列用的时候：

|          |                       |
| -------- | --------------------- |
| 入队     | offer(E e)            |
| 出队     | poll() 为空时返回null |
| 查看队首 | peek() 为空时返回null |



------

有些时候需要进行一些骚操作的时候（比如取得栈底元素，取得队尾元素），这些常规操作就不能满足了。
下面就是Deque中一些更详细的方法。

###### 从上面(头部)插入：

| 方法名                  | 作用                                                         |
| ----------------------- | ------------------------------------------------------------ |
| void addFirst(E e)      | 将指定的元素插入此双端队列的前面 ，空间不足抛异常            |
| boolean offerFirst(E e) | 将指定的元素插入此双端队列的前面 ，空间不足插入失败返回回false |
| void push(E e)          | 将指定的元素插入此双端队列的前面 ，空间不足抛异常            |

###### 从上面(头部)出来/观察:

| 方法名          | 作用                                                      |
| --------------- | --------------------------------------------------------- |
| E removeFirst() | 检索并删除第一个元素，为空时抛出异常                      |
| E remove()      | 和removeFirst一样 检索并删除第一个元素，为空时抛出异常    |
| E pop()         | 和removeFirst一样 检索并删除第一个元素，为空时抛出异常    |
| E pollFirst()   | 检索并删除第一个元素 ，为空时返回null                     |
| E poll()        | 和pollFirst一样 检索并删除第一个元素 ，为空时返回null     |
| E getFirst()    | 只看看第一个元素 ，不出来，为空就抛异常                   |
| E element()     | 和getFirst一样 只看看第一个元素 ，不出来，为空就抛异常    |
| E peekFirst()   | 只看看第一个元素 ，不出来，为空时返回null                 |
| E peek()        | 和peekFirst一样 只看看第一个元素 ，不出来，为空时返回null |

###### 从下面(尾部)插入：

| 方法名                 | 作用                                                |
| ---------------------- | --------------------------------------------------- |
| void addLast(E e)      | 将指定的元素插入此双端队列的后面 ，空间不足抛异常   |
| boolean offerLast(E e) | 将指定的元素插入此双端队列的后面，空间不足返回false |
| boolean add(E e)       | 将指定的元素插入此双端队列的后面，空间不足抛异常    |
| boolean offer(E e)     | 将指定的元素插入此双端队列的后面，空间不足返回false |

###### 从下面(尾部)出来/观察:

| 方法名         | 作用                                        |
| -------------- | ------------------------------------------- |
| E removeLast() | 检索并删除最后一个元素，为空时抛出异常      |
| E pollLast()   | 检索并删除最后一个元素 ，为空时返回null     |
| E getLast()    | 只看看最后一个元素 ，不出来，为空就抛异常   |
| E peekLast()   | 只看看最后一个元素 ，不出来，为空时返回null |