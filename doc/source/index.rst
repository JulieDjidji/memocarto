.. carto documentation master file, created by
   sphinx-quickstart on Fri Jul 17 11:01:39 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sensibilisation à la cartographie
=================================

Description
---------------------

Les applications de cartographie en ligne ont transformé notre quotidien : calcul d’itinéraire, recherche de lieux, d’équipements, de magasin, tout ceci est dorénavant possible sur la grande majorité des téléphones portables. Cette lame de fond se retrouve également dans nos activités professionnelles de DataScientist. Les logiciels de traitement de l’information modernes gèrent la géographie à travers une colonne qui décrit la géométrie associée aux unités statistiques. Il n’a jamais été aussi simple de représenter sous la forme de cartes les indicateurs socio-économiques.

A reprendre ce paragraphe : La représentation d'une données géo consiste à spatialiser l'information puis seulement à produire une carte abstraction qui représente le territoire qui est une simplification. 

La spatialisation des données statistiques consiste à affecter à chaque élément d’un ensemble d’intérêt une portion plus ou moins grande d’espace. Cette opération n’est pas naturelle et est une construction géographique, qui n’existe pas en dehors d’un certain consensus social. La taille et la forme des unités spatiales que l’on associe aux objets étudiés déterminent un point de vue qui conditionne les résultats des analyses. Loin d’être anecdotique, ce phénomène se traduit par le fait que les corrélations calculées sur des unités spatiales varient voire changent de signe selon l’échelle d’analyse (Modifiable Areal Unit Problem). 

La simplicité avec laquelle on peut mettre à présent à disposition des données spatiales et les difficultés théoriques inhérents à la spatialisation des données statistiques sont susceptibles de favoriser la diffusion de représentations erronées voire biaisées involontairement. Notre ambition à travers ce site est de questionner la spatialisation des données et d’exposer les opérations géographiques permettant de mettre à disposition du grand public des données géographiques afin de favoriser la dissémination d’analyses pertinentes.

Ce site n’a pas vocation a être exhaustif. Nous renvoyons autant que faire se peut à des documents déjà réalisés.


.. toctree::
  :maxdepth: 1
  :caption: Mémento
  
  Les fondements de la sémiologie cartographique <semio> 
  On commence par quelques concepts théoriques sur la spatialisation des données <concepts>
  
.. toctree::
  :maxdepth: 1
  :caption:  Gérer son SIG
  
  Tour d'horizon des acteurs <acteurs>
  Les accès aux données géo : quels APIs de géocodage ? <api>
  Postgis <postgis>
  Geoserver <geoserver>

.. toctree::
  :maxdepth: 1
  :caption: On s'exerce !
  
  Mini présentation de GeoPandas <geopandas>
  Galerie d'exemples <gallery/index>

Nous contacter
---------------------

- Reporter des bugs, suggérer des ajouts ou du code sur `GitHub`_.

.. _GitHub: https://github.com/JulieDjidji
