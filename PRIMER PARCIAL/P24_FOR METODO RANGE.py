#BRANDON REYES GARCIA 20110138 6E1
#FOR METODO RANGE
#EN ESTA PRACTICA APRENDEMOS A UTILIZAR EL CICLO FOR Y EL METODO RANGE

print("BRANDON REYES GARCIA 20110138 6E1 \nPRACTICA 24:FOR METODO RANGE\n")

for x in range(7,700,100):              #se crea el bucle for y con el metodo range se le agregan parametros y condiciones 
    print ("el valor de x es... ", x)   #cada iteracion imprimera el valor de la variable x

print ("\nlista de numeros\n")

numeros = [2,4,8,16,32,65,128]          #se crea una lista

for x in range(len(numeros)):           #se crea el bucle for usando el metodo len para determinar una condicion
    print ("numero de operaciones -> ",x, "multiplicacion", numeros[x]*numeros[x])  #se imprime y hace la operacion en cada iteracion

for x in range(10):                     #se crea un ciclo for usando el metodo range para poner una condicion
    print (x)                           #se imprime el valor de la variable x 
else:                                   #cuando termina el ciclo se mete a la condicion else 
    print ("se acabo el bucle for")     #imprime el mensaje al terminar el ciclo for

num1= ["1","2","3","4","5"]             #se crea una lista
num2= "0"

for x in num1:                          #se crea el cilo for
    for y in num2:                      #se anida otro ciclo for
        print(x+y)                      #si las condiciones de los 2 for se cumplen realiza la impresion de las 2 variables
    
