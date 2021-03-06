"""Leetcode #19 删除链表的倒数第N个节点"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Bad Solution"""

        cnt = 1
        node = head
        while node.next is not None:
            cnt += 1
            node = node.next

        node = head
        if cnt == 1:
            return None
        if n == 1:
            while cnt > n + 1:
                cnt -= 1
                node = node.next
            node.next = None
            return head
        while cnt > n:
            cnt -= 1
            node = node.next
        node.val = node.next.val
        node.next = node.next.next
        return head


# * 给定链表 1->2->3->4->5, 和 n = 2
# * 返回 1->2->3->5
