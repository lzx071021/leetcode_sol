# Definition for singly-linked list.
from dis import dis


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'Node(val: %s, next: %s)' % (self.val, self.next)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next is None:
            return None
        head.val, head.next.val = head.next.val, head.val
        head = self.reverseList(head.next)
        return head


def tst():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    p, rev = head, None
    while p:
        rev, rev.next, p = p, rev, p.next
    pass
    return rev


print(tst())
dis(tst)
