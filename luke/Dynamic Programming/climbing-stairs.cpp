class Solution {
public:
    int climbStairs(int n) {
        if(n <= 3){
            return n;
        }
        int first = 2;
        int second = 3;
        int count;
        for(int i = 0; i < n-3; ++i) {
            count = first + second;
            first = second;
            second = count;
        }
        
        return count;
    }
};