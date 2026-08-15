"""You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

start from a source pixel -> image[sr][sc] 
change its color value (image[i][j]) to color
for every adjacent pixel (horizontal and vertical), change their color to color 
if it matches initial color of image[sr][sc], so need to store initial color
keep repeating this process until no more adjacent pixels
return image array"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: # type: ignore
        original_color = image[sr][sc]
        if original_color == color:
                return image

        def helper(r, c):
            if not (r >= 0 and r < len(image) and c >= 0 and c < len(image[0])):
                return 
            if image[r][c] != original_color:
                return

            image[r][c] = color
            
            helper(r - 1, c)
            helper(r + 1, c)
            helper(r, c - 1)
            helper(r, c + 1)
        
            
        

        helper(sr, sc)
        return image

        