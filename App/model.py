"""
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
    catalog['ciudad'] = om.newMap(omaptype="RBT", comparefunction=compareDates) #hashciudad-info
    catalog['hash']=mp.newMap(numelements=804,maptype="LINEAR_PROBING",loadfactor=0.5) #hash-ciudad
    return catalog

# Funciones para agregar informacion al catalogo
def addUFO(catalog,UFO):
    UFO["datetime"] = datetime.datetime.strptime(UFO["datetime"], "%Y-%m-%d %H:%M:%S")
    om.put(catalog['info'], UFO['datetime'], UFO)
    
    ciudadhash = hash(UFO["city"])
    presente = om.contains(catalog["ciudad"],ciudadhash)
    if not presente:
        lista = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista,UFO)
        om.put(catalog["ciudad"], ciudadhash, lista)
    else:
        lista = om.get(catalog["ciudad"], ciudadhash)["value"]
        lt.addLast(lista,UFO)
        om.put(catalog["ciudad"], ciudadhash, lista)

    presente2 = mp.contains(catalog["hash"],UFO["city"])
    if not presente2:      
        mp.put(catalog["hash"],UFO["city"],ciudadhash)
    else:        
        None
          


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
    hash_num = mp.get(catalog["hash"],ciudad)["value"]
 
    info = om.get(catalog["ciudad"],hash_num)["value"]
    print(info)
    
  