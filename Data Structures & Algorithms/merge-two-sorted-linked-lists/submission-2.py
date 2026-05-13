# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        init = res
        while list1 and list2:
            if list1 and list2:
                if list1.val<list2.val:
                    init.next = list1
                    list1 = list1.next
                else:
                    init.next = list2
                    list2 = list2.next
                init = init.next

        if list1 and not list2:
            init.next = list1
        if list2 and not list1:
            init.next = list2
        return res.next