# Ouverture du fichier txt
art = open("inventaire.txt", "r")

# Récupération de la première ligne du fichier txt correspondant au nombres d'articles
nb_art = art.readline().strip()



def article () :

    # Récupération du reste des lignes du fichier txt correspondant aux nombres d'articles 
    liste_art = art.readlines()
    
    for i in range (len(liste_art)) :
    
        # Retire les \n dans la liste
        liste_art[0] = liste_art[0].strip()

        # Sépare les articles et leurs prix
        liste_art.append(liste_art[0].split())

        liste_art.pop(0)
    
    return (liste_art)




def calcul() :

    # Liste permettant de vérifié si l'article n'a pas déjà était traité
    already = []
    
    prix = {}
    
    articles = article()
    
    for i in articles :
        
        # Si l'article n'a pas encore été traiter
        if not (i[0] in already) :
            
            # Ajout de l'article dans la liste
            already.append(i[0])
    
            # Ajout de la valeur de l'article ainsi que son nom dans un dictionnaire
            prix[i[0]] = (int(i[1]))
    
        # Si l'article n'a pas encore été traiter
        else :

            for k in prix :
            
                if k == i[0] :
                    
                    # Mise à jour du prix de l'article présent en plusieurs exemplaire
                    prix[k] += int(i[1])
    

    """
    A modifier pour traiter le cas où 
    2 articles ont la même valeur finale
    """
    max_prix = max(prix.values())
    
    # Recherche de l'indice de la valeur la plus grande
    for i in prix :
    
        if prix[i] == max_prix :

            return f"{i} {prix[i]}"


# Appel du programme
print(calcul())