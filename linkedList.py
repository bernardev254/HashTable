class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f"{data} not found in the list.")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def len(self):
        current = self.head
        if current == None:
            return 0
        length = 0

        while current.next:
            length += 1
            current = current.next
        return length