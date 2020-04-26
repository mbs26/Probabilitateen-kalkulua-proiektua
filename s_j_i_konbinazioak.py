'''
Ondoko kodearen bertsio eraldatua:

https://stackoverflow.com/questions/39112897/how-to-find-the-number-of-ways-to-get-21-in-blackjack
'''

from math import factorial # faktorial funtzioa inportatzen du

def binom(n, k): # n,k koefiziente binomiala kalkulatzen du
    return factorial(n) / (factorial(k) * factorial(n - k))

def konb(puntuak, nkarta, hasi=1, erabilitakoak = [0]*11, karta_sorta = 1):
    '''
    Funtzio errekurtsiboaren definizioa, nkarta kartekin puntuak puntu lortzeko
    karten konbinazio guztiak kalkulatzen ditu karta_sorta kartekin.
    '''
    if puntuak==0: # irteera kondizioa definitzen dugu, puntuak 0 den kasuan
        if sum(erabilitakoak) == nkarta:
        # erabilitako karta kopurua nahi duguna denean,
        #kasu horretara heltzeko konbinazio kopuruak kalkulatzen ditu
            a = 1
            for i,x in enumerate(erabilitakoak):
                a *= binom(4*karta_sorta if i != 10 else 16*karta_sorta, x)
            return a
        else:
            return 0

    res = 0 # res-ren balioan konbinaziok zenbatuko dira
    
    for i in range(hasi, min(12, puntuak+1)):
        # hasi kartatik 11-ra edo puntuak puntuetara heltzeko kartararte
        #erabiltzen ditugu karta gehiago
        
        index = i if i != 11 else 1
        # erabilitakoak listan A-ren indizea 1 da, eta beste karta guztiena beraien balioa

        erabilgarriak = 16*karta_sorta if index == 10 else 4*karta_sorta
        # 16 karta daude 16 baliokoak

        if erabilitakoak[index] < erabilgarriak:
            # erabilgarri dauden index karta baino gutxiago erabili baditugu:
            erabilitakoak[index] += 1 # index karta bat gehiago erabiltzen dugu

            res += konb(puntuak - i, nkarta, i, erabilitakoak, karta_sorta)
            # konbinazioak kalkulatzen ditugu puntuak-i puntu lortzeko 
            
            erabilitakoak[index] -= 1 # hasierako kasura bueltatzen gara

    return res

def konb():
    f = open('konb.csv','w')
    for j in range(1,22):
        for i in range(1,12):
            a=int(konb(j,i))
            f.write(str(a)+';')
        f.write('\n')
    f.close()

def prob():
    f = open('prob.csv','w')
    for j in range(1,22):
        for i in range(1,12):
            a=int(konb(j,i))/binom(52,i)
            f.write('%.5f;' % a)
        f.write('\n')
    f.close()

#konb()
#prob()
