from funciones import *
from class_plataforma import *
from class_moneda import *


#PLATAFORMA TUBOS
tubo_1 = Generar_rects(1350,670,85,130)
tubo_2 = Generar_rects(1830,610,85,190)
tubo_3 = Generar_rects(2210,550,85,250)
tubo_4 = Generar_rects(2740,550,85,250)
tubo_5 = Generar_rects(7830,670,85,130)
tubo_6 = Generar_rects(8600,670,85,130)

#TOPE TORTUGA
tope1 = Generar_rects(3750,220,30,100)
tope2 = Generar_rects(4045,220,30,100)

#BANDERA
piso_bandera =  Generar_rects(9500,720,50,60)

#ESCALERAS
escalera_1 =  Generar_rects(6425,725,50,200)
escalera_2 =  Generar_rects(6475,670,50,200)
escalera_3 =  Generar_rects(6522,610,50,260)
escalera_4 =  Generar_rects(6570,540,50,400)

escalera_5 =  Generar_rects(6865,725,50,200)
escalera_6 =  Generar_rects(6820,670,50,200)
escalera_7 =  Generar_rects(6755,610,50,260)
escalera_8 =  Generar_rects(6710,540,50,400)

escalera_9 =  Generar_rects(7100,725,50,200)
escalera_10 =  Generar_rects(7150,670,50,200)
escalera_11=  Generar_rects(7200,610,50,260)
escalera_12 =  Generar_rects(7250,540,50,400)
escalera_13 =  Generar_rects(7300,540,50,400)

escalera_14 =  Generar_rects(7445,540,50,400)
escalera_15 =  Generar_rects(7495,610,50,260)
escalera_16 =  Generar_rects(7545,670,50,200)
escalera_17 =  Generar_rects(7595,725,50,200)

escalera_18 =  Generar_rects(8690,725,50,200)
escalera_19 =  Generar_rects(8730,670,50,200)
escalera_20 =  Generar_rects(8780,610,50,400)
escalera_21 =  Generar_rects(8830,540,50,400)
escalera_22 =  Generar_rects(8880,470,50,600)
escalera_23 =  Generar_rects(8930,410,50,700)
escalera_24 =  Generar_rects(8980,360,50,700)
escalera_25 =  Generar_rects(9030,280,50,800)
escalera_26 =  Generar_rects(9080,280,50,800)


coin_score = Coin((25,25),moneda,(910,10))
#PLATAFORMAS ?
plataforma_caja1 = Plataforma((50,50), caja_moneda, (700, 620),False)
plataforma_caja2 = Plataforma((50,50), caja_moneda, (800, 620),False)

plataforma_caja3 = Plataforma((50,50), caja_moneda, (850, 390),False)

plataforma_caja4 = Plataforma((50,50), caja_moneda, (1890, 230),True) #caja invisible

plataforma_caja5 = Plataforma((50,50), caja_moneda, (2450, 300),False)
plataforma_caja6 = Plataforma((50,50), caja_moneda, (2400, 300),False)

plataforma_caja7 = Plataforma((50,50), caja_moneda, (3550, 500),False)


plataforma_caja8 = Plataforma((50,50), caja_moneda, (4350, 300),False) #boost

plataforma_caja9 = Plataforma((50,50), caja_moneda, (4900, 550),False)
plataforma_caja10 = Plataforma((50,50), caja_moneda, (5050, 550),False)
plataforma_caja11 = Plataforma((50,50), caja_moneda, (5200, 550),False)
plataforma_caja12 = Plataforma((50,50), caja_moneda, (5350, 550),False)
plataforma_caja13 = Plataforma((50,50), caja_moneda, (4970, 400),False)
plataforma_caja14 = Plataforma((50,50), caja_moneda, (5105, 400),False)
plataforma_caja15 = Plataforma((50,50), caja_moneda, (5250, 400),False)
plataforma_caja16 = Plataforma((50,50), caja_moneda, (5120, 280),False)

plataforma_caja17 = Plataforma((50,50), caja_moneda, (6200, 400),False)
plataforma_caja18 = Plataforma((50,50), caja_moneda, (6250, 400),False)

plataforma_caja19 = Plataforma((50,50), caja_moneda, (8200, 550),False)

#PLATAFORMAS LADRILLO
plataforma_ladrillo = Plataforma((50,50),caja_ladrillo,(750,620),False)

plataforma_ladrillo1 = Plataforma((50,50),caja_ladrillo,(800,390),False)
plataforma_ladrillo2 = Plataforma((50,50),caja_ladrillo,(900,390),False)

plataforma_ladrillo3 = Plataforma((50,50),caja_ladrillo,(2300, 300),False)
plataforma_ladrillo4 = Plataforma((50,50),caja_ladrillo,(2350, 300),False)
plataforma_ladrillo5 = Plataforma((50,50),caja_ladrillo,(2500, 300),False)
plataforma_ladrillo6= Plataforma((50,50),caja_ladrillo,(2550, 300),False)

