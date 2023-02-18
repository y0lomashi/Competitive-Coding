#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

// bad solution maybe just loop through count 2's if odd then -1 
// then loop through to find where the middle of the 2's are

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int _ = 0; _ < t; _++)
    {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        int ans = 0, tracker = 0;
        for (int i = 0; i < n; i++)
        {
            int right = 0;
            if(a[i] == 2)
                tracker++;
            for (int j = 1; j < n - i; j++)
            {
                if(a[i + j] == 2)
                    right++;
            }
            if (right == tracker)
            {
                ans = i + 1;
                cout << ans << endl;
                break;
            }

        }
        if (ans == 0)
            cout << -1 << endl;
    }
}