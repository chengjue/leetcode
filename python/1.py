class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash={}
        for idx, num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num], idx]
            else:
                hash[num] = idx
        return None