
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
    while (t--)
    {
        int n, m, k; cin >> n >> m >> k;
        if (n*m-1 == k) cout << "YES" << endl;
        else cout << "NO" << endl;
    }

}