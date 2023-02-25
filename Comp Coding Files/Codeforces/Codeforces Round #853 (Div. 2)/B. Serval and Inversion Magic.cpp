#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())
#define pb push_back
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define PI 3.1415926535897932384626
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        //write code here
        int n; cin >> n;
        string num; cin >> num;
        string rev = num;
        reverse(rev.begin(), rev.end());
        if (num == rev)
        {
            cout << "YES" << endl;
        }
        else
        {
            int cons = 0;
            bool flag = false;
            int j = n -1;
            for (int i = 0; i <= n/2; i++) 
            {
                    if (num[i] != num[j] && cons == 0)
                    {
                        cons = 1;
                    }
                    else if (num[i]== num[j] && cons == 1)
                    {
                        cons = 2;
                    }
                    else if (num[i] != num[j] && cons == 2)
                    {
                        cout<<"NO"<<endl;
                        flag = true;
                        break;
                    }

                    j--;
                }
                
            
            if(!flag)
                cout << "YES" << endl;
        }
        
    }
}