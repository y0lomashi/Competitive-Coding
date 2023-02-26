#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

// ! not finished


int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    for(int i = 0; i < t; i++)
    {
        int cost = 0;
        int price1, price2; cin >> price1 >> price2;
        int amount, discount; cin >> amount >> discount;
        if(price1 >= price2)
            {
                cost += price1;
                amount -= 10;
            }
        while(amount > 0)
        {
            
            else
            {
                cost += price2;
                amount -= 1;
            }
        }


        }
        

    }