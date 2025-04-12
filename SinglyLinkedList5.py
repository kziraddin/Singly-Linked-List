import os

# >>>>>>>>>>> Singly Linked List <<<<<<<<<<<<

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# building Linked List Class to call its function in our main Program
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_at_end(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


    def insert_at_beginning(self, val):
        newNode = Node(val)
        # if no head New Node going to be our head and tail
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        


    def insert_at_position(self, pos, val):
        newNode = Node(val)

        if pos <= 0 or not self.head:
            self.insert_at_beginning(val)
            return

        curr = self.head
        i = 1
        # once loop end, curr will point to that position we want to insert
        while curr.next and i < pos:
            curr = curr.next
            i += 1

        newNode.next = curr.next
        curr.next = newNode
        if newNode.next is None:
            self.tail = newNode
        


    def reverseLinkedList(self):
        prev = None
        curr = self.head
        self.tail = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev



    def SearchValue(self, val):

        # We need to sort the list before perform Binary Search, we will perform Quick Sort Algorithm (take pivot (usualy at the end of arr (if arr sorted worst case O(n^2))) and traverse array with Right pointer, compare with pivot, write with Left pointer.
        def SortList(arr, s, e):

            if e - s + 1 <= 1:
                return arr
            
            pivot = arr[e]
            L = s # left pointer for writing

            for R in range(s, e):
                if arr[R] < pivot:
                    arr[L], arr[R] = arr[R], arr[L]
                    L += 1
            
            # when loop stops, still list will be unsorted so swap pivot with L
            arr[L], arr[e] = arr[e], arr[L]

            # recursively call for left and right side
            SortList(arr, s, L-1)  # [6,2,4,1,3] -> [2,1,3,6,4] -> 3 going to be always in there so we don't inlcude 3 when call recursive for left, right
            SortList(arr, L+1, e)

            return arr
        

        def binarySearch(arr, target):

            L, R = 0, len(arr) - 1

            while L <= R:
                mid = (L + R) // 2
                if target > arr[mid]:
                    L = mid + 1
                elif target < arr[mid]:
                    R = mid - 1
                else:
                    # returs index
                    return mid
            return -1
        

        # Extract values from Linked List
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # sort extracted values from Linked List, Quick Sort
        sorted_values = SortList(values, 0, len(values) - 1)
        # binary search, returns index
        index = binarySearch(sorted_values, val)

        if index != -1:
            return f"\nThe value {val}, you are looking for is FOUND after sorting {sorted_values} at index {index} in the list (0 indexed)."
        else:
            return f"\nThe value {val}, you are looking for is NOT FOUND in the list."




    def sortLinkedList(self):
        valuesArr = []
        curr = self.head
        while curr:
            valuesArr.append(curr.val)
            curr = curr.next

        # divide arr into halves until length == 1
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            merged = []
            i, j = 0, 0
               
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # One of the halves will have elements remaining
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
                
            return merged

        
        sorted_values = mergeSort(valuesArr)           

        self.head = None
        self.tail = None
        for val in sorted_values:
            ll.insert_at_end(val)



    def delete_node(self, val):
        if not self.head:
            print('List is empty.')
            return
        
        # if 1 node and that is head and tail
        if self.head.val == val:
            self.head = self.head.next
            # we deleted our head, tail has to be NULL then. if no head means no tail
            if not self.head:
                self.tail = None
            return
        
        # let's we have 2 node 
        prev = self.head
        curr = self.head.next
        while curr:
            # if 2 Node1 and Node2 node and we want to delete Node2
            if curr.val == val:
                prev.next = curr.next
                # if 2 nodes means tail was Node2, let's update our tail
                if curr == self.tail:
                    self.tail = prev
                return
            # 3 or more nodes
            prev = curr
            curr = curr.next
        print(f'Value {val} is not found.')



    def displayValues(self):
        curr = self.head
        values = []

        while curr:
            values.append(str(curr.val))
            curr = curr.next

        print(' -> '.join(values) if values else '\n>>> EMPTY LIST <<<')        



def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == '__main__':
    ll = LinkedList()


    while True:
        clear_screen()

        print("\n>>> CURRENT LINKED LIST <<<")
        ll.displayValues()

        print("\n PRESS 0 to EXIT.")
        print("\n PRESS 1 to INSERT at the beginning.")
        print("\n PRESS 2 to INSERT at the end.")
        print("\n PRESS 3 to INSERT at specific position. Think arrow as position starting from 1.")
        print("\n PRESS 4 to DELETE node.")
        print("\n PRESS 5 to DISPLAY list.")
        print("\n PRESS 6 to REVERSE the List.")
        print("\n PRESS 7 to SORT the Linked List.")
        print("\n PRESS 8 to SEARCH a value that you looking for.")
        print("\n")

        choice = input(" >>> CHOOSE AN OPTION <<<  >> ")
        print("\n")


        if choice == "1":
            val = int(input("Enter the VALUE which you want to insert at the BEGINNING of List.   "))
            clear_screen()
            print("\n >>> Original List <<<")
            ll.displayValues()
            ll.insert_at_beginning(val)
            print("\n >>> List after adding a Node at the beginning <<<")
            ll.displayValues()
            input("\nPress Enter to continue...")

        elif choice == "2":
            val = int(input("Enter the VALUE which you want to insert at the END of List.   "))
            clear_screen()
            print("\n >>> Original List <<<")
            ll.displayValues()
            ll.insert_at_end(val)
            print("\n >>> List after adding the element at the end <<<")
            ll.displayValues()
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            pos = int(input("Enter the position. Think arrow as position starting from 1.   "))
            val = int(input("Enter the VALUE which you want to ADD it to that position in List.   "))
            clear_screen()

            print("\n >>> Original List <<<")
            ll.displayValues()
            ll.insert_at_position(pos, val)
            print("\n")
            print(f"New Linked List after inserting at position {pos}. Think arrow as a position starting from 1. ")
            ll.displayValues()
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            val = int(input("Enter the VALUE which you want to DELETE.  "))
            clear_screen()
            print("\n >>> Original List <<<")
            ll.displayValues()
            ll.delete_node(val)
            print("\n >>> List after deletion <<<")
            ll.displayValues()
            input("\nPress Enter to continue...")

        elif choice == "5":
            clear_screen()
            print("\n >>> Our Linked List <<<")
            ll.displayValues()
            input("\nPress Enter to continue...")
        
        elif choice == "0":
            clear_screen()
            print('>>> Exiting... <<<')
            break

        elif choice == "6":
            clear_screen()
            print("\n >>> Original List <<<")
            ll.displayValues()
            ll.reverseLinkedList()
            print("\n >>> Reversed List <<<")
            ll.displayValues()
            input("\nPress Enter to continue...")
        
        elif choice == "7":
            clear_screen()
            print("\n >>> Original List <<<")
            ll.displayValues()
            ll.sortLinkedList()
            print("\n >>> Sorted List <<<")
            ll.displayValues()
            input("\nPress Enter to continue...")
        
        elif choice == "8":
            clear_screen()
            print("\n >>> Our Current Linked List <<<")
            ll.displayValues()
            val = int(input("\n Enter the value you want to find in the List.  "))
            result = ll.SearchValue(val)
            print(result)
            input("\nPress Enter to continue...")
            
        else:
            clear_screen()
            print("\n")
            print("Invalid choice. Try again.")
            
