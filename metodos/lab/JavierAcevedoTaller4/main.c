#include <stdio.h>
#include <stdlib.h>
#include <math.h>


float paso();


//Javier Alejandro Acevedo Barroso 201422995 
int main(){

  


	srand48(1);
	


	FILE *out=fopen("random_walks.txt","w+");
	int i;
	int j;
	float actual;
	for(i = 0; i<100000;i++){
		actual = 0;
		for(j=0;j<500;j++){
			actual = actual + paso();
        }
        fprintf(out,"%f\n",actual);			


	}

	
	
		
	return 0;
}

float paso(){


	float rand_num = drand48();
	if(rand_num < 0.5){
		return -1.0;
	} else {
		return 1.0;
	}


}




