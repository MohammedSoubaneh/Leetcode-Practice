class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        mx = 0

        for r, n in enumerate(nums):

            if n == 0:
                l = r + 1
            mx = max(mx, r - l + 1)
        print(mx)
        return mx


max_consecutive = Solution()

max_consecutive.findMaxConsecutiveOnes([1,1,1,1,1,0,0,1,1,1,0])