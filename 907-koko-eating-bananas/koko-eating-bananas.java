class Solution {
    int maxElement(int[] piles){
            int maxx = 0;
            for(int i = 0; i < piles.length; i++){
                if (maxx < piles[i]){
                    maxx = piles[i];
                }
            }
            return maxx;
        }
    int calculate(int[] piles, int mid){
        int total = 0;
        for(int p : piles){
            total += Math.ceil(((double) p / mid));
        }
        return total;
    }

    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = maxElement(piles);

        int ans = -1;

        while (low <= high){
            int mid = (low + high) / 2;
            int hour = calculate(piles,mid);

            if (hour <= h){
                ans = mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return ans;
    }
}