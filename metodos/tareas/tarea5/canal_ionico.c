#include <stdio.h>
#include <stdlib.h>
#include <math.h>

FILE *heh;
double func(double x0, float y0);
double x = 0;
double y = 0;
double xi = 0;
double yi = 0;
double *a;
double *b;
float dat;


int main(void){
    heh=fopen("./CircuitoRC.txt", "r");
    if(heh == NULL){
    printf("Problem opening file %s\n", "./CircuitoRC.txt");
    exit(1);
}

    fscanf(heh, "%lf.4 %lf.4\n",&a, &b);
    
    printf("%f %f\n", a, b);

    
    
}
