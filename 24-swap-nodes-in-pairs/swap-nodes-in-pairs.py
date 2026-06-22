class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        curr = head
        prev = None
        new_head = head.next

        i = 0

        while i < length - 1:
            first = curr
            second = curr.next

            first.next = second.next
            second.next = first

            if prev:
                prev.next = second

            prev = first
            curr = first.next

            i += 2

        return new_head