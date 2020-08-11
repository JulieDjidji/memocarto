La spatialisation des données statistiques
===========================================

Lorsque l'on réalise une carte thématique, on affecte implicitement à chaque unité statistique (ménages, individus, entreprise) une portion d'espace. Dans le cas des cartes de densité, on suppose que la population est répartie uniformément au sein des unités spatiales, chaque individus se voit attribuer la même quantité d'espace. Une carte de densité, comme toute carte thématique repose sur une modélisation sous-jacente du phénomène étudié. 

Cette remarque reste vérifiée pour toutes les analyses géographiques. Même si les données ont une précision métrique, la production d'un savoir géographique nécessite de les relier entre elles à l'aide de régles spatiales. Cette mise en relation spatiale s'apparente à un point de vue que l'on se donne afin de rendre intelligible les distributions spatiales. Ce point de vue opére comme un filtre qui met en valeur certaines propriétés spatiales et en délaisse d'autres. Il en résulte que les analyses géographiques ont donc toujours une part d'arbitraire et sont fonctions de la spatialisation choisie.

La difficulté à définir de façon univoque la concentration d'un ensemble de point illustre les effets de la spatialisation sur les analyses. Intuivement, un ensemble de points est aggloméré lorsque les voisinages autour de ses points se chevauchent. Cette idée a été formalisée dans la fonction de Ripley à l'aide de disque centré sur les points. En fonction de la taille des disques, le même ensemble de points peut apparaître plus ou moins concentré.

Rajouter un graphique

Openshaw a théorisé sous le concept de *Modifiable Areal Unit Problem* la dépendace des analyses à la spatialisation. Le MAUP se décompose en deux effets interdépendants : l’effet de zone et l’effet d’échelle. L'effet de zone exprime la dépendance des résultats statistiques à la forme des mailles territoriales. Dans l'image ci-dessous, en fonction de l'endroit ou passe la frontière les taux de malade sont particulièrement variables. Le redécoupage des zones éléctorales après une éléction afin de maximiser la réélection des acteurs publics est un exemple courant d'effet de zone réalisé volontairement. En anglais, le Gerrymandering désigne cette pratique en référence à l'homme politique américain Elbridge Gerry qui l'a poussée à son paroxysme.

.. figure:: _static/Maup_rate_numbers.png
   :width: 300
   
   Illustration du MAUP. Source : Wikipédia

Dans les analyses statistiques, on peut se prémunir en partie des effets de zone en recourant à des découpages réguliers tels que des carroyages ou bien encore en réalisant des lissages spatiaux. En revanche, on ne peut quasiment rien faire quant aux effets d'échelle, ils sont inhérents à la prise en compte de l'espace dans les analyses statistiques.



L'effet d'échelle 





.. figure:: _static/Maup_rate_numbers.png
   :width: 600
   
   En fonction du choix des frontières des zones le taux de malade par zone change drastiquement (Wikipedia)
   
Le choix d'unité spatiale régulière telle que des carreaux ou la pratique du lissage limite l'arbitraire lié à la 

Maup (espace le plus dense en France : région, département, commune, carreau et zoom sur les carreaux d’une commune pour montrer une très forte hétérogénéité de la densité pop au sein d’une commune
Erreur écologique (équivalent du MAUP en sociologie)
Piège territorial (Cf. John Agnew, sociologue Pinçon-Charlot et exemple https://www.comeetie.fr/galerie/francepixels/#map/basrevenus/PiYG/11/48.856/2.363)

L’impact de la discrétisation sur la représentation des densités de population
Eviter une discrétisation linéaire selon la variable ou passage en log
Loi de Zipf ou loi rang/taille http://geoconfluences.ens-lyon.fr/glossaire/zipf-loi-ou-regle-de

NB à bien garder en mémoire "Définition" ville : 100 habitants/km2 

La donnée géographique - construire des données géo par exemple.
Format de données géo : raster et vecteur (points, lignes et polygones) 
Unités spatiales (polygones): 
découpage administratif
Intérêt du carroyage : s’affranchir des unités spatiales administratives qui peuvent fortement dépendantes de choix politiques (Gerrymandering)
Quadtree : adaptation de la granularité de la grille en fonction des données cartographiées - éviter une réplication de l’information dans des carreaux voisins similaires et homogènes tout en gardant le maximum d’informations dans d’autres carreaux très hétérogènes
Autre intérêt du Quadtree : confidentialité pour le carroyage - agrégation de carreaux où l’identification serait possible

Projections géographiques et conversion (faire un exemple d’utilisation avec leaflet)
CRS : Coordinate Referential System
