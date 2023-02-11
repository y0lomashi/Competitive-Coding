#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// ! TLE 

int main() {
    int g, n;
    cin >> g >> n;
    vector<int> planes;
    for (int i = 0; i < n; i++) {
        int p;
        cin >> p;
        planes.push_back(p);
    }
    int counter = 0;
    vector<int> full;
    bool running = true;
    while (!planes.empty()) {
        int p = planes.front();
        planes.erase(planes.begin());
        while (true) {
            if (p > g || find(full.begin(), full.end(), p) != full.end()) {
                p--;
            } else if (p <= g && p != 0) {
                full.push_back(p);
                counter++;
                break;
            } else {
                running = false;
                break;
            }
        }
        if (!running) {
            break;
        }
    }
    cout << counter << endl;
    return 0;
}