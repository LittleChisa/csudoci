# csudoci
Modules et codes pour le cours d'option complémentaire informatique de DONC au CSUD

# Installation

Pour installer le package, il faut pour le moment l'installer avec 

```{bash}
$ git clone https://github.com/oci1315/csudoci.git
```

car le package n'est pas encore packagé de manière correcte pour une installation 
avec `pip`.

La structure de votre dossier devrait donc ressembler à ceci :

```{bash}
$ tree .
.
├── csudoci
│   ├── ...
├── mon_script.py
```

Autrement dit, il faut cloner le dépôt `https://github.com/oci1315/csudoci.git`
dans le même dossier que votre script.

## Importation des modules

Pour travailler avec le module `html` du package `csudoci`, il faut faire 
l'importation suivante : 

```{python}
from csudoci.html.html import *
from csudoci.html.template import FileTemplate

# faire quelque chose avec les modules
```
