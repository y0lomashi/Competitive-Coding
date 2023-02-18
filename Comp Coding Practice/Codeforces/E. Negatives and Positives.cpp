
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) (int)x.size()

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;
    for(int _ = 0; _ < t; _++)
    {
        int n; cin >> n;
        int nums[n], neg = 0;
        for(int i = 0; i < n; i++)
        {
            int in; cin >> in;
            if(in<0) 
                neg += 1;
            nums[i] = abs(in);
        }
        // * make sure to use long long to avoid unsigned integer overflow
        ll sum = 0;
        if(neg%2 == 0)
        {
            for(auto& num : nums)
                sum += num;
        }
        else
        {
            sort(nums, nums + n);
            // add all absolute value of all but lowest value, then subtract it
            // because odd amounts of negative numbers
            for(int j = 1; j < n; j++)
            {
                sum += nums[j];
            }
            
            sum -= nums[0];
        }
        cout << sum << endl;
    }
}