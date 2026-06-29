class Solution(object):
    def findDifference(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        ans = [[], []]

        for i in range(n):
            flag = True
            for j in range(m):
                if nums1[i] == nums2[j]:
                    flag = False
                    break
            if flag:
                if nums1[i] not in ans[0]:
                    ans[0].append(nums1[i])

        for i in range(m):
            flag = True
            for j in range(n):
                if nums2[i] == nums1[j]:
                    flag = False
                    break
            if flag:
                if nums2[i] not in ans[1]:
                    ans[1].append(nums2[i])

        return ans