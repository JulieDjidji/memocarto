Fichiers Géographiques
=================================================================================================

La listes des différents formats des fichiers géographiques est pléthorique. Le plus connu et le plus utilisé est le format shapefile, il est le format d'ESRI (logiciel ARCGIS). Un fond de carte est composé par 5 fichiers : le .shp qui est la porte d'entrée sur les données, un fichier .dbf qui contient les données attributaires (soit les données associées aux objets contenu dans le shapefile) et d'autres fichiers qui gére la projection est la géométrie. Il est nécessaire que tous les fichiers soient au même emplacement pour qu'un fichier puisse être ouvert par un SIG.

D'autres formats tendent progressivement à s'imposer. La communauté Qgis propose le format Geopackage. Les données sont contenues dans un unique fichier d'extension *.qgz. Ce format risque de surclasser les shapefiles dans le futur. Le format geojson est très adapté au données mais ils est particulièrement volumineux. En effet, ce format qui est une extension de json n'est pas compressé et correspond à un dictionnaire. Voici un exemple de fichier geojson est en dessous la carte associée :


L'avantage du geojson est qu'il peut être lu par n'importe quelle outil. Les plus anciens se rapelleront le format MIF-MID de mapinfo qui était également un format texte et qui présentait comme le format geojson l'avantage de pouvoir être écris à la main. Dans tous les cas, les SIG modernes sont généralement capable de lire tous les formats disponibles et vous pouvez facilement ouvir un fichier et le sauvegarder dans un autre format facilement.
