#BRANDON REYES GARCIA 20110138 6E1
#LISTAS METODO SORT
#EN ESTA PRACTICA APRENDEMOS A ORDENAR LSO DATOS DE LA LISTA
#DE MANERA ALFABETICA O ALFABETICA INVERSA

print("BRANDON REYES GARCIA 20110138 6E1 \nPRACTICA 13:LISTAS METODO SORT\n")

colores = ["rojo","azul","verde","amarillo","marron","lila","negro","rosa"] #se crea una lista

print ("la lista colores se ordena temporalmete alfabeticamente\n", sorted(colores))    #se imprime la lista temporalmente ordenada de forma alfabetica
colores.sort()                  #se ordena la lista alfabeticamente de manera permanente
print ("la lista colores se ordena alfabeticamente\n",colores)                  #se imprime la nueva lista ya ordenada de manera alfabetica
colores.sort(reverse=True)      #se ordena la lista alfabeticamente inversa de manera permanente
print ("los lista colores se ordena alfabeticamente inversa\n",colores)         #se imprime la nueva lista ya ordenada de manera alfabetica inversa

