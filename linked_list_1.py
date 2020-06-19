class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        # head node doesn't contain any actual data

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:

            current = current.next
            total += 1

        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print('error')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_idx += 1
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data

    def erase(self, index):
        if index >= self.length():
            print('error in index value')
        current_node = self.head
        current_index = 0
        while True:
            current_index += 1
            one_before_node = current_node
            current_node = current_node.next
            if current_index == index:
                one_before_node.next = current_node.next
                return

my_list = LinkedList()

my_list.append(7)
my_list.append(8)
my_list.append(9)
my_list.append(10)
my_list.append(11)


my_list.display()

print(my_list.length())
print("element at index 2 ",my_list.get(2))

my_list.erase(1)
my_list.display()
