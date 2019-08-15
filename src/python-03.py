'''
Tipos básicos de datos
----------------------
Los principales tipos de datos básicos son:
números enteros -> int
números decimales -> float
valores lógicos -> bool
cadenas de texto -> str

Para saber el tipo de un valor (o variable), usamos la función type()

print(type(variable))
'''

print(type(6))          # <class 'int'>
print(type(6.5))        # <class 'float'>
print(type(3 * 5))      # <class 'int'>
saludo = 'Hola'
print(type(saludo))     # <class 'str'>
print(type(True))       # <class 'bool'>