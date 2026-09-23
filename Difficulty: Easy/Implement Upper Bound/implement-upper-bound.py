class Solution:
    def upperBound(self, nums, target):
        index = len(nums)
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>target:
                index = mid
                high = mid-1
            else:
                low = mid+1
        return index