"""
Délimitation de tâches bâties
----------------------------------------------------------------
Dans ce notebook, nous allons délimiter des zones bâties pour la ville de Caen à partir des données de bâti de la Base de données topographique (BD TOPO).
"""
# sphinx_gallery_thumbnail_number = 3
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import wget
from zipfile import ZipFile

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))

###############################################################################
# Récupération et lecture des données
# ================================
#
# On récupère les données stockées sur un serveur de stockage (préciser où les récupérer).

url=os.getenv("URL_BATI_VILLE")
file = url.split('/')[-1] #os.path.join(BASE_DIR+'/'+url.split('/')[-1])
wget.download(url, file)
with ZipFile(file, 'r') as files: 
    files.extractall()
    
###############################################################################
# On ouvre le fond du bâti de la ville de Caen.

immeuble = gpd.read_file(file.split('.')[0]+'.shp')

###############################################################################
# Délimitation des zones bâties
# ================================
#
# On calcule un buffer de 100 mètres autour de chaque bâtiment.

immeuble['geometry']=immeuble.geometry.buffer(100)

###############################################################################
# On fusionne les buffers avec une intersection non nulle et on affiche les zones fusionnées.

union_buffer=gpd.GeoDataFrame({'geometry':immeuble.unary_union})
union_buffer.plot()

###############################################################################
# On effectue un buffer négatif pour affiner la délimitation afin de compenser le buffer positif prélablement réaliser pour capter les relations de bâtiments voisins. L'affichage de la carte montre des zones plus délimitées.

union_buffer['zone']=union_buffer.buffer(-100)
union_buffer['zone'].plot()

###############################################################################
# On décide d'afficher que les zones de plus de 8 hectares.

union_buffer['aire']=union_buffer['zone'].area/10000
union_buffer[union_buffer.aire>8].plot()
