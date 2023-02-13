#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define SZ(x) int(x.size())
// SZ(x) to get container size

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    
    string input; cin >> input;
    int hor = 1, ver = 1;
    for(int i = 0; i < SZ(input); i++)
    {
        // if input is H or V multiply value by -1
        // later check if it is positive or neg to see if you need to flip
        if(input[i] == 'H')
        {
            hor *= -1;
        }
        else
        {
            ver *= -1;
        }
    }
    if(hor == 1 && ver == 1)
    {
        cout << 1 << " " << 2 << endl;
        cout << 3 << " " << 4 << endl;
    }
    else if(hor == -1 && ver == 1)
    {
        cout << 3 << " " << 4 << endl;
        cout << 1 << " " << 2 << endl;
    }
    else if(hor == 1 && ver == -1)
    {
        cout << 2 << " " << 1 << endl;
        cout << 4 << " " << 3 << endl;
    }
    else if(hor == -1 && ver == -1)
    {
        cout << 4 << " " << 3 << endl;
        cout << 2 << " " << 1 << endl;
    }
}