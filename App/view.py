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

    elif int(inputs[0]) == 4:
        print("=" * 15 + " Req No. 2 Inputs " + "=" * 15)
        mins = input("UFO sightings between ")
        maxs = input("and ")
        info = controller.requerimiento2(catalog,mins,maxs)
        print("=" * 15 + " Req No. Answer " + "=" * 15)
        print('There are ' + str(info[0]) + ' different UFO sightings durations...')
        print('The TOP 5 durations with longest UFO sightings are:')
        print("=" * 48)
        for x in lt.iterator(info[1]):
            print('     duration (seconds): ' + str(int(x["llave"])) + ', count: ' + str(int(x["valor"])))
            print("=" * 48)
        print('There are ' + str(info[2]) + ' sightings between: ' + mins + ' and ' + maxs + ' duration')
        print('The first 3 and last 3 UFO sightings in the duration time are:')
        for x in lt.iterator(info[3]):
            print(x['city'])
            print(x['datetime'])
            print(x['duration (seconds)'])
            print (x['country'])
   
    elif int(inputs[0]) == 5:
        lim_inf = input('Ingrese el limite inferior en formato HH:MM: ')
        lim_sup = input('Ingrese el limite superior en formato HH:MM: ')

        info = controller.requerimiento3(catalog, lim_inf, lim_sup)
        print("+"+("-"*127)+"+")
        print("|"+ "datetime".center(19)+" | "+ "city".center(30)+" | "+ "country".center(15)+" | "+"shape".center(20)+" | "+ str("duration (seconds)").center(30)+" | ")
        print("+"+("-"*127)+"+")
        
        for i in lt.iterator(info[0]):                             
            print("|"+ str(i["datetime"])+" | "+ i["city"].center(30)+" | "+ i["country"].center(15)+" | "+i["shape"].center(20)+" | "+ str(i["duration (seconds)"]).center(30)+" | ")
            print("+"+("-"*127)+"+")
        
        for i in lt.iterator(info[1]):                             
            print("|"+ str(i["datetime"])+" | "+ i["city"].center(30)+" | "+ i["country"].center(15)+" | "+i["shape"].center(20)+" | "+ str(i["duration (seconds)"]).center(30)+" | ")
            print("+"+("-"*127)+"+") 

    elif int(inputs[0]) == 6:
        lim_inf = input('Ingrese el limite inferior en formato AA-MM-DD: ')
        lim_sup = input('Ingrese el limite superior en formato AA-MM-DD: ') 

        info = controller.requerimiento4(catalog, lim_inf, lim_sup)
        print("+"+("-"*127)+"+")
        print("|"+ "datetime".center(19)+" | "+ "city".center(30)+" | "+ "country".center(15)+" | "+"shape".center(20)+" | "+ str("duration (seconds)").center(30)+" | ")
        print("+"+("-"*127)+"+")
        for i in lt.iterator(info[0]):                             
            print("|"+str(i["datetime"])+" | "+ i["city"].center(30)+" | "+ i["country"].center(15)+" | "+i["shape"].center(20)+" | "+ str(i["duration (seconds)"]).center(30)+" | ")
            print("+"+("-"*127)+"+")
        
        for i in lt.iterator(info[1]):                             
            print("|"+ str(i["datetime"])+" | "+ i["city"].center(30)+" | "+ i["country"].center(15)+" | "+i["shape"].center(20)+" | "+ str(i["duration (seconds)"]).center(30)+" | ")
            print("+"+("-"*127)+"+") 
    elif int(inputs[0]) == 7:
        lat_min = input('Ingrese el limite maximo de latitud: ')
        lat_max = input('Ingrese el limite minimo de latitud: ')  
        lon_min = input('Ingrese el limite maximo de longitud: ')
        lon_max = input('Ingrese el limite minimo de longitud: ')
        
        info = controller.requerimiento5(catalog,lon_max,lon_min,lat_max,lat_min)
        print("There are "+str(info[1]) +" different UFO sightings in the area")
        print("+"+("-"*161)+"+")
        print("|"+ "datetime".center(19)+" | "+ "city".center(20)+" | "+ "state".center(15)+" | "+"country".center(20)+" | "+ str("shape").center(15)+" | "+ str("duration (seconds)").center(30)+" | "+ str("latitude").center(10)+" | "+ str("longitude").center(10)+" | ")
        print("+"+("-"*161)+"+")
        for i in lt.iterator(info[0]):                             
            print("|"+ i["datetime"]+" | "+ i["city"].center(20)+" | "+ i["state"].center(15)+" | "+i["country"].center(20)+" | "+ i["shape"].center(15)+" | "+ str(i["duration (seconds)"]).center(30)+" | "+ str(round(float(i["latitude"]),2)).center(10)+" | "+ str(round(float(i["longitude"]),2)).center(10)+" | ")
            print("+"+("-"*161)+"+")
    elif int(inputs[0]) == 8:        
  #      lat_min = input('Ingrese el limite minimo de latitud: ')
   #     lat_max = input('Ingrese el limite maximo de latitud: ')  
    #    lon_min = input('Ingrese el limite minimo de longitud: ')
     #   lon_max = input('Ingrese el limite maximo de longitud: ')

        lat_min ="31.33"
        lat_max ="37"
        lon_min ="-109.05"
        lon_max ="-103"
        info = controller.requerimiento5(catalog,lon_max,lon_min,lat_max,lat_min)
        print("There are "+str(info[1]) +" different UFO sightings in the area")
        print("+"+("-"*161)+"+")
        print("|"+ "datetime".center(19)+" | "+ "city".center(20)+" | "+ "state".center(15)+" | "+"country".center(20)+" | "+ str("shape").center(15)+" | "+ str("duration (seconds)").center(30)+" | "+ str("latitude").center(10)+" | "+ str("longitude").center(10)+" | ")
        print("+"+("-"*161)+"+")
        l = lt.newList(datastructure="ARRAY_LIST")
        for i in lt.iterator(info[0]):   
            lat = round(float(i["latitude"]),2)
            long = round(float(i["longitude"]),2)  
            city = i["city"]                        
            print("|"+ i["datetime"]+" | "+ i["city"].center(20)+" | "+ i["state"].center(15)+" | "+i["country"].center(20)+" | "+ i["shape"].center(15)+" | "+ str(i["duration (seconds)"]).center(30)+" | "+ str(lat).center(10)+" | "+ str(long).center(10)+" | ")
            print("+"+("-"*161)+"+")
            lt.addLast(l,lat)
            lt.addLast(l,long)
        
        mapa = controller.mapa(catalog,l)
         
    
    else:
        sys.exit(0)
sys.exit(0)
