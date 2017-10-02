#include <stdlib.h>
#include <stdio.h>

struct Time { int days; int hours; int minutes; int seconds; };

void byebye(){
	printf("Bye bye\n");
	exit(-1);
}


int main(){
	int sample = 0;
	int *x=0;
	x = void *malloc(sample*4);
	struct Time time1 = {3,17,3,46};
	struct Time time2 = {5,3,23,12};
	if ( time1.days<0 || time2.days<0 ||
	     time1.hours<0 || time2.hours<0 || time2.hours>24 || time2.hours>24 ||
	     time1.minutes<0 || time2.minutes<0 || time2.minutes>60 || time2.minutes>60 ||
	     time1.seconds<0 || time2.seconds<0 || time2.seconds>60 || time2.seconds>60 ){
		byebye();
		}
	
	











}
	

