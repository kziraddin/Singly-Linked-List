# Singly Linked List
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
        
    #def reverseLinkedList(self):
    



    def sortLinkedList(self):
        print("\nUnsorted Linked List:")
        ll.displayValues()
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
        print("\nSorted Linked List:")
        ll.displayValues()



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

        print(' -> '.join(values) if values else 'List is empty.')        






if __name__ == '__main__':
    ll = LinkedList()

    while True:
        print("\n")
        print("\n PRESS 1 to INSERT at the beginning.")
        print("\n PRESS 2 to INSERT at the end.")
        print("\n PRESS 3 to INSERT at specific position. Think arrow as position starting from 1.")
        print("\n PRESS 4 to DELETE node.")
        print("\n PRESS 5 to DISPLAY list.")
        print("\n PRESS 6 to EXIT.")
        print("\n PRESS 8 to SORT the Linked List.")
        print("\n")
        choice = input(" --------CHOOSE AN OPTION-------->")
        print("\n")


        if choice == "1":
            val = int(input("Enter the VALUE which you want to insert at the BEGINNING of List.   "))
            print("\n")

            ll.insert_at_beginning(val)
            print("\n")
            ll.displayValues()

        elif choice == "2":
            val = int(input("Enter the VALUE which you want to insert at the END of List.   "))
            print("\n")

            ll.insert_at_end(val)
            print("\n")
            ll.displayValues()
        
        elif choice == "3":
            pos = int(input("Enter the position. Think arrow as position starting from 1.   "))
            val = int(input("Enter the VALUE which you want to ADD it to that position in List.   "))

            print("\n")
            print("Previous Linked List: ")
            print("\n")

            ll.displayValues()
            ll.insert_at_position(pos, val)

            print("\n")
            print(f"New Linked List after inserting at position {pos}. Think arrow as a position starting from 1. ")
            print("\n")

            ll.displayValues()
        
        elif choice == "4":
            val = int(input("Enter the VALUE which you want to DELETE.  "))
            print("\n")
            ll.delete_node(val)

            print("\n")
            ll.displayValues()

        elif choice == "5":
            print("\n")
            ll.displayValues()
        
        elif choice == "6":
            print('Exiting...')
            break

        elif choice == "7":
            print("\n")
            ll.reverseLinkedList()
            print("\n")
            ll.displayValues
        
        elif choice == "8":
            print("\n")
            ll.sortLinkedList()
            print("\n")
        else:
            print("\n")
            print("Invalid choice. Try again.")
            
