import math 
diametro = float(input("digite o diametro da esfera: "))
PI = float(3.14)
raio =(diametro)/2
volume = 4.0/3.0 *PI* math.pow (raio, 3.0)
print(f"o volume da esfera é: {volume: .2f}")