class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        lowest = float('inf')
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<lowest:
                lowest = nums[mid]
            if nums[low]<=nums[mid]:
                if nums[low]<lowest:
                    lowest = nums[low]
                low = mid+1
            else:
                high = mid-1
        return lowest
            
















































        # low = 0
        # high = len(nums)-1
        # lowest = float('inf')
        # while low<=high:
        #     mid = (low+high)//2
        #     if nums[mid]<lowest:
        #         lowest = nums[mid]
        #     if nums[mid]<=nums[high]:
        #         high = mid-1
        #     else:
        #         low = mid+1
        # return lowest


#0r 

# class Solution(object):
#     def findMin(self, nums):
#         low = 0
#         high = len(nums)-1
#         lowest = float('inf')
#         while low<=high:
#             mid = (low+high)//2
#             if nums[mid]<lowest:
#                 lowest = nums[mid]
#             if nums[low]<=nums[mid]:
#                 if nums[low]<lowest:
#                     lowest = nums[low]
#                 low = mid+1
#             else:
#                 high = mid -1 
#         return lowest