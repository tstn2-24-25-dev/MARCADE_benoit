def tri_insertion(tableau):
    tab = tableau

    for i in range(1,len(tab)):
        cle = tab[i]
        j = i-1

        while j>=0 and tab[j] > cle:
            tab[j+1] = tab[j]
            j = j-1
        tab[j+1] = cle
    
    return tab

tableau = [5,4,3,1,2]

print(tri_insertion(tableau))