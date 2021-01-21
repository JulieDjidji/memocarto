Les opérations géographiques
=============================

Les opérations géographiques sont principalement des opérations géométriques. Un calcul géomatique consiste généralement en l'enchainement de plusieurs de ces opérations.

La première opération que nous allons décrire est le buffer qui consiste à créer un tampon autour d'un object. Cette opération est utilisée pour créer une tache urbaine ou pour rechercher les carreaux innondables (à moins de 5 km d'un fleuve par exemple). 
Dans ce dernier cas, on procéde en deux étapes, on calcule un buffer de 5 km autour des fleuves puis on réalise un merge spatiale de cette nouvelle couche avec les carreaux.

