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
        int a; cin >> a;
        string s; cin >> s;
        int l=0, r=a-1, len = 0;
        while(l <= r)
        {
            if(s[l] == s[r])
            {
                len = r-l + 1;
                break;
            }
            l++ , r--;
        }
        cout << len << endl;
        
    }
}