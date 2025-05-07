#1º la función "esPalindromo" con el parámetro "fraseinicial" que es la que se introduce para analizar.
def esPalindromo(fraseinicial):
   
    # La "frase final" va a ser el restultado de: eliminar los espacios con las comillas .Lo que hay dentro 
    #del parentesis, recorre todos los caracteres en la frase inicial y solo deja las letras y números. 
    #Por último ".lower()" deja solo las minúsculas.
    
    frase_final = ''.join(c for c in fraseinicial if c.isalnum()).lower()
    
    # Ahora se comparan lo recibido inicialmente con el resultado final 
    #pero dado la vuelta para ver si es palindroma
    return frase_final == frase_final[::-1]
    
    
#2º en la función main se solicita la fraseinicial.
def main():
    print("Bienvenido al verificador de palíndromos.")
    fraseintroductoria = input("Introduce una frase: ")
    
    #Establecemos el mensaje de verificación o negación del palíndromo con un condicional
    
    if esPalindromo(fraseintroductoria):
        print("La frase introducida es palíndroma.")
    else:
        print("La frase introducida no es palíndroma.")
        
#3º Ejecuta el programa directamente

if __name__ == "__main__":
    main()