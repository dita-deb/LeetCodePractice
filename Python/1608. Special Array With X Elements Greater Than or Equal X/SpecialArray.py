class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Sort the array in non-decreasing order
        nums.sort()
        
        # Step 2: Iterate through all possible values of x (from 1 to len(nums))
        for x in range(1, len(nums) + 1):
            # Step 3: Count how many numbers are greater than or equal to x
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
            
            # Step 4: If the count matches the current value of x, return x
            if count == x:
                return x
        
        # Step 5: If no such x is found, return -1
        return -1

# Example usage:
solution = Solution()
print(solution.specialArray([3, 5]))  # Output: 2
print(solution.specialArray([0, 0]))  # Output: -1
print(solution.specialArray([0, 4, 3, 0, 4]))  # Output: 3
