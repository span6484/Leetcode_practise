from collections import deque


# bfs version
def update_grid(level_i, i, grid):
    queue = deque()
    pos = (level_i, i)
    queue.append(pos)
    while queue:
        size = len(queue)
        for _ in range(size):
            cur_pos = queue.popleft()
            # down
            if cur_pos[0] < len(grid) - 1:
                if grid[cur_pos[0] + 1][cur_pos[1]] == '1':
                    grid[cur_pos[0] + 1][cur_pos[1]] = '0'
                    queue.append((cur_pos[0] + 1, cur_pos[1]))
            # up
            if cur_pos[0] > 0:
                if grid[cur_pos[0] - 1][cur_pos[1]] == '1':
                    grid[cur_pos[0] - 1][cur_pos[1]] = '0'
                    queue.append((cur_pos[0] - 1, cur_pos[1]))
            # left
            if cur_pos[1] < len(grid[level_i]) - 1:
                if grid[cur_pos[0]][cur_pos[1] + 1] == '1':
                    grid[cur_pos[0]][cur_pos[1] + 1] = '0'
                    queue.append((cur_pos[0], cur_pos[1] + 1))
            # right
            if cur_pos[1] > 0:
                if grid[cur_pos[0]][cur_pos[1] - 1] == '1':
                    grid[cur_pos[0]][cur_pos[1] - 1] = '0'
                    queue.append((cur_pos[0], cur_pos[1] - 1))
    return grid


class Solution:
    def numIslands(self, grid):
        num = 0
        for level_i in range(len(grid)):
            level = grid[level_i]
            for i in range(len(level)):
                if grid[level_i][i] == '0':
                    continue
                else:
                    num += 1
                    grid[level_i][i] = '0'
                    grid = update_grid(level_i, i, grid)
                    print(grid)
        return num


if __name__ == '__main__':
    grid = [["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]]
    num = Solution().numIslands(grid)
    print(num)
