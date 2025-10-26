def bubblesort(A):
    n = len(A)
    for i in range(0,n-1): 
        for j in range(0,n-i-1): 
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

'''
Bubble
Verste kjøretid er O(n^2), er både stabil og in-place
Etter første iterasjon vil alltid største element være plassert riktig og for andre vil nest største osv
er derfor det er n-i. Grunnen til at det er n-1 er fordi trenger ikke gjøre operajson på siste element, vil 
også få index out of bounds error 
'''

def mergesort(A):
    if len(A) < 2:
        return
    
    mid = len(A)//2
    #Inkluderer midt i venstre ikke høyre
    left = A[:mid]
    right = A[mid:]

    #splitter ned til bare et element 
    mergesort(left)
    mergesort(right)

    return merge(left, right, A)

def merge(l, r, A):
    l_len = len(l)
    r_len = len(r)

    i = j = 0
    
    #Så lenge alle elmentene i enten høyre eller venstre ikke har blitt sett på
    while i < l_len and j < r_len:
        #Arrayene er sortert fra før så når v og h skal merge så vil minste elementet til v ligge på v[0]
        #og minste til h ligge på h[0]
        if l[i] <= r[j]:
            #i+j styrer plassering i A
            A[i+j] = l[i]
            i += 1
        else:
            A[i+j] = r[j]
            j += 1
    #Fyller opp hvis det er flere elementer igjen i v
    while i < l_len:
        A[i+j] = l[i]
        i += 1
    #Samme for h
    while j < r_len:
        A[i+j] = r[j]
        j += 1
    #returnerer merged array A
    return A 

'''
Merge
Splitter array helt ned til et arrays med element og fletter dem sammen igjen sortert
Verste kjøretid er O(n*log(n)). Mergesort er ikke in-place, men er stabil. merge() er i O(n) og
mergesort() er i O(log(n))
'''

def partition(A, low, high):
    #velger pivot som første element, er ikke lurt, burde kalle choosepivot()
    p = low
    #Plasserer pivot på høyeste index
    A[p], A[high] = A[high], A[p]

    #Velger pivot element som når er bakerst
    pivot = A[high]
    left = low
    right = high-1

    #Sjekker at pekere ikke passerer hverandre slik at pivot ikke er i midten lenger
    while left <= right:
        while left <= right and A[left] <= pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        #Når vi har funnet to elementer som skal byttes så bytter vi dem
        if left < right:
            A[left], A[right] = A[right], A[left]
    #Setter pivot i midten igjen og plassere elementet der left og right møttes bakerst      
    A[left], A[high] = A[high], A[left]
    return left #returnerer neste pivot indeks


def quicksort(A, low, high):
    if low >= high:
        return A
    #Så lenge det ikke kun er et element som behandles
    #velger indeks
    p = partition(A, low, high)
    #rekrusjon på det er mindre og høyrere enn pivot
    quicksort(A, low, p-1)
    quicksort(A, p+1, high)
    return A

'''
Quicksort 
Forventet kjøretid er O(n*log(n)), men verste kjøretid er O(n^2) hvis vi velger pivot på fast sted og array
allerede er sortert, burde randomize valg av pivot da blir verste kjøre tid mye mindre sansynnelig. 
Quicksort er in-place, men ikke stabil
'''

def bucketsort(A, N):
    #Oppretter et antall bøtter basert på strukturen i A
    B = [[] for _ in range(N)]

    #Fyller opp bøttene, vil nå bli sortert
    for i in range(len(A)):
        k = A[i]
        B[k].append(A[i])
    
    #Overskriver elementer i A slik at det blir sortert 
    j = 0
    for k in range(N):
        for x in B[k]:
            A[j] = x
            j += 1

'''
Bucket
Verste kjøretid er O(n+N), hvis N er en konstant da er det O(n). Bucketsort krever at vi vet noe om elementene 
i listen fra før. Hvis det er snakk om tall må vi anta at tallene i A er heltall mellom 0-(N-1).
Bucket sort er ikke in-place, men den er stabil
'''

def bucketsort_digit(A, N, i):
    B = [[] for _ in range(N)]
    
    for x in A:
        digit = (x // (N ** i)) % N #det i-te sifferet, f.eks. x=657 og i=2(hundrer-plass) -> digit=6
        B[digit].append(x)
    
    j = 0
    for k in range(N):
        for x in B[k]:
            A[j] = x
            j += 1
    return A


def radixsort(A, N, d):
    #d er antall siffre i største tall, kan finne det, men bedre å vite fra før eller ta som argument
    for i in range(d):
        A = bucketsort_digit(A, N, i)
    return A

#Dette er orginal pesudokode, men fungerer ikke fordi i-te elementet blir ikke behandlet eller formidlet
#til original bucketsort     
def radixsort_pesu(A, N, d):
    i = d-1
    while i >= 0:
        A = bucketsort(A, N) #etter i-te elementet
        i -= 1
    return A

'''
Radix
Kjøretid er O(d*(N+n)) normalt, men hvis N er en konstant, for tall vil N vangligvis være 10. Da får vi
O(d*(10+n)) = 0(d*n). Hvis d max begrensning også er konstant og ikke veldig stor (liten i forhold til antall 
tall) så får vi bare O(n). Koden du ser over som fungerer er ikke orginal pesudeo kode, men er beregnet for 
å fungere på heltall. Radixsort er ikke in place, men den er stabil
'''

def selectionsort(A):
    n = len(A)
    for i in range(0, n):
        k = i
        for j in range(i+1, n):
            if A[j] < A[k]:
                k = j
        if i != k:
            A[i], A[k] = A[k], A[i]

'''
Selection
Starter på første indeks finner så minste elementet i listen og bytter med første indeks
gjøre dette så for alle indekser. Verste kjøretid er O(n^2)
Selection sort er ikke stabil fordi like elementer kan bytte plass, men den er in-place
'''

def insertionsort(A):
    n = len(A)
    for i in range(1, n):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j = j-1

'''
Insertion
Tar et element og flytter det på riktig plass og forskyver de andre elementene fremover, sånn som 
man ville sortert kort, alt til venstre for i er sortert og alt til høyre er ikke sortert 
Verste kjøretid er O(n^2) og algoritmen er in-place og stabil
'''


