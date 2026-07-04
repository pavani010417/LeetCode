# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))       
        dummy = ListNode(0)
        current = dummy       
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))       
        return dummy.next

      