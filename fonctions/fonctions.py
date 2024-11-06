from random import randint
import time, os

def affiche_menu():
    print("\n**************************************")
    print("Menu de l'application :\n")
    print("0. Quitter")
    print("1. Calculer une remise en %")
    print("2. Lancé de dé")
    print("3. Jeu du juste prix")
    print("4. Horloge numérique (HH:MM:SS qui défile)")
    print("5. Jeu du pendu")
    print("6. Décodeur César")
    print("7. Gestionnaire de contact")
    print("\n**************************************")
    return input("\nVotre choix : ")

def calcul_remise(_montant, _remise): 
    # print(_montant)
    # print(_remise)
    resultat = round(_montant - _montant * (_remise/100), 2)
    return print("Le prix de l'article après la remise est de : " + str(resultat) + " €")

def lancer_de(_nb_de_lances, _nb_faces = 6):
    print("Lancé de dé ...")
    resultat = ""
    for lance in range(1, _nb_de_lances + 1):
        resultat += "\nRésultat du lancé n° " + str(lance) + " : " + str(randint(1, _nb_faces)) + " !"
    return print("\n" + resultat)

def juste_prix(_debut_interval, _fin_interval):
    print("Lancement du juste prix ...")
    prix_a_trouver = randint(_debut_interval, _fin_interval)
    saisie_user = int(input("Saisir un prix : "))
    while saisie_user != prix_a_trouver:
        if (saisie_user > prix_a_trouver):
            print("C'est moins !")
        else:
            print("C'est plus !")
        saisie_user = int(input("Saisir un prix : "))
    return print("Bravo ! Le prix est de : " + str(prix_a_trouver) + " €")

def horloge_numerique(_delais : int = 10):
    print("Lancement de l'horloge numérique ...")
    nb_de_tours = 0
    while _delais > nb_de_tours:
        # clear console
        #os.system("cls" if os.name == "nt" else "clear") # clear, cls
        os.system("cls")
        # affiche l'heure au format HH:MM:SS (en nombre numérique)
        print(time.strftime("%H:%M:%S"))
        # on ajouter +1 au nb de tours (+1 seconde dans le contexte ici en réalité)
        nb_de_tours += 1 # nb_de_secondes_ecoulé
        # stop 1 sec avant prochain tour
        time.sleep(1)
    return

def jeu_du_pendu():
    print("Lancement du Jeu du pendu ...")
    liste_mots = ["foo", "bar", "barfoo", "foobar"]
    mot_a_trouver = liste_mots[randint(0,len(liste_mots)-1)]
    liste_lettre_mot_a_trouver = []
    print("RESULTAT : " + mot_a_trouver + " (" + str(len(mot_a_trouver)) + ")")
    # foo
    affichage_mot_a_trouver = []
    for lettre in mot_a_trouver:
        liste_lettre_mot_a_trouver.append(lettre)
        affichage_mot_a_trouver.append("-")
    print("Mot a trouver : " + "".join(affichage_mot_a_trouver) + " (" + str(len(affichage_mot_a_trouver)) + ")")

    while "-" in affichage_mot_a_trouver:
        lettre_user = input("Saisir une lettre : ")
        if lettre_user in liste_lettre_mot_a_trouver:
            print("Bravo vous avez trouvée une lettre du mot !")
            position_lettre_trouve = liste_lettre_mot_a_trouver.index(lettre_user)
            affichage_mot_a_trouver[position_lettre_trouve] = lettre_user
            liste_lettre_mot_a_trouver[position_lettre_trouve] = "0"
        print("Mot a trouver : " + "".join(affichage_mot_a_trouver))
        
    return print("\nBravo vous avez gagné !!")

def decodeur_cesar():
    return print("Lancement du Décodeur César ...")

def gestionnaire_contact():
    return print("Lancement du Gestionnaire de contact ...")