class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n ==0:
            return True
        
        flowerbed = [0] + flowerbed + [0]

        for i in range(1,len(flowerbed)-1):            
            if not 1 in flowerbed[i-1:i+2]:
                flowerbed[i] = 1
                n-=1
            if n <= 0:
                return True
        return False


        
