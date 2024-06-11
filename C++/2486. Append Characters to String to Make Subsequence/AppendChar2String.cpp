class Solution {
public:
    int appendCharacters(string s, string t) {
        int s_index = 0, t_index = 0;  // Initialize indices for both strings
        int s_length = s.length(), t_length = t.length();  // Get the lengths of both strings
    
        // Loop through both strings
        while (s_index < s_length && t_index < t_length) {
            if (s[s_index] == t[t_index]) {
                t_index++;  // If characters match, move to the next character in t
            }
            s_index++;  // Always move to the next character in s
        }
    
        // The number of characters to append is the remaining characters in t
        return t_length - t_index;
    }
};
