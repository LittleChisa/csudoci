# pour utiliser le module de génération de html
from csudoci.html.htmltree import *
from csudoci.html.template import FileTemplate

# pour utiliser le parseur HTML qui construit un arbre
from csudoci.html.parser import HTMLTreeParser

# pour charger les structures de donnéest
from csudoci.ds.stack import Stack

from csudoci.tests.in_files import *

''' Exercice 1'''
#links par elements

def get_elements(tree, selector):
    elements = []
    root = tree

    if root.tag == selector:
        elements.append(tree)
    else:
        for c in tree.children:
            elements += get_elements(c, selector)

    return elements
    

''' Exercice 2 '''

def table_matieres(tree, level=2):
#level : combien de balises (jusqu'à quel niveau) <h...> ont été utilisées
#On veut récupérer toutes les balises de titre pour trouver le chiffre le plus haut

    table = []

    titre = 'h' + for str(i + 1) in range()
    balisesTitre = get_elements(tree, titre)
    
    for element in balisesTitre:
        table += element
        
    return table
    


''' Exercice 3 '''

def remove_links(tree):
#Il faut pouvoir enlever les balises seulement (<a> </a>) mais laisser le contenu

'''
pour element in liens:
    tree.remove(element)
    
'''

for element in get_links(tree):
    tree.remove(element)
    
#Différencier le contenu de la balise ? Effacer tout se qui se termine par "a>" ??

    
