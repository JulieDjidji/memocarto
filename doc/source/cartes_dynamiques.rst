D'autres façons de diffuser l'nformation cartographique
=========================================

L'utilisation de Geoserver et de Postgis permet de contrôler et d'internaliser l'ensemble de la chaine de diffusion d'une information cartographique. Ceci est avantageux car vous maitrisez votre domaine, en contrepartie cette approche nécessite de configurer des serveurs et un investissement technique plus important. Des opérateurs tels que Mapbox vous permettent d'héberger vos données. Ces services deviennent payant en fonction de votre usage et de la consultation des vos données. Pour des preuves de concept, la version gratuite est généralement suffisante. 

`130 ans de variation de population <https://fsemecurbe.github.io/>`_ : Dans cette application, le fond de carte est hébergé sur Mapbox. La variation de population est calculée pour un pas quinquennal. Lorsque l'on change l'année, on observe que la carte est actualisée par grands   
carreaux, des `tuiles spatiales <https://en.wikipedia.org/wiki/Vector_tiles>`_. Cette approche est très pertinente pour stocker une information spatiale plus ou moins précise selon les échelles d'observation. Le code de cet exemple peut être consulté `ici <https://raw.githubusercontent.com/fsemecurbe/fsemecurbe.github.io/main/index.html>`_.

Dans cette dernière `application  <https://gridinshape.herokuapp.com/>` , l'information géographique est directement stockée dans un server postgis. Une requête spatiale permet de sélectionner les carreaux intersectants les territoires proposés par l'utilisateur. Le code source de l'application  est consultable `ici <https://raw.githubusercontent.com/fsemecurbe/app_gridinshape/main/app.py>`_ .   
