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
    for(int i = 0; i < n; i++)
    {
        int a[2][2];
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < 2; j++)
            {
                cin >> a[i][j];
            }
        }
        
        bool flag = false;
        for (int i = 0; i < 4; i++)
        {
            if (a[0][0] < a[0][1] && a[1][0] < a[1][1] && a[0][0] < a[1][0] && a[0][1] < a[1][1])
            {
                flag = true;
                cout << "YES" << endl;
                break;
            }
            else
            {
                int temp[2][2];
                copy(&a[0][0], &a[0][0] + 4, &temp[0][0]);
                a[0][0] = temp[1][0];
                a[0][1] = temp[0][0];
                a[1][0] = temp[1][1];
                a[1][1] = temp[0][1];
            }
        }
        if (!flag)
        {
            cout << "NO" << endl;
        }
    }
}