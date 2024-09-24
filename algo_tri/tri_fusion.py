def separe_liste(tab) :
    moitie = len(tab) // 2
    return tab[:moitie], tab[moitie:]


tableau = [5,4,8,2,4,9]

print(separe_liste(tableau))