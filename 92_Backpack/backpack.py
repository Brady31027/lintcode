class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        dp = [0] * (m+1)
        for item in A:
            for space in range(m, 0, -1):
                if space >= item:
                    dp[space] = max(dp[space], dp[space-item] + item)
        return dp[-1]
