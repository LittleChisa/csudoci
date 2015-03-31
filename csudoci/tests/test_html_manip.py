from csudoci.html.parser import html_to_tree
from csudoci.html.manip import get_links_as_ul

from csudoci.html.manip import get_links_as_ul, get_links_as_ul2


tests = []


def load_test_file(filename):
    with open('in_files/' + filename, mode='r') as fd:
        content = fd.read()

        return content


def test(test_function):
    global tests
    tests += [test_function]


@test
def test_get_links_as_ul():
    html = load_test_file('test1.html')
    try:
        tree = html_to_tree(html)
    except Exception as e:
        print('Bas', e.stack.to_list())
        raise Exception('Abandon')
    ul = get_links_as_ul(tree)
    print(ul.html())


if __name__ == '__main__':
    for test in tests:
        test()

