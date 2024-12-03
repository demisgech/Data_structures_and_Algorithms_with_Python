class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value,"-->", end="")
            temp = temp.next
        print("None")
            
    def get_tail(self):
        if self.head == None:
            raise ValueError("List is empry!")
        return self.tail.value
        
    def get_head(self):
        if self.head == None:
            raise ValueError("List is empty!")
        return self.head.value
        
    def get_length(self):
        return self.length
        
    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
            
    def prepend(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
        self.length += 1
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        prev = None
        next = None
        for i in range(self.length):
            # Move pointer forward 
            next = temp.next
            #  Switch pointer backward
            temp.next = prev
            # Move prev and temp pointer forward
            prev = temp
            temp = next
            
        

list = LinkedList(2)
list.append(3)
list.prepend(1)

head = list.get_head()
tail = list.get_tail()
length = list.get_length()

print("Head: ", head, ", Tail: ", tail,  ", Length: " ,length)
print("**** Before reversed ****")
list.print_list()
print()
list.reverse()

print("**** After reversed ******")
list.print_list()









