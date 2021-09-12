from graph_breadth_first import __version__

from graph_breadth_first.graph_breadth_first import *

def test_version():
    assert __version__ == '0.1.0'

def test_bfs_graph():
    assert __version__ == '0.1.0'
     

    graph2 = Graph()

    pandora= graph2.add_node('pandora')
    arendelle= graph2.add_node('arendelle')
    metroville= graph2.add_node('metroville')
    narina= graph2.add_node('narina')
    naboo= graph2.add_node('naboo')
    manstropolis= graph2.add_node('manstropolis')

    graph2.add_edge(pandora,arendelle)
    graph2.add_edge(arendelle,pandora)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(metroville,arendelle)
    graph2.add_edge(metroville,manstropolis)
    graph2.add_edge(metroville,naboo)
    graph2.add_edge(metroville,narina)
    graph2.add_edge(narina,metroville)
    graph2.add_edge(narina,naboo)
    graph2.add_edge(naboo,narina)
    graph2.add_edge(naboo,metroville)
    graph2.add_edge(naboo,manstropolis)
    graph2.add_edge(manstropolis,naboo)
    graph2.add_edge(manstropolis,arendelle)
    graph2.add_edge(manstropolis,metroville)
     
    actual = graph2.bfs(pandora)
    excepted = ['pandora', 'arendelle', 'metroville', 'manstropolis', 'naboo', 'narina']
    assert actual == excepted