class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        if length == n:
            return head.next

        curr = head
        for i in range(length - n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head