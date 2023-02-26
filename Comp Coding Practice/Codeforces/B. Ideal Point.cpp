#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    
    int t; cin >> t;
    for (int _ = 0; _ < t; _++)
    {
        int n, k; cin >> n >> k;
        int arr[50] = {0};
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            int a, b; cin >> a >> b;
            if (a == b && a == k)
            {
                count = 100;  // high number to make it return yes
                break;
            }
            if (min(a, b) <= k && k <= max(a, b))
            {
                for (int j = min(a, b); j <= max(a, b); j++)
                {
                    if(j == k)
                        count++;
                    else
                        arr[j-1]++;
                }
            }
        }
        string res = (count > *max_element(arr, arr + 50)) ? "YES" : "NO";
        cout << res << endl;
        
    }

}
