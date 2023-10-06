def main():
 
  n = int(input("Ingrese la cantidad de números: "))
  numeros = []
  mediana, promedio = 0, 0


  for i in range(n):
    numero = float(input("Ingrese el número {}: ".format(i + 1)))
    numeros.append(numero)

  
  numeros.sort()

 
  if n % 2 == 0:
    mediana = (numeros[n // 2] + numeros[n // 2 - 1]) / 2
  else:
    mediana = numeros[n // 2]

 
  for i in numeros:
    promedio += i
  promedio /= n

  
  print("Mediana:", mediana)
  print("Promedio:", promedio)


if __name__ == "__main__":
  main()
