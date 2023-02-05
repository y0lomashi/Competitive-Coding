#include <bits/stdc++.h>
using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    // code here
    int n = 0, num = 0, res = 0;
    vector<int> nums;

    cin >> n;
    for (int i = 1; i <= n; i++)
    {

        cin >> num;
        if (num > 0)
        {
            nums.push_back(num);
        }
        else
        {
            nums.pop_back();
        }
    }
    for (auto k: nums)
    {
        if (nums.empty())
            {
                res = 0;
            }
        else{
            res += k;
        }
    }
    cout << res;
}