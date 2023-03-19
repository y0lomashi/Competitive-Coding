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
    int t;
    cin >> t;
    while (t--)
    {
        int x, y;
        cin >> y >> x;
        int run = 1;
        for (int i = 0; i < x; i++)
        {
            if (i % 2 == 0)
            {
                run += 1;
            }
            else
            {
                run += run - 1 + 6;
            }
            // cout << run << endl;
        }
        run -= y - 1;
        cout << run << endl;
    }
    return 0;
}