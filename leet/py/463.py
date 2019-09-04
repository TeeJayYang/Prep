class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for row in range(len(grid)):
            for i in range(len(grid[row])):
                if grid[row][i] == 1:
                    sides = 4
                    if row - 1 >= 0 and grid[row-1][i] == 1:
                        sides -= 1
                    if row + 1 < len(grid) and grid[row+1][i] == 1:
                        sides -= 1
                    if i - 1 >= 0 and grid[row][i - 1] == 1:
                        sides -= 1
                    if i + 1 < len(grid[row]) and grid[row][i + 1] == 1:
                        sides -= 1
                    perimeter += sides
        return perimeter
