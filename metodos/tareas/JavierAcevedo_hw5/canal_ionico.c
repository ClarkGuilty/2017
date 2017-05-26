#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<time.h>

FILE *f1;
FILE *f2;
double func(double x0, double y0);
void n();
void nP(double D);
double prob();
double x = -2;
double y = 8;
double rtax = 0;
double rtay = 0;
double xi[100];
double yi[100];
double a;
double b;
double mem;
int total = 0;
int i;
int j;
int k;
double newx = 0;
double newy = 0;

double nx = 0;
double ny = 0;



int main(void){
   	srand((unsigned) time(NULL));
   	
    FILE *par1=fopen("res1.txt","w+");   	
    f1=fopen("Canal_ionico.txt", "r");
    if(f1 == NULL){
    printf("Problem opening file %s\n", "Canal_ionico.txt");
    exit(1);
}
    while(    fscanf(f1, "%lf\n", &a) == 1){
    yi[total/2] = a;
    total = total + 1;
    if((total % 2) == 1){ 
                xi[total/2] = a;
                }
    }
    for(i = 0; i<total/2;i++)
    {
          //printf("%f %f\n", xi[i], yi[i]);
          }
          
    //Corre el primer MCMC   
    int iter = 200000;
	i = 0;
    while(i<iter){
          fprintf(par1, "%f %f\n", x, y);
          nP(0.3);
          double alpha = func(newx,newy)/func(x,y) ;
            if(alpha >1){
                               x = newx;
                               y = newy;
                               rtax = x;
                               rtay = y;
                               }
            else{
                 mem = (double)rand()/RAND_MAX;
                 if(mem>alpha){
                               x = newx;
                               y = newy;
                                  }
                 }
	i = i+1;
          }



//Imprime la primera parte de los resultados a consola y a los .txt
//x y R
printf("rta = %f %f %f\n", newx,newy, func(newx,newy));
	FILE *out=fopen("resultados.txt","w+");    
 fprintf(out,"%f %f %f\n", newx,newy, func(newx,newy));			
          
fclose(f1);
fclose(par1);
          //Segundo archivo.
x = 0;
y = 0;
rtax = 0;
rtay = 0;
total = 0;
newx = 0;
newy = 0;
   		FILE *par2=fopen("res2.txt","w+"); 
f2=fopen("Canal_ionico1.txt", "r");
if(f2 == NULL){
    printf("Problem opening file %s\n", "Canal_ionico1.txt");
    exit(1);
}
    while(    fscanf(f2, "%lf\n", &a) == 1){
    yi[total/2] = a;
    total = total + 1;
    if((total % 2) == 1){ 
                xi[total/2] = a;
                }
    }
    for(i = 0; i<total/2;i++)
    {
          //printf("%f %f\n", xi[i], yi[i]);
          }
          
    //Corre el segundo MCMC.
    iter = 200000;
    i = 0;
    while(i<iter){
          fprintf(par2, "%f %f\n", x, y);
          nP(0.3);
          double alpha = func(newx,newy)/func(x,y) ;
            if(alpha >1){
                               x = newx;
                               y = newy;
                               rtax = x;
                               rtay = y;
                               }
            else{
                 mem = (double)rand()/RAND_MAX;
                 if(mem>alpha){
                               x = newx;
                               y = newy;
                                  }
                 }
                 i++;
          }
    

printf("rta = %f %f %f\n", newx,newy, func(newx,newy));

 fprintf(out,"%f %f %f\n", newx,newy, func(newx,newy));			
fclose(f2);
fclose(out);
fclose(par2);



}

//radio
double func(double x0, double y0){
       mem = 0;
       double rta = (double) RAND_MAX;
       for(k = 0;k<total/2;k++){
             mem = sqrt( pow((x0-xi[k]),2) + pow((y0-yi[k]),2))-1;
//             printf("mem = %f\n", mem);
             if(mem<rta){
                       rta = mem;
                       }
             }
       return rta;
       }

//actualiza n un nuevo n.
void n(){
     nx= ((double)rand()/RAND_MAX)*2-1.0;
     ny = ((double)rand()/RAND_MAX)*2-1.0;
     mem = sqrt(nx*nx+ny*ny);
     nx = nx/mem;
     ny = ny/mem;
    // nx = nx - (vx*nx)*vx;
    // ny = ny - (vy*ny)*vy;
     
     }

void nP(double D){
     n();

     newx = x + D*nx;
     newy = y + D*ny;
     
     }
     


       
