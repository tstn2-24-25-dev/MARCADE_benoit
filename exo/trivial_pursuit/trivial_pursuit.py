couleur = ["purple", "orange", "yellow", "green","pink", "blue"]


def lecture_lancer() :
    total = 0

    file = open("trivial_pursuit.txt", "r")
    file = file.readlines()

    for i in range (len(file)) :
        file[i] = file[i].strip()

    for i in file :
        total += int(i)

    return total


toto = (lecture_lancer())


def verif_couleur () :
    k = 0
    result = ""
    for i in couleur :
        if k < toto :
            result = i
            k += 1
    return result


print(verif_couleur())