# LeetCode-142
class Solution:
    def detectCycle(self, head):
        slow=head
        fast=head
        loop=False
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                loop=True
                break
        if loop==True:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow