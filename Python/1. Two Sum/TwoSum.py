class Solution(object):
    def twoSum(self, nums, target):
        num_indices = {}

        for i, num in enumerate(nums):  # Fix the syntax error here
            complement = target - num

            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i  # Store the current number's index

        return []  # Handle the case when there is no solution

# Example:
solution = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))

        
