class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;

        int startingIdx = 0;
        int endingIdx = 0;
        int tempStart = 0;

        int currMax = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < n; i++) {

            int addition = currMax + nums[i];

            if (addition > nums[i]) {
                currMax = addition;
            }
            else {
                currMax = nums[i];
                tempStart = i;   // new subarray starts here
            }

            if (currMax > maxSum) {
                maxSum = currMax;
                startingIdx = tempStart;
                endingIdx = i;
            }
        }

        System.out.println("Start Index = " + startingIdx);
        System.out.println("End Index = " + endingIdx);

        return maxSum;
    }
}