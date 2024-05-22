class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # Helper function to check if a string is a palindrome against it's inverse
        def is_palindrome(sub):
            return sub == sub[::-1]

        # Helper function to perform backtracking
        def backtrack(start, path):
            # If we've reached the end of the string, add the current path to the result
            if start == len(s):
                result.append(path[:])
                return
            
            # Try to partition the string from 'start' to 'end'
            for end in range(start + 1, len(s) + 1):
                current_sub = s[start:end]
                # If the current substring is a palindrome
                if is_palindrome(current_sub):
                    # Choose: Add the current palindrome substring to the path
                    path.append(current_sub)
                    # Explore: Recurse to continue partitioning the remainder of the string
                    backtrack(end, path)
                    # Unchoose: Remove the last added palindrome substring (backtrack)
                    path.pop()

        result = []  # List to store all palindrome partitions
        backtrack(0, [])  # Start backtracking from the beginning of the string
        return result

# Example usage:
solution = Solution()
print(solution.partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
print(solution.partition("a"))    # Output: [["a"]]
