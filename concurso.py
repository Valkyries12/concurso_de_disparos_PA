class Concurso:
    
    contador_concurso = 0
    
    def __init__(self, disparo):
        Concurso.contador_concurso += 1
        self.__id_concurso = Concurso.contador_concurso
        self.__disparos = disparo
    
    
    def get_id_concurso(self):
        return self.__id_concurso
    
    
    def get_disparos(self):
        return self.__disparos
    
    
    def set_disparos(self, disparos):
        self.__disparos.append(disparos)
        
        
    def mostrar_registros(self):
        for disparo in self.__disparos:
            print(
                f"""
                *********************************
                ****** PARTICIPANTE Nº: {disparo['nroParticipante']} ******
                *********************************
                id disparo: {disparo['idDisparo']},
                Disparos: {disparo['disparos']},
                Numero participante: {disparo['nroParticipante']},
                Nombre: {disparo['nombre']},
                Apellido: {disparo['apellido']},
                Edad: {disparo['edad']},
                Sexo: {disparo['sexo']}
                *********************************
                *********************************
                """
            )
    
    
    def mostrar_podio_ganadores(self):
        pass