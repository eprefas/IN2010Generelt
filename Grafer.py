from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
#Kjøre tid er O(V + E)
def bfs(G, s): #kan også ta med visited som argument, hvis man skal gjøre det full, altså på hver node i graf
    V, E = G
    visited = set()
    visited.add(s)
    #Kø first inn first out
    queue = deque()
    queue.append(s)
    while queue:
        #popper de som er først i køen
        u = queue.popleft()
        for (u,v) in E[u]:
            #legger barna til den noden bakerst i køen
            #vil dermed sjekke alle barna til en node før den går videre å sjekker noen av de andre 
            #nodene sine barn
            if v not in visited:
                visited.add(v)
                queue.append(v)

#Kjøretid er O(V+E)
def bfs_full(G):
    V, E = G
    visited = set()
    for v in V:
        if v not in visited:
            #gjør dette for hver node
            bfs(G,v,visited)
    #returnerer en mengde med alle nodene i grafen, 
    return visited


#Sterk sammenhengende grafer ved dfs topologisk og vanlig, grafen er rettet og kan ha sykler 
#Topologisk søk, gjør at stacken blir organisert slik at foreldre noder kommer over etterkommere i stacken
#Kjøretid er O(V+E)
def DFS_topsort(G):
    V, _ = G
    stack = list()
    visited = set() 
    for u in V:
        if u not in visited:
            DFS_visit(G, u, visited, stack)
    return stack

#Vanlig gjør ikke det topolgisk gjør, rekkefølgen blir tilfeldig, utsortert
#Kjøretid er O(V+E)
def DFS_visit(G, u, visited, stack):
    _, E = G
    stack.append(u) 
    visited.add(u)
    for (u,v) in E[u]:
        if v not in visited:
            DFS_visit(G, v, visited, stack)
    #stack.append(u) #Hvis det er topologisk sortering så skal ikke noden legges til 
            #før barna har blitt lagt til er anerledes for vanlig DFS
    return stack #return delen er heller ikke med i topsort 


#Kjøretid er O((V + E) * log(V)), kan forenkles til O(E*log(V)) hvis grafen er sammenhengende
def dijkstra(G,s):
    _,E,w = G
    #Setter alle noder sine default verdier til å være uendelig
    dist = defaultdict(lambda: float('inf'))
    #Setter startnode verdi til 0
    dist[s] = 0
    #Lager en priqueue for å holde styr laveste veiene, første vil alltid være den med lavest c
    queue = [(0,s)]

    while queue:
        cost, u = heappop(queue)
        #Brukes for å unngå å legge til større verdier, hvis cost ikke er lik dist[u] så er den større
        #grunnen til dette er at minheapen sørger for at lavest verdier blir lagt til først så når det kommer 
        #en større verdi så kan den ignoreres
        if cost != dist[u]:
            continue
        #Sjekker alle nodene u er kobla til
        for v in E[u]:
            #oppdaterer c basert på tidligere cost vekten til kanten
            c = cost + w[(u,v)]
            #sjekker om c er mindre enn den verdien som noden allerede har i ordboken
            if c < dist[v]:
                #Oppdatere nye verdien til noden til c
                dist[v] = c
                #legger til verdien i køen så det evt kan oppdaters igjen basert på veiene grafen finner
                heappush(queue, (c,v))
    #returnerer en ordbok med kortest vekt fra en node til alle andre nodene i grafen 
    return dist


#Bellman-Ford avdekker negative sykler ved å passe på at en sti ikke inneholder mer enn V-1 kanter 
#En sti kan aldri ha mer en V-1 kanter hvis den ikke går over samme noder flere ganger, noe den ikke skal
#Hvis den har mer kanter enn dette vil det tyde på at det er en negativ sykel fordi den vil kjøre evig ettersom
#c (altså cost) vil bli mindre og mindre for hver iterasjon
#Kjøretid til Bellman Ford er O(V*E) som tilsvarer O(V^3)
'''
Procedure BellmanFord(G, s)
 dist ← empty map with ∞ as default
 dist[s] = 0

#Det er uendelig verdiene som gjør at man besøker grafen systematisk, man vil jobbe seg ut fra startnode s
#fordi alle andre noder som ikke er direkte knyttet(en kant) vil ikke bli oppdatert(de er uendelig), 
#slik fortsetter det for nabonodene til disse kantene igjen osv
 repeat |V | − 1 times
   for (u, v) ∈ E do
       c ← dist[u] + w(u, v)
       if c < dist[v] then
           dist[v] ← c
 for (u, v) ∈ E do
      c ← dist[u] + w(u, v)
      if c < dist[v] then
          error G contains a negative cycle
 
 return dist
'''


#DAG funker for rettede asykligiske grafer uten sykler, bruker topologisk sortering 
#for å forsikre seg om at når en node har fått 
#en cost så kan den ikke endre seg basert på noden etterfølgere. Kjøretide er O(V+E)

'''
Procedure DAGShortestPaths(G, s)
 dist ← empty map with ∞ as default
 dist[s] = 0
 stack = TopSort(G)
 
 #Fant ut av alle noen før s i topolgiske rekkefølgen ikke vil bli påvirket siden de ikke kan 
 #nås fra s så hvis vi har x -> s -> a -> b så vil x = uendelig, mens s a og b vil oppdateres etter
 korteste avstand fra s, s vil altså være roten av noder som får tildelt verdi
 while stack:
    u = stack.pop()
    for (u, v) ∈ E[u] do
       c ← dist[u] + w(u, v)
       if c < dist[v] then
          dist[v] ← c
 
 return dist
'''

def prim(G):
    V, E, w = G
    queue = []
    parents = {}
    #Setter inn er vikårllig node, med parent None og cost 0
    heappush(queue, (0, V[0], None))
    while queue:
        #poper minste element i køen
        cost, u, p = heappop(queue)
        #oppdaterer parent
        if u not in parents:
            parents[u] = p
            for v in E[u]:
                #unngåer duplikater siden når vi går fra parent til barn så vil 
                #barn sjekke parent å legge til sammen kant på nytt
                if v not in parents:
                    #Hele greia funker p.g.a minheap, alle store kanter blir ignorert fordi 
                    #nodene allerede har blitt lagt til i parent under en lavere verdi p.g.a min heap. 
                    heappush(queue, (w[(u,v)], v, u)) 
    return parents
         
'''
Prim algortimen er for minimale spenn trær, altså et tre i grafen som kobler alle nodene og som totalt har minst 
mulig vekt som en tre som kan lages fra nodene i grafen kan ha.
Kjøretiden er O((V+E) * log(V)), som kan forkortes til O(E * log(V)) 

Kruskals algoritme funker for grafer som ikke er sammenhengende, returnerer et minimalt spenntre for hver 
komponent sjekker kontinuerlig om det oppstår sykler eller ikke. Hvis grafen er sammenhengnde vil hver 
komponent den har startet fra bli koblet sammen til slutt, på en måte der det ikke forekommer noen sykler
Kjøretid er O(E * log(V))

Boruvkas algortime gjør det samme som kruskal. Starter med å finne minste kant for hver node, vil da dannes 
mange ulike komponenter fordi ofte er den minste kanten til en node x også den minste kanten for 
en nabonode y som node x er koblet sammen med. Boruvkas terminerer når det ikke finnes kanter som forbinder de 
ulike trærne eller når hele graf er koblet sammen(er sammenhengende). 
KJøretid er O(E * log(V))
'''