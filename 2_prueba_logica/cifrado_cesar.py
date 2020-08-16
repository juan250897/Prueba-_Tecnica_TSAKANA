abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# COLOQUE LA FUNCION CIFRAR() CON EL FIN DE PROBAR LA EFECTIVIDAD DE DECIFRAR() 

def cifrar (texto, desplazamiento):
    texto_cifrar = ""

    for letra in texto:
        suma = abc.find(letra) + desplazamiento
        modulo = int(suma) % len(abc)
        texto_cifrar = texto_cifrar + str(abc[modulo])

    return texto_cifrar

def descifrar (texto_cifrado, desplazamiento):
    texto_decifrar = ""

    for letra in texto_cifrado:
        suma = abc.find(letra) - desplazamiento
        modulo = int(suma) % len(abc)
        texto_decifrar = texto_decifrar + str(abc[modulo])

    return texto_decifrar


texto = (input ("cual es el texto a cifrar: ")).upper()
desplazamiento1 = int(input ("cual es el desplazamiento: "))
print (f"el texto cifrado es: {cifrar(texto,desplazamiento1)}")

texto_cifrado = (input ('cual es el texto a decifrar: ')).upper()
desplazamiento2 = int(input ('cual es el desplazamiento: '))
print (f"el texto descifrado es: {descifrar(texto_cifrado,desplazamiento2)}")

