from concurso import Concurso
from disparo import Disparo
from participante import Participante


#maria = Disparo("Maria", "Lopez", 21, "F")
#maria.hacer_disparos()
#carlos = Disparo("Carlos", "Menem", 55, "M")
#carlos.hacer_disparos()
#pepe = Disparo("Pepe", "Argento", 45, "M")
#pepe.hacer_disparos()
#mariana = Disparo("Mariana", "Perez", 26, "F")
#mariana.hacer_disparos()
#eleonora = Disparo("Eleonora", "Ortiz", 49, "F")
#eleonora.hacer_disparos()
#marcelo = Disparo("Marcelo", "Tinelli", 55, "M")
#marcelo.hacer_disparos()
#concurso_disparo = Concurso([maria.armar_datos(), carlos.armar_datos(), eleonora.armar_datos(), marcelo.armar_datos(), mariana.armar_datos(), pepe.armar_datos()])
#concurso_disparo.mostrar_registros()
#concurso_disparo.mostrar_podio()
#concurso_disparo.mostrar_ultimo()
#concurso_disparo.cantidad_participantes()
#concurso_disparo.mostrar_ordenado_por_edad()
#concurso_disparo.mostrar_promedio_disparo()
#concurso_disparo.mostrar_mejores_disparos()
#concurso_disparo.guardar_CSV()
#concurso_disparo.borrar_CSV()

def dibujar_menu():
    print(
            f"""
            **************************************
            **************************************
            **              MENU                **
            **                                  **
            ** 0  Agregar participante          **                    
            ** 1  Mostrar registros             **
            ** 2  Mostrar podio                 **
            ** 3  Mostrar ultimo                **
            ** 4  Cantidad participantes        **
            ** 5  Ordenar por edad              **
            ** 6  Promedio disparos             **
            ** 7  Mejores disparos              **
            ** 8  Guardar CSV                   **
            ** 9  Borrar CSV                    **
            ** 10 Salir                         **
            **************************************
            **************************************
            """
        )
    opcion = input("Ingrese una opcion: ")
    return opcion
    

def iniciar():
    """
    Dibuja y contiene la lógica del menú
    """
    concurso_disparos = Concurso()
    opcion = dibujar_menu()
    while opcion != "10":
        
        if opcion == "0":
            nombre = input("Ingrese nombre del participante: ")
            apellido = input("Ingrese apellido del participante: ")
            edad = input("Ingrese la edad del participante: ")
            sexo = input("Ingrese sexo del participante [F/M]: ").upper()
            participante = Disparo(nombre, apellido, edad, sexo)
            participante.hacer_disparos() 
            concurso_disparos.set_disparos(participante.armar_datos())
        elif opcion == "1":
            concurso_disparos.mostrar_registros()
            
        opcion = dibujar_menu()
        
                

iniciar()