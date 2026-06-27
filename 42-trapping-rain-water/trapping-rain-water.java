class Solution {
    public int trap(int[] height) {
        int n = height.length;

        int leftWall = 0;
        int rightWall = 0;

        int[] leftMax = new int[n];
        int[] rightMax = new int[n];

        for (int i = 0; i < n; i++) {
            leftMax[i] = leftWall;
            leftWall = Math.max(leftWall, height[i]);
        }

        for (int i = n - 1; i >= 0; i--) {
            rightMax[i] = rightWall;
            rightWall = Math.max(rightWall, height[i]);
        }

        int summ = 0;

        for (int i = 0; i < n; i++) {
            int pot = Math.min(leftMax[i], rightMax[i]);
            summ += Math.max(0, pot - height[i]);
        }

        return summ;
    }
}