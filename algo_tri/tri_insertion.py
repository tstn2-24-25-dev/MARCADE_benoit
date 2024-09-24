def triInsertion(tableau):
    tab = tableau

    for i in range(1,len(tab)):
        cle = tab[i]
        j = i-1

        while j>=0 and tab[j] > cle:
            tab[j+1] = tab[j]
            j = j-1
        tab[j+1] = cle
    
    return tab

tableau = [4,8,2,10,1,9,7,6,3,5]

print(triInsertion(tableau))