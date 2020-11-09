Les accès aux données géo : quels outils de géocodage ?
=================================================================================================

Pour rappel, le géocodage consiste à attribuer des coordonnées x,y à une adresse.

Pour cela, il existe de nombreux outils et différentes façons de procéder. En voici quelques exemples.


A l'aide de cartes en ligne
------
- de manière unitaire
    - https://www.geoportail.gouv.fr/carte
    - https://www.google.fr/maps
    - https://www.bing.com/maps
    - https://wego.here.com/

- par lot
    - https://mesadresses.ign.fr/
    - https://geoservices.ign.fr/documentation/applications/mon-geocodeur.html

Une fois l'adresse affichée, on peut récupérer ses coordonnées


A l'aide de géocodeurs en ligne
------
- de manière unitaire
    - Etalab [1]_
      
      geocodeur gratuit (documentation: https://geo.api.gouv.fr/adresse)

      exemple: https://api-adresse.data.gouv.fr/search/?q=88+Avenue+Verdier+Montrouge
      
    - IGN
    
      ce géocodeur necessite une cle souscrite auprès de l'IGN (documentation: https://ignf.github.io/look4/latest/jsdoc)

      exemple: https://api.gouv.fr/les-api/api_look4...

    - IGN bis

      ce nouveau géocodeur de l'IGN s'appuie sur la BAN [Base d'Adresse Nationale] (documentation: https://geoservices.ign.fr/documentation/services_betas/geocodage.html)
     
      exemple: https://geocodage.ign.fr/look4/address/search?q=88+Avenue+Verdier+Montrouge

    - Google

      ce geocodeur necessite une clé de licence (documentation: https://developers.google.com/maps/documentation/geocoding/start?hl=fr)

      exemple: https://maps.googleapis.com/maps/api/geocode/json?address=188+Avenue+Verdier,+Montrouge,+FR&key=YOUR_API_KEY

    - Open Street Map
      
      geocodeur gratuit (documentation: https://wiki.openstreetmap.org/wiki/FR:Nominatim)

      exemple: https://nominatim.openstreetmap.org/search?q=188%20Avenue%20Verdier%20,Montrouge&format=json

- par lot
    - Etalab 
    
      https://adresse.data.gouv.fr/csv
      
    - de nombreux acteurs privés (et payants) : Esri, Mapbox, Bing...

A l'aide d'une application
------
- A l'Insee, c'est l'application Geoloc qui remplit ce rôle et géocode les adresses venant de nombreuses sources externes (CNAF, CNAV, CAF, Pôle Emploi...) ou internes (BPE, Sirene, Filosofi...). Le projet Gaïa en cours porte en partie sur ce sujet également.
- l'IGN propose une application appelée "Mon géocodeur" (anciennement "visualiseur d'adresses")
- D'autres acteurs privés proposent des applications de géocodage (MapInfo Géocodage, Geoconcept, ArcMap...) 

Plus d'informations sur le geocodage
------
- vous aurez sans doute lu dans les différentes documentations des références à différentes fonctionnalités liées au géocodage : le `geocodage inversé`_ et l'`autocomplétion`_ (avec un très bon exemple)
- vous pourrez trouver d'avantage d'informations sur le site https://makina-corpus.com/blog/metier/2019/les-logiciels-et-api-pour-geocoder


.. [1] Etalab est un département de la direction interministérielle du numérique. Il développe et maintient le portail des données ouvertes du gouvernement français data.gouv.fr

.. _geocodage inversé: https://fr.wikipedia.org/wiki/G%C3%A9ocodage_invers%C3%A9

.. _autocomplétion: https://adrien.poupa.fr/autocompletion-des-adresses-avec-la-base-adresse-nationale/



