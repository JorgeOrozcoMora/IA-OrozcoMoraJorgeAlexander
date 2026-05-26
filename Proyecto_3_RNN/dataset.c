#include <stdio.h>

/* 1: Suma de dos numeros */
int suma(int a,int b){
    int r=0;
    r=a+b;
    return r;
}

/* 2: Resta de dos numeros */
int resta(int a,int b){
    int r=0;
    r=a-b;
    return r;
}

/* 3: Multiplicacion de dos numeros */
int multiplicacion(int a,int b){
    int r=0;
    r=a*b;
    return r;
}

/* 4: Division de dos numeros */
int division(int a,int b){
    int r=0;
    if(b!=0){
        r=a/b;
    }
    return r;
}

/* 5: Calcula el cuadrado */
int numero_al_cuadrado(int a){
    int r=0;
    r=a*a;
    return r;
}

/* 6: Calcula el cubo */
int numero_al_cubo(int a){
    int r=0;
    r=a*a*a;
    return r;
}

/* 7: Calcula potencia */
int calcular_potencia(int base,int exp){
    int r=1;
    int i=0;
    for(i=0;i<exp;i++){
        r=r*base;
    }
    return r;
}

/* 8: Suma de 1 hasta n */
int suma_numero_n(int n){
    int r=0;
    int i=0;
    for(i=1;i<=n;i++){
        r=r+i;
    }
    return r;
}

/* 9: Calcular factorial */
int factorial(int n){
    int r=1;
    int i=0;
    for(i=1;i<=n;i++){
        r=r*i;
    }
    return r;
}

/* 10: Verifica si es par */
int numero_par(int n){
    int r=0;
    if(n%2==0){
        r=1;
    }
    return r;
}

/* 11: Verifica si es impar */
int numero_impar(int n){
    int r=0;
    if(n%2!=0){
        r=1;
    }
    return r;
}

/* 12: Devuelve el mayor de dos numeros */
int numero_mayor(int a,int b){
    int r=0;
    if(a>b){
        r=a;
    }else{
        r=b;
    }
    return r;
}

/* 13: Devuelve el menor de dos */
int numero_menor(int a,int b){
    int r=0;
    if(a<b){
        r=a;
    }else{
        r=b;
    }
    return r;
}

/* 14: Valor absoluto */
int valor_absoluto(int a){
    int r=0;
    if(a<0){
        r=a*-1;
    }else{
        r=a;
    }
    return r;
}

/* 15: Promedio de dos numeros */
int promedio(int a,int b){
    int r=0;
    r=(a+b)/2;
    return r;
}

/* 16: Suma numeros pares hasta n */
int suma_pares(int n){
    int r=0;
    int i=0;
    for(i=0;i<=n;i++){
        if(i%2==0){
            r=r+i;
        }
    }
    return r;
}

/* 17: Suma numeros impares hasta n */
int suma_impares(int n){
    int r=0;
    int i=0;
    for(i=0;i<=n;i++){
        if(i%2!=0){
            r=r+i;
        }
    }
    return r;
}

/* 18: Imprime tabla de multiplicar */
int tabla_multiplicacion(int n){
    int i=0;
    for(i=1;i<=10;i++){
        printf("%d\n",n*i);
    }
    return 0;
}

/* 19: Cuenta cuantos digitos tiene un numero */
int contar_digitos(int n){
    int r=0;
    while(n!=0){
        n=n/10;
        r=r+1;
    }
    return r;
}

/* 20: Inviertir numero */
int invertir_numero(int n){
    int r=0;
    int d=0;
    while(n!=0){
        d=n%10;
        r=r*10+d;
        n=n/10;
    }
    return r;
}

/* 21: Suma los digitos de un numero */
int suma_digitos(int n){
    int r=0;
    int d=0;
    while(n!=0){
        d=n%10;
        r=r+d;
        n=n/10;
    }
    return r;
}

/* 22: Mayor de tres numeros */
int mayor_tres_numeros(int a,int b,int c){
    int r=0;
    r=a;
    if(b>r){
        r=b;
    }
    if(c>r){
        r=c;
    }
    return r;
}

/* 23: Menor de tres numeros */
int menor_tres_numeros(int a,int b,int c){
    int r=0;
    r=a;
    if(b<r){
        r=b;
    }
    if(c<r){
        r=c;
    }
    return r;
}

/* 24: Verifica si es primo */
int numero_primo(int n){
    int i=0;
    int r=1;
    if(n<=1){
        r=0;
    }
    for(i=2;i<n;i++){
        if(n%i==0){
            r=0;
        }
    }
    return r;
}

/* 25: Area de un cuadrado */
float area_cuadrado(float lado){
    float r=0;
    r=lado*lado;
    return r;
}

/* 26: Fibonacci */
int fibonacci(int n){
    int a=0,b=1,c=0,i=0;
    for(i=0;i<n;i++){
        c=a+b;
        a=b;
        b=c;
    }
    return a;
}

/* 27: Maximo comun divisor */
int maximo_comun_divisor(int a,int b){
    while(b!=0){
        int t=b;
        b=a%b;
        a=t;
    }
    return a;
}

/* 28: Minimo comun multiplo */
int minimo_comun_multiplo(int a,int b){
    int r=0;
    r=(a*b)/mcd(a,b);
    return r;
}

/* 29: Suma de cuadrados */
int suma_cuadrados(int n){
    int r=0,i=0;
    for(i=1;i<=n;i++){
        r=r+i*i;
    }
    return r;
}

/* 30: Suma de cubos */
int suma_cubos(int n){
    int r=0,i=0;
    for(i=1;i<=n;i++){
        r=r+i*i*i;
    }
    return r;
}

