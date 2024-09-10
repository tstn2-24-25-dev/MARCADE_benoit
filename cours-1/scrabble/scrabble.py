
def scrabble (mot) :
    dic = {"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "u":1}
    result = 0
    for i in mot :
        if (i in dic) :
            result = dic[i] + result
    return result

# print(scrabble("cafe"))

# tab = ["def", "atk", "hp", "res"]
# dico = {tab[0]:0}
# dico[tab[1]] = 1
# print(dico[1])

mot = ["cafe", "face", "button", "agregre"]

def trie (mot) :
    reste_val = 0
    reste_mot = ""
    k = 0
    dico_valeur = []
    if (len(mot) == 0) :
        return "Il n'y a pas de mot dans la liste"
    if (len(mot) == 1) :
        return (mot[0])
    for i in mot :
        dico_valeur.append(scrabble(i))
        k += 1
    for i in range (len(dico_valeur) - 1) :
        if dico_valeur[i] < dico_valeur[i+1] :
            reste_val = dico_valeur[i]
            reste_mot = mot[i]
            dico_valeur[i] = dico_valeur[i+1]
            mot[i] = mot[i+1]
            dico_valeur[i+1] = reste_val
            mot[i+1] = reste_mot
    for i in range (len(dico_valeur)) :
        print (mot[i])
    return ""
    
    

print(trie(mot))
