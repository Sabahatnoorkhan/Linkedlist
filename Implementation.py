# initiating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insertionatbegning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def printlist(self):
        h=self.head
        while h!=None:
            print(h.data)
            h=h.next
    
    def insertionatlast(self, data):
        h=self.head
        if h==None:
            self.insertionatbegning(data)
        else:
            new_node=Node(data)
            while h.next!=None:
                h=h.next
            h.next=new_node

    def deletefromstart(self):
        h=self.head
        if h==None:
            print("Can not delete node because list is empty")
        else:
            self.head=self.head.next
    
    def deletefromlast(self):
        h=self.head
        if h==None:
            print("Can not delete node because list is empty")
        elif h.next==None:
            self.head=None
        else:
            while h.next.next!=None:
                h=h.next
            h.next=None
    
    def deletenode(self,data):
        h=self.head
        if h==None:
            print("Can not delete node because list is empty")
        elif h.data==data:
            self.head=h.next
        else:
            while h.next!=None:
                if h.next.data==data:
                    h.next=h.next.next
                    return
                h=h.next
            print("Node is not present")

list=Linkedlist()
list.insertionatlast(3)
list.insertionatlast(10)
list.insertionatbegning(1)
list.insertionatbegning(5)
list.deletefromstart()
list.deletefromlast()
list.insertionatlast(14)
list.insertionatlast(22)
list.insertionatlast(93)
list.deletenode(22)
list.printlist()