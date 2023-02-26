#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
#define ll long long 
#define SZ(x) int(x.size())


// ! not finished have to use prefix sums


int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int cols, n; cin >> cols >> n;
    int a[cols];
    for (int i = 0; i < cols; i++)
    {
        cin >> a[i];
    }
    for (int j = 0; j < n; j++)
    {
        int dmg = 0, s, e; cin >> s >> e;
        if (s < e)
        {
            for (int k = s - 1; k < e - 1; k++)
            {
                int temp = a[k] - a[k+1];
                if (temp > 0)
                    dmg += temp;
            }
        }
        else if (s > e){
            for (int k = s - 1; k > e - 1; k--)
            {
                int temp = a[k] - a[k-1];
                if (temp > 0)
                    dmg += temp;
            }
        }
        
        cout << dmg << endl;
    }
}
