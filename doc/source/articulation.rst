Comment toutes ces technologies s'articulent-elles?
===================================================

Parcequ'un schéma vaut mieux qu'un long discours 
------



Un implémentation partielle de ce schéma 
------
exemple de mini-application web qui :
  - affiche des informations cartographiques dans un navigateur
  - utilise leaflet
  - se connecte à OpenStreetMap
  - fait appel à un Geoserver (qui lui-même fait appel à une base de données ou à un entrepôt de fichier) pour afficher :
  
    - une couche image (appel en WMS)
    - une couche vectorielle (appel en WFS)

`application sous codepen.io`_

Vous pouvez faire des modifications directement dans le code ou dupliquer le code sur un projet à vous (codepen.io ou jsfiddle.net par exemple) pour pouvoir enregistrer vos modifications


:: _application sous codepen.io: https://codepen.io/fabcg/pen/wvWGQdW



