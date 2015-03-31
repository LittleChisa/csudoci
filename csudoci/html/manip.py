'''

``manip.py``
===========

Bibliothèque de classes et fonctions permettant de manipuler un arbre HTML
généré par ``csudoci.html.parser``.

'''

from csudoci.html.html import Ul, Li
from csudoci.html.parser import HTMLTreeParser


def get_links(tree):
    links = []
    root = tree

    if root.tag == 'a':
        links.append(tree)
    else:
        for c in tree.chilren():
            links += get_links(c)

            return links


def get_html_links(tree):
    ul_links = Ul()

    for link in get_links(tree):
        link < Li() < ul_links

    return ul_links


def test():
    test_html = '''
    <html>
      <head>...</head>
      <body>d
         <ul>
            <li><a href="...">...</a></li>
            <li><a href="...">...</a></li>
            <li><a href="...">...</a></li>
         </ul>

         <p>
            La page du collège du Sud se trouve sur
            <a href="http://www.collegedusud.ch">http://www.collegedusud.ch</a>
         </p>
      </body>
    </html>
    '''

    tree = HTMLTreeParser().feed(test_html).get_tree()
    list_of_links = get_html_links(get_links(tree))
    html = list_of_links.html()
    print(html)

if __name__ == '__main__':
    test()