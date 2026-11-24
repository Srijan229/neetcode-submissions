class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        sux = [1]
        e = 1
        l = len(nums)

        for i in range(l):
            e = e * nums[i]
            pre.append(e)
        e = 1
        
        for i in nums[::-1]:
            e = e * i
            sux.append(e)
        sux = sux[::-1]
         

        r = []

        for i in range(l):
            r.append(pre[i] * sux[i + 1])

        return r






