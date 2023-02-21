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
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    // start at 1 because we are checking next number
    // (if there are 3 values in array all increasing)
    // it will only count 2 times
    int cnt = 1, m = 1;
    for (int j = 0; j < n - 1; j++)
    {
        if (a[j + 1] >= a[j])
            cnt += 1;
        else
            cnt = 1;
        m = max(cnt, m);
    }
    cout << m << endl;
}