class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = {}
        for i in nums:
            if i not in l:
                l[i] = 1
            else:
                l[i] += 1
        c = {}
        for i in l:
            if l[i] not in c:
                c[l[i]] = [i]
            else:
                c[l[i]].append(i)
        p = []
        
        while len(p) != k:
            for i in c[max(c)]:
                p.append(i)
            c.pop(max(c))
        return p



