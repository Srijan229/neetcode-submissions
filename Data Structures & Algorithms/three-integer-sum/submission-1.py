class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        c = 0
        
        l = len(nums)
        for i in range(l):
            a = i + 1
            b = l - 1
            while a < b:
                if nums[a] + nums[b] == - nums[i]:
                    if sorted([nums[a],nums[b],nums[i]]) not in r:
                        r.append(sorted([nums[a],nums[b],nums[i]]))
                    else:
                        c = 0
                    a = a + 1
                elif nums[a] + nums[b] > - nums[i]:
                    b = b - 1
                else:
                    a = a + 1
            
        
        return r

                    

            
                
