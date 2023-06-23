from populacao import Populacao
from genetico import Genetico

gen = Genetico(
    "13 years later and this song is still a bop. From blasting it in the car, singing along at 4yrs old", 
    tamanho=15, 
    taxaSatisfatoria=100,
    numMaxGeracoes=4000
)

gen.run()





