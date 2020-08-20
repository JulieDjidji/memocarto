"""
Retour sur la discrétisation des variables quantitatives
----------------------------------------------------------------
Les méthodes de discrétisation les plus courantes sont disponibles sous Geopandas (quantile, intervalle égal, Jenks). La discrétisation dite de Jenks qui recherche à construire des classes les plus homogènes possibles est en générale la plus pertinente. Néanmoins, ce n'est pas toujours le cas, comme en témoigne les cartes suivantes de densité de population départementale.
"""
# sphinx_gallery_thumbnail_number = 3
import pandas as pd
import geopandas as gpd
import numpy as np

import matplotlib.pyplot as plt
###############################################################################
# Lecture des données
# ================================
#
# On ouvre le fond du bâti de la ville de Caen.

