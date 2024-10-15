class Solution {
public:
    long long minimumSteps(string s) {
        long long swaps = 0;  // Total swaps required
        long long oneCount = 0;  // Count of '1's encountered so far

        // Traverse the string from left to right
        for (char c : s) {
            if (c == '1') {
                oneCount++;  // Count the '1's as we encounter them
            } else {
                // For each '0', add the number of '1's seen so far to swaps
                swaps += oneCount;
            }
        }

        return swaps;
    }
};
