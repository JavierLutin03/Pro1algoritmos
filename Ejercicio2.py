def main():
 

 
  filas = int(input("Ingrese el número de filas: "))
  columnas = int(input("Ingrese el número de columnas: "))
  numero = 0
  mayor = float("-inf")
  suma = 0


  matriz = [[0 for i in range(columnas)] for j in range(filas)]


  for i in range(filas):
    for j in range(columnas):
      numero = float(input("Ingrese el valor en la posición ({},{}): ".format(i, j)))
      matriz[i][j] = numero


      if numero > mayor:
        mayor = numero

    
      suma += numero

  
  print("El número mayor es:", mayor)


  for i in range(filas):
    for j in range(columnas):
      print(matriz[i][j], end=" ")
    print()


  promedio = suma / (filas * columnas)
  print("El promedio de la matriz es:", promedio)


if __name__ == "__main__":
  main()
