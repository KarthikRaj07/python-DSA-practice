class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlylinkedlist:
    
    #initial the list
    def __init__(self):
        self.head = None
    
    #traversing the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current=current.next

    #insert at begin
    def insertAtBegin(self,data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    # insert at end
    def insertAtEnd(self,data):
        newnode = node(data)
        if not self.head:
            self.head =  newnode
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    #insert after a specific node
    def insertAfter(self,prevdata,data):
        current = self.head         
        while current and current.data != prevdata :   
            current = current.next
        
        if not current:
            print(f"prev {prevdata} not found")
            return
        newnode = node(data)
        newnode.next = current.next
        current.next = newnode
  
    #delete by value 
    def deleteByValue(self,val):
      if not self.head:
         print("List is empty")
         return
      if self.head.data == val:
          self.head = self.head.next
          return
      current = self.head 
      while current.next and current.next.data != val:
          current=current.next 

      if not current.next:
          print("Value not found")
          return
    
      current.next = current.next.next

    #search

    def serach(self,val):
        current = self.head
        while current :
            if current.data == val:
                print("Found")
                return
            current=current.next
        print("Not found")
        return
        


        


sll = singlylinkedlist()
sll.deleteByValue(0)
sll.insertAtBegin(1)
sll.insertAtBegin(5)
sll.insertAtBegin(7)
sll.insertAtBegin(9)
sll.insertAtEnd(10)
sll.insertAfter(3,8)
sll.insertAfter(5,8)


sll.traverse()

sll.deleteByValue(3)
sll.deleteByValue(8)

sll.serach(5)
sll.serach(8)

sll.traverse()


        
