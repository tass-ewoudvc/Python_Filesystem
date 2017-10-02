#include <stdio.h>
#include <stdlib.h>

int recCount(int* numbas,int danum, int i){ //use pointer to pass the memory allocation 
	int total = 0;
	//printf("size of array is: %d\n", size); 
	if(i>=0){
		if (danum == numbas[i]){
			total++;
		}
		return total+recCount(numbas, danum, i-1);
	}
	else {
		return total;
	}
}

int main(){
	int numbas[10] = {1,2,2,2,5,8,6,8,5,2};
	int i = sizeof(numbas)/sizeof(numbas[0]); //start with maximum and decrement
	int danum = 2;
	int output = recCount(&numbas, danum, i-1);
	printf ("Danum appears this many times: %d\n", output);
}
