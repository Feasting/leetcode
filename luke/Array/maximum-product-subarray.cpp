#include<iostream>
#include<limits>
#include<algorithm>
#include<vector>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        return divConquer(nums, 0, nums.size()-1);
    }
    
    int divConquer(vector<int>& nums, int lo, int hi) {
        if(lo == hi) {
            return nums[lo];
        }
        
        int mid = (hi + lo) / 2;
        int maxLeft = INT_MIN;
        int minLeft = 0;
        int leftProd = 1;
        for(int i = mid; i >= lo; --i) {
            leftProd *= nums[i];
            if(leftProd > maxLeft) {
                maxLeft = leftProd;
            }
            if(leftProd < minLeft) {
                minLeft = leftProd;
            }
        }
        
        int maxRight = INT_MIN;
        int minRight = 0;
        int rightProd = 1;
        for(int i = mid+1; i <= hi; ++i) {
            rightProd *= nums[i];
            if(rightProd > maxRight) {
                maxRight = rightProd;
            }
            if(rightProd < minRight) {
                minRight = rightProd;
            }
        }
        
        int maxOfLR = max(divConquer(nums, lo, mid), divConquer(nums, mid+1, hi));
        int maxProd;
        if(minLeft == 0 || minRight == 0) {
            maxProd = maxLeft * maxRight;
        }
        else {
            maxProd = max(maxLeft * maxRight, minLeft * minRight);
        }
            
        return max(maxOfLR, maxProd);
    }
};