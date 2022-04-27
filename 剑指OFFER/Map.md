

1. Collection的操作中每次保存的对象都是一个对象，但是在Map集合中保存的是一对对象，对象的形式是以：**key—>value**的形式保存的。就好像通讯录一样的。

##### Map接口中的方法

1、public void clear() 普通 清空Map集合。
2、public boolean containsKey(Object key)普通，判断指定的key是否存在。
3、public boolean containsValue(Object value) 普通 判断指定的value是否存在。
4、public Set<Map.Entry<K, V>>  entrySet()普通 将Map集合变为Set集合。
5、public boolean equals(Object o) 对象比较。
6、public V get(Object key)  普通 根据key取value。
7、public int hashCode() 普通 返回哈希码。
8、public boolean isEmpty() 普通 判断集合是否为空。
9、public Set<K> keySet()  普通  取得所有的key。
10、public V put(K key, V value) 向集合中加入元素。
11、public void putAll(Map<? extends K, ? extends V>  t) 普通 将一个Map集合中的内容加入到另一个Map中。
12、public V remove(Object key)根据key删除value。
13、public int size() 普通  取出集合的长度。
14、public Collection<V> values() 普通 取出全部的value。

##### Map接口的常用子类：

**HashMap**：无序存放的，是新的操作类，key不允许重复， 遍历时取到的是随机的， 不支持多线程同步
**Hashtable**：无序存放的，是旧的操作类，key值不允许重复， 不允许为空
**TreeMap**：可以排序的Map集合，按集合中的key排序，key值不允许重复，实现SortMap接口，能够把它保存的记录根据键排序,默认是按键值的升序排序，也可以指定排序的比较器，当用Iterator 遍历[TreeMap](https://so.csdn.net/so/search?q=TreeMap&spm=1001.2101.3001.7020)时，得到的记录是排过序的。
**WeakHashMap**：弱引用的Map集合，当集合中的某些内容不再使用时，可以清除掉无用的数据，可以使用gc进行回收。

**LinkedHashMap** 是HashMap的一个子类，保存了记录的插入顺序，在用Iterator遍历[LinkedHashMap](https://so.csdn.net/so/search?q=LinkedHashMap&spm=1001.2101.3001.7020)时，先得到的记录肯定是先插入的.也可以在构造时用带参数，按照应用次数排序。在遍历的时候会比HashMap慢，不过有种情况例外，当HashMap容量很大，实际数据较少时，遍历起来可能会比 LinkedHashMap慢，因为LinkedHashMap的遍历速度只和实际数据有关，和容量无关，而HashMap的遍历速度和他的容量有关。

**IdentityHashMap：key**可以重复的Map集合。

