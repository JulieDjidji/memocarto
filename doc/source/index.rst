.. carto documentation master file, created by
   sphinx-quickstart on Fri Jul 17 11:01:39 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Les territoires de la cartographie
=================================

Les progrès de l’informatique ont décuplé la capacité des acteurs publics et privés à diffuser des cartes statistiques. Il n’a jamais été aussi simple de produire et de communiquer une information statistique à l’aide d’une carte. Ce constat est néanmoins à tempérer, car la cartographie statistique reste toujours une pratique d’initiés. Pour le profane, la cartographie ressemble à une nébuleuse inextricable composée de concepts jargonant. Ce site vise à vous familiariser avec les notions de la cartographie et à vous présenter les principales solutions techniques utilisées actuellement. Il ne se veut pas une présentation exhaustive mais plutôt une entrée matière afin de démythifier la cartographie.

Réaliser et mettre en valeur une carte statistique ne sert pas (ou ne devrait plutôt jamais servir) à rajouter de la couleur dans une publication ou à dynamiser une page web. Une carte statistique n’est pas non plus une illustration d’un tableau. Une carte est une matérialisation du rôle de l’espace dans la genèse des comportements humains. L’espace intervient à la fois comme support matériel facilitant ou limitant les interactions entre les hommes mais aussi comme représentation des rapports sociaux. Par exemple, le couple centre-ville/périphérie est un découpage territorial mais aussi une grille de lecture avec ses préjugés et ses sous-entendus. De sorte qu’une carte statistique lorsqu’elle est bien réalisée est structurée et reflète des lois géographiques.

- Friction de la distance : des éléments proches ont davantage de chance d’être en relation
(concentrations et dispersions considérées en tant que processus) ou d'être similaires (concentrations
et dispersions considérées en tant qu'états) que des éléments éloignés car la friction de la distance
atténue l'influence mutuelle des phénomènes au fur et à mesure.

- Rôle de l'appartenance à un même milieu : des éléments d’un même milieu ont davantage
de chances d'être en relation (ou de se ressembler) que des éléments de milieux différents. Un même
milieu peut être autant une même maille administrative (commune, région...), une même nation, les
mêmes conditions climatiques, une même langue, un même groupe social...

- Influence de la taille des entités considérées : des entités de grande taille, ayant une large
emprise spatiale ou contenant une quantité importante d'individus, d'activités, d'information..., ont
davantage d'influence sur les éléments de leur environnement que des entités de petite taille.

- Dépendance d'échelles : pour un type donné d'implantations humaines, l'existence d'un
processus de concentration considérant un certain voisinage implique un processus de dispersion
considérant un voisinage plus large (ou plus retreint).

- Dépendance dans le temps : chaque phénomène influence sa propre variation dans le temps
(cf. Figure 1). Cette loi introduit l'explication « historique » des concentrations et dispersions
considérées en tant qu'états (Tobler 1979) ainsi que la dépendance à la trajectoire (path dependency)
dans la simulation des processus de concentration et de dispersion.




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
  :caption: Introduction
  
  Pourqoui faire des cartes <pourquoi>
  Tour d'horizon des acteurs <acteurs>



.. toctree::
  :maxdepth: 1
  :caption: Stockage des données spatiales
  
  Les fichiers cartographiques  <fichiers_geo>
  Les bases de données spatiales Postgis <postgis>
  
 
  
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




La carte de Dupin doit son succès à l'usage de la lithographie, qui permet de publier des cartes à un coût moindre  par rapport à la gravure sur Bois (Palsky 1996). Dupin avait fait appel au service de Jobard, artiste-litographe fameux pour obtenir les résultats escomptés. A présent, la diffusion des cartes est massivement numérique. La programmation a ainsi remplacé la lithographie. La deuxième partie de ce site à vocation à vous présenter les éléments de programmation et d'architecture informatique nécessaires à la publication de cartes en ligne. 


.. toctree::
  :maxdepth: 1
  :caption:  Autour de la manipulation d'informations géographiques  

  
  QGis <qgis>
  
  Geoserver <geoserver>
  Leaflet <leaflet>
  Comment tout cela s'articule-t-il? <articulation>
  Un exemple d'implémentation <implementation>
  



Comme tout site digne de ce nom, nous proposons une partie tutorielle pour vous accompagner dans la manipulation des données cartographiques.


  


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
