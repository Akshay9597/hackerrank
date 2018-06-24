#include <iostream>
#include <new>
using namespace std;
int main() {
	int T, n, k, x, d, *p, i, j;
	long long int tmp, sum;
	cin >> T;
	for(i = 0; i < T; i++) {
		cin >> n >> k >> x >> d;
		sum = 0;
		p = new int[n];
		for(j = 0; j < n; j++)
		 	cin >> p[j];
		for(j = 0; j < n; j++) {
			tmp = p[j] * x / 100;
			if(tmp < k)
				sum = sum + k;
			else
				sum = sum + tmp;
		}
		if(sum <= d)
			cout << "fee" << endl;
		else
			cout << "upfront" << endl;
		delete [] p;
	}
	return 0;
}
