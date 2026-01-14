class Solution(object):
    def trap(self, height):
        n=len(height)-1
        l=0
        r=n
        lmax=0
        rmax=0
        res=0
        while l<r:
            if height[l]<height[r]:
                if height[l]>=lmax:
                    lmax=height[l]
                else:
                    res+=lmax-height[l]
                l+=1
            else:
                if height[r]>=rmax:
                    rmax=height[r]
                else:
                    res+= rmax-height[r]
                r-=1
        return res          