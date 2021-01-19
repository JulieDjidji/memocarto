Cartes statiques
====================

.. figure:: _static/carte_finale.png
   :width: 600
   
   Densité de Population en France métropolitaine en 2020. Source : Insee
   

Une carte thématique est un ensemble d'éléments assemblés les uns aux dessus des autres. Le premier est le fond de carte portant l'information statistique, le second la légende qui permet de comprendre la carte et enfin les sources qui garantissent l'attribution des données. A ce triptyque primaire, on peut rajouter des informations supplémentaires apportées par des couches spécifiques. Dans notre exemple, on a rajouté une couche des régions françaises ainsi qu'un fond OpenStreetMap afin d'apporter un contexte spatial. L'ordre d'apparition des fonds conditionne leur visibilité.


Un peu de discrétisation
-------------------------

La discrétisation est une étape indispensable pour transformer une variable continue en une carte thématique de type aplat de couleur. Cette opération est tout sauf neutre et engage le cartographe. Sur les deux cartes suivantes sont représentées les deux méthode de discrétisation le splus utilisées :  quantiles et Jenks.


.. figure:: _static/carte_finale_quantiles.png
   :width: 200
   
   Discrétisation Quantile

.. figure:: _static/carte_finale_jenks.png
   :width: 200
   
   Discrétisation Jenks

La discrétisation quantile est ultra rapide même employée sur de très gros fonds de carte. En revanche, elle a un énorme défaut, elle tend à produire de trop belles cartes. Comprenez par là que les cartes sont automatiquement équilibrées par construction, il y le même nombre d'unités spatiales dans chaque classe. Certains statisticiens ne jurent que par elle et ne peuvent plus s'en passer, ce qui représente un vrai sujet de santé statistique. On constate dans notre exemple que les tailles des classes sont relativement homogéne, ce qui a pour conséquence une invisibilisation des valeurs extrèmes observées dans les départements contenant une métropole.

La discrétisation de Jenks est très lente (pour les gros fonds de carte) et consiste à chercher les bornes qui garantissent l'homogénéité au sein des classe et l'hétérogénité maximale entre les classes. Certains logiciels proposent de prendre un échantillon de la variable analysée pour gagner en temps de calcul. En théorie, c'est la discrétisation la plus à même de restituer la répartition d'une variable à cartographier. En pratique le résultat est parfois décevant. Dans notre cas, le département de Paris écrase totalement la discrétisation. 



