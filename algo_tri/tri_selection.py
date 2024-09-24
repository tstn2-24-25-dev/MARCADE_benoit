def tri_selection(tableau):
    tab = tableau

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

print(tri_selection(tableau))
