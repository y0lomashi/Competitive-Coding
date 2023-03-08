#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())
#define pb push_back
#define all(x) x.begin(), x.end()
#define sortAll(x) sort(all(x))
#define PI 3.1415926535897932384626
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    int arr[t][t];
    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < t; j++)
        {
            cin >> arr[i][j];
        }
    }
    bool flag = false;
    while (true)
    {
        // check if it arranged properly
        for(int i=1; i<t; i++) 
        {
            if (arr[0][i] > arr[0][i-1] && arr[0][i] < arr[1][i])
            {
                flag = true;
                break;
            }
                
        }
        if (flag == true)
            break;
        int l= 0, r = t - 1;
        while (l < r)
        {
            for (int i = 0; i < r - l; i++)
            {
                int top= l, bot = r;
                // save top left value
                int topLeft = arr[top][l + i];
                // move bottom left to top left
                arr[top][l + i] = arr[bot - i][l];
                // bottom right to bottom left
                arr[bot - i][l] = arr[bot][r - i];
                // top right to bottom right
                arr[bot][r - i] = arr[top + i][r];
                // move top left into top right
                arr[top + i][r] = topLeft;
            }
            r --;
            l ++;
        }
        
    }
    for(int i=0; i<t; i++) 
    {
        for(int j=0; j<t; j++) 
        {
            cout<<arr[i][j]<<" ";  
        }
        cout<<endl;
    }
		
}