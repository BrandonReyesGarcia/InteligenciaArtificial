#BRANDON REYES GARCIA 20110138 6E1
#WHILE
#EN ESTA PRACTICA APRENDEMOS A UTILIZAR EL CICLO WHILE

print("BRANDON REYES GARCIA 20110138 6E1 \nPRACTICA 21:WHILE\n")

x = 1               #se da de alta una variable con un valor int

while x <= 10:      #se da de alta la funcion while
    print(x)        #se imprime la variable x
    x += 1          #incrementa en 1 la variable 

y = 0               #se da de alta una variable con un valor int

while y <= 15:      #se da de alta la funcion while
    print(y)        #se imprime la variable y
    y += 5          #incrementa en 5 la variable

z = 0               #se da de alta una variable con un valor int

while z >= -100:    #se da de alta la funcion while
    print(z)        #se imprime la variable z
    z -= 20         #decrementa en 20 la variable

frase = "lo que escribas lo repito"
frase += "\n Introduce el comando 'salir' para finalizar el programa.\n "

mensaje = ""

while mensaje != "salir":
    mensaje = input(frase)
    print (mensaje)
