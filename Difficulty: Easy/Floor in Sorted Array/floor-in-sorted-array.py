class Solution:
    def findFloor(self, nums, x):
        n = len(nums)
        low = 0
        high = n-1
        indexk = float('-inf')
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>x:
                high = mid-1
            else:
                if mid>indexk:
                    floor = nums[mid]
                    indexk = mid
                low = mid+1

        if indexk == float('-inf'):
            return -1
        return indexk
        