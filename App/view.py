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
        #Como no vamos a avanzar en el requerimiento, solo haremos la carga de datos por llave: ciudad, valor: lista de avistamientos.
        print("Ciudades cargadas: " + str(om.size(catalog['ciudad'])))
        print("Altura del arbol: " + str(om.height(catalog['ciudad'])))
        ciudad = input('Ingrese la ciudad: ')
        info = controller.requerimiento1(catalog, ciudad)
        print("+"+("-"*150)+"+")
        count = 0
        for i in lt.iterator(info[0]):
            count+=1
            if count <= 3:
                l = om.get(info[1],i)["value"]        
                print("|"+ str(l["datetime"])+" | "+ l["city"].center(30)+" | "+ l["state"].center(15)+" | "+l["country"].center(20)+" | "+l["shape"].center(15)+" | "+ str(l["duration (seconds)"]).center(30)+" | ")
                print("+"+("-"*150)+"+")
            else:
                break


        
        
   
    elif int(inputs[0]) == 5:
        #Como no vamos a avanzar en el requerimiento, solo haremos la carga de datos por llave: ciudad, valor: lista de avistamientos.
        lim_inf = input('Ingrese el limite inferior en formato HH:MM: ')
        lim_sup = input('Ingrese el limite superior en formato HH:MM: ')

        #info = controller.requerimiento3(catalog, lim_inf, lim_sup)
        
    else:
        sys.exit(0)
sys.exit(0)
