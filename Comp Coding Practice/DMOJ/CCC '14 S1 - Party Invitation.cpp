#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define SZ(x) int(x.size())

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    vector <int> a;
    for (int i = 0; i < n; i++)
    {
        a.push_back(i);
    }
    int m; cin >> m;
    for (int j = 0; j < m; j++)
    {
        int temp;
        cin >> temp;
        for (int k = 0; k < n; k++)
        {
            if (a[k] % temp == 0)
            {
                a.erase(a.begin() + k);
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << endl;

    }
}