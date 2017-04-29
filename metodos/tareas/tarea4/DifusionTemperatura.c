# include <stdio.h>
# include <math.h>

#define L 100

double actual[L][L][2];
double pasado[L][L];

int main ()
{
   int a, b;
   a = 1234;
   b = -344;
  
   printf("The absolute value of %d is %lf\n", a, fabs(a));
   printf("The absolute value of %d is %lf\n", b, fabs(b));
   
   return(0);
}





