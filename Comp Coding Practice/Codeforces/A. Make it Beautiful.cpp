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
    for (int _ = 0; _ < n; _++)
    {
        int k; cin >> k;
        int a[k];
        for (int i = 0; i < k; i++)
            cin >> a[i];
        if (a[0] == a[k-1])
            cout << "NO" << endl;
        else
        {
            cout << "YES" << endl;
            int temp = a[1];
            a[1] = a[k-1];
            a[k-1] = temp;
            for (int i = 0; i < k; i++)
                cout << a[i] << " ";
            cout << endl;
        }
    }
}   