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
    string fb;
    int curr = 1;
    while (curr < 100)
    {
        if (curr % 3 == 0) fb += "F";
        if (curr % 5 == 0) fb += "B";
        curr++;
    }
    int t;
    cin >> t;
    while (t--)
    {
        int n; cin >> n;
        string s; cin >> s;
        cout << (fb.find(s) != string::npos? "YES":"NO") << endl;
    }
    return 0;
}