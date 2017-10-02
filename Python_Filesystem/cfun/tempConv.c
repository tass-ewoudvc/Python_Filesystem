#include <stdio.h>
#include <stdlib.h>

double tempConv(double temp, char a[]);

int main(){
	double temp = 300;
	char a[] = "ftk";
	double newTemp = tempConv(temp,a);
	printf("The value is: %.2f",newTemp);
}

double tempConv(double temp, char a[]){
	if (a[0] == 'f'){
		temp = (temp -32) * 5/9;
	}
	else if (a[0] == 'k'){
		temp = temp - 273.15; 
	}
	if (a[2] == 'k'){
		temp = temp + 273.15;
	}
	else if (a[2] == 'f'){
		temp = (temp + 32)*9/5; 
	}
	return temp;
}
		
		
	
