class Solution {
    public int maxProfit(int[] prices) {
        int minDay = prices[0];
        int maxProf = 0;
        int n = prices.length;
        for(int i = 1; i < n; i++){
            if(prices[i] > minDay){
                maxProf = Math.max(maxProf, prices[i] - minDay);

            }
            minDay = Math.min(minDay,prices[i]);

        }
        return maxProf;
        
    }
}