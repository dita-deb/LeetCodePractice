class Solution(object):
    def getMaximumGold(self, grid):
        # Define a DFS function to explore all possible paths and calculate maximum gold collected
        def dfs(i, j, visited):
            # Base case: If the current cell is out of bounds, contains 0 gold, or already visited, return 0
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
                return 0
            
            visited[i][j] = True  # Mark the current cell as visited
            max_gold = grid[i][j]  # Collect gold from the current cell
            
            # Explore adjacent cells (up, down, left, right) and collect gold
            max_gold += max(dfs(i+1, j, visited), dfs(i-1, j, visited), dfs(i, j+1, visited), dfs(i, j-1, visited))
            
            visited[i][j] = False  # Backtrack: Mark the current cell as not visited for other paths
            return max_gold
        
        m, n = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
        max_gold = 0  # Initialize the maximum amount of gold collected
        
        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # If the current cell contains gold, perform DFS to explore all possible paths
                if grid[i][j] != 0:
                    # Update the maximum amount of gold collected from all paths
                    max_gold = max(max_gold, dfs(i, j, [[False] * n for _ in range(m)]))
        
        return max_gold  # Return the maximum amount of gold collected

# Example usage:
solution = Solution()
grid1 = [[0,6,0],[5,8,7],[0,9,0]]
print(solution.getMaximumGold(grid1))  # Output: 24

grid2 = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print(solution.getMaximumGold(grid2))  # Output: 28
