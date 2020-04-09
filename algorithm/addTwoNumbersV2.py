# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        jinwei = 0
        dummyRoot = ListNode(0)
        
        new_list_ptr = dummyRoot
        while True:
            
            if ptr1 is None and ptr2 is None:
                break
                
            num1 = 0
            num2 = 0
            
            if ptr1:
                num1 = ptr1.val
            if ptr2:
                num2 = ptr2.val
                
            sum = num1 + num2 + jinwei
            
            if sum > 9:
                jinwei = 1
                sum -= 10
            else:
                jinwei = 0
                
            new_node = ListNode(sum)
            new_list_ptr.next = new_node
            new_list_ptr = new_node       
            
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
                
        if jinwei > 0:
            new_node = ListNode(1)
            new_list_ptr.next = new_node
            new_list_ptr = new_node
                
        ptr = dummyRoot.next
        return ptr
    
