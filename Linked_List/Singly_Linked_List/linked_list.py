class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next
        
    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_after_node(self,previous_node,data):
        if not previous_node:
            print("previous node does not exist")
            return
        new_node = Node(data)
        new_node.next=previous_node.next
        previous_node.next=new_node

    def delete_node_by_value(self, key):

        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next 
            current_node = None
            return

        previous = None
        while current_node and current_node.data != key:
            previous = current_node
            current_node = current_node.next 

        if current_node is None:
            return 

        previous.next = current_node.next
        current_node = None

    def delete_node_at_position(self, position):
        if self.head:
            current_node=self.head
            if position == 0:
                self.head = current_node.next
                current_node=None
                return
            
            previous = None
            count = 0
            while current_node and count!=position:
                previous=current_node
                current_node=current_node.next
                count+=1
            if current_node is None:
                return

            previous.next=current_node.next
            current_node=None
                
    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count+=1
            current_node=current_node.next
            
        return count

    def length_from_specific_node(self, node):
        if node is None:
            return 0
        return 1+ self.length_from_specific_node(node.next)
    
if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.append("A")
    linkedlist.append("B")
    linkedlist.append("C")
    linkedlist.prepend("E")
    linkedlist.append("D")
    linkedlist.delete_node_at_position(2)
    linkedlist.delete_node_by_value("E")
    linkedlist.insert_after_node(linkedlist.head.next, "F")
    linkedlist.print_list()
    print("Length of the list : ", linkedlist.length())
    print("Length from node C: ", linkedlist.length_from_specific_node(linkedlist.head.next))