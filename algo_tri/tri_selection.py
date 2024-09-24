def indiceMin(tab, j) :

    for i in range (j, len(tab)) :

        if min(tab) == tab[i] :
            minim = i

    return minim


def triSelection(tab):

    for i in range(len(tab)):
        min = i

        for j in range(i+1, len(tab)):
           
           if tab[min] > tab[j]:
               min = j
                
        cle = tab[i]
        tab[i] = tab[min]
        tab[min] = cle

    return tab

tableau = [5,4,3,1,2]

print(triSelection(tableau))
