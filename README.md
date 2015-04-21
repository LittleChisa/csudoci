# Package `csudoci`
Modules et codes pour le cours d'option complémentaire informatique de DONC au CSUD

# Installation

Pour installer le package, il faut pour le moment l'installer avec 

```{bash}
$ git clone https://github.com/oci1315/csudoci.git
$ cd csudoci
$ python3 setup.py build
$ sudo python3 setup.py install
```

Ces commandes vont installer le package de manière globale sur le système pour
qu'il soit possible de l'utiliser depuis n'importe où avec un simple import 

```{python}
from csudoci.html import htmltree
```

pour importer le module `csudoci.html.htmltree`.

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

## Importation des modules

Pour travailler avec le module `html` du package `csudoci`, il faut faire 
l'importation suivante : 

```{python}
# pour utiliser le module de génération de html
from csudoci.html.htmltree import *
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
