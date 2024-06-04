class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for count in counts.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                has_odd = True
        
        if has_odd:
            length += 1
        
        return length
