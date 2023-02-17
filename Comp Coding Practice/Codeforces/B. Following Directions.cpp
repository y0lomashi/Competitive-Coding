#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())


int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;
    for(int i = 0; i < t; i++){
        int n; cin >> n;
        string s; cin >> s;
        pair <int, int> pos(0, 0);
        for(int j = 0; j < n; j++){
            if(s[j] == 'L') pos.first--;
            else if(s[j] == 'R') pos.first++;
            else if(s[j] == 'U') pos.second++;
            else if(s[j] == 'D') pos.second--;
            if(pos.first == 1 && pos.second == 1){
                cout << "YES" << endl;
                break;
            }
        }
        if(pos.first != 1 || pos.second != 1) cout << "NO" << endl;
    }
}