
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define SZ(x) int(x.size())
// SZ(x) to get container size

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int n; cin >> n;
    int villages[n];
    for(int i = 0; i < n; i++){
        cin >> villages[i];
    }
    sort(villages, villages + n);
    double min = 1000000000.0;
    for(int j = 1; j < n - 1; j++){
        double size = (villages[j + 1] - villages[j])/2.0+(villages[j] - villages[j-1])/2.0;
        if(size < min){
            min = size;
        }
        
    }
    cout << fixed << setprecision(1) << min << endl;
        
    
}