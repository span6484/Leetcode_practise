
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
            #想法： 每一组先排好序， 不着急链接，设置一个动态的变量名作为链接点，最后通过循环统一链接

            # exec('connect_Node{} = {}'.format(i,h2))
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
                # new_next.next = old_next
                # if(i == 0):
                #     head = h2
                # 刚开始需要指向一个none
                # if (j == 0):
                #     new_next.next = dummy_head
                j += 1

            if(i == 0):
                head = h2
                pre_group_connetNode = connect_Node
            if(i>0):
                pre_group_connetNode.next = h2
            h2 = old_next
            pre_group_connetNode = connect_Node

            

            i += 1

        if (len_list/k > groupNums):
            connect_Node.next = h2
        else:
            connect_Node.next = None
            


            
        
        return head


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

    
    