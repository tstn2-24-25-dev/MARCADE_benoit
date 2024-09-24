def fusionner(tab1, tab2) :
    tableau = []
    i = 0
    j = 0

    while i < len(tab1) and j < len(tab2) :
        
        if tab1[i] <= tab2[j] :
            tableau.append(tab1[i])
            i += 1
        
        else :
            tableau.append(tab2[j])
            j += 1

    while i < len(tab1) :
        tableau.append(tab1[i])
        i += 1
    
    while j < len(tab2) :
        tableau.append(tab2[j])
        j += 1
        
    return tableau


def triFusion(tab) :

    if len(tab) < 2 :
        return tab[:]

    else :
        milieu = len(tab) // 2
        tab1 = triFusion(tab[:milieu])
        tab2 = triFusion(tab[milieu:])
    
    return fusionner(tab1, tab2)


tableau = [5,4,8,2,4,9]

print(triFusion(tableau))
