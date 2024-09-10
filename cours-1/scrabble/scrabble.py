dic = {"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "u":1}

def scrabble (mot, dic) :
    result = 0
    for i in mot :
        if (i in dic) :
            result = dic[i] + result
    return result

print(scrabble("cafe", dic))

tab = ["def", "atk", "hp", "res"]
dico = {tab[0]:0}
dico[tab[1]] = 1
print(dico)


def trie (mot) :
    score = {}
