class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n = len(candies)
        ans = []
        for i in range(n):
            flag = True
            addCandie = 0
            for j in range(n):
                if i != j:
                    addCandie = candies[i] + extraCandies
                    if addCandie >= candies[j]:
                        flag = True 
                    else:
                        flag = False
                        break 
            ans.append(flag)
        return ans         # [2,3,5,1,3]