#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())
#define pb push_back
#define all(x) x.begin(), x.end()
#define sortAll(x) sort(all(x))
#define PI 3.1415926535897932384626
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int m; cin >> m;
    int t; cin >> t;
    int times[t];
    string names[t];
    for(int i = 0; i < t; i++)
    {
        cin >> names[i] >> times[i];
    }
    int dp[t+1][m+1];

    return 0;
}