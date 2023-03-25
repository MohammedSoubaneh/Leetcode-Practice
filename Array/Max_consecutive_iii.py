class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        
        l = 0
        mx = 0

        for r, n in enumerate(nums):
            k -= (1-n)
            if k < 0:
                k += (1 - nums[l])
                l += 1
            mx = max(mx, r - l + 1)
        return mx



max_consecutive = Solution()
max_consecutive.longestOnes([1,1,1,1,0,0,1,1,0,1,1], 2)