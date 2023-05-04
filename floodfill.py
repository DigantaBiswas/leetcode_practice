from functools import lru_cache


class Solution:
    def floodFill(self, image, sr, sc, color):
        row = len(image)
        column = len(image[0])
        start_color = image[sr][sc]
        pixel_stack = [(sr, sc)]
        visited = [(sr, sc)]
        image[sr][sc] = color
        while pixel_stack:
            r, c = pixel_stack.pop()
            for r1, c1 in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= r1 < row and 0 <= c1 < column and image[r1][c1] == start_color and (r1, c1) not in visited:
                    image[r1][c1] = color
                    pixel_stack.append((r1, c1))
                    visited.append((r1, c1))

        return image

print(Solution().floodFill(image=[[0,0,0],[0,0,0]], sr=1, sc=0, color=2))
