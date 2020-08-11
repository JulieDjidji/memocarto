Postgis
=================================================================================================

On commence par se connecter à la base de données Postgis (ici defaultdb).

.. sourcecode:: python

    >>> user=os.getenv('db_user')
    >>> password=os.getenv('db_password')
    >>> host=os.getenv('db_host')

    >>> engine = create_engine('postgresql+psycopg2://'+user+':'+password+'@'+host+'/defaultdb')

On importe les données relatives aux communes de France puis celles des arrondissements pour les villes de Paris, Lyon et Marseille. Puis, on charge ces données dans Postgis.

.. sourcecode:: python

    >>> communes = gpd.read_file(os.getenv("URL_GEOJSON_COMMUNES"))
    >>> communes.to_postgis(name="commune", con=engine)

    >>> armf = gpd.read_file(os.getenv("URL_GEOJSON_ARMF")
    >>> armf.to_postgis(name="armf2", con=engine)

On peut récupérer les données relatives aux communes. Attention, la variable de géométrie recherchée par défaut est 'geom'. Si elle porte un nom différent, il est nécessaire d'indiquer son nom dans le paramètre geom_col.

.. sourcecode:: python

    >>> sql = 'SELECT * FROM communes;'
    >>> data = gpd.read_postgis(sql=sql, con=engine, geom_col='geometry')

On peut aussi choisir de récupérer seulement les données relatives aux communes de la région Ile-de-France.

.. sourcecode:: python

    >>> sql = "SELECT * FROM communes WHERE reg ='11';"
    >>> data = gpd.read_postgis(sql=sql, con=engine, geom_col='geometry')
    >>> ax=data.plot()

Enfin, on peut réaliser des opérations croisées sur deux tables. Par exemple, on peut ne garder que les communes présentes dans la table relative aux arrondissements. On s'attend alors à retrouver les trois villes avec des arrondissements, c'est-à-dire Paris, Lyon et Marseille.

.. sourcecode:: python
    >>> sql="SELECT b.geometry::geometry As geometry, b.* FROM communes b INNER JOIN armf p ON ST_Intersects(b.geometry::geometry, p.geometry::geometry);"
    >>> data = gpd.read_postgis(sql=sql, con=engine, geom_col='bgeom')

    >>> ax=data.plot()
    >>> ax.axis('off')

