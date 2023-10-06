#include <iostream>

using namespace std;

float calcularCargos(int horas) {

  if (horas <= 3) {
    return 2.00;
  }

  float cargoExtra = (horas - 3) * 0.50;

  
  if (cargoExtra > 7.00) {
    return 10.00;
  }

  return 2.00 + cargoExtra;
}

int main() {

  int horas[3];
  float cargos[3];
  float total = 0;

  for (int i = 0; i < 3; i++) {
    cout << "Ingrese las horas de estacionamiento para el automovil " << i + 1 << ": ";
    cin >> horas[i];
  }


  for (int i = 0; i < 3; i++) {
    cargos[i] = calcularCargos(horas[i]);
    total += cargos[i];
  }

  cout << "Automovil | Horas | Cargo" << endl;
  for (int i = 0; i < 3; i++) {
    cout << "     " << i + 1 << "     | " << horas[i] << "     | " << cargos[i] << endl;
  }

  cout << "TOTAL | " << total << endl;

  return 0;
}
