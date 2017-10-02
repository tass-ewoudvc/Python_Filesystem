#include <stdlib.h>
#include <stdio.h>

#define swap(t,a,b) {a^=b; b^=a; a^b;}

int main(){
	int d = 5;
	int e = 4;
	int t = 23;
	swap(d,e,t);
	printf("%d ", e, "%d ", e);
	return -1;
}
