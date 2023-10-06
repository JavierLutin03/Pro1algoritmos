#include <iostream>
#include <algorithm>

using namespace std;

int main() {
 
  int n;
  int numeros[100];


  cin >> n;

 
  for (int i = 0; i < n; i++) {
    cin >> numeros[i];
  }

  sort(numeros, numeros + n);

  
  int mediana = numeros[n / 2];

  double promedio = 0;
  for (int i = 0; i < n; i++) {
    promedio += numeros[i];
  }
  promedio /= n;

 
  cout << "Mediana: " << mediana << endl;
  cout << "Promedio: " << promedio << endl;

  return 0;
}

