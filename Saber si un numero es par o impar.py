def es_par(n):          # funcion para saber si el numero es par 
    if n % 2 == 0:
        return True
    else:
        return False

def es_primo(n):           # funcion para saber si el numero es primo
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def contar_numeros_primos(a, b):        # funcion para contar los numeros primos
    c = 0 
    for x in range(a, b + 1):
        if es_primo(x):
            c += 1
    return c

for i in range(1, 101): 
    print(i, es_par(i), es_primo(i))

print("Numeros primos entre 0 y 100 = ", contar_numeros_primos(0, 100))
