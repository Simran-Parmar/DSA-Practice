class Solution:
    def countFreq(self, nums, target):
        def lowerbound(nums,target):
            n = len(nums)
            low = 0
            high = n-1
            lb = n
            while low<=high:
                mid = (low+high)//2
                if nums[mid]<target:
                    low = mid+1
                else:
                    high = mid-1
                    if mid<lb:
                        lb = mid
            return lb
        def upperbound(nums,target):
            n = len(nums)
            low = 0
            high = n-1
            ub = n
            while low<=high:
                mid = (low+high)//2
                if nums[mid]<=target:
                    low = mid+1
                else:
                    high = mid-1
                    if mid<ub:
                        ub = mid
            return ub
            
        lb = lowerbound(nums,target)
        ub = upperbound(nums,target)
        
        return ub-lb
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def lowerBound(nums, target):
        #     lower = len(nums)
        #     low = 0
        #     high = len(nums)-1
        #     while low<=high:
        #         mid = (low+high)//2
        #         if target<=nums[mid]:
        #             high = mid-1
        #             lower = mid
        #         else:
        #             low = mid+1
        #     return lower
        # def upperBound(nums, target):
        #     upper = len(nums)
        #     low = 0
        #     high = len(nums)-1
        #     while low<=high:
        #         mid = (low+high)//2
        #         if target < nums[mid]:
        #             upper = mid
        #             high = mid-1
        #         else:
        #             low = mid+1
        #     return upper
        # lb = lowerBound(nums,target)
        # ub = upperBound(nums,target)
        # return ub-lb