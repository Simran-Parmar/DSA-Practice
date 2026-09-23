class Solution(object):
    def searchInsert(self, nums, target):
        high = len(nums)-1
        low = 0
        lowest = float('inf')
        lowerbound = len(nums) 
        while low<=high:
            mid = (low+high)//2
            if target<=nums[mid]:
                if nums[mid]<lowest:
                    lowerbound = mid
                high = mid-1
            else:
                low = mid+1
        return lowerbound
            
        




























        # indx = len(nums)
        # low = 0
        # high = len(nums)-1
        # while low<=high:
        #     mid = (low+high)//2
        #     if target<=nums[mid]:
        #         high = mid-1
        #         indx = mid
        #     else:
        #         low = mid+1
        # return indx
                

        