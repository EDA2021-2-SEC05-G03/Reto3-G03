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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de UFOS
def init():
    return model.newCatalog()

# Funciones para la carga de datos
def loadData(catalog,archivo):
    archivo = cf.data_dir + archivo
    input_file = csv.DictReader(open(archivo, encoding="utf-8"),
    delimiter = ",")
    for ufo in input_file:
        model.addUFO(catalog,ufo)
    #Función que crea un rbt con el numero de avistamientos por ciudad.
    model.requerimiento1topciudades(catalog)
    return catalog

# Funciones de consulta sobre el catálogo

def requerimiento1(catalog, ciudad):
    return model.requerimiento1(catalog, ciudad)

def requerimiento2(catalog,mins,maxs):
    return model.requerimiento2(catalog,mins,maxs)

def requerimiento3(catalog, begin, end):
    return model.requerimiento3(catalog, begin, end)

def requerimiento4(catalog, begin, end):
    return model.requerimiento4(catalog, begin, end)

def requerimiento5(catalog,lon_max,lon_min,lat_max,lat_min):
    return model.requerimiento5(catalog,lon_max,lon_min,lat_max,lat_min)

def mapa(catalog,l):
    return model.mapa(catalog,l)