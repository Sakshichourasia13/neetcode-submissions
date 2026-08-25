# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in lists:
            temp=i
            while temp:
                arr.append(temp.val)
                temp=temp.next
        arr.sort()
        head=None

        for i in arr:
            if not head:
                head=ListNode(i)
                temp=head
            else:
                temp.next=ListNode(i)
                temp=temp.next
        return head