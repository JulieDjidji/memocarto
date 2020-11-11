PostGIS
======

Présentation
------
PostGIS est l'extension spatiale de PostgreSQL. Elle permet de manipuler des objets géographiques grâce à des géométries (points, lignes, polygones...), la géométrie étant alors un type à part entière et non une simple succession de coordonnées. Ce type est alors manipulable au même titre que les autres, avec lequel il est possible de réaliser un grand nombre d'opérations.
PostGIS est à PostgreSQL ce que Oracle spatial est à Oracle.

Quelques exemples d'opération courantes
------
- conaitre le système de projection de chaque enregistrement de la colonne geom (le nom par défaut de la colonne contenant la géométrie)
SELECT ST_SRID(geom) from [tablename];

- connaître le type d'une géométrie
SELECT GeometryType(geom) FROM [tablename] WHERE ... ;

- créer une enveloppe autour d'une géométrie (un rectangle au plus près de la géométrie)
SELECT ST_ENVELOPPE(geom) FROM [tablename] WHERE ... ;;

- créer un polygone à partir de coordonnées
SELECT ST_Polygon('LINESTRING(75 29, 77 29, 77 29, 75 29)'::geometry, 4326);

- afficher le contenu d'une géométrie au format texte
SELECT ST_AsText(geom) FROM [tablename] WHERE ... ;

- afficher les données de la table dont les géométries ne sont pas valides avec la raison pour laquelle elles ne le sont pas
SELECT *, ST_IsValidReason(geom)
FROM [tablename]
WHERE not ST_IsValid(geom); 

- convertir le système de projection (ici en Lambert93)
SELECT ST_TRANSFORM(geom, 2154) FROM [tablename]  WHERE ... ;

- conaître la superficie d'une géométrie (polygone par exemple)
SELECT ST_AREA(geom) FROM [tablename] WHERE ... ;
Attention, la superficie sera retournée dans la même unité que même système de projection que la géométrie. Evitez donc le 4326.

- connaître le périmètre d'une géométrie;
SELECT ST_Perimeter(geom) FROM [tablename] WHERE ... ;

- savoir si 2 géométries ont une intersection
SELECT ST_INTERSECTS(a.geom,b.geom)
FROM [tablename1] a, [tablename2] b
WHERE ... ;

- savoir si 2 géométries se touchent
SELECT ST_TOUCHES(a.geom,b.geom)
FROM [tablename1] a, [tablename2] b
WHERE ... ;

- indexer la colonne géométrique (rend les requêtes topologiques incroyablement rapides)
CREATE INDEX [indexname] ON [tablename] USING GIST (geom);


Un tutoriel pour débuter avec PostGIS
------
https://www.sigterritoires.fr/index.php/debuter-avec-postgresql-postgis-introduction-a-pgadmin4/

Le site de référence
------
http://postgis.net avec la documentation de la dernière version http://postgis.net/docs/manual-dev/postgis-fr.html
