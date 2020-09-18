
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math





xAxis = []
yAxis= []


#Angulo
Ang = 30
#Radianes
rad = (Ang*math.pi)/180
#Vel prueba
Vp = 250
#Vel x
Vx = Vp*math.cos(rad)
#Vel y
Vy = Vp*math.sin(rad)
#CampoE
Campo = 10e-5
#Masa Particula
masaP = 1.67e-27
#Carga Particula
qP = 1.60e-19
#Elevacion maxima
hMax = 1e+01
t = 0e+0
currentH = 0e+0
currentX = 0e+0

while ((currentH<hMax) & ((-hMax)<currentH)):
    a = (qP*Campo)/masaP
    currentH = Vy*t+(0.5)*a*(t**2)
    currentX = Vx*t
    t += 1e-3
    xAxis.append(currentX)
    yAxis.append(currentH)
d = {'x':xAxis,'y':yAxis}
df = pd.DataFrame(data=d)
plt.plot(df['x'], df['y'])
plt.show()
    
print ("Bienvenido al programa que mostrará la trayectoria de una partícula")
opcion = 0
while opcion != "4":
    print ("------ MENÚ DE OPCIONES ------")
    print ("1. Velocidad inicial de la particula")
    print ("2. Intensidad de campo eléctrico")
    print ("3. Tipo de partícula")
    print ("4. Salir")
    opcion = input("Elija los parámetros que desea ingresar: ")
    
    if opcion == '1':
        magni = input("Ingrese la magnitud de la velocidad: ")
        direc = input("Ingrese la dirección de la velocidad: ")
        
    elif opcion == '2':
        magnit = input("Ingrese la magnitud del campo eléctrico: ")
        senti = input("Ingrese el sentido del campo eléctrico: ")
        
    elif opcion == '3':
        print("1. Electrón \n2. Positrón \n3. Protón \n4. Neutrón \n5. Partícula alfa")
        print("6. Núclo de deuterio \n7. Muón\n8. Gravitón \n9. Fotón\n10. Átomo de calcio")
        opcion2 = input("Elija el tipo de partícula")
        
    elif opcion == '4':
        print("Feliz día")
        
    elif opcion >= '5':
        print('Opción inválida')

