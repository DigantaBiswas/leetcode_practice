# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            merged_linked_list = ListNode(val=list1.val)
            list1 = list1.next
        else:
            merged_linked_list = ListNode(val=list2.val)
            list2 = list2.next

        final = merged_linked_list
        while list1 and list2:
            if list1.val <= list2.val:
                merged_linked_list.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                merged_linked_list.next = ListNode(val=list2.val)
                list2 = list2.next
            merged_linked_list = merged_linked_list.next

        while list1:
            merged_linked_list.next = ListNode(val=list1.val)
            list1 = list1.next
            merged_linked_list = merged_linked_list.next

        while list2:
            merged_linked_list.next = ListNode(val=list2.val)
            list2 = list2.next
            merged_linked_list = merged_linked_list.next
        return final
