
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    int ans = 0;
    ans += n / 100;
    n %= 100;
    ans += n / 20;
    n %= 20;
    ans += n / 10;
    n %= 10;
    ans += n / 5;
    n %= 5;
    ans += n;
    cout << ans << endl;
}