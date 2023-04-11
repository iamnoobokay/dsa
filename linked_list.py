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
    def insertAfter(self,prevnode,newData):
        print('zxc')
    
    # Search for particular key in linked list
    def search(self,key):
        print('searching')
    
    # delete node of linked list
    def deleteNode():
        print('deleting')
    
    #sort numeric values of linked list
    def sortList():
        print('sorting')
    
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

list1.returnAsList()
list1.insertAtEnd('Friday')
list1.insertAtEnd('Saturday')
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