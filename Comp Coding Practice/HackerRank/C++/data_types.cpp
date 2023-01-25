#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main()
{
    //* declaring different data types
    int a;
    long b;
    char c;
    float d;
    double e;
    // taking inputs as specific data types
    scanf("%d %ld %c %f %lf", &a, &b, &c, &d, &e);

    // print inputs with newline inbetween
    cout << a << endl
         << b << endl
         << c << endl;
    // print new
    cout << fixed << setprecision(3) << d << endl
         << fixed << setprecision(9) << e;
    return 0;
}
