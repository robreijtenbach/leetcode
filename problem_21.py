#!/usr/bin/python3

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = ListNode()
        cur = ret

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1,cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return ret.next

s = Solution()

list1 = ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 4, next= None)))
list2 = ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= None)))

r = s.mergeTwoLists(list1, list2)
print("\nResult:")
while r:
    print(r.val)
    r = r.next
