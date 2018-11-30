class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        robbed = 0
        pre_robbed = 0
        not_robbed = 0
        pre_not_robbed = 0
        for i in range(0, len(nums)-1):
            robbed = pre_not_robbed + nums[i]
            not_robbed = max(pre_robbed, pre_not_robbed)
            pre_robbed = robbed
            pre_not_robbed = not_robbed
        best = max(robbed, not_robbed)
        robbed = 0
        pre_robbed = 0
        not_robbed = 0
        pre_not_robbed = 0
        for i in range(len(nums)-1, 0, -1):
            robbed = pre_not_robbed + nums[i]
            not_robbed = max(pre_robbed, pre_not_robbed)
            pre_robbed = robbed
            pre_not_robbed = not_robbed
        best = max(best, robbed, not_robbed)
        return best


    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = nums[0]
        maximum = max(cur, 0)
        minimum = min(cur, 0)
        for i in range(1, len(nums)):
            number = nums[i]
            a = maximum*number
            b = minimum*number
            maximum = max(a, b, max(number,0))
            minimum = min(a, b, min(number,0))
            cur = max(cur, maximum)
        return cur
