#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    // taking in inputs
    int dist; cin >> dist;
    int n; cin >> n;
    int clubs[n];
    for (int i = 0; i < n; i++) cin >> clubs[i];

    // creating dp array
    // setting all values to dist + 1 (could be any number greater than dist)
    // first value to 0
    int dp[dist+1];
    fill(dp, dp + dist + 1, dist + 1);
    dp[0] = 0;

    // for each distance until the target distance
    // get the minimum number of strokes to get to that distance
    for (int i = 1; i <= dist; i++)
    {
        for (auto j: clubs)
        {
            if (i - j >= 0)
            {
                // add 1 to total and continue subtracting club distances for each club
                // store the minimum number of strokes
                dp[i] = min(dp[i], 1 + dp[i - j]);
            }
        }
    }
    // if the target distance in the dp array is not dist + 1 (default value)
    // then print the number of strokes
    if (dp[dist] != dist + 1) cout << "Roberta wins in " << dp[dist] << " strokes." << endl;
    else cout << "Roberta acknowledges defeat." << endl;

}