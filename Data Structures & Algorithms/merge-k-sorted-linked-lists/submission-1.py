# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 0:
            return None
        if l == 1 and lists[0] == None:
            return None
        curr = None
        for i in range(l):
            curr = self.mergeIntoList1(curr,lists[i])
        return curr


    def mergeIntoList1(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next
