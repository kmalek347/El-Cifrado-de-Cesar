que = ""
mensaje = []
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"," ",",","."]
def recorrer(opcion, que):
   
   frase = input(f"Ingrese la frase a {que}: ")
   frase = frase.lower()
   for letra in frase:   #recorre cada letra de la frase
        coincidencia = abc.index(letra)  #busca la letra en el abecedario y guarda el indice   
        if letra == abc[coincidencia]:
            
            if coincidencia + opcion > len(abc)-opcion:
              coincidencia = (coincidencia + opcion) - len(abc) #si la coincidencia es mayor a la longitud del abecedario, se le resta la longitud del abecedario
              mensaje.append(abc[coincidencia])

            else:
              coincidencia = coincidencia + opcion #cifra la letra segun la opcion elegida (+3 o -3)
              mensaje.append(abc[coincidencia]) 
            

bucle = 1
while(bucle !=0):
     
   
     mensaje=[]
     print("1. Cifrar codigo\n2. Descifrar codigo\n0. Salir")
     
     try: 
       bucle = int(input("Ingrese una opcion: "))
       print()
       if bucle == 1:
        que = "cifrar"
        recorrer(3, que)
        mensaje_string = "".join(mensaje)
        print(f"El mensaje es: {mensaje_string} \n")
     
         
              
       elif bucle == 2:
        que = "descifrar"
        recorrer(-3, que)
        mensaje_string = "".join(mensaje)
        print(f"El mensaje es: {mensaje_string} \n")
   
       
     except Exception as err:
            
        print(f"Pero que pedazo de boludo, cometiste el error: {err}\n")
                  
           
    