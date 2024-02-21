import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current.next is None:
                    self.tail = prev
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def traversal(self):
        print("Linked list elements:")
        for data in self:
            print(data, end=" -> ")
        print("None")

# Measure time for linked list operations
def linked_list_operations():
    linked_list = SinglyLinkedList()
    linked_list.append("Main Street")
    linked_list.append("Broadway")
    linked_list.append("Park Avenue")
    linked_list.append("Elm Street")

    # Start measuring time for deletion
    start_time_delete = time.time()
    linked_list.delete("Broadway")
    end_time_delete = time.time()
    delete_time = end_time_delete - start_time_delete

    # Start measuring time for traversal
    start_time_traversal = time.time()
    linked_list.traversal()
    end_time_traversal = time.time()
    traversal_time = end_time_traversal - start_time_traversal

    return delete_time, traversal_time

# Measure time for linked list operations
delete_time, traversal_time = linked_list_operations()
print("Time taken for deletion:", delete_time, "seconds")
print("Time taken for traversal:", traversal_time, "seconds")