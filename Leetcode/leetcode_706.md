# HashMap   
* Question link  https://leetcode.com/problems/design-hashmap/
* [leetcode_706_DesignHashMap](./leetcode_706_DesignHashMap.py):

* 设置一个dummy，可以检测Head，Hash Map使用案例与dictionary一样

# exampe    d[key, value]
d = dict()
d['steven'] = 10
d['Andy'] = 20
d.items()
d['steven']

hash("steven") % 20    得到所在的index
# hash-function 算出hash value， 然后去数组上取值, 会逼遍历找值更快， 一个人一个房间， O（1）