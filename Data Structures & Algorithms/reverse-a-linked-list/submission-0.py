# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr=arr[::-1]
        temp=head
        i=0
        while temp:
            temp.val=arr[i]
            temp=temp.next
            i+=1
        return head