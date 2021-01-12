.. carto documentation master file, created by
   sphinx-quickstart on Fri Jul 17 11:01:39 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Les territoires de la cartographie
=================================

Les progrès de l’informatique ont décuplé la capacité des acteurs publics et privés à diffuser des cartes statistiques. Il n’a jamais été aussi simple de produire et de communiquer une information statistique à l’aide d’une carte. Ce constat est néanmoins à tempérer, car la cartographie statistique reste toujours une pratique d’initiés. Pour le profane, la cartographie ressemble à une nébuleuse inextricable composée de concepts jargonant. Ce site vise à vous familiariser avec les notions de la cartographie et à vous présenter les principales solutions techniques utilisées actuellement. Il ne se veut pas une présentation exhaustive mais plutôt une entrée matière afin de démythifier la cartographie.








.. toctree::
  :maxdepth: 1
  :caption: Introduction
  
  Pourquoi faire des cartes ? <pourquoi>
  Tour d'horizon des acteurs <acteurs>



.. toctree::
  :maxdepth: 1
  :caption: Stockage des données spatiales
  
  Les fichiers cartographiques  <fichiers_geo>
  Les bases de données spatiales Postgis <postgis>
  
Dans cette partie, nous nous intéréssons aux différentes possibilités existantes pour stocker l'information géographique. Initialement, le principal outil de stockage était le fichier cartographique. Progressivement, des bases de données spatiales, POSTGIS extension de POSTGRESQL et SpatiaLite extension de SQLite, ont été élaborées pour traiter de grands volumes de données. En pratique avec les outils modernes, la manipulation d'une base de données ou d'un fichier géographique se ressemble de plus en plus. La dimension spatiale apparait comme une colonne supplémentaire qui décrit pour chaque observation son emprise spatiale associée. Par exemple, une commune convexe est décrite par un polygon composé d'une succession de coordonnées correspondant aux sommets : POLYGON((X_1, Y_1), (X_2, Y_2)). Une commune disposant d'une exclave est décrite par la réunion de deux polygons. On parle dans ce cas de MULTIPOLYGON.   
 
.. toctree::
  :maxdepth: 1
  :caption: Traitement
   
   Qgis, la boite à outils du cartographe <qgis>
   Requêtes spatiales sous SQL <qgis>
   Les accès aux données géo : quels outils de géocodage ? <geocodage>


.. toctree::
  :maxdepth: 1
  :caption: Diffusion


  La sémiologie : une grammaire spatiale  <semio> 
  Heurs et malheurs de la spatialisation des données statistiques <concepts>
  
  Les cartes statiques <qgis>
  Geoserver <geoserver>
  Leaflet <leaflet>
  Comment tout cela s'articule-t-il? <articulation>
  Un exemple d'implémentation <implementation>







  


.. toctree::
  :maxdepth: 1
  :caption: On s'exerce !
  
  Mini présentation de GeoPandas <geopandas>
  Galerie d'exemples <gallery/index>
  Postgis sous Python <postgisPy>
  
.. toctree::
  :maxdepth: 1
  :caption: Contributeurs

   Contributeurs <contributors>

Nous contacter
---------------------

- Reporter des bugs, suggérer des ajouts ou du code sur `GitHub`_.

.. _GitHub: https://github.com/JulieDjidji
