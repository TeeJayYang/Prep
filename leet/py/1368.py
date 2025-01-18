from math import inf
from heapq import heappush, heappop

DIR = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]
class Solution:
    # dijkstra beats 20%
    def minCost(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        dp = [[inf] * len(grid[0]) for row in grid]
        seen = set()
        pq = []
        heappush(pq, (0, (0, 0)))
        min_cost = inf
        def valid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[i])
        while pq:
            cost, coords = heappop(pq)
            if coords in seen:
                continue
            else:
                seen.add((coords))
            # print(f'Popped {coords}, cost {cost}, seen {seen}')
            i, j = coords
            for d in range(len(DIR)):
                next_dir = DIR[d]
                i_next, j_next = i + next_dir[0], j + next_dir[1]
                if not valid(i_next, j_next) or (i_next, j_next) in seen:
                    continue
                # print(f'\tNext look {(i_next, j_next)}')
                if i_next == len(grid) - 1 and j_next == len(grid[0]) - 1:
                    min_cost = min(cost, min_cost) if d == grid[i][j] - 1 else min(cost + 1, min_cost)
                    # print(f'\t\tIs end, min_cost {min_cost}')
                else:
                    if d == grid[i][j] - 1:
                        heappush(pq, (cost, (i_next, j_next)))
                        # print(f'\t\tNatural direction')
                    else:
                        heappush(pq, (cost + 1, (i_next, j_next)))
                        # print(f'\t\tChanged direction')
        return min_cost

  # 1-0 BFS beats 53 %
  def minCost(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        cost = [[inf] * len(grid[0]) for row in grid]
        cost[0][0] = 0
        pq = deque([(0,0)])
        min_cost = inf
        def valid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[i])
        while pq:
            i, j = pq.popleft()
            curr_cost = cost[i][j]
            for d in range(len(DIR)):
                next_dir = DIR[d]
                i_next, j_next = i + next_dir[0], j + next_dir[1]
                if not valid(i_next, j_next):
                    continue
                if i_next == len(grid) - 1 and j_next == len(grid[0]) - 1:
                    min_cost = min(curr_cost, min_cost) if d == grid[i][j] - 1 else min(curr_cost + 1, min_cost)
                else:
                    if d == grid[i][j] - 1:
                        if cost[i_next][j_next] > curr_cost:
                            cost[i_next][j_next] = curr_cost
                            pq.appendleft((i_next, j_next))
                    else:
                        if cost[i_next][j_next] > curr_cost + 1:
                            cost[i_next][j_next] = curr_cost + 1
                            pq.append((i_next, j_next))
        return min_cost
