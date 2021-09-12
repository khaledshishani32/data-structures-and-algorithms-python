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
    


if __name__ == '__main__':
    
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
    # print(graph.get_nodes())




    