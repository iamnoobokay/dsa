class Node:
    def __init__(self,dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None
        
class SLinkedList:
    def __init__(self):
        self.headVal = None
       
list1 = SLinkedList()
list1.headVal = Node("Mon")
print(list1.headVal)
e2 = Node("Tue")
e3 = Node("Wed")

list1.headVal.nextVal = e2
e2.nextVal = e3

# print(e1.dataVal)
print(e2.dataVal)
print(e2.nextVal)
print(e3.dataVal)
print(list1.headVal)
print(list1.headVal.nextVal)
print(list1.headVal.dataVal)
print(list1.headVal.nextVal.dataVal)
print(list1.headVal.nextVal.nextVal.dataVal)