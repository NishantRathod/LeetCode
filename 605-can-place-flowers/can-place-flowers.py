class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        m = len(flowerbed)
        cnt = 0
        
        for i in range(m):
            if flowerbed[i] == 0:
                
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)

                right_empty = (i == m - 1) or (flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:

                    flowerbed[i] = 1
                    cnt += 1
            
                    if cnt >= n:
                        return True
                        
        return cnt >= n