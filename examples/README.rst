.. _gallery:

Examples Gallery
----------------

Les exemples proposés sont réalisés sous Python avec le package `GeoPandas`_

.. image:: ../_static/PandasVsGeoPandas.png
   :width: 600

.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Méthode
     - Explication
     - Exemple de code
   * - `read_file`_
     - Crée un GeoDataFrame à partir d'un *shapefile*, d'un *GeoJSON*, ...  
     - gpd.read_file('data.shp')
   * - `to_file` 
     - Exporte en GeoDataFrame dans un format shapefile, GeoJSON (driver='GeoJSON') ou GeoPackage (driver="GPKG") 
     - gdf.to_file("data.geojson", driver='GeoJSON')
   * - cx 
     - Sélectionne les polygones au sein d'un cadre donné 
     - df.cx[xmin:xmax, ymin:ymax]]
   * - merge 
     - Fusionne un GeoDataFrame avec un DataFrame 
     - df.merge(gdf, on='code')
   * - sjoin 
     - Fusionne deux GeoDataFrame en s'appuyant sur leur relation spatiale. On fixe le paramètre *how*  pour décider du type de jointure et le paramètre *op* pour choisir si la jointure a lieu 
     - geopandas.sjoin(gdf1, gdf2, how="inner", op='intersects')
   * - append 
     - Concatène deux GeoDataFrame mais attention les colonnes de géométrie doivent avoir le même CRS 
     - gdf1.append(gdf2) |
   * - dissolve 
     - Fusionne les géométries et agrège (somme, moyenne, minimum, maxmum ...) des données spatiales par groupe 
     - gdf.dissolve(by='variableAgrégation', aggfunc='sum')
        
Avant de commencer les exemples, faisons le point sur les principales méthodes de GeoPandas :

Le package contextily permet notamment d'ajouter un fond OpenStreetMap. Il faut d'abord importer le package *contextily* comme *ctx* puis ajouter ce fond de carte OpenStreetMap à la carte représentée.

.. list-table:: 
   :widths: 15 10 30
   :header-rows: 1

   * - Méthode
     - Explication
     - Exemple de code
   * - `add_basemap`_
     - Ajoute un fond de carte OPenStreetMap à notre *plot*
     - ctx.add_basemap(ax)

La `geometry`_ possède différents attributs et méthodes très utiles :

Voici quelques exemples de visualisation réalisables avec GeoPandas !



.. _Geopandas: https://geopandas.org
.. _read_file: https://geopandas.org/reference/geopandas.read_file.html
.. _to_file: https://geopandas.org/reference.html#geopandas.GeoDataFrame.to_file
.. _cx: https://geopandas.org/indexing.html
.. _merge: https://geopandas.org/mergingdata.html
.. _sjoin: https://geopandas.org/reference/geopandas.sjoin.html
.. _append: https://geopandas.org/mergingdata.html#appending
.. _dissolve: https://geopandas.org/aggregation_with_dissolve.html
.. _add_basemap: https://geopandas.org/gallery/plotting_basemap_background.html
.. _geometry: https://geopandas.org/geometric_manipulations.html
