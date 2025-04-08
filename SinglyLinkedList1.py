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



print("**********************************************************************************************************************")

if __name__ == '__main__':
    ll = LinkedList()


    while True:
        print("\n")
        print("\n PRESS 1 to INSERT at the beginning.")
        print("\n PRESS 2 to INSERT at the end.")
        print("\n PRESS 3 to DELETE node.")
        print("\n PRESS 4 to DISPLAY list.")
        print("\n PRESS 5 to EXIT.")
        print("\n")
        choice = input(" --------CHOOSE AN OPTION-------->")
        print("\n")


        if choice == '1':
            val = int(input("Enter the VALUE that you want to insert at the BEGINNING.  "))
            print("\n")

            ll.insert_at_beginning(val)

        elif choice == '2':
            val = int(input("Enter the VALUE that you want to insert at the END.  "))
            print("\n")
            ll.insert_at_end(val)
            

        elif choice == "3":
            val = int(input("Enter the VALUE that you want to DELETE.  "))
            print("\n")
            ll.delete_node(val)

        elif choice == "4":
            print("\n")
            ll.displayValues()
        
        elif choice == "5":
            print('Exiting...')
            break
        else:
            print("\n")
            print("Invalid choice. Try again.")
            
        print("**********************************************************************************************************************")
