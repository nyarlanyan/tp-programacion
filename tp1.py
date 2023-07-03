

# Realice un programa que contenga una función que se llame “conversion”, que la misma contenga tres parámetros
# Se pide convertir los segundos ingresados en horas, minutos y segundos

def conversion(segundos):
   horas = segundos // 3600 
   segundos %= 3600
   minutos = segundos// 60
   segundos %= 60
   return horas, minutos, segundos

segundos_totales = int(input ("ingrese la cantidad de segundos")) 

horas, minutos, segundos = conversion( segundos_totales) 

print(f"{segundos_totales} segundos equivale a:{horas} horas, {minutos} minutos, {segundos} segundos," )
 



 
