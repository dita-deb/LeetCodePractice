class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0  # Initialize the count of beautiful subsets
        n = len(nums)  # Get the number of elements in nums
        banned = set()  # Initialize a set to keep track of banned bitmasks
        
        # Loop through each pair of elements in nums
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the absolute difference between nums[i] and nums[j] is equal to k
                if abs(nums[i] - nums[j]) == k:
                    # Create a bitmask representing the pair (i, j)
                    ban = (1 << j) + (1 << i)
                    banned.add(ban)  # Add the bitmask to the banned set
        
        # Loop through all possible subsets represented by bitmasks from 1 to (1 << n) - 1
        for i in range(1, (1 << n)):
            flag = True  # Initialize a flag to check if the subset is beautiful
            
            # Check if the current subset represented by bitmask i contains any banned pair
            for ban in banned:
                if (ban & i) == ban:
                    flag = False  # If a banned pair is found, set flag to False
            
            # If no banned pair is found, increment the count of beautiful subsets
            if flag:
                count += 1
        
        return count  # Return the total count of beautiful subsets
