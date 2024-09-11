import random
dic = {"jus" : 15, "pq" : 3, "coca" : 5, "cayou" : 77, "mayo" : 14, "chips" : 6, "telephone" : 17, "vache" : 29, "acer predator" : 61, "lait" : 128}
produit = ["jus", "pq", "coca", "cayou", "mayo", "chips", "telephone", "vache", "acer predator", "lait"]

def article (produit) :
    # prix = []
    liste_produit = []
    nb_article = random.randint(10,30)
    for i in range (nb_article+1) :
        random_produit = random.randint(0,len(produit)-1)
        liste_produit.append(produit[random_produit])
        # prix.append(dic[produit[random_produit]])
    return liste_produit #, prix

def calcul(produit, dic) :
    resultat = []
    prix = {}
    articles = article(produit)
    for i in articles :
        if not (i in resultat) :
            resultat.append(i)
            prix[i] = dic[i]
        else :
            prix[i] *= 2
    max_prix = max(prix.values())
    
    return max_prix

print (calcul(produit, dic))