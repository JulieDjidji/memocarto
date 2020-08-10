Discussion des règles de sémiologie cartographique 
===================================================

Une carte thématique a vocation à représenter l'organisation spatiale d'une quantité déterminée. Deux types de cartes (en dehors des cartes de flux) sont principalement utilisés : les cartes en aplat de couleur et les ronds. Les premières servent à cartographier des ratios et les secondes des volumes (la surface des ronds est proportionnelle à la variable d'intérêt). Ces régles immuables que d'aucuns considérent comme des conventions trouvent leur justification dans la manière dont on envisage la spatialisation des données étudiées. 

Les cartes choroplèthes (aplats de couleur)
--------------------------------------------

La carte de densité est la carte de taux la plus simple, le dénominateur est la surface des unités spatiales considérées. L'unité de la légende est une population par unité de surface. Sur la figure ci-dessous a été représentée la densité de population communale autour de Paris. L'intensité du dégradé de couleur est croissant avec la densité.
 
.. figure:: _static/carte_densite.png
   :width: 300
Densité de population autour de Paris. Souce :  RP 2017

Construire une carte de densité revient implicitement à postuler que la population est répartie uniformément dans les unités spatiales. Cette idée a été schématisée sur la figure ci-dessous à l'aide de cartes à point. Chaque point bleu représente 100 personnes. Lorsque la densité au sein d'une unité spatiale est forte, les points ont tendance à occuper l'ensemble de son espace. Au contraire, pour les unités spatiales de faible densité, la population est dispersée et semble disparaître dans l'immensité du vide apparent. Ce simple procédé crée un dégradé bleu qui oppose les zones denses aux zones peu denses (**par commune**). Les trois autres cartes **par département**, **par commune focus sur Paris** et **par carreau focus sur Paris** illustrent le *Modifiable Areal Unit Problem*. La répartition de la population change drastiquement en fonction de la taille des unités spatiales considérés. A l'échelle des départements, la variabilité communale est masquée. Il est en de même à l'échelle des communes qui masque totalement la répartition fine de la population contenue dans les carreaux de 200 m.


.. figure:: _static/densite.png
   :width: 600

.. figure:: _static/carte_taux.png
   :width: 600


Chaque point représente 100 personnes

.. figure:: _static/taux.png
   :width: 600

Carte de taux. Chaque point représente 50 ménages : en rouge, les ménages pauvres et en vert les ménages non pauvres

.. figure:: _static/carte_rond.png
   :width: 600


.. figure:: _static/rond.png
   :width: 600

Carte de taux des ménages pauvres un point représente 1000 personnes



