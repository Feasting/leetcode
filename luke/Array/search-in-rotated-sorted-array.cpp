#include<vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int index = -1;
        int low = 0;
        int hi = nums.size() - 1;
        int mid;

        while(hi >= low) {
            mid = (hi + low) /2;
            // if(hi == low) {
            //     if(nums[mid] == target) {
            //         index = mid;
            //     }
            //     break;
            // }
            if(nums[mid] == target) {
                index = mid;
                break;
            }
            else if(nums[mid] >= nums[low]) {
                if(nums[low] <= target && nums[mid] > target) {
                    hi = mid-1;
                }
                else {
                    low = mid+1;
                }
            }
            else {
                if(nums[hi] >= target && nums[mid] < target) {
                    low = mid+1;
                }
                else {
                    hi = mid-1;
                }
            }
        }
        
        return index;
    }
};