#Problem16
def solve(n):
    x=str(2**n)
    somme=0
    for k in x:
        somme+=int(k)
    return somme

#Problem22

f = open('fichier texte TD1.txt','r') #ouverture du fichier en mode lecture
for ligne in f: #description séquentielle du fichier
    L=ligne.split(',')  #on sépare la chaine de caractère ligne en liste L selon les virgules
    liste2=sorted(L) #la liste est désormais triée
    print(liste2)
    
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def position(lettre): #à chque lettre on attribue une valeur de 1 à 26
    pos=1
    for L in alphabet:
        if L==lettre:
            return pos
        pos+=1
    return 0 #ici on traite le cas des guillemets en leur attribuant la position 0
scoretot=0
pos=1
for k in liste2:
    somme=0
    for lettre in k:
        somme+=int(position(lettre)) #c'est la valeur d'un mot 
    scoretot+=somme*pos #on calcule enfin le score voulu
    pos+=1
print(scoretot)

#Problem55

def palindrome(i): #on teste si un nombre est un palindrome avec cette fonction. 
        liste2=list(str(i))
        for k in range(0,len(liste2),1):
            if liste2[k]==liste2[-k]:
                return True
        return False
        
listenombres=[k for k in range(1,10001,1)]   
for i in listenombres:
    if palindrome(i):
        listenombres.remove(i) #on supprime de la liste les palindromes


        
def inversadd(n): #reverse&add process
    stri=str(n)
    listouille=list(stri)
    stringdeux=''
    for i in range(len(listouille)-1,-1,-1):
        stringdeux+= stri[i]
    somme=n+int(stringdeux)
    return(somme)
    

nombrelychrel=0
nombrepalindrome=0
for k in listenombres:
    compteur=0
    while compteur<=50:
        n3=inversadd(k)
        if palindrome(n3)==False:
            compteur+=1
    nombrelychrel+=1
print(nombrelychrel)
            
    