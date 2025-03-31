# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = ""
        arr2 = ""
        while l1 and l2:
            arr1+=str(l1.val)
            arr2+=str(l2.val)
            l1 = l1.next
            l2 = l2.next
        while l1:
            arr1+=str(l1.val)
            l1 = l1.next
        while l2:
            arr2+=str(l2.val)
            l2 = l2.next
        arr1  = list(arr1)
        arr2 = list(arr2)
        arr1 = int("".join(arr1[::-1]))
        arr2 = int("".join(arr2[::-1]))
        s = list(str(arr1+arr2))
        s = s[::-1]
        dummy = ListNode()
        curr = dummy
        for i in s:
            curr.next = ListNode(int(i))
            curr = curr.next
        return dummy.next



        