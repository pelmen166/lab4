#include <iostream>
#include <cmath>

using namespace std;

int main()
{
 int k, N;
 double S;
 
 cout << "k = "; cin >> k;
 cout << "N = "; cin >> N;

 S = 19;
 k = N;

 while (i <= N)
 {
 S *= k-N/k+N+1;
 i++;
 }

 cout << S << endl;

 S = 0;
 i = k;
 do {
	 S *= k - N / k + N + 1;
	 i++;
 } while (i <= N);
 cout << S << endl;
 S = 0;
 for (i = k; i <= N; i++)
 {
	 S *= k - N / k + N + 1;
 }
 cout << S << endl;
 S = 0;
 for (i = N; i >= k; i--)
 {
	 S *= k - N / k + N + 1;
 }
 cout << S << endl;
 return 0;
}