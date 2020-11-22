# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp = 0
        newHead = ListNode(0)
        start = newHead
        h1 = l1
        h2 = l2
        
        while h1 != None and h2 != None:
            val = h1.val + h2.val+temp
            temp = 0
            
            if(val >= 10):
                temp += 1
                h3 = newHead
                newHead = ListNode(val-10)
                h3.next = newHead
            
            else:
                h3 = newHead
                newHead = ListNode(val)
                h3.next = newHead
                
            h1 = h1.next
            h2 = h2.next
            
        while h1 != None:
            val = h1.val+temp
            temp = 0
            
            if(val >= 10):
                temp += 1
                h3 = newHead
                newHead = ListNode(val-10)
                h3.next = newHead
            
            else:
                h3 = newHead
                newHead = ListNode(val)
                h3.next = newHead
            
            h1 = h1.next
 
        while h2 != None:
            val = h2.val+temp
            temp = 0
            
            if(val >= 10):
                temp += 1
                h3 = newHead
                newHead = ListNode(val-10)
                h3.next = newHead
            
            else:
                h3 = newHead
                newHead = ListNode(val)
                h3.next = newHead
            
            h2= h2.next
            
        if(temp != 0):
            
            h3 = newHead
            newHead = ListNode(temp)
            h3.next = newHead
            
        return start.next
        

class SolutionImproved_1:
    # Note: 技巧--变量替换
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp = 0
        newHead = ListNode(0)
        start = newHead
        h1 = l1
        h2 = l2
        
        # 合并公共部分
        while h1 != None and h2 != None:
            val = h1.val + h2.val+temp
            temp = 0
            
            if(val >= 10):
                temp += 1
                h3 = newHead
                newHead = ListNode(val-10)
                h3.next = newHead
            
            else:
                h3 = newHead
                newHead = ListNode(val)
                h3.next = newHead
                
            h1 = h1.next
            h2 = h2.next
            
        # 合并剩余部分
        rem_head = h1 if h1 != None else h2             
        while rem_head != None:
            val = rem_head.val+temp
            temp = 0
            
            if(val >= 10):
                temp += 1
                h3 = newHead
                newHead = ListNode(val-10)
                h3.next = newHead
            
            else:
                h3 = newHead
                newHead = ListNode(val)
                h3.next = newHead
            
            rem_head = rem_head.next
 
        # while h2 != None:
        #     val = h2.val+temp
        #     temp = 0
            
        #     if(val >= 10):
        #         temp += 1
        #         h3 = newHead
        #         newHead = ListNode(val-10)
        #         h3.next = newHead
            
        #     else:
        #         h3 = newHead
        #         newHead = ListNode(val)
        #         h3.next = newHead
            
        #     h2= h2.next
            
        if(temp != 0):
            
            h3 = newHead
            newHead = ListNode(temp)
            h3.next = newHead
            
        return start.next



class SolutionRickImproved_2:
    # Note1: 进位叫做`carry`
    # Note2: 提炼出 add_helper
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        # h3: tail of return list
        h3 = dummy_head = ListNode(0)
        h1 = l1
        h2 = l2

        # 合并公共部分
        while h1 != None and h2 != None:
            digit_sum = h1.val + h2.val + carry
            
            h3,carry = self.add_helper(digit_sum, h3)

            h1 = h1.next
            h2 = h2.next

        # 合并剩余部分
        rem_head = h1 if h1 != None else h2
        while rem_head != None:
            digit_sum = rem_head.val+carry
            
            h3,carry = self.add_helper(digit_sum, h3)
            
            rem_head = rem_head.next
            
        if(carry != 0):
            h3.next = ListNode(carry)
            
        return dummy_head.next

    # add a node after h3
    def add_helper(self, val, h3):
        carry=0
        if(val >= 10):
            carry = 1
            newHead = ListNode(val-10)
        else:
            newHead = ListNode(val)
        h3.next = newHead
        return newHead, carry