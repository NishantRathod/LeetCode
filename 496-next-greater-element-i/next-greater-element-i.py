class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for i in range(len(nums1)):

            greater = -1
            
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                   
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            greater = nums2[k]
                            break
                    break

            ans.append(greater)

        return ans