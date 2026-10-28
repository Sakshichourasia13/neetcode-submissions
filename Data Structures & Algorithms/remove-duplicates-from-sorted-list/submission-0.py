# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        arr=[]
        if not head:
            return None
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr=sorted(list(set(arr)))
        temp=head
        temp.val=arr[0]
        for i in arr[1:]:
            temp=temp.next
            temp.val=i
        temp.next=None
        return head