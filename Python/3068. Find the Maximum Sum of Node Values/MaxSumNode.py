class Solution:
    def maximumValueSum(self, nums, k, edges):
        # Get the length of the nums list, which represents the number of nodes in the tree
        n = len(nums)
        # Initialize a list 'diff' to store the differences between XORed and original values for each node
        diff = [0] * n
        # Calculate the total sum of all node values
        total_sum = sum(nums)
        
        # Calculate the differences for each node between its XORed value and original value
        for i in range(n):
            diff[i] = (nums[i] ^ k) - nums[i]
        
        # Sort the differences in descending order
        diff.sort(reverse=True)
        
        # Iterate through the differences in pairs, starting from index 0 with a step of 2
        for i in range(0, n, 2):
            # If the current index is the last one (odd number of nodes), return the total sum
            if i + 1 == n:
                return total_sum
            # Calculate the sum of differences for the current pair
            pair_sum = diff[i] + diff[i + 1]
            # If the sum of differences for the pair is positive, add it to the total sum
            if pair_sum > 0:
                total_sum += pair_sum
        
        # Return the total sum after considering all pairs of differences
        return total_sum
