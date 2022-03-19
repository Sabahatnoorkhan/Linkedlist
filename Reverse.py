# LeetCode-206
class Solution:
    def reverseList(self, head):
        aftr=prev=None
        curr=head
        while curr!=None:
            aftr=curr.next
            curr.next=prev
            prev=curr
            curr=aftr
        head=prev
        return head