class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) < 4: return []
        n = len(nums)
        res= []
        l ,r = 0, n-1
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            k = target - nums[i]
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = n-1
                h = k - nums[j]
                while l<r:
                    if nums[l] +nums[r] == h:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l< r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r and nums[r] == nums[r-1]:
                            r-=1
                        l+=1
                    elif nums[l] + nums[r] > h:
                        r-=1
                    else:
                        l+=1
        return res