/* 31: Cuenta pares hasta n */
int contar_pares(int n){
    int r=0,i=0;
    for(i=0;i<=n;i++){
        if(i%2==0){
            r=r+1;
        }
    }
    return r;
}

/* 32: Cuenta impares hasta n */
int contar_impares(int n){
    int r=0,i=0;
    for(i=0;i<=n;i++){
        if(i%2!=0){
            r=r+1;
        }
    }
    return r;
}

/* 33: Mayor numero en un arreglo */
int mayor_numero_arreglo(int a[],int n){
    int r=a[0],i=0;
    for(i=1;i<n;i++){
        if(a[i]>r){
            r=a[i];
        }
    }
    return r;
}

/* 34: Menor numero en un arreglo */
int menor_numero_arreglo(int a[],int n){
    int r=a[0],i=0;
    for(i=1;i<n;i++){
        if(a[i]<r){
            r=a[i];
        }
    }
    return r;
}

/* 35: Suma de valores de un arreglo */
int suma_arreglo(int a[],int n){
    int r=0,i=0;
    for(i=0;i<n;i++){
        r=r+a[i];
    }
    return r;
}

/* 36: Promedio valores de un arreglo */
int promedio_arreglo(int a[],int n){
    int r=0;
    r=suma_arreglo(a,n)/n;
    return r;
}

/* 37: Multiplica numeros de arreglo */
int multiplicar_arreglo(int a[],int n){
    int r=1,i=0;
    for(i=0;i<n;i++){
        r=r*a[i];
    }
    return r;
}

/* 38: Busca valor en arreglo */
int buscar_valor_arreglo(int a[],int n,int x){
    int i=0;
    for(i=0;i<n;i++){
        if(a[i]==x){
            return 1;
        }
    }
    return 0;
}

/* 39: Cuenta cuantas veces aparece un valor en el arreglo */
int contar_valor(int a[],int n,int x){
    int r=0,i=0;
    for(i=0;i<n;i++){
        if(a[i]==x){
            r=r+1;
        }
    }
    return r;
}

/* 40: Suma multiplos (X) */
int suma_multiplos(int n,int m){
    int r=0,i=0;
    for(i=0;i<=n;i++){
        if(i%m==0){
            r=r+i;
        }
    }
    return r;
}

/* 41: Verificar si es multiplo */
int verificar_multiplo(int a,int b){
    int r=0;
    if(a%b==0){
        r=1;
    }
    return r;
}

/* 42: Potencia de 2 */
int potencia_de_2(int n){
    int r=1,i=0;
    for(i=0;i<n;i++){
        r=r*2;
    }
    return r;
}

/* 43: Perimetro de un cuadrado */
float perimetro_cuadrado(float lado){
    float r=0;
    r=lado*4;
    return r;
}

/* 44: Area de un rectangulo */
float area_rectangulo(float base,float altura){
    float r=0;
    r=base*altura;
    return r;
}

/* 45: Area de un triangulo */
float area_triangulo(float base,float altura){
    float r=0;
    r=(base*altura)/2;
    return r;
}

/* 46: Cuenta los divisores de un numero */
int contar_divisores(int n){
    int r=0,i=0;
    for(i=1;i<=n;i++){
        if(n%i==0){
            r=r+1;
        }
    }
    return r;
}

/* 47: Perimetro de un triangulo */
float perimetro_triangulo(float a,float b,float c){
    float r=0;
    r=a+b+c;
    return r;
}

/* 48: Area de un circulo */
float area_circulo(float radio){
    float r=0;
    r=3.1416*radio*radio;
    return r;
}

/* 49: Perimetro de un circulo */
float perimetro_circulo(float radio){
    float r=0;
    r=2*3.1416*radio;
    return r;
}

/* 50: Area de un trapecio */
float area_trapecio(float B,float b,float h){
    float r=0;
    r=((B+b)*h)/2;
    return r;
}

/* 51: Area de un rombo */
float area_rombo(float D,float d){
    float r=0;
    r=(D*d)/2;
    return r;
}

/* 52: Volumen de un cubo */
float volumen_cubo(float lado){
    float r=0;
    r=lado*lado*lado;
    return r;
}

/* 53: Volumen de un prisma rectangular */
float volumen_prisma(float largo,float ancho,float alto){
    float r=0;
    r=largo*ancho*alto;
    return r;
}

/* 54: Mayor digito de un numero */
int mayor_digito(int n){
    int r=0,d=0;
    while(n!=0){
        d=n%10;
        if(d>r){
            r=d;
        }
        n=n/10;
    }
    return r;
}

/* 55: Menor digito de un numero */
int menor_digito(int n){
    int r=9,d=0;
    while(n!=0){
        d=n%10;
        if(d<r){
            r=d;
        }
        n=n/10;
    }
    return r;
}

/* 56: Calcular distancia */
float distancia(float velocidad,float tiempo){
    float r=0;
    r=velocidad*tiempo;
    return r;
}

/* 57: Calcular tiempo */
float tiempo(float distancia,float velocidad){
    float r=0;
    if(velocidad!=0){
        r=distancia/velocidad;
    }
    return r;
}


/* 58: Area de un pentagono regular */
float area_pentagono(float perimetro,float apotema){
    float r=0;
    r=(perimetro*apotema)/2;
    return r;
}

/* 59: Convierte grados a radianes */
float grados_a_radianes(float grados){
    float r=0;
    r=grados*3.1416/180;
    return r;
}

/* 60: Calcular velocidad */
float velocidad(float distancia,float tiempo){
    float r=0;
    if(tiempo!=0){
        r=distancia/tiempo;
    }
    return r;
}