# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        res = []
        for i in range(0, len(arr), k):
            if i+k <= len(arr):
                res.extend(list(reversed(arr[i:i+k])))
            else:
                res.extend(arr[i:])
        dummy = ListNode()
        curr = dummy
        for i in res:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        