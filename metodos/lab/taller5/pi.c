#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//float delta_n_step(float n, float lambda, float dt);
//void single_decay(float N0, float lambda, float dt, float *datos, int Nes);
double inside;
double total;
double mcPi;
double x;
double y;
int i;
int j;
int k;

//Javier Acevedo 201422995  02 de Mayo de 2017
int main(){
  	FILE *out=fopen("resultados.txt","a");
  
    inside = 0;
//	float *data=malloc(enes*sizeof(float)); /*Alocamos memoria*/
    total = 100000;
    x = 0;
    y = 0;
	float Dt = 0.001;

//	srand48(1);
	
    for(i = 0; i< total;i++){
          x = (double) rand()/RAND_MAX;
          y = (double) rand()/RAND_MAX;
          printf("%f",y);
          if(x*x+y*y < 1){
                     inside++;
                     }
          
          
          }
  	mcPi = inside/total;
    printf("%f\n", mcPi);
	mcPi = 4*inside/total;
	fprintf(out, "El valor de la constante pi es: \\textit{%f}", mcPi);
	printf("El valor de la constante pi es: \\textit{%f}", mcPi);
	return 0;
}














