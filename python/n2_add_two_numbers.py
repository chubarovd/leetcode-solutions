# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # wow, same as best :)
    def my_addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nf = ListNode(0, None)  # first node
        nc = nf                 # current node
        nc.next = ListNode((nc.val + l1.val + l2.val) // 10, None)
        nc.val = (nc.val + l1.val + l2.val) % 10
        while l1.next is not None and l2.next is not None:
            l1 = l1.next
            l2 = l2.next
            nc.next.next = ListNode((nc.next.val + l1.val + l2.val) // 10, None)
            nc.next.val = (nc.next.val + l1.val + l2.val) % 10
            nc = nc.next
        while l1.next is not None:
            l1 = l1.next
            nc.next.next = ListNode((nc.next.val + l1.val) // 10, None)
            nc.next.val = (nc.next.val + l1.val) % 10
            nc = nc.next
        while l2.next is not None:
            l2 = l2.next
            nc.next.next = ListNode((nc.next.val + l2.val) // 10, None)
            nc.next.val = (nc.next.val + l2.val) % 10
            nc = nc.next
        if nc.next.val == 0:
            nc.next = None
        return nf


i1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
i2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
sln = Solution()
lr = sln.my_addTwoNumbers(i1, i2)
while lr is not None:
    print(lr.val)
    lr = lr.next
