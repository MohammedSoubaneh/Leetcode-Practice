class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(numbers) - 1
        res = []

        while numbers[l] + numbers[r] != target:
            
            temp_target = numbers[l] + numbers[r]
            if temp_target > target:
                r -= 1
            
            if temp_target < target:
                l += 1
        
        res.append(l + 1)
        res.append(r + 1)

        return res