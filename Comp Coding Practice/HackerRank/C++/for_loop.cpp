#include <iostream>
using namespace std;

int main()
{
  int a, b;

  string num[10] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

  cin >> a >> b;

  for (int i = a; i <= b; i++)
  {

    if (i < 10)
    {

      cout << num[i] << endl;
    }
    else if (i >= 9)
    {
      // checking if divisble by 2
      if (i % 2 == 0)
      {
        cout << "even" << endl;
      }
      else
      {
        cout << "odd" << endl;
      }
    }
  }

  return 0;
}
