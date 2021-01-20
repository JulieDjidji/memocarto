Projections
==============

Contrairement à ce qu'affirme la Flat Earth Society:https://www.tfes.org , la terre n'est pas plate mais sphérique. Ceci a pour principale conséquence que l'on doit en permanence faire face à des problèmes de projections. Une projection est une méthode permettant de transformer une surface sphérique en une surface plane:https://fr.wikipedia.org/wiki/Projection_cartographique . La principale difficultée avec les projections provient du fait que leur nombre est incommensurable. Chaque projection répond à un besoin particulier et est définie par un ensemble de norme. Par exemple, en France, les administrations sont sensés utiliser la projection Lambert 93 centrée sur la France métropole. Cette projection a pour vocation de déformer le moins possible la France Métropolitaine. En projection, Lambert 93 Le centre de Lille a pour coordonnée , et celui de Marseille , . La distance calculé avec Pythagore est de alors que la distance vol d'oiseau est de  km. La déformation entre les deux valeurs est minime. En pratique, lorsque les distances entre les objets sont minimes la distance de pythagore est totalement satisfaisante. Ces d'ailleurs cette approche que l'on adopte généralement en statistique spatiale.

On passe d'une projection à une autre, en effectuant une opération de reprojection. Cette opération peut être très longue en fonction de la taille de la couche cartographique. Il est donc important de bien réflechir à adopter une projection unique dès le début d'un projet cartographique.

Exemple de cartes 

Sur la figure 1, nous comparons l'effet de deux projections sur la France métropolitaine : Lambert 93 et LAEA la projection adoptée par l'Europe. On constate une légére déformation entre les deux cartes. Cette déformation explique l'énigme des carreaux de travers des données carroyées qui ont perturbé plus d'un d'entre nous. Les carreaux ont été calculés en LAEA puis ensuite reprojeté en lambert 93. Un carreau est défini par 4 points. Le premier point est le coin en haut en bas de coordonnées X, Y. Les autres sont déterminées en rajoutant à la coordonnées X : 0 ou 200 m. L'horizontale cartographique est implicitement déterminé par l'axe qui passe par les points (X,Y) et (X + 200, Y). En reprojetant la carte en lambert 93, l'horizontale précédent est dévie et tous les carreaux sont de travers :

Les coor
La définition des carreaux en rajoutant des multiples de leur 
Une astuce afin de calculer des données carroyées 


La projection WGS84 est trés utilisée pour la cartographie dynamique et les données issues des GPS. A proprement parler, ce n'est pas une projection mais une modélisation du globe terrestre. Les coordonnées sont des angles qui permettent de situer tout point sur la surface de la terre à partir d'une référence. Par exemple, le centre de Lille a pour coordonnée : et celui de Marseille. Avec le WGS84, il est absurde de calculer des distances avec la formule de Pythagore et donc de faire de l'analyse spatiale. Une erreur courante est de confondre les deux angles ce qui explique que de nombreux analyses finissent ici :
