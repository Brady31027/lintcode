class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        dp = [0] * (m+1)
        for item_idx in range(len(A)):
            for space in range(m, 0, -1):
                if space >= A[item_idx]:
                    dp[space] = max(dp[space], dp[space - A[item_idx]] + V[item_idx])
        return dp[-1]
                
