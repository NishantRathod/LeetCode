class Solution {
    public int maxProfit(int[] prices) {
        int minDay = prices[0];
        int maxProfit = 0;
        int n = prices.length;
        
        for(int i = 1; i < n; i++){
            minDay = Math.min(minDay,prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minDay);
        }
        return maxProfit;
    }
}