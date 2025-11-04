# Gi en algoritme som finner alle forskningsprosjekter i grafen.
# Algoritmen skal ta G som input, og returnere en liste med forskningsprosjekter som output.

from TopSort import TopSort
from Grafer import DFS_visit
# from 2sammenhengende import ReverseGraph


#Reversere alle rettede kanter 
def ReverseGraph(G):
    V, E = G
    Er = set()
    for (u,v) in E:
        Er.add(v,u)
    return V, Er
#Kjøretid O(|E|)


components = set()
stack = TopSort(G)

visited = set()

gR = ReverseGraph(G)

while stack:
    u = stack.pop()
    if u not in visited:
        c = set()
        DFS_visit(gR, u, visited, c)
        components.add(frozenset(c))

print(components)









