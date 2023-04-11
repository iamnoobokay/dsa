class Solution(object):    
    def __init__(self):
        val = input("Enter string: ")
        self.reverse(val)
            
    def reverse(self,val):
        valArr = []
        for v in val:
            valArr.append(v)
        
        string = ""
        while(len(valArr)):
            string += valArr.pop()
        
        print("The reversed string is "+'\"'+string+'\"')
    
Solution()