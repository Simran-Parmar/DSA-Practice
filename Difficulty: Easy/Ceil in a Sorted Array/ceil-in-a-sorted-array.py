class Solution:
    def findCeil(self, nums, x):
        n = len(nums)
        low = 0
        high = n-1
        index = n
        while low <= high:
            mid = (low+high)//2
            if nums[mid]<x:
                low = mid+1
            else:
                high = mid-1
                if mid<index:
                    ceil = nums[mid]
                    index = mid
        if index == n:
            return -1
        return index
