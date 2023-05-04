# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = head
        lst = dummy
        size = 0
        while head:
            size += 1
            head = head.next 
        stop = size - n

        if size == 0 or size < n:
            return lst
        counter = 1
        while dummy:
            if counter == stop:
                dummy.next = dummy.next.next
                return lst 
            counter += 1
            dummy = dummy.next