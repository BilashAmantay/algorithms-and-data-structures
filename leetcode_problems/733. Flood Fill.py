class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        if image[sr][sc] == newColor: return image
        rows, cols = len(image), len(image[0])
        orgColor = image[sr][sc]

        def fill(image, sr, sc, orgColor,newColor):
            if sr<0 or sc<0 or sr>=rows or sc>=cols or image[sr][sc]!=orgColor:
                return
            image[sr][sc]=newColor
            fill(image, sr-1, sc, orgColor, newColor)
            fill(image, sr+1, sc, orgColor, newColor)
            fill(image, sr, sc+1, orgColor, newColor)
            fill(image, sr, sc-1, orgColor, newColor)
        fill(image, sr,sc, orgColor, newColor)
        return image

image = [[1,1,1],[1,1,0],[1,0,1]]; sr = 1; sc = 1; newColor = 2
s = Solution()
r = s.floodFill(image, sr, sc, newColor)   
print(r)
print()  

image = [[0,0,0],[0,0,0]]; sr = 0; sc = 0; newColor = 2
s = Solution()
r = s.floodFill(image, sr, sc, newColor)   
print(r)
print() 
