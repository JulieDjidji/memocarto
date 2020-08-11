"""
Délimitation de tâches bâties
----------------------------------------------------------------
Dans ce notebook, nous allons délimiter des zones bâties pour la ville de Caen.
"""
# sphinx_gallery_thumbnail_number = 3
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

###############################################################################
# Lecture des données
# ================================
#
# On ouvre le fond du bâti de la ville de Caen.

bati = gpd.read_file(os.getenv("URL_BATI_VILLE"))

###############################################################################
# Délimitation des zones bâties
# ================================
#
# On calcule un buffer de 100 mètres autour de chaque bâtiment.

bati_buffer_positif=bati.copy()
bati_buffer_positif['geometry']=bati_buffer_positif.geometry.buffer(100)

###############################################################################
# On fusionne les buffers avec une intersection non nulle et on affiche les zones fusionnées.

union_buffer=gpd.GeoDataFrame({'geometry':bati_buffer_positif.unary_union})
ax = union_buffer.plot()

###############################################################################
# On effectue un buffer négatif pour affiner la délimitation afin de compenser le buffer positif prélablement réaliser pour capter les relations de bâtiments voisins. L'affichage de la carte montre des zones plus délimitées.

union_buffer_negatif=union_buffer.copy()
union_buffer_negatif['geometry']=union_buffer_negatif.buffer(-100)
#ax = union_buffer_negatif['geometry'].plot()

###############################################################################
# On décide d'afficher que les zones de plus de 8 hectares.

#union_buffer_negatif['aire']=union_buffer_negatif['geometry'].area/10000
#ax = union_buffer_negatif[union_buffer_negatif.aire>8].plot()
