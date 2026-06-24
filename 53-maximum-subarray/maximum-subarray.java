class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        if(n < 1){
            return nums[0];
        }
        int currMax = nums[0];
        int maxSum = nums[0];
        for(int i=1;i<n;i++){
            currMax = Math.max(currMax + nums[i] , nums[i]);
            maxSum = Math.max(currMax , maxSum);
        }
        return maxSum;
    }
}