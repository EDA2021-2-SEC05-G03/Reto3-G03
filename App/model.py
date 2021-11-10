﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.bst import keySet
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'info': None,
    'ciudad' : None
    }
    catalog['info'] = om.newMap(omaptype="RBT", comparefunction=compareDates)
    catalog['ciudad']=mp.newMap(numelements=804,maptype="LINEAR_PROBING",loadfactor=0.5) #ciudad-rbtavistamientos
    catalog['topciudades'] = om.newMap(omaptype="RBT", comparefunction=compareDates) #rbt ordenado por cantidad de avistamientos.
    catalog['hh:mm'] = om.newMap(omaptype="RBT", comparefunction=compareDates) #hora:min--arbolfecha-info
    catalog['AA-MM'] = om.newMap(omaptype="RBT", comparefunction=compareDates) #A-M-D--arbolfecha-info
    return catalog

# Funciones para agregar informacion al catalogo
def addUFO(catalog,UFO):

    #Carga del rbt principal ordenado por datetime de todos los avistamientos.
    date = datetime.datetime.strptime(UFO["datetime"], "%Y-%m-%d %H:%M:%S")
    om.put(catalog['info'], date, UFO)
    
    #Req1: Carga de ciudad-rbt ordenado por fecha de avistamiento
    presente = mp.contains(catalog["ciudad"],UFO['city'])
    if not presente:
        arbol = om.newMap(omaptype="RBT", comparefunction=compareDates)      
        om.put(arbol,date,UFO)
        mp.put(catalog["ciudad"], UFO['city'], arbol)
    else:
        arbol = mp.get(catalog["ciudad"], UFO['city'])["value"]
        om.put(arbol,date,UFO)
        mp.put(catalog["ciudad"], UFO['city'], arbol)

    #Req3:
    
    h = int(UFO["datetime"][-8:-6])
    m = int(UFO["datetime"][-5:-3])
    s = int(00)
    
    hora = datetime.time(h,m,s)
    presente1 = om.contains(catalog["hh:mm"],hora)
    if not presente1:
        arbol = om.newMap(omaptype="RBT", comparefunction=compareDates)      
        om.put(arbol,date,UFO)
        om.put(catalog["hh:mm"], hora, arbol)
    else:
        arbol = om.get(catalog["hh:mm"], hora)["value"]
        om.put(arbol,date,UFO)
        om.put(catalog["hh:mm"], hora, arbol)

    #Req4:
    aa = int(UFO["datetime"][0:4])    
    mm = int(UFO["datetime"][5:7])    
    dd = int(UFO["datetime"][8:10])
    fecha = datetime.date(aa,mm,dd)
    presente3 = om.contains(catalog["AA-MM"],fecha)
    if not presente3:
        arbol2 = om.newMap(omaptype="RBT", comparefunction=compareDates)      
        om.put(arbol2,date,UFO)
        om.put(catalog["AA-MM"], fecha, arbol2)
    else:
        arbol2 = om.get(catalog["AA-MM"], fecha)["value"]
        om.put(arbol2,date,UFO)
        om.put(catalog["AA-MM"], fecha, arbol2)   

def requerimiento1topciudades(catalog):
    """ 
    Se va a crear un rbt ordenado por la cantidad de avistamientos
    en cada ciudad, para hacer la tabla del requerimiento 1 del top
    5 ciudades con mayor número de avistamientos.
    """
    #Se obtienen las llaves de todo el mapa
    ciudades = mp.keySet(catalog['ciudad'])
    #Se itera para ir agregando al order map en orden de avistamientos.
    for ciudad in lt.iterator(ciudades):
        arbol = mp.get(catalog['ciudad'], ciudad)['value']
        tamaño = om.size(arbol)
        datos = (ciudad,tamaño)
        presente = om.contains(catalog['topciudades'], tamaño)
        if not presente:
            lista = lt.newList(datastructure="ARRAYLIST")
            lt.addLast(lista, datos)
            om.put(catalog['topciudades'], tamaño, lista)
        else:
            lista = om.get(catalog['topciudades'], tamaño)['value']
            lt.addLast(lista,datos)





    



# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# Funciones de comparación

def compareDates(date1, date2):
   
    if (date1 == date2):
        return 0
    elif (date1>date2):
        return 1
    else:
        return -1


