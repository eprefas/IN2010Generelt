from heapq import heappop, heappush
#Huffman handler om å representere symbolder med binære tall, dette skal optimaliseres
#symbolene har også en frekvens som sier noe om hvor ofte de forekommer
#Huffman tærer er lagd for å komprimere data
#Kjøretid er O(n*log(n))


#Bruk indekser - Alex
#C er biblotek med symbol og frekvens

class Node:
    def __init__(self, freq, symbol, left_child, right_child):
        self._freq = freq
        self._symbol = symbol
        self._left = left_child
        self._right = right_child


def huffman(C):
    queue = []
    for (s,f) in C:
        heappush(queue, Node(f, s, None, None))
    
    while len(queue) > 1:
        v1 = heappop(queue)
        v2 = heappop(queue)
        f = v1.freq + v2.freq
        heappush(queue, Node(None, f, v1, v2)) 

    #returnerer rooten til treet 
    return heappop(queue)


#P er problemer løseslige i polynomisk tid, mens NP kan ikke det
#Man kan sjekke om en løselig er riktig i polynomisk tid for NP problemer 