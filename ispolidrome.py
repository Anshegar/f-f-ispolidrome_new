class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Reverse the second half of the linked list
        slow, fast = head, head
        second_half = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = self.reverse_linked_list(slow)

        # Step 2: Compare the first half with the reversed second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev