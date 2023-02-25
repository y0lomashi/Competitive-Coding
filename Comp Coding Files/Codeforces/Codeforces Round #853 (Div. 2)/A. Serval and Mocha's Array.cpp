#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())
#define pb push_back
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define PI 3.1415926535897932384626
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        int n; cin >> n;
        int arr[n];
        for(auto &x : arr) cin >> x;
        sort(arr, arr + n);
        if (arr[0] <= 2)
        {
            cout << "YES" << endl;
        }
        else
        {
            bool flag = false;
            for (int i = 0; i < n; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    
                    if(gcd(arr[i], arr[j]) <= 2)
                    {
                        cout << "YES" << endl;
                        flag = true;
                        break;
                    }
                }
                if(flag)
                    break;

            }
            if(!flag)
                cout << "NO" << endl;
        }
    }
    return 0;
}
