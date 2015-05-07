from tp_html import *

with open('test.html', 'r', encoding='utf8') as fd:
     tree = html_to_tree(fd.read())
 
     
def test_get_elements():

   link_list = get_elements(tree, ['a'])
   header_list = get_elements(tree, ['h1', 'h2'])
   
   print(link_list)
   print(link_list)

def test_table_matieres():

   tdm = table_matieres(tree, level=2)
   html = tdm.html()
   print(html)

def test_remove_links():

   # rédiger le test ici
   pass