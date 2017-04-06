class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer
    def backPackVI(self, nums, target):
        # Write your code here
        dp = [1] + [0] * (target)
        for i in range(1, target + 1, 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[-1]
