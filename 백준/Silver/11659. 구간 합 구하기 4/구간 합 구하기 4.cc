#include <iostream>
using namespace std;

int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, q;

	cin >> n >> q;

	int value[100000];

	int result[100001] = {0};

	for (int i = 0; i < n; i++)
	{
		cin >> value[i];
	}

	for (int i = 1; i <= n; i++)
	{
		result[i] = result[i-1] + value[i-1];
	}

	for (int j = 0; j < q; j++)
	{
		int s, k;
		cin >> s >> k;
		cout << result[k] - result[s - 1] << '\n';
	}

	return 0;
}