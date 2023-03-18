class Solution {
public:
    int rob(vector<int>& nums) {
        int h1 = 0, h2 = 0;
        for (auto i:nums){
            int temp = max(h1 + i, h2);
            h1 = h2;
            h2 = temp;
        }
        return h2;
    }
};