
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int n; cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num; cin >> num;
        int res = 0;
        for (int j = 1; j <= (num+ 1 )/2; j++)
        {
        if (num % j == 0)
            res += j;
        }
        if (res < num)
            cout << num << " is a deficient number." << endl;
        else if (res > num)
            cout << num << " is an abundant number." << endl;
        else
            cout << num << " is a perfect number." << endl;
    }
    
}