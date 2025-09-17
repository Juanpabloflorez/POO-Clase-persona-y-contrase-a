#Autor: Juan Pablo Florez Rubio

from Persona import Persona
import random
import string

class password:
    def __init__(self,password):
        self.password=password

def crear_password():
    caracteres = string.ascii_letters + string.digits
    contraseña = "".join(random.choice(caracteres) for _ in range(8))
    return contraseña

code=crear_password()

def ver_password():
    print(f"Contraseña de la persona 1: {code}")

    
def main():

    persona1=Persona("Winchester", 57, "Masculino", 72, 1.6," ")

    print("Bienvenido al creador y visualizador de contraseñas")
    crear=int(input("Ingrese 1 para iniciar con el generador de contraseña para la persona: "))
    if(crear!=1):
        crear=input("Incorrecto, Ingrese 1 para generar la contraseña para la persona: ")

    persona1.code=code
    print("Contraseña creada exitosamente")


    if(any(c.isupper() for c in persona1.code) and any(c.islower() for c in persona1.code) and any(c.isdigit() for c in persona1.code)):
        print("La contraseña es muy segura")
    else:
        print("La contraseña no es tan segura (Pudieron faltar mayúsculas, minúsculas o números)")

    ver_password()

if __name__ == "__main__":
    main()