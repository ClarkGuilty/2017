#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float delta_n_step(float n, float lambda, float dt);
void single_decay(float N0, float lambda, float dt, float *datos, int Nes);
float n_t(float t, float N0, float lambda);
float prom(float *datos, int Nes);


//Javier Acevedo 201422995  28 de Marzo de 2017
int main(){

  
	int enes =15;
	float *data=malloc(enes*sizeof(float)); /*Alocamos memoria*/
	float N_0 = 100.0;
	float Lambda = 1.0/2.0;
	float Dt = 0.001;

	srand48(1);
	
	single_decay(N_0, Lambda, Dt, data, enes);
		
	return 0;
}

float n_t(float t, float N0, float lambda){
	return N0*exp(-lambda*t);
}

float delta_n_step(float n, float lambda, float dt){
	
	float rand_num = drand48();
	if(rand_num < lambda*n*dt){
		return -1.0;
	} else {
		return 0.0;
	}
}

float prom(float *datos, int Nes){
	float rta = 0;
	int i;
	for(i = 0; i<Nes;i++){
		rta +=  datos[i];
	    
	}
	rta = rta/Nes;
	return rta;
}





void single_decay(float N0, float lambda, float dt, float *datos, int Nes){

  
	int j;
	float t_total = 5.0/lambda;
	int n_points = (int)t_total/dt;
	int i;
	
	float t = 0.0;
	float n = n_t(0.0, N0, lambda);
	for(j = 0; j<Nes; j++){
		

		datos[j] = n;	
	
	}
	float pro = prom(datos,Nes);
	
    FILE *out=fopen("data.txt","w+");
    
	fprintf(out,"%f %f\n", t, pro);

	float non;
	for(i=0;i<n_points;i++){
		int k;
		t += dt;
		non = n_t(t,N0,lambda);

		float delta_n;
		for(k = 0;k<Nes;k++){
			delta_n = delta_n_step(non, lambda, dt);
			datos[k] = non+ delta_n;

		}
		float satan = prom(datos, Nes);
		
		//printf("%f %f\n",t, satan);
		//printf("%f\n",satan);
		
		fprintf(out,"%f %f\n", t, satan);		
	}
}
















