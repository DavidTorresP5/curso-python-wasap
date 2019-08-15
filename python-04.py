'''
int & float
-----------
Con los datos numéricos podemos realizar diferentes operaciones:

suma: a + b
resta: a - b
producto: a * b
división: a / b   (a // b)
resto/módulo: a % b
potencia: a ** b

El tipo del resultado será siempre el tipo de los números que utilicemos. 
Si son de tipos diferentes (un int y un float) el resultado será siempre del tipo float.
'''
print(2 + 2.0)                      # 4.0
print(15 % 4)                       # 3

base = 2.0
exponente = 4
resultado = base ** exponente
print(resultado)                    # 16.0
print(type(resultado))              # <class 'float'>

'''
En el caso de la división podemos obtener dos tipos de valores numéricos como resultado:

int, para lo que utilizamos //
float, usando /
'''
print(15 // 2)                      # 7
print(15 / 2)                       # 7.5