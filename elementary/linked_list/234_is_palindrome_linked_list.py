"""Leetcode #234 回文链表"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'Node(val: %s, next: %s)' % (self.val, self.next)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_lst = []
        while head is not None:
            val_lst.append(head.val)
            head = head.next
        n = len(val_lst)
        i = 0
        while i < n:
            if val_lst[i] != val_lst[n-1]:
                return False
            i += 1
            n -= 1
        return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

sol = Solution()
print(sol.isPalindrome(head))
