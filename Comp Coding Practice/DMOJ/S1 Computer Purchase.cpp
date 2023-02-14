#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

// ! not finished

using namespace std;

int main() {
    int n;
    cin >> n;
    unordered_map<string, int> computers;
    vector<pair<string, int>> res;
    for (int i = 0; i < n; i++) {
        string name;
        int r, s, d;
        cin >> name >> r >> s >> d;
        computers[name] = 2 * r + 3 * s + d;
    }
    // Sort by performance metric
    for (auto it = computers.begin(); it != computers.end(); it++) {
        res.push_back(make_pair(it->first, it->second));
    }
    sort(res.begin(), res.end(), [](pair<string, int> a, pair<string, int> b) {
        return a.second > b.second;
    });
    // Sort by alphabetical order if performance metric is the same
    if (res.size() > 1 && res[0].second == res[1].second) {
        sort(res.begin(), res.end(), [](pair<string, int> a, pair<string, int> b) {
            return a.first < b.first;
        });
    }
    if (res.size() > 0) {
        cout << res[0].first << endl;
    }
    if (res.size() > 1) {
        cout << res[1].first << endl;
    }
    return 0;
}