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
        int inf = 0, x, y; cin >> x >> y;
        string t1, t2; cin >> t1 >> t2;
        for (int i = 0; i < y; i++)
        {
            t1 += t2.back();
            t2.pop_back();
        }
        for (int i = 0; i < x + y - 1; i++)
        {   
            if (t1[i] == t1[i + 1])
            {
                inf ++;
            }
            if (inf > 1)
            {
                cout << "NO" << endl;
                break;
            }
        }
        if (inf <= 1)
        {
            cout << "YES" << endl;
        }
    }
}