
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int len = 8;
        char a[len][len];
        string newline;
        getline(cin, newline);
        for (int j = 0; j < len; j++)
        {
            for (int k = 0; k < len; k++)
            {
                cin >> a[j][k];
            }
        }
        bool flag = false;
        for (int r = 0; r < len; r++)
        {
            if (a[r][0] == 'R')
            {
                flag = true;
                for (int c = 0; c < len; c++)
                {
                    if (a[r][c] != 'R')
                    {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag)
            {
                cout << "R" << endl;
                break;
            }
        }
        if (!flag)
        {
            for (int c = 0; c < len; c++)
            {
                if (a[0][c] == 'B')
                {
                    cout << "B" << endl;
                    break;
                }
            }
        }
    }
}