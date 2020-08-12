La spatialisation des données statistiques
===========================================

Le Modifiable Areal Unit Problem
---------------------------------

Même si les données ont une précision métrique, la production d'un savoir géographique nécessite de les relier entre elles à l'aide de régles spatiales, autrement dit de spatialiser les données. La spatialisation constiste à associer à chaque objet une portion, une quantité d'espace bien défini. Cette mise en relation spatiale s'apparente à un *point de vue* que l'on se donne afin de rendre intelligible les distributions spatiales. Ce point de vue opére comme un filtre qui met en valeur certaines propriétés spatiales et en délaisse d'autres. Il en résulte que les analyses géographiques ont donc toujours une part d'arbitraire et sont fonctions de la spatialisation choisie.

La difficulté à définir de façon univoque la concentration d'un ensemble de point illustre les effets de la spatialisation sur les analyses. Intuivement, un ensemble de points est aggloméré lorsque les voisinages autour de ses points se chevauchent. Cette idée a été formalisée dans la fonction de Ripley à l'aide de disque centré sur les points. En fonction de la taille des disques, le même ensemble de points peut apparaître plus ou moins concentré.

Rajouter un graphique

Openshaw a théorisé sous le concept de *Modifiable Areal Unit Problem* la dépendace des analyses à la spatialisation. Le MAUP se décompose en deux effets interdépendants : l’effet de zone et l’effet d’échelle. L'effet de zone exprime la dépendance des résultats statistiques à la forme des mailles territoriales. Dans l'image ci-dessous, en fonction de l'endroit ou passe la frontière les taux de malade sont particulièrement variables. Le redécoupage des zones éléctorales après une éléction afin de maximiser la réélection des acteurs publics est un exemple courant d'effet de zone réalisé volontairement. En anglais, le Gerrymandering désigne cette pratique en référence à l'homme politique américain Elbridge Gerry qui l'a poussée à son paroxysme.

.. figure:: _static/Maup_rate_numbers.png
   :width: 300
   
   Illustration du MAUP. Source : Wikipédia

Dans les analyses statistiques, on peut se prémunir en partie des effets de zone en recourant à des découpages réguliers tels que des carroyages ou bien encore en réalisant des lissages spatiaux. En revanche, on ne peut quasiment rien faire quant aux effets d'échelle - le choix du rayon dans la définition de la concentration d'un ensemble est un effet d'échelle - ils sont inhérents à la prise en compte de l'espace dans les analyses statistiques. Les 4 cartes de densité de la figure ci-dessous témoignent des effets d'échelle sur un indicateur statistique simple : il est impossible de définir une densité dans l'absolu. Néanmoins, ceci ne veut pas dire que la densité évolue n'importe comment en fonction de la taille des unités spatiales. Généralement, la variabilité spatiale des densités augmente avec la finesse de l'échelle d'analyse. Ceci s'explique par le fait qu'aux échelles grossières, les unités spatiales incorporent et moyennisent des zones de densité très variable.   

.. figure:: _static/carte_maup.png
   :width: 600

   Effets d'échelle. Source : RP 2017
   
Jusqu'a récemment, le Maup était considéré comme une limite à la connaissance géographique. Dans le meilleur des cas, les statisticiens et les géographes le *résolvaient*  en recherchant une échelle caractéristique au phénomène étudié ou en utilisant l'échelle d'action des acteurs publics. Cette démarche n'allait pas sans poser de problème :

* Sur quel critére peut-on se baser pour définir une échelle caractéristique optimale ? 
* L'échelle d'action de l'acteur public n'est pas forcément la plus pertinente pour explorer un phénomène spatial (cf en dessous le piége territorial). 

A présent, le MAUP est pensé comme une source d'information sur l'organisation spatiale des distributions étudiées. Plus précisément, la variation des indicateurs à travers les échelles dévoile le caractère multiscalaire des distributions spatiales étudiées. C'est-à-dire que pour comprendre l'organisation d'une distribution spatiale, on doit nécéssairement l'observer à différentes échelles. 

L'erreur écologique
--------------------
Dans son article liminaire sur le MAUP, openshaw relie celui-ci à l'erreur écologique. Cette erreur, bien connu des statisticiens, désigne le fait que l'on ne peut pas déduire à partir de statistiques agrégées (sur des unités spatiales) une connaissance à l'échelle des individus. L'analyse de Durkheim sur la prévalence du suicides selon la confession religieuse à l'échelle des provinces de la Prusse est souvent citée comme un exemple manifeste d'erreur écologique (Daniel Cuurgeau 2000). 


.. figure:: _static/caf_1149-1590_2000_num_60_1_T6_0051_0000_1.png
   :width: 300

   Taux de suicide selon la part de protestants pour les provinces de Prusse (1883-1990). Source : Durkheim tirée de Courgeau 2000. 

La linéarité des taux de suicide en fonction de la part des protestants permet à Durkheim d'extrapoler un taux de suicide pour les protestants. Courgeau 2000 observe cependant que ce taux est quatre fois supérieur à celui calculé directement au niveau des individus. Ceci s'explique intuitivement par le fait que le taux de suicide des protestants et des catholiques dans les provinces de Prusse ne sont pas constants. En particulier, l'organisation sociale varie selon la part plus ou moins importante de catholique et de protestant, de sorte que l'environnement des protestants (sont ils majoritaires ou minoritaires dans leur province) influence leur propention individuelle à se suicider.

Le caractére extrème de cet exemple se rencontre néanmoins rarement dans les analyses statistiques et géographiques usuelles. L'erreur écologique 

les rapports sociaux entre les deux communa

 


Le piége territorial
---------------------

« Il n’est pas question de nier l’importance des facteurs urbains dans le développement des problèmes
sociaux. Mais en centrant les analyses de cette façon on a sans doute hypertrophié la
responsabilité des urbanistes et des architectes dans les difficultés actuelles des " quartiers
". Cette manière de s’exprimer, devenue usuelle, est d’ailleurs révélatrice du déplacement
opéré. Ce sont les quartiers qui posent problème, et plus le chômage, la formation, la
famille, l’intégration. Tout se passe comme si la dégradation des quartiers était posée
comme cause avant d’être examinée comme conséquence » PINÇON et PINÇON-CHARLOT


Erreur écologique (équivalent du MAUP en sociologie)
Piège territorial (Cf. John Agnew, sociologue Pinçon-Charlot et exemple https://www.comeetie.fr/galerie/francepixels/#map/basrevenus/PiYG/11/48.856/2.363)





Projections géographiques et conversion (faire un exemple d’utilisation avec leaflet)
CRS : Coordinate Referential System
