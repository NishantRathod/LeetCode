class Solution {
    public int gcdOfOddEvenSums(int n) {
        int even = n * (n + 1);
        int odd = n * n;
        return gcd(odd,even);
    }

    public static int gcd(int a, int b){
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}