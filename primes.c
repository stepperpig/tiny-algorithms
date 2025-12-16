#include <stdio.h>
#include <stdlib.h>

void factor(int n, int i) {
	if (n == 1) {
		return;
	}

	if (n % i == 0) { // if divisible, divide and recurse
		printf("%d ", i);
		factor(n/i, i);
	} else {		 // if not, increase factor and try again
		factor(n, i+1);
	}
}

int main(void) {
	// Q: What is a prime number?
	// A: Whole number > 1 that only has factors 1 and itself.

	// Prime Factors of 6:
	// If 6 greater than 1, divide by 2? Yes. (Add 2. Result: 3). 
	// If 3 greater than 1, divide by 2? No. Divide by 3? Yes. (Add 3. Result: 1).

	factor(7, 2);
}