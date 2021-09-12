from collections import deque


class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Vertix:
    def __init__(self, value):
        self.value = value
    # def __repr__(self):
    #   return str(self)
class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight

class Graph:
    
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, value):
        vertix = Vertix(value)
        self.adjacency_list[vertix] = []
        return vertix
    
    def add_edge(self, vertix_start, vertix_end, weight=0):
        all_all_nodes=self.adjacency_list.keys()
        if not vertix_start in all_all_nodes and not vertix_end in all_all_nodes:
            return 'Both all_nodes not exisist'
        elif not vertix_start in all_all_nodes:
            return 'The first node is not in the Graph'
        elif not vertix_end in all_all_nodes:
            return 'The seconde node is not in the Graph'
        
        edge = Edge(vertix_end, weight)
        self.adjacency_list[vertix_start].append(edge)
    
    def get_all_nodes(self):
        temp=[]
        for vertix in self.adjacency_list.keys():
            temp.append(vertix)
        if len(temp)==0:
            return None
        return temp
    
    def get_neighbors(self, node):
        temp=[]
        
        if node in self.adjacency_list :

            for edge in self.adjacency_list[node]:

               temp.append((edge.vertix, edge.weight))

            return temp
        if len(temp)==0:
            return None
 
    
    def size(self):
        return len(self.adjacency_list.keys())

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
    
            output += vertix.value
           
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value 
            
            output += '\n'
        return output
    
    def bfs(self,node):
        if node not in self.adjacency_list:
            return 'This node is not in the graph'
        all_nodes=[]
        breadth_nodes = Queue()
        visited_nodes = set()

        breadth_nodes.enqueue(node)
        visited_nodes.add(node)

        while breadth_nodes:
            front=breadth_nodes.dequeue()
            all_nodes.append(front)
            for edge in self.adjacency_list[front]:

                if edge.vertix not in visited_nodes:
                
                    visited_nodes.add(edge.vertix)
                    breadth_nodes.enqueue(edge.vertix)
        
        return [vertex.value for vertex in all_nodes]

   


if __name__ == '__main__':

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

    print(graph2.bfs(pandora))