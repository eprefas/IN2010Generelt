def parent(i):
    return (i-1) // 2

#Kjøretid er O(log(n))
def innsetting(A, x):
    i = len(A)
    A.append(x)
    #Sjekker at alle parent etter nytt element er satt inn blir oppdatert riktig
    while i>0 and A[i] < A[parent(i)]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def leftchild(i):
    return 2*i + 1

def rightchild(i):
    return 2*i + 2

##Kjøretid er O(log(n))
def fjern_minste(A):
    lengde = len(A)-1
    #Setter x til minste element, først i heap
    x = A[0]
    #Flytter siste element øverst i treet og oppdaterer
    A[0] = A[lengde]
    i = 0
    while leftchild(i) < lengde:
        j = leftchild(i)
        #Endrer j til høyrebarn hvis det er mindre enn venstre
        if rightchild(i) < lengde and A[rightchild(i)] < A[j]:
            j = rightchild(i)
        #Sjekker at parent er mindre eller lik minste barn, hvis så så er algoritmen ferdig
        if A[i] <= A[j]:
            return x
        #Bytter plass på parent og minste barn
        A[i], A[j] = A[j], A[i]
        #Setter i til å være sitte minste barn, sjkker så videre for denne indeksen sine barn igjen
        i = j
    return x 


#Heapsort
def Bubbledown(A, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    #Bytter plass på largest(parent) med største child
    if left < n and A[largest] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    
    #Så lenge largest finner et større barn byttes plass, kalles rekursivt fra barnenode(som nå er largest) 
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Bubbledown(A, largest, n)

#Kan bygge en heap i O(n)    
def BuildMaxHeap(A,n):
    #Trenger bare gjøre det for halvparten fordi når du har gjort det for parent har du også gjort det for child
    i = n//2
    while i >= 0:
        Bubbledown(A,i,n)
        i -= 1

##Kjøretid er O(n*log(n)) på heapsort
def HeapSort(A):
    n = len(A) - 1
    BuildMaxHeap(A,n)
    while n > 0:
        #Bytter plass på største og det elementet som er bakerst
        A[0], A[n] = A[n], A[0]
        #regulrer indeks slik at sorterte elemnter ikke blir tukla med, kommer ikke til å skje da ;)
        n -= 1
        #Fikser sånn at største element kommer fremst igjen etter elementene har bytta plass
        Bubbledown(A,0,n)
    return A
        



