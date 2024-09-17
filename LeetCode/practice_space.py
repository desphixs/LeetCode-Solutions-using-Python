class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        return dummy.next

def list_to_linkedlist(lst):
    head = ListNode(lst[0]) if lst else None
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linkedlist(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Convert lists to linked lists
list1 = [1, 4, 2, 4, 5]
list2 = [1, 3, 4, 3]
l1 = list_to_linkedlist(list1)
l2 = list_to_linkedlist(list2)

# Merge the linked lists
sol = Solution()
merged_head = sol.mergeTwoLists(l1, l2)

# Print the merged linked list
print_linkedlist(merged_head)








"""def mergeTwoLists(list1, list2):
        new_list = list1 + list2
        

        if not new_list:
              return new_list
        
        swapped = True
        while swapped:
            swapped = False

            for i in range(len(new_list) - 1):
                if new_list[i] > new_list[i + 1]:
                    current = new_list[i]
                    next_ = new_list[i + 1]
                    new_list[i] = next_
                    swapped = True
                    new_list[i + 1] = current
                    
        return new_list


list1 = [1,4,2,4,5]
list2 = [1,3,4,3]
print(mergeTwoLists(list1, list2))

"""