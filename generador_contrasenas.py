import random
import string
import pyperclip

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    while True:
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (not incluir_mayusculas or any(c.isupper() for c in contrasena)) and \
           (not incluir_numeros or any(c.isdigit() for c in contrasena)) and \
           (not incluir_simbolos or any(c in string.punctuation for c in contrasena)):
            return contrasena

def main():
    print("Generador de Contraseñas Seguras")
    
    while True:
        try:
            longitud = int(input("Longitud de la contraseña (8-32): "))
            if 8 <= longitud <= 32:
                break
            else:
                print("Por favor, ingrese un número entre 8 y 32.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

    contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    
    print(f"\nContraseña generada: {contrasena}")
    
    if input("¿Desea copiar la contraseña al portapapeles? (s/n): ").lower() == 's':
        pyperclip.copy(contrasena)
        print("Contraseña copiada al portapapeles.")

if __name__ == "__main__":
    main()

# Ejecutar el programa
main()
