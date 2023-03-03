#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())
#define pb push_back
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define PI 3.1415926535897932384626
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    vector <float> streams;
    int n; cin >> n;
    for (int i = 0; i < n; i++)
    {

        int t; cin >> t;
        streams.pb(t);
    }
    while (true)
    {

        int a; cin >> a;
        if (a == 99)
        {
            float i, j; 
            cin >> i;
            cin >> j;
            float calc = streams[i- 1] * (1 - (j / 100));
            streams.insert(streams.begin() + i, calc);
            streams[i - 1] *= j/100;
        }
        else if (a == 88)
        {
            int i; cin >> i;
            streams[i- 1] += streams[i];
            streams.erase(streams.begin() + i);
        }
        else if (a == 77)
        {
            for (auto flow: streams)
            {
                cout << int(flow) << " ";
            }
            break;
        }
            
    }
}

