# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1,l2)
        l1_list = self._to_list(l1)
        l2_list = self._to_list(l2)
        
        print(l1_list, l2_list)
        
        l1_list.reverse()
        l2_list.reverse()
        
        num1 = int(''.join([str(i) for i in l1_list]))
        num2 = int(''.join([str(i) for i in l2_list]))
        
        print(num1, num2)
        
        sum = num1 + num2
        sum_str = str(sum)
        sum_list = list(sum_str)
        sum_list.reverse()
        
        print(sum_list)
        
        sum_num_list = [int(i) for i in sum_list]
        
        return self._to_ListNode(sum_num_list)
        
    def _to_list(self, l):
        lst = []
        ptr = l
        while True:
            lst.append(ptr.val)
            if ptr.next is None:
                break
            ptr = ptr.next
        return lst

    def _to_ListNode(self,l):
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in l:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr
    
