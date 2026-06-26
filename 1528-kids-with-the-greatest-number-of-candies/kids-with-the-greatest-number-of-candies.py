class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=max(candies)
        ans=[]
        for i in candies:
            if (i+extraCandies)>=a:
                ans.append(True)
            else:
                ans.append(False)
        return ans