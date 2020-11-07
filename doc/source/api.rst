Les accès aux données géo : quels APIs de géocodage ?
=================================================================================================

Pour rappel, le géocodage consiste à attribuer des coordonnées x,y à une adresse.

Pour cela, il existe de nombreux outils et différentes façons de procéder.


A l'aide d'une carte
------
- de manière unitaire
    - https://www.geoportail.gouv.fr/carte
    - https://www.google.fr/maps

- par lot
    - https://mesadresses.ign.fr/
    - https://geoservices.ign.fr/documentation/applications/mon-geocodeur.html


A l'aide d'un géocodeur
------
- de manière unitaire
    - Etalab
      geocodeur gratuit (documentation: https://geo.api.gouv.fr/adresse)
      exemple: https://api-adresse.data.gouv.fr/search/?q=88+Avenue+Verdier+Montrouge
    - IGN
      ce géocodeur necessite une cle souscrite auprès de l'IGN (documentation: https://ignf.github.io/look4/latest/jsdoc)
      exemple: https://api.gouv.fr/les-api/api_look4...
    - IGN
      ce nouveau géocodeur de l'IGN s'appuie sur la BAN (documentation: https://geoservices.ign.fr/documentation/services_betas/geocodage.html)
      exemple: https://geocodage.ign.fr/look4/address/search?q= 88+Avenue+Verdier+Montrouge
    - Google
      ce geocodeur necessite une clé de licence (documentation: https://developers.google.com/maps/documentation/geocoding/start?hl=fr)
      exemple: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

- par lot
    - Etalab 
      https://adresse.data.gouv.fr/csv


A l'aide d'une application
------
- A l'Insee, c'est l'application Geoloc qui remplit ce rôle. Le projet Gaïa est en cours en partie sur ce sujet également.
- l'IGN propose une application appelée "Mon géocodeur" (anciennement "visualiseur d'adresses")

