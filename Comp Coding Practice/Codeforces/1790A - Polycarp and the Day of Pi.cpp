#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    // t = number of test cases
    int t; cin >> t;
    // * first 30 chars of pi
    string pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";
    for(int _ = 0; _ < t; _++){
        string n; cin >> n;
        // * add # to the end of n to print i if all chars are right
        n += "#";
        for(int i = 0; i < SZ(n); i++){
            if (pi[i] != n[i]){
                cout << i << endl;
                break;
            }
        }
        
    }
        
            
}