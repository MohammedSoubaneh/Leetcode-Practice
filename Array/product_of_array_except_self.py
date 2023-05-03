class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        mx = 1


        if len(nums) > 0:
            for i in nums:
                nxt = i
                prev = i
                if i == 0:
                    while nxt:
                        i = i + 1
                        mx = mx * nums[i]
                    res.append(mx)
        print(res)
        return res
        

S = Solution()
S.productExceptSelf([1,2])