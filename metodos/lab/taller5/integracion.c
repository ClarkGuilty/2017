#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//float delta_n_step(float n, float lambda, float dt);
//void single_decay(float N0, float lambda, float dt, float *datos, int Nes);
double inside;
double total;
double integral;
double x;
double y;
int i;
int j;
int k;
double fune(double x);

//Javier Acevedo 201422995  02 de Mayo de 2017
double fune(double x){
       
       return exp(-x);
       
       }

int main(){
  	FILE *out=fopen("resultados.txt","w+");
  
    inside = 0;
//	float *data=malloc(enes*sizeof(float)); /*Alocamos memoria*/
    total = 100000;
    x = 0;
    y = 0;


//	srand48(1);
	
    for(i = 0; i< total;i++){
          x = (double) rand()/RAND_MAX;
          y = (double) rand()/RAND_MAX;
          printf("%f",x);
          if(exp(-x) - y > 0){
                     inside++;
                     }
          
          
          }
  	integral = inside/total;
	fprintf(out, "El valor de la integral es: \\textit{%f}\n", integral);
	printf("El valor de la integral es: \\textit{%f}", integral);
	return 0;
}

