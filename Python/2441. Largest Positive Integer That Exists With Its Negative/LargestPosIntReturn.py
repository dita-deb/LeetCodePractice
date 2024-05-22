class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert nums to a set for fast lookup
        num_set = set(nums)
        # Initialize the variable to store the largest k
        max_k = -1

        # Iterate through the nums array
        for num in nums:
            # We are interested in positive numbers only as long as it's negative counterpart exists too in the set
            if num > 0 and -num in num_set:
                # Update max_k if we find a larger k
                max_k = max(max_k, num)
        
        return max_k

# Example usage:
solution = Solution()
print(solution.findMaxK([-1, 2, -3, 3]))  # Output: 3
print(solution.findMaxK([-1, 10, 6, 7, -7, 1]))  # Output: 7
print(solution.findMaxK([-10, 8, 6, 7, -2, -3]))  # Output: -1
