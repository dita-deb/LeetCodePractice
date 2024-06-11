class Solution {
public:
    int maxScore = 0;  // Initialize the maximum score as a class member variable

    // Function to calculate the score of a given word if it can be formed with the available letters
    int calculateScore(string &word, unordered_map<char, int>& letterCount, vector<int>& letterScores) {
        int currentScore = 0;  // Initialize current score to 0
        for (char ch : word) {  // Loop through each character in the word
            if (letterCount.count(ch)) {  // Check if the character is available in the letter count map
                if (letterCount[ch] > 0) {  // Check if the count of the character is greater than 0
                    currentScore += letterScores[ch - 'a'];  // Add the character's score to the current score
                    letterCount[ch]--;  // Decrement the count of the character
                } else {
                    return 0;  // If the character is not available in sufficient quantity, return 0
                }
            } else {
                return 0;  // If the character is not found in the letter count map, return 0
            }
        }
        return currentScore;  // Return the calculated score for the word
    }

    // Recursive function to find the maximum score by exploring all combinations of words
    void findMaxScore(int index, vector<string>& words, vector<int>& letterScores, unordered_map<char, int> letterCount, int currentVal) {
        if (index == words.size()) {  // If we have considered all words
            maxScore = max(maxScore, currentVal);  // Update the maximum score if the current score is higher
            return;
        }

        // Exclude the current word and move to the next word
        findMaxScore(index + 1, words, letterScores, letterCount, currentVal);

        // Include the current word if it can be formed with the available letters
        int wordScore = calculateScore(words[index], letterCount, letterScores);
        if (wordScore > 0) {  // If the word can be formed
            findMaxScore(index + 1, words, letterScores, letterCount, currentVal + wordScore);  // Recur with the word included
        }
    }

    // Main function to calculate the maximum score of words that can be formed with the given letters
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& letterScores) {
        unordered_map<char, int> letterCount;  // Map to count the frequency of each letter in the given letters
        for (char ch : letters) {  // Populate the letter count map
            letterCount[ch]++;
        }
        findMaxScore(0, words, letterScores, letterCount, 0);  // Start the recursive function to find the maximum score
        return maxScore;  // Return the maximum score found
    }
};
