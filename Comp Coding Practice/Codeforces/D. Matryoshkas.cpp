
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;
    
    for(int _ = 0; _ < t; _++)
    {
        int n; cin >> n;
        int sizes[n];
        for(int i = 0; i < n; i++)
        {
            cin >> sizes[i];
        }
        sort(sizes, sizes + n);
        int counter = 0;
        for(int j = 0; j < n - 1; j++)
        {
            if(sizes[j] + 1 != sizes[j+1])
            {
                counter++;
            }
        }
            
        cout << counter << endl;
    }
    
}   