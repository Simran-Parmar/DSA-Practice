class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range (0,n-1):
            if arr[i]>arr[i+1]:
                key = arr[i+1]
                for j in range(i,-1,-1):
                    if arr[j]>key:
                        arr[j+1],arr[j]= arr[j],arr[j+1]
                    else:
                        break
        return arr
        