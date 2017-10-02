#include <stdio.h>
#include <stdlib.h>

int safeMalloc(int size);

int main(){
	int size1 = 500000000;
	safeMalloc(size1);
}

int safeMalloc(int size){
	int x = (int*)malloc(size);
	if (x == 0){
		printf("Allocation has failed.");
		exit(-1);
	}
}
		
