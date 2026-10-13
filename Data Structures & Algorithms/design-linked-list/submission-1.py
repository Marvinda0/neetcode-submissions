class Node:
    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.tail = self.dummy
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
                    return -1
        node = self.dummy.next
        for i in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == self.size:    
            self.addAtTail(val)
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = Node(val, prev.next)
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        if index == self.size - 1:      # deleted the last node: tail moves back
            self.tail = prev
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)