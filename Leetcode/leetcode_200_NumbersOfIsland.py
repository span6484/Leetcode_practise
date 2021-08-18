from collections import deque



class Solution:
    
    def numIslands(self, grid):
        
        if grid == []:
            return 0
        
        len_i = len(grid)
        len_j = len(grid[0])
        
        def bfs(level_i, j, grid):
            queue = deque()
            grid[level_i][j] = '0'
            pos = (level_i, j)
            queue.append(pos)
            while queue:
                size = len(queue)
                for _ in range(size):
                    cur_pos = queue.popleft()
                    if cur_pos[0] < len(grid) - 1:
                        if grid[cur_pos[0] + 1][cur_pos[1]] == '1':
                            grid[cur_pos[0] + 1][cur_pos[1]] = '0'
                            queue.append((cur_pos[0] + 1, cur_pos[1]))

                    if cur_pos[0] > 0:
                        if grid[cur_pos[0] - 1][cur_pos[1]] == '1':
                            grid[cur_pos[0] - 1][cur_pos[1]] = '0'
                            queue.append((cur_pos[0] - 1, cur_pos[1]))

                    if cur_pos[1] < len(grid[level_i]) - 1:
                        if grid[cur_pos[0]][cur_pos[1] + 1] == '1':
                            grid[cur_pos[0]][cur_pos[1] + 1] = '0'
                            queue.append((cur_pos[0], cur_pos[1] + 1))



                    if cur_pos[1] > 0:
                        if grid[cur_pos[0]][cur_pos[1] - 1] == '1':
                            grid[cur_pos[0]][cur_pos[1] - 1] = '0'
                            queue.append((cur_pos[0], cur_pos[1] - 1))
            return grid
        
        def dfs(level_i,j,grid):
            grid[level_i][j] = '0'
            dirctions = {(-1,0),(1,0),(0,1),(0,-1)}
            
            for d_i,d_j in dirctions:
                new_i = level_i+d_i
                new_j = j+d_j
                if new_i < len_i and new_j < len_j and new_i >= 0 and new_j >= 0 and grid[new_i][new_j] == '1':
                    grid = dfs(new_i, new_j,grid)
            return grid
                        
        
        num = 0
        for level_i in range(len(grid)):
            level = grid[level_i]
            for j in range(len(level)):
                if grid[level_i][j] == '0':
                    continue
                else:
                    num += 1
                    #method 1 bfs
                    # grid = bfs(level_i, j, grid)
                    
                    #method2 dfs
                    grid = dfs(level_i,j,grid)
        return num
        
#main
# if __name__ == '__main__':
#     grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
#     num = Solution().numIslands(grid)
#     print(num)
