"""Leetcode #21 合并两个有序链表"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'Node(val: %s, next: %s)' % (self.val, self.next)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # """迭代法"""
        # head = ListNode('sentinel')
        # prev = head
        # while l1 is not None and l2 is not None:
        #     if l1.val <= l2.val:
        #         prev.next = l1
        #         l1 = l1.next
        #     else:
        #         prev.next = l2
        #         l2 = l2.next
        #     prev = prev.next
        # prev.next = l1 if l2 is None else l2
        # return head.next
        """递归法"""
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

sol = Solution()
print(sol.mergeTwoLists(l1, l2))
