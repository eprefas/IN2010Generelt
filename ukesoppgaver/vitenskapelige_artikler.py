# Gi en algoritme som finner alle forskningsprosjekter i grafen.
# Algoritmen skal ta G som input, og returnere en liste med forskningsprosjekter som output.

from TopSort2 import topological_sort
from Grafer import DFS_visit


def ReverseGraph(G):
    V, E = G
    Er = set()
    for (u,v) in E:
        Er.add(v,u)
    return V, Er
#Kjøretid O(|E|)

def Strongly_connected_comps(G):
    components = set()
    stack = topological_sort(G)
    visited = set()
    gR = ReverseGraph(G)

    while stack:
        u = stack.pop()
        if u not in visited:
            c = set()
            DFS_visit(gR, u, visited, c)
            components.add(frozenset(c))

    return components




#-----------------------_oppg B----------------------
# Du ser nå at grafen du har tegnet kan forenkles. En oversikt over hvordan forskningsprosjektene henger sammen er tilstrekkelig.
# Gi en algoritme som tar grafen G og lista med forskningsprosjekter som input, og gir en ny graf K = (Vk, Ek) som output.
# En node u i Vk representerer et forskningsprosjekt, og en kant (u, v) i Ek illustrerer at en artikkel i u inneholder en referanse til en artikkel i v.
# Oppgi i tillegg kjøretidskompleksiteten til algoritmen din i stor O-notasjon, og gi en kort begrunnelse for svaret ditt.

#Kjøretidskompleksitet er O(V+E)
def forenkle(G, projects):
    V, E = G
    Vk = set()
    Ek = set()
    components = dict()

    for p in projects:
        for node in p:
            Vk.add(node)
            components[node] = p
    
    for (u, v) in E: 
        if u not in components or v not in components:
            continue
        
        c1 = components[u]
        c2 = components[v]
        if c1 != c2:
            edge = (c1, c2)
            Ek.add(edge)
    
    K = (Vk, Ek)
    return K

    
#Oppgave C 



#Oppgave D


