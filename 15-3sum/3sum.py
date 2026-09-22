class Solution(object):
    def threeSum(self, arr):
        result = []
        n = len(arr)
        arr.sort()
        for i in range(0,n-1):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                if arr[i]+arr[j]+arr[k]>0:
                    k = k-1
                elif arr[i]+arr[j]+arr[k]<0:
                    j = j+1
                else:
                    if j<k:
                        temp = [arr[i],arr[j],arr[k]]
                        result.append(temp)
                        while j<k and arr[j] == arr[j+1]:
                            j = j+1
                        while j<k and arr[k] == arr[k-1]:
                            k = k-1
                        j = j+1
                        k = k-1
        return result

        