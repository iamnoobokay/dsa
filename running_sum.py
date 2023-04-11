class Solution(object):
    def __init__(self):
        val = input("Enter your array(string of numbers separated by commas 1,2,3): ")
        valArr = val.split(',')
        self.runningSum(valArr)

    def runningSum(self,nums):
        # now, nums = valArr

        # problem statement
        # Example 1:

        # Input: nums = [1,2,3,4]
        # Output: [1,3,6,10]
        # Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
        # Example 2:

        # Input: nums = [1,1,1,1,1]
        # Output: [1,2,3,4,5]
        # Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
        # Example 3:

        # Input: nums = [3,1,2,10,1]
        # Output: [3,4,6,16,17]
        string = ""
        runningsumarr = []
        for i in nums:
            string += i+","
            runningsumarr.append(string)  


        finalArr = []
        for string in runningsumarr:
            arr = string.split(',')
            arr.pop()
            sums = 0
            for a in arr:
                if(a == ','):
                    break
                sums += int(a)
            finalArr.append(sums)

        print(finalArr)
Solution()