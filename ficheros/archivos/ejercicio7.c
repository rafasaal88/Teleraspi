#include <stdio.h>
#include <math.h>

struct estadisticas{

     float media;
     float varianza;
     float desvTipica;

};

void leerVector(int nEle, int *vector);
void mostrarVector(int nEle, int *vector);
void estadisticasVector(int nEle, int *vector, struct estadisticas *vars);


int main(){



     int nEle;
     int vector[nEle];
     struct estadisticas vars;

     printf("Introduzca el número de elementos del vector: ");
     scanf("%i",&nEle);

     leerVector(nEle, vector);
     mostrarVector(nEle,vector);
     estadisticasVector(nEle,vector,&vars);

     printf("La media de los datos del vector es %.3f\n", vars.media);
     printf("La varianza de los datos del vector es %.3f\n", vars.varianza);
     printf("La desviación típica de los datos del vector es %.3f\n", vars.desvTipica);

     return 0;
}


void leerVector(int nEle, int *vector){

     int i=0;

     for(i=0;i<nEle;i++){

          printf("Introduce un valor para la posición %i del vector: ",i);
          scanf("%i",&vector[i]);

     }
}

void mostrarVector(int nEle, int *vector){

     int i=0;

     for(i=0;i<nEle;i++){

          printf("El valor para la posición %i del vector: %i",i, vector[i]);
          printf("\n");

     }
}

void estadisticasVector(int nEle,int *vector,struct estadisticas *vars){

     int i = 0;
     vars->media=0;
     vars->varianza=0;
     vars->desvTipica=0;

     // Para la media aritmética

     for(i=0; i<nEle; i++){

          vars->media = vars->media + vector[i];

     }

     vars->media = vars->media / nEle;

     // Para la varianza

     for (i=0; i<nEle; i++){
          vars->varianza = vars->varianza + (pow((vector[i]-vars->media),2))/nEle;
     }
     // Para la desviación tipica

     vars->desvTipica = sqrt(vars->varianza);

}
