class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []

        for i, num in enumerate(nums):

            if i > 0 and num == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                
                temp_target = num + nums[l] + nums[r]
                if temp_target > 0:
                    r -= 1
                
                elif temp_target < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res