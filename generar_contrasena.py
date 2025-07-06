# Generador de contraseña segura basado en palabras clave
import random
import string

def generar_contrasena(palabras_clave, longitud=12):
    """
    Genera una contraseña segura combinando palabras clave con caracteres aleatorios.
    :param palabras_clave: lista de palabras clave (strings)
    :param longitud: longitud mínima de la contraseña
    :return: contraseña generada
    """
    # Une todas las palabras clave en una base
    base = ''.join(palabras_clave)
    
    # Conjunto de caracteres extra: letras, números y símbolos
    caracteres_extra = string.ascii_letters + string.digits + string.punctuation
    
    # Añade caracteres aleatorios hasta llegar a la longitud deseada
    while len(base) < longitud:
        base += random.choice(caracteres_extra)
    
    # Desordena los caracteres para mayor seguridad
    contrasena_lista = list(base)
    random.shuffle(contrasena_lista)
    
    # Devuelve solo los primeros 'longitud' caracteres
    contrasena = ''.join(contrasena_lista[:longitud])
    return contrasena

def main():
    print("=== Generador de Contraseña Segura ===")
    entrada = input("Ingresa una o varias palabras clave separadas por espacio: ")
    palabras = entrada.strip().split()
    
    try:
        longitud = int(input("Longitud deseada de la contraseña (mínimo 12): "))
    except ValueError:
        print("Valor inválido, se usará longitud 12 por defecto.")
        longitud = 12
    
    if longitud < 12:
        print("Longitud mínima es 12. Se ajustará automáticamente.")
        longitud = 12
    
    contrasena = generar_contrasena(palabras, longitud)
    print(f"\nTu contraseña segura es: {contrasena}")

if __name__ == "__main__":
    main()
