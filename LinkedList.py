class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_List(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next 
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    def prepop(self):
        if self.length == 0:
            return None
        temp = self.head 
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            temp.value = value
        self.value = temp.value
    def remove(self, index):
        if index <0 or index >= self.length:
            return None
        if index == 0:
            self.prepop()
        if index == index -1 :
            self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

        


        
        
            
        
            
                

            

my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.prepend(5)
my_linked_list.print_List()
print ("size:" + str(my_linked_list.length))

print(my_linked_list.pop())
print ("size:" + str(my_linked_list.length))
# print(my_linked_list.pop())

# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.prepop())
# print(my_linked_list.prepop())
# print(my_linked_list.prepop())
# print(my_linked_list.prepop())

print(my_linked_list.get(3))
my_linked_list.set_value(1,3)
print(my_linked_list.remove(1))
my_linked_list.print_List()

# my_linked_list.print_List()