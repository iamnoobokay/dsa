class Node:
    def __init__(self,dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None
        
class SLinkedList:
    def __init__(self):
        self.headVal = None
    
    # insert at beginning of linked list
    def insertAtBeginning(self,newData):
        newNode = Node(newData)
        newNode.nextVal = self.headVal
        self.headVal = newNode
    
    # insert at end of linked list
    def insertAtEnd(self,newData):
        temp = self.headVal
        while(temp):
            if temp.nextVal == None :
                temp.nextVal = Node(newData)
                break
            temp = temp.nextVal
    
    # insert after particular index     
    def insertAfter(self,index,newData):
        length = self.getLength()
        if(length < index):
            print("Error list is of total length "+str(length))
            return
        
        i = 2
        temp = self.headVal
        while(temp):
            if(i == index):
                node = temp.nextVal
                newnode = Node(newData)
                if(node == None):
                    newnode.nextVal = None
                    temp.nextVal = newnode
                else:
                    newnode.nextVal = node.nextVal
                    node.nextVal = newnode
                break
            
            i = i + 1
            temp = temp.nextVal
    
    # Search for particular key in linked list
    def search(self,key):
        print('searching')
    
    # delete node of linked list
    def deleteNode():
        print('deleting')
    
    #sort numeric values of linked list
    def sortList():
        print('sorting')
    
    def getLength(self):
        if(self.headVal == None):
            print("List is empty")
        temp = self.headVal
        i = 1
        while(temp):
            i = i+1
            temp = temp.nextVal
        return i
    
    def returnAsList(self):
        returnList = []
        temp = self.headVal
        while(temp):
            returnList.append(temp.dataVal)
            temp = temp.nextVal
        
        print(returnList)
       
list1 = SLinkedList()
list1.headVal = Node("Mon")
# print(list1.headVal)
e2 = Node("Tue")
e3 = Node("Wed")

list1.headVal.nextVal = e2
e2.nextVal = e3
list1.insertAtBeginning("Sun")
list1.insertAtEnd("Thurs")

# list1.returnAsList()
list1.insertAtEnd('Friday')
list1.insertAtEnd('Saturday')

list1.returnAsList()
list1.insertAfter(2,'pranav')
list1.returnAsList()
# print(list1.headVal.nextVal.nextVal.dataVal)
# print(e1.dataVal)
# print(e2.dataVal)
# print(e2.nextVal)
# print(e3.dataVal)
# print(list1.headVal)
# print(list1.headVal.nextVal)
# print(list1.headVal.dataVal)
# print(list1.headVal.nextVal.dataVal)
# print(list1.headVal.nextVal.nextVal.dataVal)