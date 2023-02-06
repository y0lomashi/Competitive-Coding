#include <bits/stdc++.h>
using namespace std;

#define endl "\n"
#define SZ(x) (int)(x).size()

int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    int a[n], b[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for(int i = 0; i < n; i++){
        cin >> b[i];
    }
    int sumA = 0, sumB = 0, counter = 0;
    for(int j = 0; j < n ; j++){
        sumA += a[j];
        sumB += b[j];
        if(sumA == sumB){
            counter = j + 1;
        }
    
    }
    cout << counter << endl;
}