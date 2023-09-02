# Pro1algoritmos
// condigo en pseint  // 
Algoritmo TriplesPitagoras
    Definir lado1, lado2, hipotenusa, limite como Entero
// lado1,lado2 y hipotenusa representan los lados del triangulo con lo que que podemos inicializar las variables necesarias para el codigo y el limite = se utiliza para representar
el limite del valor del triangulo, en este caso se usar 500 dado el requerimiento del enunciado
    limite <- 500

    Escribir "Triples de Pitágoras menores o iguales a 500:"
    Para hipotenusa <- 1 Hasta limite Hacer
    // Inicia un bucle que varía la longitud de la hipotenusa desde 1 hasta el valor límite 500 en este caso.//
        Para lado1 <- 1 Hasta hipotenusa Hacer
        // Inicia otro bucle para el primer lado del triángulo, que varía desde 1 hasta el valor actual de la hipotenusa. Esto asegura que lado1 no sea mayor que la hipotenusa //
            Para lado2 <- lado1 Hasta hipotenusa Hacer
             //Inicia un tercer bucle para el segundo lado del triángulo, que varía desde el valor actual de lado1 hasta la hipotenusa. Esto evita repetir combinaciones ya probadas //
                Si lado1^2 + lado2^2 = hipotenusa^2 Entonces // Verifica si los valores actuales de lado1, lado2 e hipotenusa satisfacen la condición del teorema de Pitágoras//
                    Escribir lado1, ", ", lado2, ", ", hipotenusa //  Si se cumple la condición, imprime el triple de Pitágoras encontrado//
                Fin Si
            Fin Para
        Fin Para    // en los FIN PARA se utiliza para cerrar el bucle // 
    Fin Para

FinAlgoritmo // fin del algotimo //








