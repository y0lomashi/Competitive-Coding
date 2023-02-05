#include <bits/stdc++.h>
using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    // code here
    
    string s; 
    int countS = 0, countT = 0;
    int n; cin >> n;
    cin.ignore();
    for(int i = 0; i < n; i++){
        getline(cin, s);
        for(int j = 0; j < s.size(); j++){
            if(s[j] == 's' or s[j] == 'S'){
                countS += 1;
            }
            else if(s[j] == 't' or s[j] == 'T'){
                countT += 1;
            }
        }
        
    }
    if(countS >= countT){
        cout << "French" << endl;
        }
    else{
        cout << "English" << endl;
        }
}