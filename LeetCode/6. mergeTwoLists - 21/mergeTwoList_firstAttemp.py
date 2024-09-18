def mergeTwoLists(list1, list2):
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