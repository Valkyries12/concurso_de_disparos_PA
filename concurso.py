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
        disparos = self.__disparos.copy()
        for disparo in disparos:
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
    
    
    def mostrar_podio(self):
        """
        Muestra los primeros tres puestos de ganadores segun su disparo
        """
        participantes = self.__puntuacion_total()
        podio = self.__armar_podio(participantes)
        podio.reverse()
        for i in range(len(podio)):
            print(
                f"""
                ***********************************
                ********** PUESTO Nº: {i+1} **********
                ***********************************
                id disparo: {podio[i]['idDisparo']},
                Disparos: {podio[i]['disparos']},
                Numero participante: {podio[i]['nroParticipante']},
                Nombre: {podio[i]['nombre']},
                Apellido: {podio[i]['apellido']},
                Edad: {podio[i]['edad']},
                Sexo: {podio[i]['sexo']},
                Puntaje: {podio[i]['puntaje_total']}
                ***********************************
                ***********************************
                """
            )
    
    
    def mostrar_ultimo(self):
        """
        Muestra el tercer puesto
        """
        participantes = self.__puntuacion_total()
        podio = self.__armar_podio(participantes)
        print(
                f"""
                ***********************************
                ********** ULTIMO PUESTO **********
                ***********************************
                id disparo: {podio[0]['idDisparo']},
                Disparos: {podio[0]['disparos']},
                Numero participante: {podio[0]['nroParticipante']},
                Nombre: {podio[0]['nombre']},
                Apellido: {podio[0]['apellido']},
                Edad: {podio[0]['edad']},
                Sexo: {podio[0]['sexo']},
                Puntaje: {podio[0]['puntaje_total']}
                ***********************************
                ***********************************
                """
            )
    
    
    def cantidad_participantes(self):
        """
        Muestra la cantidad de participantes en el concurso
        """
        print(
            f"""
            ************************************************
            ******** SE ENCONTRARON {len(self.__disparos)} PARTICIPANTES ********
            ************************************************
            """
        )
    
    
    def mostrar_ordenado_por_edad(self):
        """
        Muestra los datos de los participantes ordenados de menor a mayor por edad
        """
        participantes = self.__disparos.copy()
        sorted_participantes = self.__ordenar_por_edad(participantes)
        for participante in sorted_participantes:
            print(
                f"""
                *********************************
                ****** PARTICIPANTE Nº: {participante['nroParticipante']} ******
                *********************************
                id disparo: {participante['idDisparo']},
                Disparos: {participante['disparos']},
                Numero participante: {participante['nroParticipante']},
                Nombre: {participante['nombre']},
                Apellido: {participante['apellido']},
                Edad: {participante['edad']},
                Sexo: {participante['sexo']},
                Puntaje: {participante['puntaje_total']}
                *********************************
                *********************************
                """
            )
    
    
    def mostrar_promedio_disparo(self):
        """
        Muestra el promedio de los disparos de cada participante
        """
        participantes = self.__disparos.copy()
        promedios = self.__calcular_promedio_disparo(participantes)
        for promedio in promedios:
            print(
                f"""
                *********************************
                ****** PARTICIPANTE Nº: {promedio['nroParticipante']} ******
                *********************************
                Disparos: {promedio['disparos']},
                Nombre: {promedio['nombre']},
                Apellido: {promedio['apellido']},
                Promedio: {promedio['promedio']}
                *********************************
                *********************************
                """
            )
        
        
    def __calcular_promedio_disparo(self, participantes):
        """
        Devuelve un diccionario con los datos del participante con un campo de promedio
        """
        promedios = []
        for participante in participantes:
            total = 0
            for puntaje in participante['disparos']:
                total += puntaje
            participante['promedio'] = round(total / len(participante['disparos']))
            promedios.append(participante)
        return promedios
    
    
    def __ordenar_por_edad(self, participantes):
        """
        Devuelve una lista de diccionarios con los datos de los participantes ordenados descendente por edad
        """
        sorted_participantes = []
        while len(participantes) > 0:
            menor_edad = self.__calcular_menor_edad(participantes)
            sorted_participantes.append(menor_edad)
            for participante in participantes:
                if menor_edad['nroParticipante'] == participante['nroParticipante']:
                    participantes.remove(participante)
        return sorted_participantes
    
    
    def __calcular_menor_edad(self, participantes):
        """
        Devuelve un diccionario con los datos del participante de menor edad
        """
        menor_edad = 999
        temp = None
        for participante in participantes:
            if participante['edad'] < menor_edad:
                menor_edad = participante['edad']
                temp = participante
        return temp
    
    
    def __armar_podio(self, participantes):
        """
        Devuelve una lista con los datos de los tres mejores participantes
        """
        podio = []
        
        while len(podio) < 3:
            participante_mejor_puntaje = self.__calcular_disparo_ganador(participantes)
            podio.append(participante_mejor_puntaje)
            for disparo in participantes:
                if disparo['puntaje_total'] == participante_mejor_puntaje['puntaje_total']:
                    participantes.remove(disparo)
        return podio
    
    
    def __calcular_disparo_ganador(self, disparos):
        """
        Devuelve diccionario con los datos del participante con el puntaje mejor calificado [puntaje mas bajo es el ganador]
        """
        ganador = None
        participante = ""
        puntaje_mas_chico = 0
        for disparo in disparos:
            if puntaje_mas_chico <= disparo['puntaje_total']:
                puntaje_mas_chico = disparo['puntaje_total']
                participante = disparo
        ganador = dict(participante)
        return ganador

    
    def __puntuacion_total(self):
        """
        Devuelve una lista con los datos del participante y una nueva key con el puntaje_total 
        a partir de los 3 disparos hechos
        """
        disparos = []
        for disparo in self.__disparos:
            total = 0
            for puntaje in disparo['disparos']:
                total += puntaje
            disparo['puntaje_total'] = total
            disparos.append(disparo)
        return disparos