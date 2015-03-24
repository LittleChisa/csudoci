# Package `csudoci`
Modules et codes pour le cours d'option complémentaire informatique de DONC au CSUD

# Installation

Pour installer le package, il faut pour le moment l'installer avec 

```{bash}
$ git clone https://github.com/oci1315/csudoci.git
```

car le package n'est pas encore packagé de manière correcte pour une installation 
avec `pip`.

La structure de votre dossier devrait donc ressembler à ceci :

[//]: # (tree . | grep -v "pyc" pour générer l'arbre)

```{bash}
$ tree .
├── README.md
├── __init__.py
├── ds
│   ├── __init__.py
│   └── stack.py
├── html
│   ├── __init__.py
│   ├── html.py
│   ├── parser.py
│   └── template.py
└── setup.py
```

Autrement dit, il faut cloner le dépôt `https://github.com/oci1315/csudoci.git`
dans le même dossier que votre script.

## Importation des modules

Pour travailler avec le module `html` du package `csudoci`, il faut faire 
l'importation suivante : 

```{python}
# pour utiliser le module de génération de html
from csudoci.html.html import *
from csudoci.html.template import FileTemplate

# pour utiliser le parseur HTML qui construit un arbre
from csudoci.html.parser import HTMLTreeParser

# pour charger les structures de donnéest
from csudoci.ds.stack import Stack

# faire quelque chose avec les modules
```

# Utilisation du parseur HTMLTreeParser

Pour utiliser le parseur HTML qui définit la classae ``HTMLTreeParser``, il faut importer ``csudoci.html.parser``

```{python}
>>> from csudoci.html.parser import HTMLTreeParser
>>> html = '<ul><li><p class="salut">Du texte</p><img src="image.jpeg" /></li></ul>'
>>> p = HTMLTreeParser()
>>> p.feed(html)
>>> tree = p.get_tree()
>>> tree.draw()
 Element :  ul
    Element :  li
       Element :  p
          Text :  Du texte
       Element :  img
```