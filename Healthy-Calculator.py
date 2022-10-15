print("HOLA!!, te presento a la calculadora FITNESS, donde se calculara el peso ideal, , el procentaje de masa \n corporal y el indice metabolico basal.")
print("por favor dinos los siguientes datos :)")
peso= float(input ("digite su peso: "))
estatura= float(input ("digite su estatura(centimetros): "))
Edad= float(input ("digite su edad: "))
#conversion de centimetros a metros
estaturam=estatura/100
generoDigitado=  input("Digite su genero(masculino o femenino): ")
IMC= peso/estaturam**2


#dependiendo de lo que digite en geneor me de los diferentes resultados
def Genero(generoDigitado):
 if generoDigitado == "masculino":
 #el peso ideal  mas
   ideal= 56.2 + 1.41 * (estatura / 2.54 - 60)
   print("su peso ideal es:", ideal)

 #porcentaje corporal  mas
   porcentaje= (1.20) * (IMC) + (0.23) * (Edad) - (16.2)
   print("su porcentaje de grasa corporal es de: ", porcentaje)

#indice metabolico  mas 
   indice= (13.397) * (peso) + (4.799) * (Edad) - (5.677) *(estatura) + (88.362)
   print("su indice metabolico basal es de: ", indice)
   
   

   
if generoDigitado == "femenino":
 #el peso ideal  fem
  ideal= 53.1 + 1.36 * (estatura / 2.54 - 60)
  print("su peso ideal es: ", ideal)

  
  #porcentaje corporal fem 
  
  porcentaje= (1.20) * (IMC) + (0.23) * (Edad) - (5.4)
  print("su porcentaje de masa corporal es de: ", porcentaje)
  
 #indice metabolico fem  
  indice= (9.247) * (peso) + (3.098) * (Edad) - (4.330) * (estatura) + (447.593)
  print("su indice metabolico basal es de: ", indice)
  
Genero(generoDigitado)

met=input("Escriba que actividad suele realizar(correr,caminar,tenis,bicicleta o nadar): ")

tiempo=float(input("digite el tiempo de ejercicio qe suele realizar(minutos): "))
# dependiendo de que actividad registre, me de las calorias quemadas con cada uno
def calorias(met):
  if met== "correr":
    calquemadas= (tiempo) * (6) * (peso) / (200)
    print("sus calorias quemadas son: ", calquemadas)
    
  if met== "caminar":
    calquemadas= (tiempo) * (2) * (peso) / (200)
    print("sus calorias quemadas son: ", calquemadas)
    
  
  if met== "tenis":
    calquemadas= (tiempo) * (5) * (peso) / (200)
    print("sus calorias quemadas son: ", calquemadas)
    
  
  if met== "bicicleta":
    calquemadas= (tiempo) * (14) * (peso) / (200)
    print("sus calorias quemadas son: ", calquemadas)
    
    
  if met== "nadar":
    calquemadas= (tiempo) * (9.8) * (peso) / (200)
    print("sus calorias quemadas son: ", calquemadas)

calorias(met)

print("ha finalizado su proceso en la calculadora FITNESS ")