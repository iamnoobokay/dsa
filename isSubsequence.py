class Solution(object):
    def isSubsequence(self,ss,tt):
        if not len(ss):
            return True
        sList = list(ss)
        tList = list(tt)
        finalstr = ''
        for s in enumerate(sList):
            for inj,t in enumerate(tList):
                if(s == t):
                    finalstr = finalstr + tList[inj]
                    tList = tList[inj+1:]
                    break
        if(finalstr == ss):
            return True
        else:
            return False


s = Solution()
s.isSubsequence('paa','pranav')











        
# class Solution(object):
#     def isSubsequence(self,ss,ts):
#         if(not len(ss)):
#             return True
        
#         tList = list(ts)
#         sList = list(ss)
#         for j,s in enumerate(sList):
#             sList.pop()
#             for i,t in enumerate(tList):
#                 if(s==t):
#                     string = ts
#                     string = string[i:]
#                     ts = string
#                     if not len(string) and j == len(sList) - 1:
#                         print('subsequence')
#                         return True
#         else:
#             print('false') 
#             return False               
# class Solution(object):
#     def isSubsequence(self,st,t):
#         tList = list(t)
#         sList = list(st)
#         nList = []
#         for s in sList:
#             for j,t in enumerate(tList):
#                 if(t == s):
#                     nList.append(j)
#                     break
        
#         print(nList)
#         if((nList == sorted(nList) and len(nList) == len(st)) or st == ""):
#             print('true')
#             return True
#         else:
#             print('false')
#             return False

# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         sList = list(s)
#         tList = list(t)
#         nList = list()
#         for j in tList:
#             for i in sList:
#                 if(i==j):
#                     nList.append(j)
                    
#         print(nList)
#         print(sList)
        
# s = 'p','a','n'
# t = 'p','r','a','n','a','v'pranav
# q = 'p','a','r'

# class Solution(object):ahbgdc
#     def isSubsequence(self,a,b): 
#         li = []
#         i = 0
#         for _ in a:
#             if _ in b:
#                 li.append(_)
#         print(li)
        
#         while i < len(li):
#             if li[i]==a[i]:
#                 i+=1
#                 if i == len(li):
#                     print("Sequence")
#             else:
#                 print("Not a sequence")
#                 break
  
  
# isseq(s,t)

# isseq(q,t)
        