"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Iniciar catálogo")
    print("2- Cargar información de avistamientos")
    print("3- Requerimiento 1: Contar los avistamientos en una ciudad")
    print("4- Requerimiento 2: Contar los avistamientos por duración")
    print("5- Requerimiento 3: Contar avistamientos por Hora/Minutos del día")
    print("6- Requerimiento 4: Contar los avistamientos en un rango de fechas")
    print("7- Requerimiento 5: Contar los avistamientos de una Zone Geográfica")
    print("8- Requierimiento 6: Visualizar los avistamientos de una zona geográfica")
    print("0- Salir")


catalog = None
archivo = "UFOS//UFOS-utf8-small.csv"

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando el catálogo ...")
        catalog = controller.init()

    elif int(inputs[0]) == 2:
        controller.loadData(catalog, archivo)
        print("Avistamientos cargados: " + str(om.size(catalog['info'])))
        print("Altura del arbol: " + str(om.height(catalog['info'])))
        print("Menor llave: " + str(om.minKey(catalog['info'])))
        print("Mayor llave: " + str(om.maxKey(catalog['info'])))
    
    elif int(inputs[0]) == 3:
        print("=" * 15 + " Req No. 1 Inputs " + "=" * 15)
        ciudad = input("UFO Sightings in the city of: ")
        info = controller.requerimiento1(catalog, ciudad)
        print("=" * 15 + " Req No. 1 Outputs " + "=" * 15)
        print('There are ' + str(info[1]) + ' different cities with UFO sightings...')
        print('The TOP 5 cities with most UFO sightings are: ')
        #Se imprimen las top 5 mayores ciudades con mayor cantidad de avistamientos
        y = 0
        print ("=" * 48)
        for x in lt.iterator(info[2]):
            if y > 4:
                break
            y += 1
            print(str(y) + ". City: " + x[0] + ", Count: " + str(x[1]))
            print("=" * 48)
        #
        print('There are ' + str(info[0]) + ' sigthings at the: ' + ciudad + ' city')
        print('The first 3 and last 3 UFO sigthings in the city are:')
        print("=" * 50)
        for x in lt.iterator(info[3]):
            print('datetime: ' + str(x['datetime']))
            print('city: ' + x['city'])
            print('state: ' + x['state'])
            print('country: ' + x['country'])
            print('shape: ' + x['shape'])
            print('duration (seconds): ' + x['duration (seconds)'])
            print("=" * 50)
            


        
        
   
    elif int(inputs[0]) == 5:
        lim_inf = input('Ingrese el limite inferior en formato HH:MM: ')
        lim_sup = input('Ingrese el limite superior en formato HH:MM: ')

        #info = controller.requerimiento3(catalog, lim_inf, lim_sup)
        
    else:
        sys.exit(0)
sys.exit(0)
