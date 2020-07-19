Quelques concepts théoriques sur la spatialisation des données 
==================================================================

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
