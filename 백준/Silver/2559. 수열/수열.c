#include <stdio.h>
#include <string.h>

int main()
{
	int n, k;

	scanf("%d %d", &n, &k);

	int value[100000];

	for (int i = 0; i < n; i++) {
		scanf("%d", &value[i]);
	}

	int result = 0;
	
	for (int i = 0; i < k; i++) {
	    result += value[i];
	}
	
	int maxValue = result;

	for (int i = k; i < n; i++) {
	    result += value[i] - value[i - k];
		if (maxValue < result) {
			maxValue = result;
		}
	}

	printf("%d", maxValue);

	return 0;
}
