#include <iostream>
using namespace std;

int main()
{ // setting variables
  int dayNum = 0;
  int numDays;

  cin >> dayNum >> numDays;

  int rowCount = dayNum - 1;

  cout << "Sun Mon Tue Wed Thu Fri Sat" << endl;
  for (int i = 1; i < dayNum; i++)
  {
    if (i == 1)
    {
      cout << "   ";
    }
    else if (i < 10)
    {
      cout << "    ";
    }
  }

  for (int j = 1; j <= numDays; j++)
  {

    if (rowCount == 7)
    {
      cout << endl;
      rowCount = 0;
    }
    if (rowCount == 0 && j < 10)
    {
      cout << "  " << j;
    }
    else if (rowCount == 0 && j >= 10)
    {
      cout << " " << j;
    }

    else if (j < 10)
    {
      cout << "   " << j;
    }
    else
    {
      cout << "  " << j;
    }
    rowCount++;
  }
}
