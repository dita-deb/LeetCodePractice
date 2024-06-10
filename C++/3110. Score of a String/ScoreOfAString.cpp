class Solution {
public:
    int scoreOfString(string s) {
        int total = 0;  // Initialize the total score to 0
        
        // Loop through each character in the string except the last one
        for(int i = 0; i < s.size() - 1; i++) {
            // Calculate the absolute difference between adjacent characters
            total += abs(s[i] - s[i + 1]);
        }
        
        // Return the accumulated total score
        return total;
    }
};
