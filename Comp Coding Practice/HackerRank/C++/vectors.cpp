#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */     vector<int>v;
    int size = v.size();
    int n, input;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>input;
        v.push_back(input);
    }
    sort(v.begin(),v.end());
    for(int i=0;i<n;i++)
    {
        cout<<v[i]<<" ";
    }
    return 0;
}
