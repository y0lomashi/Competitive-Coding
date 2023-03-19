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
    int t; cin >> t;
    ll res = 0;
    int prev = 0;
    for(int i = 0; i < t; i++){
        int n; cin >> n;
        if (i != 0){
            if (n < prev){
                res += prev-n;
            }
        }
        prev = max(n, prev);
    }
    cout << res;

}
