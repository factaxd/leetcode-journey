# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Initialize a dummy node to build the result list
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    # Loop through lists l1 and l2 until you reach both ends and there is no carry
    while l1 or l2 or carry:
        # Get the current values
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Compute the sum and the carry over
        total = val1 + val2 + carry
        carry = total // 10
        new_digit = total % 10

        # Create a new node with the digit and attach it to the result list
        current.next = ListNode(new_digit)
        current = current.next

        # Move to the next nodes in l1 and l2
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Return the result list, which is next to the dummy head
    return dummy_head.next
