class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None
        Do not return anything, modify s in-place instead.
        """
        n = len(s)  # Get the length of the input array
        # Loop from the start of the array to the middle
        for i in range(n // 2):
            # Swap the character at position i with the character at position n - i - 1
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
