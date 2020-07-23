"""
Premières manipulations de données spatiales
----------------------------------------------------------------
Dans ce notebook, nous allons apprendre à lire, écrire, merger et aggréger des données spatiales.
"""
# sphinx_gallery_thumbnail_number = 3
import os
import pandas as pd
import geopandas as gpd
import config

###############################################################################
# Ouverture des données
# ================================
#
# Les données attributaires proviennent du recensement de la population de 2017. La base commune contient la population communale, PTOT (et par arrondissement pour Paris, Lyon et Marseille). Attention, les données sont en géographie 2019.

population = pd.read_csv(os.getenv("URL_DATA_COMMUNES"), sep=";", dtype={'DEPCOM':str})
population.head(2)

###############################################################################
# On ouvre le fond des communes et on lui rajoute les arrondissements.

commune = gpd.read_file(os.getenv("URL_GEOJSON_COMMUNES"))
#armf = gpd.read_file("armf_francemetro_2019.geojson")
#armf['dep'] = armf.code.str.slice(0,3) # il manque le numèro de département dans le fond armf
#commune = commune.append(armf, sort=False)

###############################################################################
# Jointure des données
# ================================
# 
# La jointure entre les deux tables s'opère simplement à l'aide de la fonction ``gpd.merge()``.

pop_com = commune.merge(population, left_on='code', right_on='DEPCOM')

###############################################################################
# On peut afficher une carte de densité en quelques lignes de code en recourant à la fonction ``gpd.plot()``. 

pop_com['densite'] = pop_com.PTOT / pop_com.geometry.area * 1000000 
pop_com.plot('densite',legend=True, scheme='quantiles', cmap='OrRd', figsize=(10,10))

###############################################################################
# Aggregation des données pour produire des données départementales et régionales
# ====================================================================================
# 
# L'aggrégation des données spatiales s'effectue à l'aide de la fonction ``gpd.dissolve()`` qui repose sur la méthode **groupby** de pandas. **aggfunc** définit la fonction a appliqué aux données attributaires.

###############################################################################
# Carte au niveau départemental
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

pop_dep = pop_com.dissolve(by='dep', aggfunc='sum', as_index=False)
pop_dep['densite'] = pop_dep.PTOT / pop_dep.geometry.area * 1000000
pop_dep.plot('densite',legend=True, scheme='quantiles', figsize=(10,10),cmap='OrRd')

###############################################################################
# Carte au niveau régional
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

pop_reg = pop_com.dissolve(by='reg', aggfunc='sum', as_index=False)
pop_reg['densite'] = pop_reg.PTOT / pop_reg.geometry.area * 1000000
pop_reg.plot('densite',legend=True, scheme='quantiles', figsize=(10,10),cmap='OrRd')
