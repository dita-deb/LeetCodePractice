class Solution:
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        # Find the index of the first occurrence of ch
        idx = word.find(ch)
        
        # If ch is not found in word, return the original word
        if idx == -1:
            return word
        
        # Reverse the segment from the start to the index of the first occurrence of ch and concatenate it with the rest of the word
        reversed_segment = word[:idx + 1][::-1]
        remaining_segment = word[idx + 1:]
        
        # Return the concatenated result
        return reversed_segment + remaining_segment

# Example usage:
solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))  # Output: "dcbaefd"
print(solution.reversePrefix("xyxzxe", "z"))   # Output: "zxyxxe"
print(solution.reversePrefix("abcd", "z"))     # Output: "abcd"
