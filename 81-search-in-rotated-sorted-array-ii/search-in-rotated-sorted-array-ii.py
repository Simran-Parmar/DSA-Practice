class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return True
            while nums[low]==nums[mid]==nums[high] and low<high:
                low = low + 1
                high = high - 1
            if nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
        return False
























        # low = 0
        # high = len(nums)-1
        # while low<=high:
        #     mid = (low+high)//2
        #     if nums[mid]==target:
        #         return True
        #     elif nums[mid]==nums[low]==nums[high]:
        #         low = low+1
        #         high = high-1
        #     else:
        #         if nums[mid+1]<=nums[high]:
        #             if nums[mid+1]<=target<=nums[high]:
        #                 low = mid+1
        #             else:
        #                 high = mid-1
        #         else:
        #             if nums[low]<=target<=nums[mid-1]:
        #                 high = mid-1
        #             else:
        #                 low = mid+1
        # return False


        