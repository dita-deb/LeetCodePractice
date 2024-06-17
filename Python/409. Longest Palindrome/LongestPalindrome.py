class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter  # Import Counter to count the frequency of each character
        
        counts = Counter(s)  # Count the frequency of each character in the string
        length = 0  # Initialize the length of the longest palindrome
        has_odd = False  # Flag to check if there's at least one character with an odd count
        
        for count in counts.values():  # Iterate through the frequency of each character
            length += (count // 2) * 2  # Add the largest even number <= count to the length
            if count % 2 == 1:  # If there's an odd count
                has_odd = True  # Set the flag to True
        
        if has_odd:  # If there's at least one odd count
            length += 1  # Add one to the length to account for a single central character
        
        return length  # Return the computed length
