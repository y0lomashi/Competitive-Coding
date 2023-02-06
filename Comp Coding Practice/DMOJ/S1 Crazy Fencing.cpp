#include <bits/stdc++.h>
using namespace std;

#define endl "\n"
#define SZ(x) (int)(x).size()

int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    int a[n], b[n];
    for(int i = 0; i <= n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        cin >> b[i];
    }
    int p1 = 0, p2 = 1;
    int area = 0;
    for(int j = 0; j < n ; j++){
        area += b[j]*(a[p1] + a[p2]);
        p1 += 1; p2 += 1;
    }
    if(fmod(area/2.0, 1) == 0){
        cout << area/2 << endl;
    }
    else if(fmod(area/2.0, 1) != 0){
        cout << area/2 << ".5" << endl;
        }

}