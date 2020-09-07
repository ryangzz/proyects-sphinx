# C - Strings

Las cadenas son en realidad una matriz unidimensional de caracteres terminados por un carácter nulo '\ 0'. Por lo tanto, una cadena terminada en nulo contiene los caracteres que componen la cadena seguida de un nulo .

La siguiente declaración e inicialización crean una cadena que consta de la palabra "Hola". Para contener el carácter nulo al final de la matriz, el tamaño de la matriz de caracteres que contiene la cadena es uno más que el número de caracteres de la palabra "Hola".

```C
char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
```
Si sigue la regla de inicialización de la matriz, puede escribir la declaración anterior de la siguiente manera:

```C
char greeting[] = "Hello";
```

![picture alt](https://www.tutorialspoint.com/cprogramming/images/string_representation.jpg "Strings in C")

## Poniendo en la practica lo aprendido

Solo veremos un pequeño programa de como se veria en realidad ya completo

```C
#include <stdio.h>

int main () {

   char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
   printf("Greeting message: %s\n", greeting );
   return 0;
}
```