import pygame
from personaje import *


personaje_camina = [pygame.image.load("./src/recursos/camina/0.png"),
                    pygame.image.load("./src/recursos/camina/1.png"),
                    pygame.image.load("./src/recursos/camina/2.png"),
                    pygame.image.load("./src/recursos/camina/3.png"),
                    pygame.image.load("./src/recursos/camina/4.png"),
                    pygame.image.load("./src/recursos/camina/5.png"),
                    pygame.image.load("./src/recursos/camina/6.png"),
                    ]


personaje_camina_izquierda = girar_imagenes(personaje_camina, True,False)

personaje_quieto = [pygame.image.load("./src/recursos/quieto/0.png"),
                    pygame.image.load("./src/recursos/quieto/1.png"),
                    pygame.image.load("./src/recursos/quieto/2.png")
                    ]



personaje_salta = [pygame.transform.scale(pygame.image.load("./src/recursos/salta/0.png"),(70,106))]




personaje_salta_adelante =[pygame.image.load("./src/recursos/salto_adelante/0.png"),
                        pygame.image.load("./src/recursos/salto_adelante/9.png"),
                        pygame.image.load("./src/recursos/salto_adelante/10.png"),
                        pygame.image.load("./src/recursos/salto_adelante/11.png"),
                        pygame.image.load("./src/recursos/salto_adelante/12.png")
]



personaje_ataque = [pygame.image.load("./src/recursos/ataque/0.png"),
]
personaje_telaraña = pygame.transform.scale(pygame.image.load("./src/recursos/ataque/1.png"),(30,70))





personaje_columpio = [pygame.image.load("./src/recursos/telaraña/0.png"),
                    pygame.image.load("./src/recursos/telaraña/1.png"),
                    pygame.image.load("./src/recursos/telaraña/2.png"),
                    pygame.image.load("./src/recursos/telaraña/3.png"),
                    pygame.image.load("./src/recursos/telaraña/4.png"),
                    pygame.image.load("./src/recursos/telaraña/5.png"), 
                    pygame.image.load("./src/recursos/telaraña/7.png"),
                    pygame.image.load("./src/recursos/telaraña/8.png"),
                    pygame.image.load("./src/recursos/telaraña/9.png"),
                    pygame.image.load("./src/recursos/telaraña/10.png"),
                    pygame.image.load("./src/recursos/telaraña/11.png"),
                    pygame.image.load("./src/recursos/telaraña/12.png")
                    ]


personaje_defensa =[pygame.image.load("./src/recursos/defensa/0.png"),  
                    pygame.image.load("./src/recursos/defensa/1.png"),
                    pygame.image.load("./src/recursos/defensa/2.png"),
                    pygame.image.load("./src/recursos/defensa/3.png"),
                    pygame.image.load("./src/recursos/defensa/4.png"),
                    pygame.image.load("./src/recursos/defensa/5.png"),
                    pygame.image.load("./src/recursos/defensa/5.png"),
                    pygame.image.load("./src/recursos/defensa/5.png"),
                    pygame.image.load("./src/recursos/defensa/5.png"),
]

lista_animaciones = [personaje_salta,
                    personaje_quieto,
                    personaje_camina,
                    personaje_camina_izquierda,
                    personaje_salta_adelante,
                    personaje_ataque,
                    personaje_columpio,
                    personaje_defensa
                    ]

lista_animaciones = reescalar_imagenes(lista_animaciones,(90,140))
