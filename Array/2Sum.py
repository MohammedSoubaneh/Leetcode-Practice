class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = []

        for i, l in enumerate(nums):
            for j, r in enumerate(nums):
                if i != j:
                    if l + r == target:
                        res.append(i)
                        res.append(j)
                        return res