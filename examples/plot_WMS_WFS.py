"""
Exploitation des flux WFS et WMS
----------------------------------------------------------------
Dans ce notebook, nous allons exploiter des flux WMS et WFS, comprendre leur contenu et afficher les cartes.
Nous utilisons les services mis à disposition par le partenariat breton des données géolocalisées sur le site [cms.geobretagne](https://cms.geobretagne.fr/). Les services proposés sont listés à l'adresse https://cms.geobretagne.fr/services.
"""
# sphinx_gallery_thumbnail_number = 1
import io
import matplotlib.pyplot as plt
import requests
import geopandas as gpd
from owslib.wms import WebMapService
from owslib.wfs import WebFeatureService
import json
from lxml import etree

#######################################################################################
# Récupération du flux  WFS
# ================================
#
# Présenter les flux WFS ...

#######################################################################################
# Exploration du contenu de la requête GetCapabilities
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# On effectue la requête GetCapabilities qui permet d'accéder aux paramètres du service et aux couches disponibles avec les informations nécessaires pour paramétrer les requêtes.

wfs_url="https://ows.region-bretagne.fr/geoserver/rb/wfs?service=wfs&request=getCapabilities"
response=requests.get(wfs_url).content

#######################################################################################
# On peut par exemple afficher l'ensemble des opérations réalisables avec ce service. 

root=etree.fromstring(response)

ns={'xsi':"http://www.w3.org/2001/XMLSchema-instance",
        'wfs':"http://www.opengis.net/wfs/2.0",
        'wps':"http://www.opengis.net/wps/1.0.0",
        'ows':"http://www.opengis.net/ows/1.1",
        'gml':"http://www.opengis.net/gml/3.2",
        'fes':"http://www.opengis.net/fes/2.0",
        'xlink':"http://www.w3.org/1999/xlink",
        'xs':"http://www.w3.org/2001/XMLSchema",
        'inspire_dls':"http://inspire.ec.europa.eu/schemas/inspire_dls/1.0",
        'inspire_common':"http://inspire.ec.europa.eu/schemas/common/1.0",
        'rb':"http://bretagne.fr/rb",
        'schemaLocation':"http://www.opengis.net/wfs/2.0 https://ows.region-bretagne.fr/geoserver/schemas/wfs/2.0/wfs.xsd http://inspire.ec.europa.eu/schemas/inspire_dls/1.0 http://inspire.ec.europa.eu/schemas/inspire_dls/1.0/inspire_dls.xsd"
    }

for element in root.findall('.//ows:Operation', ns):
    print(element.attrib)

#######################################################################################
# On peut aussi afficher le nom des couches disponibles

root=etree.fromstring(response)
features=[]
for name in root.iter('{http://www.opengis.net/wfs/2.0}Name'):
    features.append(name.text)
print(features[0:4])
    
#######################################################################################
# Récupération des données de la couche relative aux aires urbaines
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#

#######################################################################################
# Méthode 1 : on peut les récupérer directement si on connaît la formulation de la requête

wfs_url="https://ows.region-bretagne.fr/geoserver/rb/wfs?service=wfs&version=2.0.0&request=GetFeature&typeName=rb:aire_urbaine&outputFormat=json"

#######################################################################################
# On affiche les premières observations de la base de données
gpd.read_file(wfs_url).head(2)

#######################################################################################
# On affiche la carte diffusée par le flux WFS

gpd.read_file(wfs_url).plot()

#######################################################################################
# Méthode 2 : on peut les récupérer à partir du package owslib

#######################################################################################
# On indique l'URL du service
url = "https://ows.region-bretagne.fr/geoserver/rb/wfs"

#######################################################################################
# On initialise
wfs = WebFeatureService(url=url)

#######################################################################################
# On peut afficher le nom des couches disponibles
print(list(wfs.contents)[0:4])

#######################################################################################
# On précise la couche souhaitée
layer='rb:aire_urbaine'

#######################################################################################
# On effectue la requête pour récupérer les données
params = dict(service='WFS', version="1.0.0", request='GetFeature',
      typeName=layer, outputFormat='json')
q = requests.Request('GET', url, params=params).prepare().url

#######################################################################################
# On met en forme les données et affiche les deux premières observations
data = gpd.read_file(q)
data.head(2)


#######################################################################################
# Récupération et exploitation du flux  WMS
# ================================
#
# Présenter les flux WMS ...

#######################################################################################
# Affichage de la carte diffusée relative à la couche de la localisation des cœurs d'habitat (ou réservoirs de biodiversité) du campagnol amphibie en Bretagne et Loire-Atlantique continentales.
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Méthode 1 : on peut récupérer directement l'image si on connaît la formulation de la requête avec la requête GetMap puis l'afficher

wfs_url="https://geobretagne.fr/geoserver/gmb/wms?request=GetMap&format=image/png&width=600&height=600&layers=campagnol_amphibie&bbox=124702.3554,6651480.7257,403802.3554,6881080.7257&CRS=EPSG:2154"

response=requests.get(wfs_url).content
img=plt.imread(io.BytesIO(response))
plt.imshow(img)

#######################################################################################
# Méthode 2 : on peut la récupérer à partir du package owslib

wms = WebMapService('https://geobretagne.fr/geoserver/gmb/wms')

name = 'campagnol_amphibie'
layer = wms.contents[name]
response = wms.getmap(layers=[name,],
                 bbox=layer.boundingBox[0:4], # Left, bottom, right, top
                 format='image/png',
                 size=(600,600),
                 srs=layer.boundingBox[4],
                 time=layer.timepositions,
                 transparent=True)

img=plt.imread(io.BytesIO(response.read()))
plt.imshow(img)
