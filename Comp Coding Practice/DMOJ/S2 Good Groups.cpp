#include <bits/stdc++.h>
using namespace std;

// ! not finished

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    // code here
    map<string, string> together;
    map<string, string> apart;
    int x; cin >> x;
    string temp1, temp2;
    for(int i = 0; i < x; i++){
        // putting pairs into hashmap
        cin >> temp1 >> temp2;
        together.insert({temp1, temp2});
    }
    int y; cin >> y;
    for(int j = 0; j < y; j++){
        cin >> temp1 >> temp2;
        apart.insert({temp1, temp2});
    }
    int infractions = 0, g; cin >> g;
    string a, b, c;
    for(int k = 0; k < g; k++){
        cin >> a >> b >> c;
        // checking if a exists in together hashmap
        if(together.find(a)!=apart.end()){
            // adding infraction key a is not with "together" people
            if(together[a] != b and together[a] != c){
                infractions += 1;
            }
            
        }
        if(together.find(b)!=apart.end()){
            if(together[b] != a and together[b] != c){
                infractions += 1;
            }
        }
        if(together.find(c)!=apart.end()){
            if(together[c] != a and together[c] != b){
                infractions += 1;
            }
        }
        if(apart.find(a)!=apart.end()){
            if(apart[a] == b or apart[a] == c){
                infractions += 1;
            }
        }
        if(apart.find(b)!=apart.end()){
            if(apart[b] == a or apart[b] == c){
                infractions += 1;
            }
        }
        if(apart.find(c)!=apart.end()){
            if(apart[c] == a or apart[c] == b){
                infractions += 1;
            }
        }
    }
    cout << endl;
    for(const auto& elem : together)
    {
        std::cout << elem.first << " " << elem.second<< "\n";
    }
    // cout << infractions << endl;

}