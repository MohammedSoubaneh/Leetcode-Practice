class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        l = 0
        count = 0
        dic = {}
        temp = k

        for i in nums:
            for r, num in enumerate(nums):
                if num not in dic:
                    dic[num] = r
                    k -= 1
                
                if k == 0:
                    count += 1

                if k < 0:
                    dic.clear()
                    k = temp
            nums.pop(0)

        if len(nums) == k:
            temp = {}
            temp_counter = 0
            for i, num in enumerate(nums):
                if num in temp:
                    temp_counter = 1
                    break
                if num not in temp:
                    temp[num] = i
            
            if temp_counter == 0:
                count += 1
        return count
                    
                
                
                
