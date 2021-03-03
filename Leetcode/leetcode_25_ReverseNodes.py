
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        

        if k == 1:
            return head
        # 每组实际更改次数，第一个为0
        lenEachGroup = k-1

        # List length
        len_list = 0
        h1 = head

        while h1 != None:
            len_list += 1
            h1 = h1.next

        # Group Nums 
        groupNums = int(len_list/k)

        #old next就是 new head
        old_next = None
        # 循环
        h2 = head
        i = 0
        # i = 1
        while(i < groupNums):
            
            # k为1不需要任何变化
            j = 0
            
            #设置一个动态的node名字，
            #想法： 每一组先排好序， 不着急链接，设置一个动态的变量名作为链接点，最后通过循环统一链接·

            connect_Node = h2
            while(j < lenEachGroup):
                
                # 即将作为next的值
                new_next = h2

                #仅作用第一次获得old_next值
                # if(old_next == None):
                if(j == 0):
                    old_next = h2.next
                h2 = old_next

                #控制最后一次old_next存在的位置，当来到最后一次old next 不会再次前进
                # if(j < lenEachGroup-1):
                if(h2.next != None):
                    old_next = h2.next
                
                h2.next = new_next
                j += 1

        # 通过pre_connectNode和connectnode 链接每一组排好序的list， connectnode是每一组的末尾和开头
            if(i == 0):
                head = h2
                pre_group_connetNode = connect_Node
            if(i>0):
                pre_group_connetNode.next = h2
            h2 = old_next
            pre_group_connetNode = connect_Node

            i += 1

        # 判断，如果不是整数，说明后面有不变的list需要接上， 如果是整数，末尾添加none
        if (len_list/k > groupNums):
            connect_Node.next = h2
        else:
            connect_Node.next = None

        return head


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if k == 1:
            return head
        # 每组实际更改次数，第一个为0
        lenEachGroup = k-1

        # List length
        len_list = 0
        h1 = head

        while h1 != None:
            len_list += 1
            h1 = h1.next

        # Group Nums 
        groupNums = int(len_list/k)

        #old next就是 new head
        old_next = None
        # 循环
        h2 = head
        i = 0
        # i = 1
        while(i < groupNums):
            
            # k为1不需要任何变化
            j = 0
            
            #设置一个动态的node名字，
            #想法： 每一组先排好序， 不着急链接，设置一个动态的变量名作为链接点，最后通过循环统一链接·

            connect_Node = h2
            while(j < lenEachGroup):
                
                # 即将作为next的值
                new_next = h2

                #仅作用第一次获得old_next值
                # if(old_next == None):
                if(j == 0):
                    old_next = h2.next
                h2 = old_next

                #控制最后一次old_next存在的位置，当来到最后一次old next 不会再次前进
                # if(j < lenEachGroup-1):
                if(h2.next != None):
                    old_next = h2.next
                
                h2.next = new_next
                j += 1

        # 通过pre_connectNode和connectnode 链接每一组排好序的list， connectnode是每一组的末尾和开头
            if(i == 0):
                head = h2
                pre_group_connetNode = connect_Node
            if(i>0):
                pre_group_connetNode.next = h2
            h2 = old_next
            pre_group_connetNode = connect_Node

            i += 1

        # 判断，如果不是整数，说明后面有不变的list需要接上， 如果是整数，末尾添加none
        if (len_list/k > groupNums):
            connect_Node.next = h2
        else:
            connect_Node.next = None

        return head


    class Rick's Solution(object):

        def reverseKGroup(self, head, k):
            """
            :type head: ListNode
            :type k: int
            :rtype: ListNode
            思路:
            1. dummy肯定是要的
            2. defend k==1
            3. general:
                产生一个group:
                    足够k个则返回k个, 不足则告知不足
                    翻转一个group后, 接上prev, 接上next
                    不足则直接break.  如果next为空, 也break.
            """
            if k == 1:
                return head
            
            prev = dummy = ListNode(None)
            dummy.next = head
            rem = head
            while rem:
                ghead, rem, enough = self.return_group(rem, k)
                if enough:
                    new_head = self.reverse(ghead)
                    prev.next = new_head
                    prev = ghead # currently ghead is the last node of new_head
                    prev.next = rem
            return dummy.next

        def return_group(self, head, k):
            """
            "返回[head, cur]作为k group, 如果k不足, 会告知caller不足"
            采用双闭区间的话, 如果为right边界为None, 则判断为not enough
            """
            k = k - 1
            enough = True
            cur = head
            while k and cur:
                cur = cur.next
                k -= 1
            if not cur:
                return head, None, not enough
            else:
                rem = cur.next
                cur.next = None
                return head, rem, enough
            

        def reverse(self, head):
            "翻转链表"
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
if __name__ == "__main__":
    
    h1 = ListNode(1)
    h2 = ListNode(2)
    h3 = ListNode(3)
    h4 = ListNode(4)
    h5 = ListNode(5)
    h6 = ListNode(6)
    h7 = ListNode(7)
    h8 = ListNode(8)
    h9 = ListNode(9)

    h1.next = h2
    h2.next = h3
    h3.next = h4
    h4.next = h5
    h5.next = h6
    h6.next = h7
    h7.next = h8
    h8.next = h9

    k = 3
    h1 = Solution().reverseKGroup(h1, k)

    while h1.next!= None:
        print(str(h1.val)+"->", end = '')
        h1= h1.next
    print(str(h1.val))

    
    