
#include <iostream>
using namespace std;

int main()
{
  // setting variables
  int b = 0;
  cin >> b;
  int arr[b];
  // run loop b amount of times
  for (int i = 0; i < b; i++)
  {
    cin >> arr[i];
  }
  for (int j = b - 1; j >= 0; j--)
  {
    cout << arr[j] << " ";
  }
  return 0;
}