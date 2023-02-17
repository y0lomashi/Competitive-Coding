#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

// * Solved: rated 1100

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for (int _ = 0; _ < t; _++)
    {
        int n, coins, counter = 0;
        cin >> n >> coins;
        // take inputs into list
        int a[n];
        for (int i = 0; i < n; i++)
        {
            int b; cin >> b;
            a[i] = b + i + 1;
            
        }
        // sort list
        sort(a, a + n);
        // check if coins are enough to buy
        for (int i = 0; i < n; i++)
        {
            if (coins >= a[i])
            {
                coins -= a[i];
                counter++;
            }
            else
                break;
        }
        cout << counter << endl;
    }
}
