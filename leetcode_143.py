# 143. Reorder List



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
