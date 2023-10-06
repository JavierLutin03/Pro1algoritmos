#include <iostream>

using namespace std;

int main() {
  // Declarar variables
  int filas, columnas;
  int numero;
  int mayor = INT_MIN;
  int suma = 0;

  // Leer las dimensiones de la matriz
  cout << "Ingrese el número de filas: ";
  cin >> filas;
  cout << "Ingrese el número de columnas: ";
  cin >> columnas;

  // Declarar la matriz
  int matriz[filas][columnas];

  // Leer los valores de la matriz
  for (int i = 0; i < filas; i++) {
    for (int j = 0; j < columnas; j++) {
      cout << "Ingrese el valor en la posición (" << i << "," << j << "): ";
      cin >> numero;
      matriz[i][j] = numero;

      // Actualizar el número mayor
      if (numero > mayor) {
        mayor = numero;
      }

      // Actualizar la suma
      suma += numero;
    }
  }

  // Imprimir el número mayor
  cout << "El número mayor es: " << mayor << endl;

  // Imprimir los datos de la matriz
  for (int i = 0; i < filas; i++) {
    for (int j = 0; j < columnas; j++) {
      cout << matriz[i][j] << " ";
    }
    cout << endl;
  }

  // Imprimir el promedio de la matriz
  float promedio = (float)suma / (filas * columnas);
  cout << "El promedio de la matriz es: " << promedio << endl;

  return 0;
}
