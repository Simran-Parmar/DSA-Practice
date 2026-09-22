class Solution:
    def longestConsecutive(self, arr):
        s = set()
        max_c = 1
        for i in range(0,len(arr)):
            s.add(arr[i])
        for ss in s:
            count = 1
            if ss-1 not in s:
                while ss+1 in s:
                    count = count + 1
                    ss = ss+1
                if max_c<count:
                    max_c = count
                
        return max_c
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # s = set()
        # max_seq = 0
        # for i in range(0,len(arr)):
        #     s.add(arr[i])
        # for num in s:
        #     count = 1
        #     if num-1 not in s:
        #         while num+1 in s:
        #             num = num+1
        #             count = count + 1
        #         if count>max_seq:
        #             max_seq = count
            
        # return max_seq
 
        # 