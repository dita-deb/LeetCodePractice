import sys

class Solution(object):
    def largestLocal(self, grid):
        # Get the size of the grid (it's a square grid)
        n = len(grid)
        # Initialize an empty list to store the result
        maxLocal = []

        # Iterate over the rows of the grid, skipping the outer edges
        for i in range(1, n - 1):
            row = []  # Initialize an empty list to store the values for the current row
            # Iterate over the columns of the grid, skipping the outer edges
            for j in range(1, n - 1):
                # Extract the 3x3 submatrix centered around grid[i][j]
                submatrix = [
                    [grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1]],
                    [grid[i][j - 1], grid[i][j], grid[i][j + 1]],
                    [grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]]
                ]
                # Find the maximum value in the submatrix
                max_val = max(map(max, submatrix))
                # Append the maximum value to the current row
                row.append(max_val)
            # Append the row to the result matrix
            maxLocal.append(row)

        # Return the result matrix
        return maxLocal

# Example usage:
solution = Solution()
grid1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(solution.largestLocal(grid1))  # Output: [[9,9],[8,6]]

grid2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(solution.largestLocal(grid2))  # Output: [[2,2,2],[2,2,2],[2,2,2]]
