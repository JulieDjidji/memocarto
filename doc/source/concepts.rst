La spatialisation des données statistiques
===========================================

Lorsque l'on réalise une carte thématique, on affecte implicitement à chaque unité statistique (ménages, individus, entreprise) une portion d'espace. Dans le cas des cartes de densité, on suppose que la population est répartie uniformément au sein des unités spatiales. Une carte de densité, comme toute carte thématique repose sur une modélisation sous-jacente du phénomène étudié. 

Cette remarque reste vérifiée pour toutes les analyses géographiques. Même si les données ont une précision métrique, la production d'un savoir géographique nécessite de les relier entre elles à l'aide de régles spatiales. Cette mise en relation spatiale s'apparente à un point de vue que l'on se donne afin de rendre intelligible les distributions spatiales. Ce point de vue opére comme un filtre qui met en valeur certaines propriétés spatiales et en délaisse d'autres. De sorte que toute analyse géographique est partielle et dans une certaine mesure arbitraire. Il en résulte que les analyses géographiques sont donc toujours tributaires du point de vue choisi.







Ce fait a été théorisé par Openshaw   


Par exemple, les méthodes d'analyses spatiales modernes basées sur la fonction de Ripley 




recquiert recquiert 

 que l'on se donne pour comprendre le positionnement relatif des objets contenu dans une distribution spatiale.
La localisation des objets peut-être 
L'émergence des données géoréférencées de précision métrique n'a pas transformé l. En effet, toute analyse géographique d'une données  



La dépendance des résultats statistique aux choix des unités spatiales a été théorisée par Openshaw sous le concept de Modifiable Areal Unit Problem. Le MAUP résulte du fait que les objets mesurés par les statistiques n’ont pas d’emprise spatiale définie a priori. Par exemple, les tâches urbaines qui déterminent l’emprise spatiale des villes sont des artefacts géographiques. Même si les contours des bâtiments sont bien définis, cette information n’est pas suffisante pour construire une tâche urbaine. La continuité du bâti est assurée par une zone tampon dont l’épaisseur est choisie par le géomaticien. Selon la taille des zones tampons, l'emprise spatiale des villes fluctuent.

Le MAUP se décompose en deux effets interdépendants : l’effet de zone et l’effet d’échelle. L'effet de zone exprime la dépendance des résultats statistiques à la forme des mailles territoriales. Dans l'image ci-dessous, en fonction de l'endroit ou passe la frontière les taux de malade sont particulièrement variable. Le redécoupage des zones éléctorales après une éléction afin de maximiser la réélection des acteurs publics est un exemple courant d'effet de zone réalisé volontairement. En anglais, le Gerrymandering désigne cette pratique en référence à l'homme politique américain Elbridge Gerry qui l'a poussée à son paroxysme.

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
