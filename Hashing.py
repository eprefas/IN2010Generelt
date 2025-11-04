#Fuksjon som hasher strenger, brukes i Java, bra i forhold til håndtering av kollisjoner
def hash(string, N):
    h = 0
    for letter in string:
        h = 31*h + ord(letter) #ord gir ascii verdi til bokstav
    return h % N #merk modulo så ikke h overgår N 


#Seperat chaning
#N er antall plasser i arrayet og n er antall elementer i arrayet, key er nøkkelen, kan f.eks. være en string
#og v er verdien f.eks. et tall

#Viktig å merke seg her at key er string verdien og ikke indeks så for if-testen i løkka så sjekkes keys mot
#hverandre ikke index og hvis key(string) samsvarer byttes verdi, hvis ikke legges key og verdi i lista 
def Innsetting(A, N, key, v):
    #ensurecapasity() #sjekker ratio mellom n og N(n/N), skal som regel være under 0,75 for å ha nok space

    i = hash(key, N)
    
    #Hvis det ikke finnes noe på denne indkesen i arrayet oppretter vi en liste
    if A[i] == None:
        A[i] = []
    
    bucket = A[i]
    #Hvis key finnes i bucket før så oppdateres value v 
    for j in range(len(bucket)):
        keyj, _ = bucket[j]
        if keyj == key:
            bucket[j] = (key, v)
            return
    
    #self._n += 1 #anta at vi har tilgang til antall elementer som en klasse instans, øker med 1
    #Hvis det ikke finnes noen elementer i listen fra før vil ikke for-løkken kjøre og nøkkel og value 
    #blir satt inn
    bucket.append((key, v))

def Oppsalg(A, key, N):
    i = hash(key, N)
    bucket = A[i]

    if bucket == None:
        return None
    
    for keyi, v in bucket:
        if keyi == key:
            return v
    
def Sletting(A, key, N):
    i = hash(key, N)
    bucket = A[i]

    if bucket == None:
        return None
    
    A[i] = [(keyi, v) for keyi, v in bucket if keyi != key] #kode for å enkelt fjerne element med nøkkel key i A



#Linear Probing
    
def Innsetting(A, N, key, v):
    #ensurecapasity() #sjekker ratio mellom n og N
    i = hash(key, N) 

    while A[i] != None:
        keyi, _ = A[i]
        if key == keyi:
            #Sjekker fra A til vi har funnet key og bytter v 
            A[i] = (key, v)
            return 
        
        i = (i+1) % N # Sjekker at i ikke overskrider N, begynner i så fall fra 0
    
    #self._n += 1 #antar vi har tilgang til n
    #Hvis A er None setter vi inn
    A[i] = (key, v)

def Oppsalg(A, N, key):
    i = hash(key, N)
    #Samme prinsipp som innsetting bare at v returneres
    while A[i] != None:
        keyi, vi = A[i]
        if keyi == key:
            return vi
        
        i = (i+1) % N
    return None

def Sletting(A, N, key):
    i = hash(key, N)

    while A[i] != None:
        keyi, _ = A[i]
        if keyi == key:
            #self._n -= 1
            A[i] = None
            #self._fill_hole(i) 
            #metode som finner neste verdi i arrayet eller et tomrom, 
            #hvis metoden ummidelbart finner et tomrom er det ikke noe som trengs å flytte på seg
            #Men hvis det er en nøkkel der må den flyttes på poisjon i, dette skjer rekursivt helt til 
            #det dukker opp et tomrom
            return 
        i = (i+1) % N 
    return None

'''
Alle operasjoner på et hashmap vil ha verste kjøretid O(n), men forventet kjøretid er O(1)
Ved innnsetting må det en sjelden gang forekomme en rehash når n/N blir større enn 0,75
Derfor sier vi at innsetting har en forventet amortisert kjøretid på O(1), mens oppslag og sletting har
forventet O(1). En rehash forekommer 1/n ganger og bruker c * n arbeid, der c er en konstant arbeid som 
brukes for hvert element. Forventet amortisert kjøretid går ut på å fordele den ene O(n) operasjonen, 
altså rehashen på alle O(1) operasjonene, rehashen forekommer 1/n ganger. 
Dette gjør at vi bare kan pluss O(1) operajsonen med en kostant c altså arbeid som ble gjort 
per element i rehashen. Da får vi forventet amotisert kjøretid er O(1+c) = O(1)
'''

    