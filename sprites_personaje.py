import pygame
from personaje import *
from config import *
from funciones import *


personaje_camina_derecha = [pygame.image.load("./src/recursos/camina/0.png"),
                    pygame.image.load("./src/recursos/camina/1.png"),
                    pygame.image.load("./src/recursos/camina/2.png"),
                    pygame.image.load("./src/recursos/camina/3.png"),
                    pygame.image.load("./src/recursos/camina/4.png"),
                    pygame.image.load("./src/recursos/camina/5.png"),
                    pygame.image.load("./src/recursos/camina/6.png"),
                    ]

personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True,False)

personaje_quieto_derecha = [pygame.image.load("./src/recursos/quieto/0.png"),
                    pygame.image.load("./src/recursos/quieto/1.png"),
                    pygame.image.load("./src/recursos/quieto/2.png")
                    ]

personaje_quieto_izquierda = [pygame.image.load("./src/recursos/quieto/0left.png"),
                    pygame.image.load("./src/recursos/quieto/1left.png"),
                    pygame.image.load("./src/recursos/quieto/2left.png")
                    ]


personaje_salta = [pygame.image.load("./src/recursos/salta/0.png")]

personaje_salta_adelante =[pygame.image.load("./src/recursos/salto_adelante/0.png"),
                        pygame.image.load("./src/recursos/salto_adelante/9.png"),
                        pygame.image.load("./src/recursos/salto_adelante/10.png"),
                        pygame.image.load("./src/recursos/salto_adelante/11.png"),
                        pygame.image.load("./src/recursos/salto_adelante/12.png")
]

personaje_ataque = [pygame.image.load("./src/recursos/ataque/0.png"),
]
personaje_telaraña =[pygame.image.load("./src/recursos/ataque/1.png")]

# personaje_columpio = [pygame.image.load("./src/recursos/telaraña/0.png"),
#                     pygame.image.load("./src/recursos/telaraña/1.png"),
#                     pygame.image.load("./src/recursos/telaraña/2.png"),
#                     pygame.image.load("./src/recursos/telaraña/3.png"),
#                     pygame.image.load("./src/recursos/telaraña/4.png"),
#                     pygame.image.load("./src/recursos/telaraña/5.png"), 
#                     pygame.image.load("./src/recursos/telaraña/7.png"),
#                     pygame.image.load("./src/recursos/telaraña/8.png"),
#                     pygame.image.load("./src/recursos/telaraña/9.png"),
#                     pygame.image.load("./src/recursos/telaraña/10.png"),
#                     pygame.image.load("./src/recursos/telaraña/11.png"),
#                     pygame.image.load("./src/recursos/telaraña/12.png")
#                     ]

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


dic_animaciones = {}
dic_animaciones["quieto_derecha"] = personaje_quieto_derecha
dic_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
dic_animaciones["salta"] = personaje_salta
dic_animaciones["camina_derecha"] = personaje_camina_derecha
dic_animaciones["camina_izquierda"] = personaje_camina_izquierda
dic_animaciones["personaje_defensa"] = personaje_defensa
dic_animaciones["personaje_ataca"] = personaje_ataque
