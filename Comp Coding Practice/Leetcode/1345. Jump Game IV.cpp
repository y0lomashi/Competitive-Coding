#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define ll long long
#define SZ(x) int(x.size())
#define arrSZ(x) int(sizeof(x) / sizeof(x[0])
#define pb push_back
#define all(x) x.begin(), x.end()
#define sortAll(x) sort(all(x))


class Solution {
public:
    int minJumps(vector<int>& arr) 
    {
    
        int n = arr.size();
        unordered_map<int, vector<int>> indicesOfValue;
        for (int i = 0; i < n; i++)
            indicesOfValue[arr[i]].push_back(i);
        vector<bool> visited(n); visited[0] = true;
        queue<int> q; q.push(0);
        int step = 0;
        while (!q.empty()) {
            for (int size = q.size(); size > 0; --size) {
                int i = q.front(); q.pop();
                if (i == n - 1) return step; // Reached to last index
                vector<int>& next = indicesOfValue[arr[i]];
                next.push_back(i - 1); next.push_back(i + 1);
                for (int j : next) {
                    if (j >= 0 && j < n && !visited[j]) {
                        visited[j] = true;
                        q.push(j);
                    }
                }
                next.clear(); // avoid later lookup indicesOfValue arr[i]
            }
            step++;
        }
        return 0;
    }
};




// ! for testing
int main()
{
    vector <int> arr = {100,-23,-23,404,100,23,23,23,3,404};
    Solution find;
    int res;
    res = find.minJumps(arr);
    cout << res << endl;
}