def requerimiento1(catalog, ciudad):
    #Se obtiene el rbt que tiene ordenado por fechas los avistamientos de esa ciudad:
    info = mp.get(catalog["ciudad"],ciudad)["value"]
    #Se obtiene el tamaño que es la cantidad de avistamientos en esa ciudad:
    size = om.size(info)
    #Se obtiene el total de ciudad con avistamientos:
    sizecitys = mp.size(catalog['ciudad'])
    #Lista con el top 5 de las ciudades con mayor avistamiento:
    mayores5 = lt.newList(datastructure="ARRAY_LIST")
    x = 0
    while x < 5:
        maxkeyciudades = om.maxKey(catalog['topciudades'])
        ciudades = om.get(catalog['topciudades'], maxkeyciudades)['value']
        for ciudad in lt.iterator(ciudades):
            lt.addLast(mayores5, ciudad)
            x += 1
        om.deleteMax(catalog['topciudades'])

    #Se obtienen los primeros 3 y ultimos 3 avistamientos de la ciudad.
    #Hacemos copia para no modificar el rbt original
    info = info.copy()
    #Lista para guardar una lista con los primeros 3 y últimos 3
    menoresymayores3 = lt.newList(datastructure="ARRAY_LIST")
    #Lista para guardar los mayores, ya que por el API de los ordered maps quedan al revés si se ingresan así
    mayoresinorganizar = lt.newList(datastructure="SINGLE_LINKED")
    #Se hacen 3 iteraciones para tomar los primeros 3
    for x in range(0,3):
        minimakey= om.minKey(info)
        minima = om.get(info, minimakey)["value"]
        lt.addLast(menoresymayores3,minima)
        om.deleteMin(info)
    #Se hacen 3 iteraciones para tomar los últimos 3, se agregan a otra lista para luego agregarlos a la lista de salida ya ordenados.
    for x in range(0,3):
        maxkey= om.maxKey(info)
        max = om.get(info, maxkey)["value"]
        lt.addFirst(mayoresinorganizar,max)
        om.deleteMax(info)
    #Se agregan los datos de la lista que contiene los mayores, a la lista de salida para que todo quede en orden.
    for x in lt.iterator(mayoresinorganizar):
        lt.addLast(menoresymayores3,x)
    return(size, sizecitys,mayores5,menoresymayores3)


def requerimiento3(catalog, begin, end):
    h1 = int(begin[0:2])
    h2 = int(end[0:2])
    min_begin = int(begin[3:5])
    min_end= int(end[3:5])  

    info = lt.newList(datastructure="ARRAY_LIST")

    for i in range(min_begin,59):
        key = datetime.time(h1,i)
        presente = om.contains(catalog["hh:mm"],key)               
        if presente:
            f = om.get(catalog["hh:mm"],key)["value"]
            keys = om.keySet(f)                                             
            for k in lt.iterator(keys):
                size = lt.size(info)
                if size < 3:     
                    d = om.get(f,k)["value"]                   
                    lt.addLast(info,d)
                else:
                    break           
        else:
            None

    info2 = lt.newList(datastructure="ARRAY_LIST")

    for s in range(min_end,0,-1):
        key = datetime.time(h2,s)
        presente = om.contains(catalog["hh:mm"],key)               
        if presente:
            f = om.get(catalog["hh:mm"],key)["value"]
            keys = om.keySet(f)                                                                 
            for k in range(0,3):
                t = lt.lastElement(keys)
                size = lt.size(info2)
                if size < 3:  
                    lt.removeLast(keys)                    
                    d = om.get(f,t)["value"]
                    lt.addFirst(info2,d)                    
                else:
                    break           
        else:
            None
   

    tot = om.keys(catalog["hh:mm"],datetime.time(h1,min_begin),datetime.time(h2,min_end))
    
    total = 0
    for i in lt.iterator(tot):             
        j = om.get(catalog["hh:mm"],i)["value"]       
        total += om.size(j)

    print("El total de avistamientos durante estas horas es de "+str(total))

    return(info,info2)


def requerimiento4(catalog, begin, end):
    aa_beg = int(begin[0:4])
    mm_beg = int(begin[5:7])
    dd_beg = int(begin[8:10])

    aa_end = int(end[0:4])
    mm_end = int(end[5:7])
    dd_end = int(end[8:10])

    fecha1 = datetime.date(aa_beg,mm_beg,dd_beg)
    fecha2 = datetime.date(aa_end,mm_end,dd_end)
    
    total_d = om.size(catalog["AA-MM"])

    print("There are "+ str(total_d)+" days whith UFO sightings ")

    keys = om.keys(catalog["AA-MM"],fecha1,fecha2)
    
    s = 0
    for i in lt.iterator(keys):             
        j = om.get(catalog["AA-MM"],i)["value"]       
        s += om.size(j)

    print("There are "+ str(s)+" sightings between "+ str(begin)+" and "+str(end))
    
    p1 = lt.newList(datastructure="ARRAY_LIST")

    for i in lt.iterator(keys):
        tam = lt.size(p1)
        if tam < 3:
            f = om.get(catalog["AA-MM"],i)["value"]["root"]["value"]
            lt.addLast(p1,f)
        else:
            break
    
    p2 = lt.newList(datastructure="ARRAY_LIST")
    c = lt.size(keys)

    for i in range(c,0,-1):
        
        tam = lt.size(p2)
        if tam < 3:
            elm = lt.getElement(keys,i)          
            f = om.get(catalog["AA-MM"],elm)["value"]["root"]["value"]
            lt.addFirst(p2,f)
        else:
            break
    return p1,p2


        