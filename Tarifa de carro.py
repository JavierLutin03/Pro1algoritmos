def calcular_cargos(horas):
  """
  Calcula los cargos por estacionamiento.

  Args:
    horas: El número de horas de estacionamiento.

  Returns:
    El cargo por estacionamiento.
  """

  # Cargo mínimo de $2.00 por estacionarse hasta tres horas.
  if horas <= 3:
    return 2.00

  # Cargo adicional de $0.50 por cada hora o fracción que se pase de tres horas.
  cargo_extra = (horas - 3) * 0.50

  # Cargo máximo de $10.00 para cualquier periodo dado de 24 horas.
  if cargo_extra > 7.00:
    return 10.00

  return 2.00 + cargo_extra


def main():
  """
  Programa principal.
  """

  # Declarar variables.
  horas = [0, 0, 0]
  cargos = [0, 0, 0]
  total = 0

  # Leer las horas de estacionamiento para cada cliente.
  for i in range(3):
    print("Ingrese las horas de estacionamiento para el automóvil {}:".format(i + 1))
    horas[i] = float(input())

  # Calcular los cargos por estacionamiento.
  for i in range(3):
    cargos[i] = calcular_cargos(horas[i])
    total += cargos[i]

  # Imprimir los resultados en un formato tabular ordenado.
  print("Automóvil | Horas | Cargo")
  for i in range(3):
    print("{} | {} | {}".format(i + 1, horas[i], cargos[i]))

  # Imprimir el total de los recibos de ayer.
  print("TOTAL | {}".format(total))


if __name__ == "__main__":
  main()
