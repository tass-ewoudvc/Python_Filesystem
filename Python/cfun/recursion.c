#include <stdio.h>
#include <stdlib.h>

int resultRec(int n){
	if(n>0){
		return n + resultRec(n-1);
	}
	else{
		return n;
	}
}

int main(){
	int n = 5;
	int res = resultRec(n);
	printf("The result is %d", res);
}
