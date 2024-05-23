class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Function to check if a given subset is beautiful
        def is_beautiful(subset):
            seen = set()  # Set to track elements in the subset
            for num in subset:
                # Check if there's an element in the set that makes the absolute difference k
                if (num + k) in seen or (num - k) in seen:
                    return False
                seen.add(num)  # Add current number to the set
            return True

        # Backtracking function to generate all subsets
        def backtrack(start, path):
            # If the path (subset) is not empty and is beautiful, add it to the results
            if path and is_beautiful(path):
                beautiful_subsets.append(path[:])  # Append a copy of the path to results
            
            # Iterate over the possible next elements to include in the subset
            for i in range(start, len(nums)):
                path.append(nums[i])  # Include nums[i] in the current subset
                backtrack(i + 1, path)  # Recurse with the next starting index
                path.pop()  # Remove the last element to backtrack and explore other subsets

        beautiful_subsets = []  # List to store all beautiful subsets
        backtrack(0, [])  # Start the backtracking process with an empty path from index 0
        return len(beautiful_subsets)  # Return the count of beautiful subsets

# Example usage:
solution = Solution()
print(solution.beautifulSubsets([2, 4, 6], 2))  # Output: 4
print(solution.beautifulSubsets([1], 1))  # Output: 1
