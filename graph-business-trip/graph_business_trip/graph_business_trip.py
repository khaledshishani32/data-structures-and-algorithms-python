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

def business_trip(graph,cities_names):
    
    total_cost = 0
    is_have_path= True
    for index in range(len(cities_names)-1):
        for city_name in graph.get_neighbors(cities_names[index]):
            if cities_names[index+1]==city_name[0]:
                total_cost+=city_name[1]
                break
            else:
                is_have_path=False
        
    if is_have_path==False:
            total_cost=0
    
    return is_have_path, f'${total_cost}'   

   


if __name__ == '__main__':

    graph = Graph()

    pandora= graph.add_node('pandora')
    arendelle= graph.add_node('arendelle')
    metroville= graph.add_node('metroville')
    narina= graph.add_node('narina')
    naboo= graph.add_node('naboo')
    manstropolis= graph.add_node('manstropolis')

    
    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(pandora,metroville,82)
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,manstropolis,105)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,manstropolis,42)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(metroville,narina,37)
    graph.add_edge(narina,metroville,37)
    graph.add_edge(manstropolis,naboo,73)
    graph.add_edge(manstropolis,arendelle,42)
    graph.add_edge(manstropolis,metroville,105)
    graph.add_edge(narina,naboo,250)
    graph.add_edge(naboo,narina,250)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,manstropolis,73)

    print(business_trip(graph,[metroville,pandora]))
    print(business_trip(graph,[naboo, pandora]))
    # print(graph.get_neighbors(pandora))