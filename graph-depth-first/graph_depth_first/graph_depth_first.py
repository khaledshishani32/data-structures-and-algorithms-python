
class Vertix:
    def __init__(self, value):
        self.value = value
    # def __repr__(self):
    #   return str(self)

    def __len__(self):
        return len(self.value)
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
        restult = ''
        for vertix in self.adjacency_list.keys():
    
            restult += vertix.value
           
            for edge in self.adjacency_list[vertix]:
                restult += ' -> ' + edge.vertix.value 
            
            restult += '\n'
        return restult
    
    def depth_first(self,start_point):
        if start_point not in self.adjacency_list.keys():
            return 'The node is not Exiest'
        restult=[]

        def dfs(node):
            
            if not node in restult:
                restult.append(node)
            for node2 in self.get_neighbors(node):
                if not node2[0] in restult:
                    dfs(node2[0])

        dfs(start_point)
      
        return  

if __name__ == '__main__':
    
    graph = Graph()

    a= graph.add_node('a')
    b= graph.add_node('b')
    c= graph.add_node('c')
    d= graph.add_node('d')
    e= graph.add_node('e')
    f= graph.add_node('f')
    g= graph.add_node('g')
    h= graph.add_node('h')
    
    graph.add_edge(a,b)
    graph.add_edge(a,d)
    graph.add_edge(b,a)
    graph.add_edge(b,c)
    graph.add_edge(b,d)
    graph.add_edge(c,b)
    graph.add_edge(c,g)
    graph.add_edge(g,c)
    graph.add_edge(d,a)
    graph.add_edge(d,b)
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    graph.add_edge(e,d)
    graph.add_edge(f,d)
    graph.add_edge(f,h)
    graph.add_edge(h,d)
    graph.add_edge(h,f)

    print(graph.depth_first(a))

    


    