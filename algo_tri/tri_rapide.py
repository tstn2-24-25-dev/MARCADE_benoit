def tri_rapide(tab) :

    if tab == [] :
        return tab
    
    tab_gauche = []
    tab_droit = []

    for i in range (1, len(tab)) :

        # Les éléments inférieurs ou égaux au pivot vont dans la liste gauche
        if tab[i] <= tab[0] :
            tab_gauche.append(tab[i])
        
        # Les éléments supérieur au pivot vont dans une liste droite
        else :
            tab_droit.append(tab[i])
    
    # On renvoie la fonction récurcive qui va répéter les étapes pour avoir une liste droite et une liste gauche trié et on ajoute le pivot au milieu des 2 listes
    return tri_rapide(tab_gauche) + [tab[0]] + tri_rapide(tab_droit)    # tab[0] représente le pivot



tableau = [8,4,7,11,15,5,17,1,10,18]

print(tri_rapide(tableau))
