class Solution(object):
    def matrixScore(self, grid):
        # Get the number of rows and columns in the grid
        m, n = len(grid), len(grid[0])
        
        # Step 1: Ensure the most significant bit in each row is 1
        for i in range(m):
            if grid[i][0] == 0:
                # If the most significant bit is 0, flip the entire row
                grid[i] = [1 - x for x in grid[i]]
        
        # Step 2: Calculate the score based on the number of 1s in each column
        score = 0
        for j in range(n):
            # Count the number of 1s in the current column
            count_1s = sum(grid[i][j] for i in range(m))
            # Calculate the contribution of the column to the score
            # by taking the maximum of the count of 1s and the count of 0s
            # (complement of 1s), and multiplying it by a factor
            score += max(count_1s, m - count_1s) * (2 ** (n - 1 - j))
        
        # Return the calculated score
        return score

# Example usage:
solution = Solution()
grid1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(solution.matrixScore(grid1))  # Output: 39

grid2 = [[0]]
print(solution.matrixScore(grid2))  # Output: 1
