

def lecture_dico () :       # Récupère le critère de notation des mots dans le fichier txt
    i = 0
    dico = {}
    fichier = open("cours-1\scrabble\jeu.txt", "r")
    tab_dico = fichier.readline().strip()
    while i < len(tab_dico) :
        dico[tab_dico[i]] = int (tab_dico[i+2])
        i += 4
    return dico


def lecture_mot() :     # Récupère les mots dans le fichier txt
    tab_pro = []
    fichier = open("cours-1\scrabble\jeu.txt", "r")
    fichier = (fichier.readlines())
    for i in range (1, len(fichier)) :
        tab_pro.append(fichier[i].strip())
    return tab_pro

dic = lecture_dico()
mot = lecture_mot()


def scrabble (mot, dic) :       # Calcul du score
    result = 0
    for i in mot :
        if (i in dic) :
            result = dic[i] + result
    return result


def trie (mot) :        # Trie des mots selon le score dans l'ordre décroissant
    reste_val = 0
    reste_mot = ""
    k = 0
    dico_valeur = []
    if (len(mot) == 0) :
        return "Il n'y a pas de mot dans la liste\n"
    if (len(mot) == 1) :
        return (mot[0])
    for i in mot :
        dico_valeur.append(scrabble(i, dic))
        k += 1
    for i in range (len(dico_valeur) - 1) :
        if dico_valeur[i] < dico_valeur[i+1] :
            reste_val = dico_valeur[i]
            reste_mot = mot[i]
            dico_valeur[i] = dico_valeur[i+1]
            mot[i] = mot[i+1]
            dico_valeur[i+1] = reste_val
            mot[i+1] = reste_mot
    return affiche(mot)
    

def affiche(tableau) :      # Affichage du final
    for i in range (len(tableau)) :
        print (tableau[i])
    return ""


print(trie(mot))        # Lancement du programme
