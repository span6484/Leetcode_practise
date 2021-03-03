# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        array = []
        if(root == None):
            for i in range(0,k):
                array.append(root)
                
            return array
        dic = {}
        head = root
        len = 0
        while head != None:
            dic[head] = ListNode(head.val)
            len += 1
            head = head.next
            
        head = root
        #设置一个point是因为head会随着变化， point用来指着array什么时候插入
        point = head 
        # 处理[1,2,3] k = 5 这种情况    
        if len<k:
            num_null = k-len
            while head != None:
                    array.append(dic[head])
                    head = head.next
            for i in range(0,num_null):
                array.append(None)
                
        
        else:
            #向上取整 ceil
            numInside_MoreeachspliteList= math.ceil(len/k)   
            # 向下取整 int()
            numInside_elseEachspliteList = int(len/k)
            num_MoreeachspliteList = len%k
            num_elseEachspliteList = k- num_MoreeachspliteList
            if(len%k != 0):
                for i in range(0,len%k):
                    for j in range(0, numInside_MoreeachspliteList):
                        if (j == numInside_MoreeachspliteList-1):
                            dic[head].next = None
                            break
                        dic[head].next = dic[head.next]
                        head = head.next

                    array.append(dic[point])
                    if (head.next != None):
                        head = head.next
                        point = head
            
            if(num_elseEachspliteList != 0):            
                for i in range(0, num_elseEachspliteList):
                    for j in range(0, numInside_elseEachspliteList):
                        if (j == numInside_elseEachspliteList-1):
                            dic[head].next = None
                            break
                        dic[head].next = dic[head.next]
                        head = head.next

                    array.append(dic[point])
                    if (head.next != None):
                        head = head.next
                        point = head
                
        return array