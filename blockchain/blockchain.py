fichier = open("blockchain.txt", "r")
fichier = fichier.readlines()

def nombre_personne () :
    nb_personne = fichier[0].strip()
    return(nb_personne)


def lecture_mot_valeur () :
    tab_mot = []
    for i in range(2, len(fichier)):
        fichier[i] = fichier[i].strip()
        tab_mot.append(fichier[i].split())
    return tab_mot


def verification (tab) :
    tab_result = []
    for i in tab :
        if int(i[1]) >= int(nombre_personne())/2:
            tab_result.append(i)
    return tab_result


tab = lecture_mot_valeur()
tableau = verification(tab)


def affiche(tableau):
    for i in tableau:
        print(i[0], end="")


affiche(tableau)
