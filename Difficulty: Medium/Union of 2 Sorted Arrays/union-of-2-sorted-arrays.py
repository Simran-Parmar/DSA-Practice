class Solution:
    def findUnion(self, a, b):
        r = []
        i,j = 0,0
        while i<len(a) and j<len(b):
            if a[i]<=b[j]:
                if len(r)==0 or r[-1]!=a[i]:
                    r.append(a[i])
                    i = i+1
                else:
                    i = i+1
            else:
                if len(r)==0 or r[-1]!=b[j]:
                    r.append(b[j])
                    j = j+1
                else:
                    j = j+1
            
        while i<len(a):
            if len(r)==0 or r[-1]!=a[i]:
                    r.append(a[i])
                    i = i+1
            else:
                i = i+1
        while j<len(b):
            if len(r)==0 or r[-1]!=b[j]:
                    r.append(b[j])
                    j = j+1
            else:
                j = j+1
        return r