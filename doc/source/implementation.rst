Un exemple d'implémentation partielle du schéma précédent 
------

Vous trouverez un exemple de mini-application web disponible ici :

`application sous codepen`_


Cette application :
  - utilise leaflet pour afficher des informations cartographiques dans un navigateur
  - récupère des fonds de carte sur les serveurs d'OpenStreetMap
  - fait appel à un Geoserver (qui lui-même fait appel à une base de données ou à un entrepôt de fichier) pour afficher :
  
    - une couche image (appel en WMS)
    - une couche vectorielle (appel en WFS)
    
  - fait appel à un geocodeur (celui de l'IGN basé sur la BAN) 

Vous avez accès aux 3 composantes du code (html, css, et javascript) que vous pouvez manipuler à loisir. Vous pouvez également dupliquer le code sur un projet à vous ou, par exemple, sous codepen.io ou jsfiddle.net en vous créant un compte. Vous pourrez ainsi enregistrer vos modifications. 

Le geoserver est en revanche mis à disposition par GéoBretagne, une plate-forme issue d'une démarche partenariale mise en place par la Préfecture de la région Bretagne et la Région Bretagne. Sa configuration et ses sources de données ne nous/vous sont donc pas accessibles.



.. _application sous codepen: https://codepen.io/fabcg/pen/wvWGQdW
