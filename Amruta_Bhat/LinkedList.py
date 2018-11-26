import pdb
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def isEmpty(self):
        return self.head == None

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.getNext()

    def search_item(self,item):
        temp=self.head
        isitem=False
        while temp!=None:
           if temp.getData() == item:
                isitem = True
                temp=None
           else:
                temp =temp.getNext()

        return isitem

    def fetch_index(self,data1):
        current=self.head
        position=0
        while current!=None:
            if current.data== data1:
                return position
            else:
                current=current.getNext()
                position +=1
        print("item does not exist in the linked list")

    def remove(self, data2):
        current = self.head
        previous = None
        isitem = False
        while not isitem:
            if current.getData() == data2:
                isitem = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append_item(self, item):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(Node(item))


mylinkedlist = LinkedList()
print(mylinkedlist.isEmpty())
mylinkedlist.add(1)
mylinkedlist.add(2)
mylinkedlist.add(3)
print("size of the linkedlist is:")
print(mylinkedlist.size())
print("items in the linked list are:")
mylinkedlist.print()
print(mylinkedlist.isEmpty())
item1=int(input("enter the item you want to search:"))
print(mylinkedlist.search_item(item1))
data1=int(input("enter the item for searching index:"))
print(mylinkedlist.fetch_index(data1))
data2=int(input("enter the item for removal:"))
#print(mylinkedlist.remove(data2))
#mylinkedlist.print()
mylinkedlist.append_item(5)
mylinkedlist.print()
