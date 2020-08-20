.. carto documentation master file, created by
   sphinx-quickstart on Fri Jul 17 11:01:39 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sensibilisation à la cartographie
=================================

Description
---------------------

Il est courant pour les statisticiens et les datascientists de vouloir représenter  sous forme de cartes les valeurs de leurs indicateurs. Pourtant, l'acte de cartographier des abstractions que sont des populations ou des taux de prévalence est tout sauf naturel et s'apparente même à une révolution silencieuse. Les cartes topographiques nécessitent un haut degré d'abstraction. Mais contrairement, aux cartes thématiques, elles représentent encore des objets physiques (fleuves, montagnes) qui ont une existence propre.

   

.. figure:: _static/Carte_figurative_de_l'instruction_populaire_de_la_France.jpg
   :width: 600
   
   Carte figurative de l'instruction populaire de la France, 1826, Dupin (Plus le dégradé est foncé et plus faible est la part d'enfants scolarisés). Malte-Brun désignait cette carte sous le nom de *carte de la France obscure et de la France éclairée*. On constate à travers cet exemple, à quel point, les choix sémiologiques sont susceptibles de véhiculer des jugements normatifs. 

Avec sa *Carte figurative de l'instruction populaire de la France* en 1826, Charles Dupin, baron de son état, a ouvert la voie aux méthodes standard de représentation  des données statistiques que l'on utilise encore aujourd'hui. L'apport majeur de celui-ci est d'avoir inventé un langage graphique pour restituer la variation d'un phénomène quantifiable (dans cet exemple, un dégradé sert à quantifier la part des enfants scolarisés). Ce langage joue implicitement plusieurs rôles :

- Spatialiser les données statistiques : soit associer aux phénomènes quantifiables une part plus ou moins importante d'espace ;
- Représenter sous une forme graphique des phénomènes quantifiables complexes.

Ces deux points à l'interface de la géographie, de la sémiologie, de la statistique, voire de l'esthétique doivent toujours questionner les statisticiens qui s'aventurent à réaliser des cartes. Toute carte thématique est en effet un artefact géographique qui nécessite d'être bien réfléchie pour ne pas prêter le flanc à de mauvaises interprétations. C'est l'objectif de la première partie de ce site que de fournir rapidement des éléments de réponse sur ces points.

.. toctree::
  :maxdepth: 1
  :caption: Mémento
  
  Les fondements de la sémiologie cartographique <semio> 
  On commence par quelques concepts théoriques sur la spatialisation des données <concepts>


La carte de Dupin doit son succès à l'usage de la lithographie, qui permet de publier des cartes à un coût moindre  par rapport à la gravure sur Bois (Palsky 1996). Dupin avait fait appel au service de Jobard, artiste-litographe fameux pour obtenir les résultats escomptés. A présent, la diffusion des cartes est massivement numérique. La programmation a ainsi remplacé la lithographie. La deuxième partie de ce site à vocation à vous présenter les éléments de programmation et d'architecture informatique nécessaires à la publication de cartes en ligne. 

.. toctree::
  :maxdepth: 1
  :caption:  Gérer son SIG
  
  Tour d'horizon des acteurs <acteurs>
  Les accès aux données géo : quels APIs de géocodage ? <api>
  Postgis <postgis>
  Geoserver <geoserver>

















.. Les applications de cartographie en ligne ont transformé notre quotidien : calcul d’itinéraire, recherche de lieux, d’équipements, de magasin, tout ceci est dorénavant possible sur la grande majorité des téléphones portables. Cette lame de fond se retrouve également dans nos activités professionnelles de DataScientist. Les logiciels de traitement de l’information modernes gèrent la géographie à travers une colonne qui décrit la géométrie associée aux unités statistiques. Il n’a jamais été aussi simple de représenter sous la forme de cartes les indicateurs socio-économiques.

.. A reprendre ce paragraphe : La représentation d'une données géo consiste à spatialiser l'information puis seulement à produire une carte abstraction qui représente le territoire qui est une simplification. 

.. La spatialisation des données statistiques consiste à affecter à chaque élément d’un ensemble d’intérêt une portion plus ou moins grande d’espace. Cette opération n’est pas naturelle et est une construction géographique, qui n’existe pas en dehors d’un certain consensus social. La taille et la forme des unités spatiales que l’on associe aux objets étudiés déterminent un point de vue qui conditionne les résultats des analyses. Loin d’être anecdotique, ce phénomène se traduit par le fait que les corrélations calculées sur des unités spatiales varient voire changent de signe selon l’échelle d’analyse (Modifiable Areal Unit Problem). 

.. La simplicité avec laquelle on peut mettre à présent à disposition des données spatiales et les difficultés théoriques inhérents à la spatialisation des données statistiques sont susceptibles de favoriser la diffusion de représentations erronées voire biaisées involontairement. Notre ambition à travers ce site est de questionner la spatialisation des données et d’exposer les opérations géographiques permettant de mettre à disposition du grand public des données géographiques afin de favoriser la dissémination d’analyses pertinentes.

Comme tout site digne de ce nom, nous proposons une partie tutorielle pour vous accompagner dans la manipulation des données cartographiques.


  


.. toctree::
  :maxdepth: 1
  :caption: On s'exerce !
  
  Mini présentation de GeoPandas <geopandas>
  Galerie d'exemples <gallery/index>
  
.. toctree::
  :maxdepth: 1
  :caption: Contributeurs

   Contributeurs <contributors>

Nous contacter
---------------------

- Reporter des bugs, suggérer des ajouts ou du code sur `GitHub`_.

.. _GitHub: https://github.com/JulieDjidji
