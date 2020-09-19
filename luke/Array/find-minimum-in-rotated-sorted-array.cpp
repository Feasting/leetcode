#include<limits>
#include<algorithm>
#include<vector>

using namespace std;

class Solution1 {
public:
    int findMin(vector<int>& nums) {
        int first = nums[0];
        int mid = (nums.size() - 1) / 2;
        int leftmin = INT_MAX;
        int rightmin = INT_MAX;
        for(int i = 0; i <= mid; ++i) {
            if(nums[i] < leftmin) {
                leftmin = nums[i];
            }
        }
        for(int i = mid+1; i < nums.size(); ++i) {
            if(nums[i] < rightmin) {
                rightmin = nums[i];
            }
        }
        
        return min(rightmin, leftmin);
    }
};

class Solution2 {
public:
    int findMin(vector<int>& nums) {
        int low = 0;
        int hi = nums.size() - 1;
        int mid;
        while(low < hi) {
            mid = (hi + low) / 2;
            if(nums[mid] < nums[hi]){
                hi = mid;
            }
            else {
                low = mid+1;
            }
            
            
        }
        
        return nums[low];
    }
};