La spatialisation des données statistiques
===========================================

Le Modifiable Areal Unit Problem
---------------------------------

Même si les données ont une précision métrique, la production d'un savoir géographique nécessite de les relier entre elles à l'aide de règles spatiales, autrement dit de spatialiser les données. La spatialisation consiste à associer à chaque objet une portion, une quantité d'espace bien défini. Cette mise en relation spatiale s'apparente à un *point de vue* que l'on se donne afin de rendre intelligible les distributions spatiales. Ce point de vue opère comme un filtre qui met en valeur certaines propriétés spatiales et en délaisse d'autres. Il en résulte que les analyses géographiques ont donc toujours une part d'arbitraire et sont fonction de la spatialisation choisie.

.. La difficulté à définir de façon univoque la concentration d'un ensemble de points illustre les effets de la spatialisation sur les analyses. Intuivement, un ensemble de points est aggloméré lorsque les voisinages autour de ses points se chevauchent. Cette idée a été formalisée dans la fonction de Ripley à l'aide de disque centré sur les points. En fonction de la taille des disques, le même ensemble de points peut apparaître plus ou moins concentré.

Openshaw a théorisé sous le concept de *Modifiable Areal Unit Problem* la dépendance des analyses à la spatialisation. Le MAUP se décompose en deux effets interdépendants : l’effet de zone et l’effet d’échelle. L'effet de zone exprime la dépendance des résultats statistiques à la forme des mailles territoriales. Dans l'image ci-dessous, en fonction de l'endroit où passe la frontière les taux de malade sont particulièrement variables. Le redécoupage des zones électorales après une élection afin de maximiser la réélection des acteurs publics est un exemple courant d'effet de zone réalisé volontairement. En anglais, le Gerrymandering désigne cette pratique en référence à l'homme politique américain Elbridge Gerry qui l'a poussée à son paroxysme.

.. figure:: _static/Maup_rate_numbers.png
   :width: 300
   
   Illustration du MAUP. Source : Wikipédia