plataforma_ladrillo7 = Plataforma((50,50),caja_ladrillo,(3750, 300),False)
plataforma_ladrillo8 = Plataforma((50,50),caja_ladrillo,(3800, 300),False)
plataforma_ladrillo9 = Plataforma((50,50),caja_ladrillo,(3850, 300),False)
plataforma_ladrillo10 = Plataforma((50,50),caja_ladrillo,(3900, 300),False)
plataforma_ladrillo11 = Plataforma((50,50),caja_ladrillo,(3950, 300),False)
plataforma_ladrillo12 = Plataforma((50,50),caja_ladrillo,(4000, 300),False)
plataforma_ladrillo13 = Plataforma((50,50),caja_ladrillo,(4200, 300),False)
plataforma_ladrillo14 = Plataforma((50,50),caja_ladrillo,(4250, 300),False)
plataforma_ladrillo14 = Plataforma((50,50),caja_ladrillo,(4250, 300),False)
plataforma_ladrillo15 = Plataforma((50,50),caja_ladrillo,(4300, 300),False)

plataforma_ladrillo16 = Plataforma((50,50),caja_ladrillo,(3500, 500),False)
plataforma_ladrillo17 = Plataforma((50,50),caja_ladrillo,(3600, 500),False)

plataforma_ladrillo18 = Plataforma((50,50),caja_ladrillo,(4350, 500),False)

plataforma_ladrillo19 = Plataforma((50,50),caja_ladrillo,(5800, 550),False)
plataforma_ladrillo20 = Plataforma((50,50),caja_ladrillo,(5900, 400),False)
plataforma_ladrillo21 = Plataforma((50,50),caja_ladrillo,(5950, 400),False)
plataforma_ladrillo22 = Plataforma((50,50),caja_ladrillo,(6000, 400),False)

plataforma_ladrillo23 = Plataforma((50,50),caja_ladrillo,(6150, 400),False)
plataforma_ladrillo24 = Plataforma((50,50),caja_ladrillo,(6300, 400),False)

plataforma_ladrillo25 = Plataforma((50,50),caja_ladrillo,(8100, 550),False)
plataforma_ladrillo26 = Plataforma((50,50),caja_ladrillo,(8150, 550),False)
plataforma_ladrillo27 = Plataforma((50,50),caja_ladrillo,(8250, 550),False)

lista_plat_sorpresa = [plataforma_caja1,
                    plataforma_caja2,
                    plataforma_caja3,
                    plataforma_caja4,
                    plataforma_caja5,
                    plataforma_caja6,
                    plataforma_caja7,
                    plataforma_caja9,
                    plataforma_caja10,
                    plataforma_caja11,
                    plataforma_caja12,
                    plataforma_caja13,
                    plataforma_caja14,
                    plataforma_caja15,
                    plataforma_caja16,
                    plataforma_caja17,
                    plataforma_caja18,
                    plataforma_caja19]

lista_plat_ladrillo =[plataforma_ladrillo,
                    plataforma_ladrillo1,
                    plataforma_ladrillo2,
                    plataforma_ladrillo3,
                    plataforma_ladrillo4,
                    plataforma_ladrillo5,
                    plataforma_ladrillo6,
                    plataforma_ladrillo7,
                    plataforma_ladrillo8,
                    plataforma_ladrillo9,
                    plataforma_ladrillo10,
                    plataforma_ladrillo11,
                    plataforma_ladrillo12,
                    plataforma_ladrillo13,
                    plataforma_ladrillo14,
                    plataforma_ladrillo15,
                    plataforma_ladrillo16,
                    plataforma_ladrillo17,
                    plataforma_ladrillo18,
                    plataforma_ladrillo19,
                    plataforma_ladrillo20,
                    plataforma_ladrillo21,
                    plataforma_ladrillo22,
                    plataforma_ladrillo23,
                    plataforma_ladrillo24,
                    plataforma_ladrillo25,
                    plataforma_ladrillo26,
                    plataforma_ladrillo27,
                    tubo_1,
                    tubo_2,
                    tubo_3,
                    tubo_4,
                    tubo_5,
                    tubo_6,
                    piso_bandera]

lista_escalera = [escalera_1,
                escalera_2,
                escalera_3,
                escalera_4,
                escalera_5,
                escalera_6,
                escalera_7,
                escalera_8,
                escalera_9,
                escalera_10,
                escalera_11,
                escalera_12,
                escalera_13,
                escalera_14,
                escalera_15,
                escalera_16,
                escalera_17,
                escalera_18,
                escalera_19,
                escalera_20,
                escalera_21,
                escalera_22,
                escalera_23,
                escalera_24,
                escalera_25,
                escalera_26,
                ]

topes = [tope1,tope2]

next_lvl =  Generar_rects(9800,600,50,800)
