class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        curr = self.dummy.next
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val,self.dummy.next)
        self.dummy.next = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return None
        newNode = Node(val)
        prev = self.dummy
        for i in range(index):
            prev = prev.next
        temp = prev.next
        prev.next = newNode
        newNode.next = temp
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or index < 0:
            return None
        curr = self.dummy
        for i in range(index):
            curr = curr.next
        delete = curr.next
        curr.next = delete.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)