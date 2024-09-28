

class Solution(object):

    def __init__(self,value=0, next=None):
        self.value = value
        self.next = next

    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return
        else:
            dummy = Solution()
            current = dummy
            for l1, l2 in zip(list1, list2):
                if l1 < l2:
                    current.next = l1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next

                current = current.next

            if list1:
                current.next = list1
            else:
                current.next = list2

            return dummy.next


# list1 = Solution(1)
# list1.next = Solution(3)
# list1.next.next = Solution(5)
#
# list2 = Solution(2)
# list2.next = Solution(4)
# list2.next.next = Solution(6)

list1 = [1, 3, 5]
list2 = [2, 4, 6]

solution_instance = Solution()
merged_list = solution_instance.mergeTwoLists(list1, list2)


current = merged_list
while current:
    print(current.value)
    current = current.next


