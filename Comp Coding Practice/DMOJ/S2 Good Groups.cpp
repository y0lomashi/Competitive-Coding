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
    unordered_map<string, vector<string>> together;
    unordered_map<string, vector<string>> apart;
    int x;
    cin >> x;
    string temp1, temp2;
    for (int i = 0; i < x; i++)
    {
        // putting pairs into hashmap
        cin >> temp1 >> temp2;
        together[temp1].pb(temp2);
    }
    int y;
    cin >> y;
    for (int j = 0; j < y; j++)
    {
        cin >> temp1 >> temp2;
        apart[temp1].pb(temp2);
    }
    int infractions = 0;
    int g; cin >> g;
    string a, b, c;
    for (int k = 0; k < g; k++)
    {
        cin >> a >> b >> c;
        // checking if a exists in together hashmap
        if (together.find(a) != apart.end())
        {
            // adding infraction key a is not with "together" people
            if (together[a] != b and together[a] != c)
            {
                infractions += 1;
            }
        }
        if (together.find(b) != apart.end())
        {
            if (together[b] != a and together[b] != c)
            {
                infractions += 1;
            }
        }
        if (together.find(c) != apart.end())
        {
            if (together[c] != a and together[c] != b)
            {
                infractions += 1;
            }
        }
        if (apart.find(a) != apart.end())
        {
            if (apart[a] == b or apart[a] == c)
            {
                infractions += 1;
            }
        }
        if (apart.find(b) != apart.end())
        {
            if (apart[b] == a or apart[b] == c)
            {
                infractions += 1;
            }
        }
        if (apart.find(c) != apart.end())
        {
            if (apart[c] == a or apart[c] == b)
            {
                infractions += 1;
            }
        }
    }

    cout << infractions << endl;
}