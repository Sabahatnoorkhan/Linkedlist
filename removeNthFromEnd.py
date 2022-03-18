class Solution:
    def removeNthFromEnd(self, head, n):
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        curr=head
        for i in range(n):
            curr=curr.next
        while curr!=None:
            prev=prev.next
            curr=curr.next
        prev.next=prev.next.next
        head=dummy.next
        return head