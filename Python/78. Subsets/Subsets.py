class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            # Append the current subset (path) to the result list
            res.append(path)
            # Explore further elements to include in the subset
            for i in range(start, len(nums)):
                # Include nums[i] in the subset and recurse
                backtrack(i + 1, path + [nums[i]])

        res = []
        # Start the backtracking with an empty path
        backtrack(0, [])
        return res

# Example usage:
solution = Solution()
print(solution.subsets([1, 2, 3]))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(solution.subsets([0]))  # Output: [[], [0]]
