def reverseHalf(head):
    if head is None:
        return None
    curr = head
    slow=curr
    fast= curr
    while fast and fast.next:
        slow= slow.next
        fast=fast.next.next
    secondhead =slow.next
    slow.next =None
    firstpart = reverse(curr)
    secondpart = reverse(secondhead)
    while firstpart.next:
        firstpart = firstpart.next
    firstpart.next=secondpart

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# 1 -> 2 -> 3 -> 4 -> 8 -> 7 -> 6 -> 5
def reverse(head):
    prev = None
    curr= head
    while(curr):
        nex = curr.next
        curr.nex=prev 
        prev=curr
        curr=nex
    head=prev
    return head
    