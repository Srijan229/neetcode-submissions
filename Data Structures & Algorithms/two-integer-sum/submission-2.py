class Solution:
    def twoSum(self, nums, target):
        # build value -> indices mapping
        idx = {}
        for i, v in enumerate(nums):
            idx.setdefault(v, []).append(i)

        arr = sorted(nums)
        i, j = 0, len(arr) - 1

        while i < j:
            s = arr[i] + arr[j]
            if s == target:
                if arr[i] != arr[j]:
                    return sorted([idx[arr[i]][0], idx[arr[j]][0]])
                else:
                    return [idx[arr[i]][0], idx[arr[i]][1]]
            elif s < target:
                i += 1
            else:
                j -= 1
