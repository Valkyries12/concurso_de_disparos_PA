from concurso import Concurso
from disparo import Disparo
from participante import Participante


maria = Disparo("Maria", "Lopez", 21, "F")
maria.hacer_disparos()
carlos = Disparo("Carlos", "Menem", 55, "M")
carlos.hacer_disparos()
pepe = Disparo("Pepe", "Argento", 45, "M")
pepe.hacer_disparos()
mariana = Disparo("Mariana", "Perez", 26, "F")
mariana.hacer_disparos()
eleonora = Disparo("Eleonora", "Ortiz", 49, "F")
eleonora.hacer_disparos()
marcelo = Disparo("Marcelo", "Tinelli", 55, "M")
marcelo.hacer_disparos()
concurso_disparo = Concurso([maria.armar_datos(), carlos.armar_datos(), eleonora.armar_datos(), marcelo.armar_datos(), mariana.armar_datos(), pepe.armar_datos()])
concurso_disparo.mostrar_registros()