class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        temp = 1
        prefix =[]
        sufix =[]
        for i in nums:
            temp = temp * i 
            prefix.append(temp)
        temp = 1
        for i in nums[::-1]:
            temp = temp * i
            sufix.append(temp)
        sufix = sufix[::-1]
        l = len(nums)
        re = []
        for i in range(l):
            if i-1 < 0:
                psum = 1
            else:
                psum = prefix[i-1]
            if i+1>=l:
                ssum = 1
            else:
                ssum = sufix[i+1]
            re.append(psum*ssum)
            
        return re





