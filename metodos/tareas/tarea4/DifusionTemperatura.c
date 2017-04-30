# include <stdio.h>
# include <math.h>

#define L 100

double actual[L][L];
double pasado[L][L];
double T[10000][4];
int i;
int j;
int k;
int l;
double dx;
double v;
double alpha;
double dt;



double pos(int x, int y){
    x = x%100;
    y = y%100;
    return actual[x][y];
}

double prom(){
       double total = 0.0;
       for(i = 0;i<L;i++){
             for(j = 0;j<L;j++){
                   total = total+ actual[i][j];
                   }
             }
             return        total = total / 10000;      
}
       
int con1(){
    for(i = 0;i<L;i++){
      for(j = 0;j<L;j++){
            actual[i][j] = 50;
            actual[i][j] = 50;
            pasado[i][j] = 50;
            }
    }

 for(i = 49-5;i<49+5;i++){
      for(j = 19; j<19+20;j++){
            actual[i][j] = 100;        
            }
      }   
      return 1;
}

//Resuelve la ecuación para un tiempo tmax en segundos y con condiciones de frontera 1.
int eq1(int tmax){
tmax = tmax*4;
for(k = 0 ; k<tmax;k++){
      if(tmax == 10000){
                    T[k][0] = prom();
                    }
      for(i = 1;i<L-1;i++){
            for(j = 1;j<L-1;j++){
                  pasado[i][j]=actual[i][j];
                  actual[i][j]= actual[i][j] - 4*alpha*actual[i][j] + alpha*(actual[i-1][j]+actual[i+1][j]+actual[i][j-1]+actual[i][j+1]);
                  }
            }
      }
    
    return 1;  
}

//Resuelve la ecuación para un tiempo tmax en segundos y con condiciones de frontera T = 50.
int eq2(int tmax){
tmax = tmax*4;
for(k = 0 ; k<tmax;k++){
            if(tmax == 10000){
                    T[k][2] = prom();
                    }
      for(i = 1;i<L-1;i++){
            for(j = 1;j<L-1;j++){
                  pasado[i][j]=actual[i][j];
                  if( actual[i][j] != 100){
                      
                  actual[i][j]= actual[i][j] - 4*alpha*actual[i][j] + alpha*(actual[i-1][j]+actual[i+1][j]+actual[i][j-1]+actual[i][j+1]);
                  }
                  }
            }
      }
    
    return 1;
    
}

//Resuelve la ecuación para un tiempo tmax en segundos y con condiciones de frontera 1 periodicas. 
int eq3(int tmax){
tmax = tmax*4;
for(k = 0 ; k<tmax;k++){
            if(tmax == 10000){
                    T[k][1] = prom();
                    }
      for(i = 0;i<L;i++){
            for(j = 0;j<L;j++){
                  pasado[i][j]=actual[i][j];
                  actual[i][j]= pos(i,j) - 4*alpha*pos(i,j) + alpha*(pos(i-1,j)+pos(i+1,j)+pos(i,j-1)+pos(i,j+1));
                  }
            }
      }
    
    return 1;  
}

//Resuelve la ecuación para un tiemp tmax en segundos y con condiciones de frontera 2 periodicas.
int eq4(int tmax){
tmax = tmax*4;
for(k = 0 ; k<tmax;k++){
            if(tmax == 10000){
                    T[k][3] = prom();
                    }
      for(i = 0;i<L;i++){
            for(j = 0;j<L;j++){
                  pasado[i][j]=actual[i][j];
                                    if( actual[i][j] != 100){
                  actual[i][j]= pos(i,j) - 4*alpha*pos(i,j) + alpha*(pos(i-1,j)+pos(i+1,j)+pos(i,j-1)+pos(i,j+1));
                  }
                  }
            }
      }
    
    return 1;  
}



//Imprime el arreglo 
int impD(char s[]){
    
    FILE *arch =fopen(s,"w+");    
    for(i = 0;i<L;i++){
      for(j = 0;j<L;j++){
            fprintf(arch,"%f ",actual[i][j]);
            }
            fprintf(arch,"\n");
    }

    
    
}


int main ()
{
    
dx = 0.01;
v = 0.0001;
alpha = 0.25;
dt = 0.25;


//imprimir para las condiciones iniciales.
con1();
impD("c1t0.txt");


//imprimir para las condiciones iniciales 1, t = 100s, con fronteras fijas en T=50.
con1();
eq1(100);
impD("c1t100c.txt");

//imprimir para las condiciones iniciales 1, t = 2500s, con fronteras fijas en T=50.
con1();
eq1(2500);
impD("c1t2500c.txt");




//imprimir para las condiciones iniciales 1, t = 100s, con fronteras periodicas.
con1();
eq3(100);
impD("c1t100p.txt");

//imprimir para las condiciones iniciales 1, t = 2500s, con fronteras periodicas.
con1();
eq3(2500);
impD("c1t2500p.txt");




//imprimir para las condiciones iniciales 2, t = 100s, con fronteras fijas en T=50.
con1();
eq2(100);
impD("c2t100c.txt");

//imprimir para las condiciones iniciales 2, t = 2500s, con fronteras fijas en T=50.
con1();
eq2(2500);
impD("c2t2500c.txt");




//imprimir para las condiciones iniciales 2, t = 100s, con fronteras periodicas.
con1();
eq4(100);
impD("c2t100p.txt");

//imprimir para las condiciones iniciales 2, t = 2500s, con fronteras periodicas.
con1();
eq4(2500);
impD("c2t2500p.txt");





FILE *arch =fopen("Tmean.txt","w+");
     for(i = 0;i<10000;i++){
           fprintf(arch,"%f %f %f %f\n",T[i][0],T[i][1],T[i][2], T[i][3]);
                 
    }














}





