from graph import __version__

from graph.graph import *
def test_version():
    assert __version__ == '0.1.0'




def test_add_node():
    graph = Graph()
    a = graph.add_node('a')
    actual = graph.size()
    excepted = 1
    assert actual == 1


def test_print_graph():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)
    
    actual = graph.size()
    excepted = 6

    assert actual== excepted          