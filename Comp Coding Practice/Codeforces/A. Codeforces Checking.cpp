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
    string codeforces = "codeforces";
    for(int i = 0; i < n; i++)
    {
        char c; cin >> c;
        if(codeforces.find(c) != string::npos)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
        
    }
}