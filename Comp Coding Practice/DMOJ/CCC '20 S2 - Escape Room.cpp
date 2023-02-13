#include <bits/stdc++.h>

using namespace std;

// Initializing the vector and arrays
int M, N;
vector<vector<int>> room(1000001);
bool visited[1000001];

void dfs(int x)
{
    if (visited[x])
    {
        return;
    }
    // Checking if we have reached exit or not
    if (x == N * M)
    {
        cout << "yes" << endl;
        exit(0);
    }
    // Setting the cell as visited
    visited[x] = 1;
    for (int &t : room[x])
    {
        dfs(t);
    }
}

int main()
{

    cin >> M >> N;
    for (int i = 1; i <= M; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            int x;
            cin >> x;
            room[i * j].push_back(x);
        }
    }
    dfs(1);
    cout << "no" << endl;
}
