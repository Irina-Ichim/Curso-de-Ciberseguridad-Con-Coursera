import bcrypt
import os

def generar_salt():
    # Generar un "salt" aleatorio usando os.urandom
    return bcrypt.gensalt()

def hashear_contraseña(contraseña, salt):
    # Hashear la contraseña junto con el "salt"
    contraseña_hasheada = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
    return contraseña_hasheada

# Ejemplo de uso:
if __name__ == "__main__":
    # Contraseña del usuario
    contraseña_usuario = "mi_contraseña_secreta"

    # Generar un "salt" aleatorio
    salt = generar_salt()

    # Hashear la contraseña con el "salt"
    contraseña_hasheada = hashear_contraseña(contraseña_usuario, salt)

    # Mostrar resultados
    print("Contraseña Original:", contraseña_usuario)
    print("Salt utilizado:", salt)
    print("Contraseña Hasheada:", contraseña_hasheada)
