class Solution:
    def merge(self,left,right,arr):
            n,m = len(left),len(right)
            i,j = 0,0
            result=[]
            while i<n and j<m:
                if left[i]<=right[j]:
                    result.append(left[i])
                    i = i+1
                else:
                    result.append(right[j])
                    j = j+1
            if i<n:
                for k in range(i,n):
                    result.append(left[k])
            else:
                for k in range(j,m):
                    result.append(right[k])
            arr[:] = result
            return arr
    def mergeSort(self, arr, l=0, r=0):
        n = len(arr)
        if n<=1:
            return arr
        mid = n//2
        left = self.mergeSort(arr[0:mid])
        right = self.mergeSort(arr[mid:n])
        return self.merge(left,right,arr)
    