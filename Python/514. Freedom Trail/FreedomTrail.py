class Solution(object):
    def findRotateSteps(self, ring, key):
        # Create a dictionary to store the indices of each character in the ring
        char_indices = {}
        for i, char in enumerate(ring):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        # Create a memoization table to store the minimum steps required to spell each prefix of the key
        memo = {}

        # Recursive function to find the minimum steps
        def dp(cur_index, key_index):
            if key_index == len(key):
                return 0

            if (cur_index, key_index) in memo:
                return memo[(cur_index, key_index)]

            min_steps = float('inf')
            for next_index in char_indices[key[key_index]]:
                # Calculate the steps required to move from cur_index to next_index
                clock_steps = (next_index - cur_index) % len(ring)
                anti_clock_steps = (cur_index - next_index) % len(ring)
                steps = min(clock_steps, anti_clock_steps) + 1

                # Calculate the steps required for the remaining key
                steps += dp(next_index, key_index + 1)

                min_steps = min(min_steps, steps)

            # Store the result in the memoization table
            memo[(cur_index, key_index)] = min_steps
            return min_steps

        # Start the recursion from the initial position of the ring and the first character of the key
        return dp(0, 0)

# Example usage:
solution = Solution()
ring = "godding"
key = "gd"
print(solution.findRotateSteps(ring, key))  # Output should be 4
