"""
542. 01 Matrix
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

# from collections import deque
#
# neighbours = [
#     (0, 1),
#     (0, -1),
#     (1, 0),
#     (-1, 0)
# ]
#
#
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         mat = [[(x if x == 0 else float('inf')) for x in y] for y in mat]
#         q = deque()
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 if mat[i][j] == 0:
#                     q.append((i, j, 0))
#
#         while q:
#
#             i, j, d = q.popleft()
#
#             for di, dj in neighbours:
#                 newi, newj = i + di, j + dj
#
#                 if 0 <= newi < len(mat) and 0 <= newj < len(mat[0]) and mat[newi][newj] > mat[i][j] + 1:
#                     mat[newi][newj] = mat[i][j] + 1
#                     q.append((newi, newj, d + 1))
#
#         return mat
from collections import deque
class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        # print(rows, cols)
        ans = [[0] * cols for _ in range(rows)]
        queue = deque()
        # print(ans)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        for r in range(rows):
            for c in range(cols):
                # print(r,c)
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        # print(q)
        dist = 0
        # print(queue)
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # print(r, c)
                if mat[r][c] == 1:
                    # print(f"r : {r}, c : {c}")
                    ans[r][c] = dist
                # print(queue)
                for dr, dc in directions:
                    new_r, new_c = dr + r, dc + c
                    # print(new_r, new_c)
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                        # print(f"new_r: {new_r}  new_c : {new_c}")
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                # print(queue)
            dist += 1

        return ans

mat = [[0,0,0],[0,1,0],[1,1,1]]
obj = Solution()
print(obj.updateMatrix(mat))

