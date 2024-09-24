def triRapide(tab) :

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
    return triRapide(tab_gauche) + [tab[0]] + triRapide(tab_droit)    # tab[0] représente le pivot



tableau = [4,8,2,10,1,9,7,6,3,5]

print(triRapide(tableau))
