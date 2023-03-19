#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())
#define arrSZ(x) int(sizeof(x) / sizeof(x[0]);
#define pb push_back
#define all(x) x.begin(), x.end()
#define sortAll(x) sort(all(x))
#define PI 3.1415926535897932384626
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    unordered_map<char, char> code;
    string s; getline(cin, s);
    string t; getline(cin, t);
    for (int i = 0; i < SZ(s); i++){
        // if not in hashmap, add it in
        if (code.find(t[i]) == code.end())
            code[t[i]] = s[i];
        
    }

    string decode; getline(cin, decode);
    for (int j = 0; j < SZ(decode); j++){
        // if in hashmap, decode it
        if (code.find(decode[j]) != code.end()){
            decode[j] = code[decode[j]];
        }
        else{
            decode[j] = '.';
        }
    }
    cout << decode << endl;
}