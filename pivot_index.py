# array = [1,2,1]
# i = 0
# length = len(array)
# hasPivot = False
# for i in range(length):
#     left_half = array[:i]
#     right_half = array[i:]
#     right_half.pop(0)
#     sum_left = 0
#     sum_right = 0
#     if len(left_half) == 0:
#         sum_left = 0
#     if len(right_half) == 0:
#         sum_right = 0
#     for r in right_half:
#         sum_right += r
#     for l in left_half:
#         sum_left += l
#     if sum_left  == sum_right:
#         # print("Pivot index is " + str(i))
#         # print(array[i])
#         print(i)
#         hasPivot = True
#         break

# if not hasPivot:
#     print("-1")


class Solution(object):
    def __init__(self):
        # val = input("Enter your array(string of numbers separated by commas 1,2,3): ")
        # valArr = val.split(',')
        # self.pivotIndex(valArr)
        self.pivotIndex([-3,3,0,2,1])
                
    def pivotIndex(self,valArr):
        nums = valArr
        size = len(nums)
        for i in range(size):
            left = nums[:i]
            forright = nums[i:]
            forright.pop(0)
            right = forright
            left_sum = sum(left)
            right_sum = sum(right)
            if(left_sum == right_sum):
                print("the pivot index is "+str(i))
                break;
        else:
            print(-1)
        # for a in valArr
        
Solution()