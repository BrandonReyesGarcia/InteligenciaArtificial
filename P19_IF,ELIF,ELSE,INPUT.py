#BRANDON REYES GARCIA 20110138 6E1
#IF,ELIF,ELSE,INPUT
#EN ESTA PRACTICA APRENDEMOS A USAR EL CONDICIONAL IF, ELIF, ELE
#ADEMAS DE INGRESAR DATOS MEDIANTE LA CONSOLA

print("BRANDON REYES GARCIA 20110138 6E1 \nPRACTICA 19:IF,ELIF,ELSE,INPUT\n")

edad = int(input("¿Cual es tu edad? ... "))         #se ingresa en consola un dato de tipo int y se guarda en la variable

if edad <=0:                                        #se da de alta la funcion if
    print("nadie puede tener esas edad")            #si se cumple la condicion se imprime la cadena

elif edad >=1 and edad <=17:                        #se da de alta la funcion elif
    print("Eres menor de edad")                     #si se cumple la condicion se imprime la cadena

elif edad >=18 and edad <=45:                       #se da de alta la funcion elif
    print("Su edad esta entro los 18 a 45 años")    #si se cumple la condicion se imprime la cadena

elif edad <=100:                                    #se da de alta la funcion elif
    print("Eres mayor de edad")                     #si se cumple la condicion se imprime la cadena
    
elif edad >=100 and edad <=120:                     #se da de alta la funcion elif
    print("Su edad esta entro los 100 a 120 años")  #si se cumple la condicion se imprime la cadena
    
else:                                               #se da de alta la funcion else
    print("Edad no valida")                         #si se cumple la condicion se imprime la cadena

