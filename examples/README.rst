.. _gallery:

Examples Gallery
----------------

Les exemples proposés sont réalisés sous Python avec le package `GeoPandas`_

.. image:: ../_static/PandasVsGeoPandas.png
   :width: 600

Avant de commencer les exemples, faisons le point sur les principales méthodes de GeoPandas :

| Méthode | Explication | Exemple de code |
| :---: | :---: | :--- |
| [read_file](https://geopandas.org/reference/geopandas.read_file.html) | Crée un GeoDataFrame à partir d'un *shapefile*, d'un *GeoJSON*, ...  | gpd.read_file('data.shp') |
| [to_file](https://geopandas.org/reference.html#geopandas.GeoDataFrame.to_file) | Exporte en GeoDataFrame dans un format shapefile, GeoJSON (driver='GeoJSON') ou GeoPackage (driver="GPKG") | gdf.to_file("data.geojson", driver='GeoJSON') |
| [cx](https://geopandas.org/indexing.html) | Sélectionne les polygones au sein d'un cadre donné | df.cx[xmin:xmax, ymin:ymax]] |
| [merge](https://geopandas.org/mergingdata.html) | Fusionne un GeoDataFrame avec un DataFrame | df.merge(gdf, on='code') |
| [sjoin](https://geopandas.org/reference/geopandas.sjoin.html) | Fusionne deux GeoDataFrame en s'appuyant sur leur relation spatiale. On fixe le paramètre *how*  pour décider du type de jointure et le paramètre *op* pour choisir si la jointure a lieu | geopandas.sjoin(gdf1, gdf2, how="inner", op='intersects') |
| [append](https://geopandas.org/mergingdata.html#appending) | Concatène deux GeoDataFrame mais attention les colonnes de géométrie doivent avoir le même CRS | gdf1.append(gdf2) |
| [dissolve](https://geopandas.org/aggregation_with_dissolve.html) | Fusionne les géométries et agrège (somme, moyenne, minimum, maxmum ...) des données spatiales par groupe | gdf.dissolve(by='variableAgrégation', aggfunc='sum') |




Voici quelques exemples de visualisation réalisables avec GeoPandas !



.. _Geopandas: https://geopandas.org
