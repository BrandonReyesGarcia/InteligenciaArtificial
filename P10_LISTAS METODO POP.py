#BRANDON REYES GARCIA 20110138 6E1
#LISTAS METODO POP
#EN ESTA PRACTICA APRENDEMOS A ACCEDER A UN DATO DE LA LISTA Y
#COMO ELIMINARLO UTILIZANDO EL METODO POP

print("BRANDON REYES GARCIA 20110138 6E1 \nPRACTICA 10:LISTAS METODO POP\n")

colores = ["rojo","azul","verde","amarillo","marron","lila","negro","rosa"] #se crea una lista

eliminados1 = colores.pop(0)        #se elimina un dato cero de la lista y se almacena en una variable mediante el metodo pop 
eliminados2 = colores.pop(0)        #se elimina el dato cero de la nueva lista y se almacena en una variable mediante el metodo pop
print(colores)                      #se imprime la nueva lista ya con los datos eliminados
coloreseliminados = [eliminados1 , eliminados2]             #se crea una lista con los datos eliminados de la lista colores
print("los colores eliminados son..." , coloreseliminados)  #se imprime la lista con los colores eliminados 
