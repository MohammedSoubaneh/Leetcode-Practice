# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists or len(lists) == 0:
            return None
        

        while len(lists) > 1:

            merge_lists = []

            for i in range(0, len(lists), 2):
                lst1 = lists[i]
                lst2 = list(i + 1) if (i + 1 ) < len(lists) else None
                merge_lists.append(self.mergeSorted(lst1, lst2))
                lists = merge_lists
            return lists[0]
        
    
    def mergeSorted(lst1, lst2):

        dummy_node = ListNode(None, None)
        tail = dummy_node

        while lst1 and lst2:

            if lst1.val < lst2.val:
                tail.next = lst1.val
                lst1 = lst1.next
            else:
                tail.next = lst2.val
                lst2 = lst2.next
        
        if lst1:
            tail.next = lst1
        
        if lst2:
            tail.next = lst2
        
        return dummy_node.next
