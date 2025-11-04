#Sterk sammenhengende grafer ved dfs topologisk og vanlig, grafen er rettet og kan ha sykler 
#Topologisk søk, gjør at stacken blir organisert slik at foreldre noder kommer over etterkommere i stacken
def DFS_topsort(G):
    V, _ = G
    stack = list()
    visited = set() 
    for u in V:
        if u not in visited:
            DFS_visit(G, u, visited, stack)
    return stack

#Vanlig gjør ikke det topolgisk gjør, rekkefølgen blir tilfeldig, utsortert
def DFS_visit(G, u, visited, stack):
    _, E = G
    stack.append(u) 
    visited.add(u)
    for (u,v) in E[u]:
        if v not in visited:
            DFS_visit(G, v, visited, stack)
    #stack.append(u) #Hvis det er topologisk sortering så skal ikke noden legges til 
            #før barna har blitt lagt til er anerledes for vanlig DFS
    return stack 

#Reversere alle rettede kanter 
def ReverseGraph(G):
    V, E = G
    Er = set()
    for (u,v) in E:
        Er.add(v,u)
    return V, Er
#Kjøretid O(|E|)

def Strongly_connected_comp(G):
    #Får en stack med foreldre noder over etterfølgere i stacken
    stack = DFS_topsort(G)
    #reverser så retning på alle kantene, grafen er rettet
    Gr = ReverseGraph(G)
    visited = set()
    comps = set()
    while stack:
        #Vil poppe systematisk, foreldre først 
        u = stack.pop()
        if u not in visited:
            #siden vi har en topolgisk sortert graf og vi opperer med kanter som er snudd vil roten i den 
            #orginal være den laveste noden i grafen der kantene er reversert, siden vi starter algoritmen
            #fra roten vil vi altså starte fra bunnen i Gr. Hvis vi starter fra bunnen og jobber oss opp
            #vil comp i DFS_visit kun inneholde noden selv altså u, hvis ikke det er en sykel, da vil flere 
            #noder legges til siden de kan nås fra noden med lavere topologi(ingrad).
            #Hvis det ikke er noen sterke komonenter returneres en mengde med mengder med kun en node i seg, 
            #hvis mengdene har 2 eller flere noder i seg da er det sterke komponeter på fære 
            comp = set() #kan være liste, men må fortsatt konverteres til frozenset
            DFS_visit(Gr, u, visited, comp) 
            comps.add(frozenset(comp))#forzenset tilater mengde og bli lagt til inni mengde, kan ikke endres
    
    #returnerer en mengde med mengder som inneholder alle sykler i den rettede grafen
    return comps
#Kjøretid er O(|E| + |V|)

#Finne seperasjonsnoder 
#Kjøretid er O(|E| + |V|)
depth = dict()
low = dict()
seps = set()
def Seperation_Nodes(G):
    V, E = G
    s = V[0]
    depth[s] = 0
    low[s] = 0
    children = 0

    #Iterer over alle noder relatert til s og gjør et dfs-søk
    for (s,u) in E[s]:
        if u not in depth:
            SepRec(G,s,u,1)
            children += 1 #øker antall barn med 1

    #Hvis children er større enn 1 vil det si at node som er relatert til s ikke ble funnet i dybde først søket
    #Det vil si at s er den eneste sammenhengen mellom de to barnene
    if children > 1:
        seps.add(s)
    
    return seps


def SepRec(G, p, u, d):
    #Setter u sin dybde og low nummer til nodens dybde fra etterfølger
    V, E = G
    depth[u] = d
    low[u] = d
    
    #Iterer gjennom alle noder relatert til u, altså barnet til tidligere u som nå er p
    for (u,v) in E[u]:
        #Passer på at etterfølgeren ikke arver lownummeret til foreldrenoden 
        if v == p:
            continue
        #Hvis v allerede er besøkt oppdater lownummeret til enten u sit lownummer eller v sin dybde
        #Hvis v allerede er besøkt så er den en back-edge 
        if v in depth:
            low[u] = min(low[u],depth[v])
            continue
        
        #Kaller metoden rekursivt på etterkommeren av u, altså v
        SepRec(G, u, v, d+1)
        #Setter u sitt low nummer til å være enten sitt eget eller v sitt lownummer
        low[u] = min(low[u],low[v])
        #Hvis v ikke har noe lavere low nummer en den orginale dybden til u vet vi at den ikke er 
        #sammenhengende med noen av nodene som er lenger opp i grafen, altså er u en seperasjonsnode
        #fordi det ikke finnes noen back-edge for v lenger back en dybde u 
        if d <= low[v]:
            seps.add(u)

#Returnerer True eller False om det er noen seperasjonsnoder
def Is_biconncected(G):
    return len(Seperation_Nodes(G)) == 0


