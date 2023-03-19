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
    ll t;
    cin >> t;
    while (t != 1){
        cout << t << " ";
        if (t % 2 == 0){
            t /= 2;
        }
        else{
            t = t * 3 + 1;
        }
        
    }
    cout << t;
    return 0;
}