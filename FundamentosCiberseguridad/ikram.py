def sumar_numeros_positivos(n):
    
    suma= 0
    for i in range(1, n + 1):
        suma +=i
    return suma

print(sumar_numeros_positivos(3))  # Resultado: 6
print(sumar_numeros_positivos(5))  # Resultado: 15