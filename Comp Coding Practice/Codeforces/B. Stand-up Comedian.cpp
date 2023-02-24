
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())


// * Greedy Method, Math method much better
// this code is funny
// ! oh it tle on test 3


int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    for (int _ = 0; _ < n; _++)
    {
        int a[4];
        
        for (int i = 0; i < 4; i++)
        {
            cin >> a[i];
        }
        if (a[0] == 0)
        {
            cout << 1 << endl;
            continue;
        }
        // using all jokes that increase both spectator's moods first
        int m1 = a[0], m2 = a[0], res = a[0];
        int calc = a[0] + a[1] + a[2] + a[3];
        if (a[1] > 0 && a[2] > 0)
        {
            int num = min(a[1], a[2]);
            
            res += 2 * num;
            a[1] -= num;
            a[2] -= num;
        }
        
        while (m1 > 0 && m2 > 0)
        {
            
            if (a[1] > 0)
            {
                int num = min(m1, a[1]);
                res += num;
                m1 -= num;
                a[1] = 0;

            }
            else if (a[2] > 0)
            {
                int num = min(m2, a[2]);
                res += num;
                m2 -= num;

                a[2] = 0;
            }
            

            else if(a[3] > 0)
            {
                if (a[3] > m1 && a[3] > m2)
                {
                    res +=  min(m1, m2);
                    a[3] -= min(m1, m2);
                }                    
                else if (a[3] > m1)
                    res += m1, a[3] -= m1;
                    
                else if (a[3] > m2)
                    res += m2, a[3] -= m2;
                    
                else
                    res += a[3], a[3] = 0;
                    
            
                // breaking loop
                break;
            }
            else
            {
                break;
            }
        }
        if (res < calc)
        {
            res += 1;
        }

        cout << res << endl;
    }
}